# WSL2 Ubuntu (22.04) Installation
This read me is an instruction how to properly install WSL2 and Ubuntu 22.04 for the use in the BRT-CARLA setup. (for Windows 10/11)

## Install WSL with command
Open PowerShell as an administrator and run:
```bash 
wsl --install -d Ubuntu-22.04
```
This command will download Ubuntu 22.04 and automatically make a Ubuntu 22.04 distro.
After the download of Ubuntu is done, the console will ask you to create a username and password for the automatically created distro. Make sure you choose something that you remeber. After, the console will switch to the Ubuntu distro. Your command line will look something like this:
```bash
User@Computer:/mnt/c/Users/user$
```
Now the console is accessesing the Ubuntu distro and is no longer PowerShell. Open another PowerShell console and check the distro like this.
```bash
wsl -l -v
```
you should see something like:
```text
  NAME              STATE           VERSION
* Ubuntu-22.04      Running         2
```
Make sure the version is 2 and not 1. This means the distro is using WSL2. We need it for compatibility with dockers. If you already installed Docker Desktop you might see a docker-desktop distro.

Then verify what version of Ubuntu was installed. Inside Ubuntu run:
```bash
lsb_release -a
```
If your Ubuntu Terminal is no longer open for some reason, you can start it by klicking on the arrows next to the plus to add a new terminal, or run:
```bash
wsl -p <DistroName> (most likely Ubuntu-22.04)
```
Under Release it should say "22.04". If this is the case, [skip to final check](#final-check). If it says something else go back to PowerShell and run:
```bash
wsl --list --online
```
This will list all avalible Ubuntu versions
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
WARNING: This permanently deletes distro.

## Final Check
Run in PowerShell:
```bash
wsl -l -v
```
You should only have one Ubuntu distro. If you already installed Docker Desktop you might also have a distro named docker-desktop. Then, open the distro with:
```bash
wsl -p <DistroName> 
```
Inside run:
```bash
lsb_release -a
```
if it says "22.04" under Release, your distro is setup correctly. Continue with Setup readME
