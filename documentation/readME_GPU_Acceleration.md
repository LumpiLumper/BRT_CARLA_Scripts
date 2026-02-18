# GPU Acceleration (WSL2 + NVIDIA + Docker Desktop)
For significantly better performance, CARLA should run using GPU acceleration instead of CPU software rendering.

If you see this in the logs:
```bash
WARNING: lavapipe is not a conformant vulkan implementation
```
CARLA is using CPU-based rendering (software Vulkan), which causes very high CPU usage (e.g., 300–400%). GPU acceleration reduces CPU load dramatically and improves simulation performance.

## Requirements
1. NVIDIA GPU (RTX / GTX)
2. Latest NVIDIA Windows drivers (with WSL support)
3. WSL2 (not WSL1)
4. Docker Desktop
5. Docker Desktop → Settings → Resources → WSL Integration → Ubuntu enabled
6. Docker Desktop → Settings → Resources → GPU support enabled

## Setup 
### Verify GPU is Avalible in WSL
Inside Ubuntu (WSL):
```bash
nvidia-smi
```
If working, you will see:
- GPU name
- Driver version
- Memory usage

If command not found or no devices appear:
- Update Windows NVIDIA driver
- Ensure WSL GPU support is installed
### Verify Docker can Access GPU
Inside Ubuntu (WSL):
```bash
docker run --rm --gpus all nvidia/cuda:12.2.0-base nvidia-smi
```
If GPU is correctly configured, this will display your GPU information inside a container.

If this fails:
- Enable GPU support in Docker Desktop settings
- Restart Docker Desktop
### Run CARLA with GPU Support:
Stop existing container:
```bash
docker stop carla916
docker rm carla916
```
Recreate container with GPU enabled:
```bash
docker run -d --name carla916 \
  --gpus all \
  -p 2000-2002:2000-2002 \
  carlasim/carla:0.9.16 \
  bash -lc "./CarlaUE4.sh -RenderOffScreen -quality-level=Epic -carla-rpc-port=2000"
```
Explanation:
- --gpus all → enables NVIDIA GPU passthrough
- -RenderOffScreen → headless rendering
- -quality-level=Epic → full quality (optional)
- -carla-rpc-port=2000 → RPC port

### Verify GPU is used
After strating the container:
```bash 
docker logs -f carla916
```
You should NOT see the lavapipe warning anymore.

Then check GPU usage while CARLA is running:
```bash
nvidia-smi
```
You should see:
- CarlaUE4 process
- GPU memory usage increasing

CPU usage in Docker Desktop should drop significantly.