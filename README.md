# BRT-CARLA-Scripts
This Repository is a collection of examples, experiments and default scripts to use with the BRT-CARLA setup. 

## Folder Structure
```text
BRT_CARLA_Scripts
│
├── READMEs/                    # Documentation and setup guides
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
If contrutors have a test/experiment that they want to add to the repo they should always make a new folder inside BRT_code that has a meaningfull name for the experiment or test. Put the corresponding file or files in the new folder. Don't make experiments/tests directily in BRT_CARLA_Scrips. Please keep the repository structured and consistent. If needed update .gitignore!

For setup checkout:
- [readME_WSL2_Ubuntu](readME_WSL2_Ubuntu.md)
- [readME_Setup](readME.md)
-[readME_GPU_Acceleration](readME_GPU_Acceleration.md)