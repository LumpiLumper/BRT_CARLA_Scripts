# BRT-CARLA-Scripts
This Repository is a collection of examples, experiments and default scripts to use with the BRT-CARLA setup. 

## Folder Structure
```text
BRT_CARLA_Scripts
    └─ readME's
    └─ examples_from_carla (contains example scripts provided by CARLA)
        └─ example1.py
        └─ example2.py
        └─ ...
    └─ carla (contains wheels for carla and agents useful for python scripts)
        └─ ...
    └─ BRT_code
        └─ experiment1
            └─ experiment1.py (experiment by team member X)
        └─ experiment2
            └─ experiment2.py (experiment by team member Y)
        └─ ...
```
If contrutors have a test/experiment that they want to add to the repo they should always make a new folder inside BRT_code that has a meaningfull name for the experiment or test. Put the corresponding file or files in the new folder. Don't make experiments/tests directily in BRT_CARLA_Scrips. Keep the repo organized! If needed update .gitignore!