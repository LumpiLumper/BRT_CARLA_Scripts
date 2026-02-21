# Workstation SSH Setup
This README explains how properly setup the SSH-connection on the BRT-Workstation, how users can get access to the Workstation and the CARLA-Simulation running on it, and how to how to trouble shoot if there are issues.

## Setup SSH on Workstation
### Activate SSH
We need to activate SSH-Services on the workstation. Open Powershell as an administrator and run:
```bash
Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'
```
If you see:
```text
Name  : OpenSSH.Client~~~~0.0.1.0
State : Installed

Name  : OpenSSH.Server~~~~0.0.1.0
State : Installed
```
SSH-Services are installed and ready to use.

If you get NotPresent, the services are not installed. Get them by running:
```bash
Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0
```
```bash
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0
```
Now when services are installed, enable and start SSH server service:
```bash
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'
```
Verify the server is running with:
```bash
Get-Service sshd
```
You should see:
```bash
Status   Name               DisplayName
------   ----               -----------
Running  sshd               OpenSSH SSH Server
```
### Find IP of Workstation
Open Powershell and run:
```bash
ipconfig
```
This will output the IP configuration. Under ```Wireless LAN adapter WLAN:``` ```IPv4 Address``` search for something like:
```text
10.206.228.xx
```
The IP has this form because the workstation is on the Campus Network.

This IP adress will be the connection for BRT-Driverless members to access the CARLA-Simulator running on the Workstation.

