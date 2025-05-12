import os
from src.WineQuality import logger
import json
import yaml
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its contents as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Returns:
        ConfigBox: Contents of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError:
            raise ValueError(f"yaml file is empty")
    except Exception as e:
         raise e



@ensure_annotations
def create_directories(path_to_directories: list, verbose= True) :
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool): If True, prints the status of directory creation.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Creating directory: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves a dictionary as a JSON file.

    Args:
        path (str): Path to save the JSON file.
        data (dict): Dictionary to save as JSON.
    """
    with open(path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
        logger.info(f"JSON file saved at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads a JSON file and returns its contents as a dictionary.

    Args:
        path (path): Path to the JSON file.

    Returns:
        ConfigBox: Data as ConfigBox insted of dict.
    """
    with open(path) as f:
        content = json.load(f)
        logger.info(f"json file loaded succesfully from: {path}")
        return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any,path:Path):
    """
    Saves binary file.

    Args:
        path (path): path to binary file.
        data (Any): data to save as binary.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Model saved at {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Loads a binary file.

    Args:
        path (path): path to binary file.

    Returns:
        Any: loaded data.
    """
    data = joblib.load(path)
    logger.info(f"Model loaded from {path}")
    return data