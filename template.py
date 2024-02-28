import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


project_name= "textSummarizer"

list_files= [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "exploration/tests.ipynb"
]

for filepath in list_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    #check if filedir is not empty ""
    if filedir != "":
        #create directory. If already exists don't alter
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    # check if filepath doesn't exists or the file is empty->create a new file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) ==0) :
        with open(filepath,'w') as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")