import os
from pathlib import Path
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

project_name = "Wine Quality"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "schema.yaml",
    "params.yaml",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir,file_name = os.path.split(file_path)
    if file_dir != "":
        # Create directories if they do not exist
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for {file_name}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        # Create the file if it does not exist
        with open(file_path, 'w') as f:
            pass
        logging.info(f"Creating file: {file_name}")
    else:
        logging.info(f"{file_name} already exists")


