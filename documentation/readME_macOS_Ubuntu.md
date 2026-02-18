# Ununtu 22.04 on macOS
This README explains how to properly install WSL2 and Ubuntu 22.04 for the use in the BRT-CARLA setup. 

(Tested on M1(arm64) processor but is applicable for Intel. Differences in steps are marked)

## Get UTM
UTM is a virtualizition and emulation app for macOS that enables us to emulate other operating systems. Get UTM from https://mac.getutm.app/

Download it from the website, don't get the App Store version.

After the download is comlete go into your donwload and install the UTM.dmg.

When it is done, verify it is compatible with your architecture by opening the terminal (command+Spacebar, type terminal) and running:
```bash
file file /Applications/UTM.app/Contents/MacOS/UTM
```
you should see something like:
```text
/Applications/UTM.app/Contents/MacOS/UTM: Mach-O universal binary with 2 architectures: [x86_64:Mach-O 64-bit executable x86_64] [arm64]
/Applications/UTM.app/Contents/MacOS/UTM (for architecture x86_64):	Mach-O 64-bit executable x86_64
/Applications/UTM.app/Contents/MacOS/UTM (for architecture arm64):	Mach-O 64-bit executable arm64
```
Normally it downoads the universal binary with 2 architectures as you can see in the first line. This is compatible with arm64 and x86_64. In the second and third line you can see that both are avalible. If you see your architecture, you're fine.

### Give UTM premission to access files
1. Open system settings
2. Go to Privacy and Security in the list on the left
3. Click on Full Disk Access
4. UTM should be listed, enable the switch so it's green 

## Get Ubuntu 22.04
You can get the disk image for ubuntu 22.04 live server from the ubuntu website. You wont find them if you go to the official website over the browser but you can get it from:
```text
https://cdimage.ubuntu.com/releases/jammy/release/ubuntu-22.04.5-live-server-arm64.iso
```
for arm64,

or from:
```text
dunno (figure out and update)
```
for x64/Intel architecture.

Or get it from BRT-Teams

Now you should have a .iso file that with the name: "ubuntu-22.04.5-live-server-arm64.iso" or "ubuntu-22.04.5-live-server-amd64.iso" depending on the architecture. Make sure the architecture in the file name matches the architecture of your device.

If you are unsure what architecture your devicei is, open terminal and run:
```bash
uname -m
```

## Setup Ubuntu in UTM
### 1. Open UTM
### 2. Add a new virtual machine
### 3. Choose Virtualize
![Image not found]()
4. (Window: Operating System) Choose Linux
5. (Window: Hardware) Give the VM a minimum of 4GB of RAM, if your device has 16BG or more you can give it 8GB, CPU