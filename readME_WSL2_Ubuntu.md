# WSL2 Ubuntu (22.04) Installation
This read me is an instruction how to properly install WSL2 and Ubuntu 22.04 for the use in the BRT-CARLA setup. (for Windows 10/11)

## Install WSL with command
Open PowerShell as an administrator and run:
```bash 
wsl --install
```
This command will install wsl and automatically make a Ubuntu distro. Most likely Ubuntu 24.04
After the download of Ubuntu is done, the console will ask you to create a username and password for the automatically created distro. Make sure you choose something that you remeber. 
Check your WSL distros like this:
```bash
wsl -l -v
```
you should see something like:
```text
  NAME              STATE           VERSION
* Ubuntu            Running         2
```
Make sure the version is 2 and not 1. This means the distro is using WSL2.
