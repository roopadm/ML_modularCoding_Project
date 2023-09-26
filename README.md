# ML_modularCoding_Project


**Project Initialization:** 

The Python script in template.py automates the day to day task of creating project folders and files. 
It helps initialize a project by creating a directory structure and necessary files based on user input for the project name. It is designed to streamline the setup process for new projects.

--> You will be prompted to enter a project name. Once you provide a non-empty project name, the script will create the following directory structure and files:
   - `source/__init__.py` (Project-level init file)
   - Subdirectories for components, config, constants, entity, exception, logger, pipeline, and utils.
   - Configuration files: `config/config.yaml` and `schema.yaml`.
   - Python source files: `app.py`, `main.py`, `setup.py`, `logs.py`, and `exception.py`.

### Notes

- The script ensures that directories are created only if they don't already exist.
- Existing files will not be overwritten, and the script logs a message when a file already exists.


**Project Setup & Setup file Execution**

1. Create new Environment

conda create -p env python=3.9 -y         # one of the stable python version supported by conda and our project requirements




