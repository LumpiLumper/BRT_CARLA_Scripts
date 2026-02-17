# WSL2(Ubuntu 22.04) + Docker Desktop + Carla Container + Python Venv Setup

This document describes how to set up and run the BRT CARLA development environment using:
- WSL2 (Ubuntu 22.04)
- Docker Desktop (Windows)
- CARLA 0.9.16 Docker container
- Python virtual environment inside WSL

This setup allows CARLA to run inside Docker while Python scripts run inside WSL and connect via localhost.

## Architecture Overview
```text
Windows
└─ Docker Desktop
   └─ CARLA Container (carlasim/carla:0.9.16)

WSL2 (Ubuntu 22.04)
└─ Python venv (carla-venv)
   └─ Python scripts connecting to 127.0.0.1:2000
```
Docker runs on Windows.
WSL connects to Docker via Docker Desktop integration.

## Requirements
- Windows 10/11
- WSL2 installed
- Ubuntu 22.04 installed in WSL
- Docker Desktop installed
- Docker Desktop → Settings → Resources → WSL Integration → Ubuntu enabled
### Optional (recommended):
NVIDIA GPU + WSL GPU support

## Make Setup
### Verify Docker Works Inside WSL
Open Ubuntu(WSL):
```bash
docker info
 ```
If Docker is running correctly, you will see server information.
If not:
Start Docker Desktop on Windows.
### Pull CARLA Docker Image
```bash
docker pull carlasim/carla:0.9.16
```
This downloads CARLA Docker Image. (Download ~16GB; Effective diskspace used ~30GB)

Verify:
```bash
docker images | grep carla
```
Expected:
```text
carlasim/carla:0.9.16   ...
```
### Create and Run the CARLA Container
Create Container (only once)
without GPU:
```bash
docker run -d --name carla916 \
  -p 2000-2002:2000-2002 \
  carlasim/carla:0.9.16 \
  bash -lc "./CarlaUE4.sh -RenderOffScreen -carla-rpc-port=2000"
```
with GPU:
```bash
docker run -d --name carla916 \
  --gpus all \
  -p 2000-2002:2000-2002 \
  carlasim/carla:0.9.16 \
  bash -lc "./CarlaUE4.sh -RenderOffScreen -quality-level=Epic -carla-rpc-port=2000"
```
Explanation:
- --gpus all → requests GPU access
- -p 2000-2002:2000-2002 → Exposes CARLA RPC ports
- RenderOffScreen → Headless mode
- carla-rpc-port=2000 → Default RPC port
### Setup Python Virtual Environment (WSL)
Navigate to where you want the venv to be and
create venv (first time only)
```bash
python3 -m venv carla-venv
source carla-venv/bin/activate
pip install --upgrade pip
pip install carla==0.9.16
```
Test:
```bash
python - <<'PY'
import carla
client = carla.Client("127.0.0.1", 2000)
client.set_timeout(60.0)
world = client.get_world()
print("Connected to:", world.get_map().name)
PY
```
If successful:
```bash
Connected to: TownXX
```
## Daily Workflow
### Start CARLA
```bash
docker start carla916
docker logs -f carla916
```
Wait until CARLA finishes loading
Now the console will output the logs of the carla container. CARLA is pretty quiet so
most likely you won't see much written as an output just now. This is expected
### Check Ports
Open another Ubuntu console window and leave the one with the logs open
Then run in the new console
```bash
docker ps
```
Under PORTS, you should see something like:
```bash
0.0.0.0:2000-2002->2000-2002/tcp
```
### Run Your Python Scripts
Example:
```bash
source path-to-venv/carla-venv/bin/activate
python path-to-script/your_script.py
```
make sure scripts use:
```bash
client = carla.Client("127.0.0.1", 2000)
client.set_timeout(60.0)
```
### Stop CARLA
```bash
docker stop carla916
```
## Troubleshooting
### Docker not reachable
→ Start Docker Desktop on Windows.

### Python cannot connect
Check:
```bash
docker ps
ss -lin | grep 2000
```
Ensure ports are exposed and container is running.

If you get an error looking something like this:
```text
RuntimeError: time-out of 60000ms while waiting for the simulator, make sure the simulator is ready and connected to 127.0.0.1:2000
```
This means the client didn't receive a response from the CARLA server within the set timeout window.
If the ports are exposed and docker is running, the most likely fix is increasing the timeout window of client:
```bash
client.set_timeout(120.0)
```
### High CPU Usage in Docker Desktop
In Docker Desktop the procentage seen under CPU(%) means how much of a CPU core is used by
the container.
- 100% → 1 CPU core is fully used
- 250% → 2.5 CPU cores are used 

If you see the carla916 container is using a lot of CPU check what the output is in the terminal afer you run:
```bash
docker start carla916
docker logs -f carla916
```
If you see 
```bash
WARNING: lavapipe is not a conformant vulkan implementation
```
CARLA is using CPU rendering instead of GPU

For GPU acceleration:
- Enable NVIDIA support in WSL
- Run container with --gpus all

More Details in [GPU Acceleration readME](readME_GPU_Acceleration.md)

## Full Startup Summary
1. Start Windows
2. Start Docker Desktop (if not auto-started)
3. Open WSL Ubuntu
4. docker start carla916
5. Activate venv
6. Run Python scripts
