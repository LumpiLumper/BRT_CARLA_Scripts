# WSL2 Ubuntu (22.04) Installation
This README explains how to properly install WSL2 and Ubuntu 22.04 for the use in the BRT-CARLA setup. (for Windows 10/11)

## Requirements
### Operating System
- Windows 10 (Version 2004 or higher, Build 19041+)
- Windows 11

To check version:
```powershell
winver
```
### WSL2 Support
Your system must support:
- Virtualization enabled in BIOS
- Virtual Machine Platform enabled
- Windows Subsystem for Linux feature enabled

Check if WSL is installed:
```powershell
wsl --status
```
If wsl is installed you will see a default version message like:
```text
Default Version: 2
or
Default Version: 1
```
If Default Version is 1, change it by running:
```powershell
wsl --set-default-version 2
```
If you don't see any version message, install wsl by running:
```powershell
wsl --install
```
Then check that default version is 2.

If you still don't see a version message after installing wsl with the command, enable required Windows features manually. Open PowerShell as an administrator and run:
```powershell
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```
Then check again.
## Install WSL with command
Open PowerShell as an administrator and run:
```bash 
wsl --install -d Ubuntu-22.04
```
This command will download Ubuntu 22.04 and automatically make a Ubuntu 22.04 distro.
After the download of Ubuntu is done, the console will ask you to create a username and password for the automatically created distro. Make sure you choose a username and password that you remember, because you will need them later for administrative tasks. After, the console will switch to the Ubuntu distro. Your command line will look something like this:
```bash
User@Computer:/mnt/c/Users/user$
```
Now the console is accessing the Ubuntu distro and is no longer PowerShell. Open another PowerShell console and check the distro by running:
```bash
wsl -l -v
```
you should see something like:
```text
  NAME              STATE           VERSION
* Ubuntu-22.04      Running         2
```
Make sure the version is 2 and not 1. This means the distro is using WSL2. We need it for compatibility with dockers. If you already installed Docker Desktop you might also see a docker-desktop distro.

Then verify what version of Ubuntu was installed. Inside Ubuntu run:
```bash
lsb_release -a
```
If your Ubuntu Terminal is no longer open for some reason, you can start it by clicking on the arrows next to the plus to add a new terminal, or run:
```bash
wt -p <DistroName> (most likely Ubuntu-22.04)
```
Under Release it should say "22.04". If this is the case, [skip to final check](#final-check). If it says something else go back to PowerShell and run:
```bash
wsl --list --online
```
This will list all available Ubuntu versions
```text
Ubuntu
Ubuntu-22.04
Ubuntu-20.04
...
``` 
Then run:
```bash
wsl --install -d Ubuntu-22.04
```
Do the check again and make sure you only keep the distro that is 22.04. Remove the other distro with:
```bash
wsl --unregister <DistroName>
```
WARNING: This permanently deletes the selected distribution and all its data.

## Final Check
Run in PowerShell:
```bash
wsl -l -v
```
You should see only one Ubuntu distribution with VERSION 2. If you already installed Docker Desktop you might also see a docker-desktop distro. Then, open the distro with:
```bash
wt -p <DistroName> 
```
Inside run:
```bash
lsb_release -a
```
if it says "22.04" under Release, your distro is setup correctly. Continue with [Setup readME](readME_Setup.md)
