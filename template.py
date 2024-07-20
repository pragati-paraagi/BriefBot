import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')
project_name = "BriefBot"

list_of_files = [
     ".github/workflows/.gitkeep",                   #whenever we will do deployment, we will create this folder
     f"src/{project_name}/__init__.py",              #constructor file (needed when we import data from other file)
     f"src/{project_name}/components/__init__.py",   #componenet is folder inside which constructor file is present (another local package)
     f"src/{project_name}/utils/__init__.py",        #utils is folder where all utility related codes are present
     f"src/{project_name}/utils/common.py",          # common.py is file where all common utility codes are present
     f"src/{project_name}/logging/__init__.py",      # logging is folder where all logging related codes are present
     f"src/{project_name}/config/__init__.py",       # config is folder where all configuration related codes are present
     f"src/{project_name}/config/configuration.py",  # configuration.py is file where all configuration settings are present
     f"src/{project_name}/pipeline/__init__.py",     # pipeline is folder where all pipeline related codes are present
     f"src/{project_name}/entity/__init__.py",       # entity is folder where all entity related codes are present
     f"src/{project_name}/constants/__init__.py",    # constants are folder where all constants are present
     "config/config.yaml",                           # this file contains all configuration settings
     "params.yaml",                                  # this file contains all parameters
     "app.py",                          # main file for starting the application
     "main.py",                         # main file for starting the application
     "Dockerfile",                      # Dockerfile for creating Docker image
     "requirements.txt",                # this file contains all required packages
     "setup.py",                        # setup file for creating package
     "research/trials.ipynb",           # Dockerfile for creating Docker image for research environment
     "README.md",                     # readme file for project
]

for filepath in list_of_files:
    filepath = Path(filepath)                      
    filedir, filename = os.path.split(filepath)    # Splitting file path into directory and filename

    if filedir != "":                              
        os.makedirs(filedir, exist_ok=True)         # Creating directory if it doesn't exist
        logging.info(f"Created directory: {filedir} for the file {filename}")  # Logging directory creation

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):   # Checking if file already exists
        with open(filepath, "w") as f:
            pass           # Creating file if it doesn't exist
            logging.info(f"Created file: {filepath}")    # Logging file creation

    else:
        logging.info(f"{filename} is already exists")    # Logging file creation if it already exists

