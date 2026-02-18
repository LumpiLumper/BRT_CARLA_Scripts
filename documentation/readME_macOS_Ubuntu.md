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
<img src="images/UTM_Win_Main_woVM.jpeg" width="33%">

- Click Create a NewVirtual Machine

### 3. Choose Virtualize
<img src="images/UTM_Win_Start.jpeg" width="33%">

- Click Virtualize

### 4. Choose Linux
<img src="images/UTM_Win_OS.jpeg" width="33%">

- Click Linux

### 5. Hardware
<img src="images/UTM_Win_Hardware.jpeg" width="33%">

- Give the VM a minimum of 4GB RAM, if your device has 16GB RAM you can increase it to 8GB.
- Everything else same as seen in image

### 6. Choose Boot Option
<img src="images/UTM_Win_Boot_Option.jpeg" width="33%">

- Leave Apple virtualization unchecked
- Choose Boot from ISO image (file you downloaded earlier)
- Click on Browse... and select the .iso file you downloaded in the finder
- Click continue

### 6. Storage
<img src="images/UTM_Win_Storage.jpeg" width="33%">

- By default set to 64GB, leave it like this.

### 6. Shared Directory
<img src="images/UTM_Win_SharedDir.jpeg" width="33%">
- Don't connect a path, leave it as is.

### 7. Summary
<img src="images/UTM_Win_Summary.jpeg" width="33%">

- Click save

### 8. See VM in UTM
<img src="images/UTM_Win_Main_wVM.jpeg" width="33%">

- You will see the new VM on the left
- It will be called Linux and has the Penguin logo
- Make sure it's selected (blue) and scroll to bottom
- Verify CD/DVD is selected and the on the right to it it says the file name
- the click on the play symbol

### 9. Setup Ubuntu
A second window will open in a command line style.

<img src="images/UTM_Linux_Setup_Start.jpeg" width="33%">

- Press enter on Try or Install Ubuntu Server
- Wait for it to load

### 10. Select language
<img src="images/UTM_Linux_Setup_select_lanuage.jpeg" width="33%">

- choose whatever language you like, BUT all BRT documentation will be with english language

### 11. Update Request
<img src="images/UTM_Linux_Setup_update_request.jpeg" width="33%">

- Select Continue without updating

### 12. Set Keyboard Setting
<img src="images/UTM_Linux_Setup_keyboard_setting.jpeg" width="33%">