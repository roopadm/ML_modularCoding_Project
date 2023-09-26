import os,sys
from pathlib import Path
import logging

#Prompt the user for a project name until a non-empty name is provided
while True:
    project_name=input("Please enter project name :")
    if project_name!="":
        break



#List of files to create
list_of_files_needed=[

f"{project_name}/__init__.py",
f"{project_name}/components/__init__.py",
f"{project_name}/config/__init__.py",
f"{project_name}/constants/__init__.py",
f"{project_name}/entity/__init__.py",
f"{project_name}/exception/__init__.py",
f"{project_name}/logger/__init__.py",
f"{project_name}/pipeline/__init__.py",
f"{project_name}/utlis/__init__.py",
f"config/config.yaml",
    "schema.yaml",
    "app.py",
    "main.py",
    "setup.py",
    "logs.py",
    "exception.py"
]

# Iterate through the list of files to create
for filepth in list_of_files_needed :
    filepath=Path(filepth)
    filedir,filename=os.path.split(filepath)

    # Create subdirectories if necessary
    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
    
    #  Create an empty file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or(os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass

    # Log a message if the file already exists        
    else :
        logging.info("file is already present at :{filepath}")

