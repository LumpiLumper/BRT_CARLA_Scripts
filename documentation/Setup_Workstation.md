# Setup BRT-Workstation

## 1. Download Docker Desktop

Make sure once Docker Desktop installs it automatically activates WSL. If not, manually install it with:

```bash
wsl --install -d Ubuntu-22.04
```

To check if it's installed properly run:

```bash
wsl --status
```

if it says: 

```text
Default Version: 2
```

Everything is good. If Version is 1, change to 2 with:

```bash
wsl --set-default-version 2
```

