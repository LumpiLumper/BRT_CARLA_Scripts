# BRT-CARLA-Scripts
This Repository is a collection of examples, experiments and default scripts to use with the BRT-CARLA setup. It is not production code and can contain broken or unstable code. It is used for team-members to share code, make prototypes and learn about CARLA. 

## Folder Structure
```text
BRT_CARLA_Scripts
│
├── documentation/              # Documentation and setup guides
│
├── examples_from_carla/        # Official example scripts from CARLA
│   ├── example1.py
│   ├── example2.py
│   └── ...
│
├── carla/                      # CARLA Python API wheels and agents
│   └── ...
│
└── BRT_code/                   # Team experiments and custom development
    ├── experiment1/
    │   └── experiment1.py
    │
    ├── experiment2/
    │   └── experiment2.py
    │
    └── ...
```
If contributors have a test/experiment that they want to add to the repo they should always make a new folder inside BRT_code that has a meaningful name for the experiment or test. Put the corresponding file or files in the new folder. Don't make experiments/tests directly in BRT_CARLA_Scrips. Please keep the repository structured and consistent. If needed update .gitignore!

## Getting started
To set your device up to use with the BRT-CARLA Setup checkout the documentation.

- [Setup Windows devices for BRT-CARLA-Setup](documentation/readME_WSL2_Ubuntu.md)
- [Setup macOS devices for BRT-CARLA-Setup](documentation/readME_macOS_Ubuntu.md)
- [Setup Windows devices with CARLA](documentation/readME_Setup.md)
- [Run CARLA with GPU Acceleration](documentation/readME_GPU_Acceleration.md)