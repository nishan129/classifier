import os
from ensure import ensure_annotations
import yaml
from box import ConfigBox
from pathlib import Path
from typing import Any
from src.classifier.exception import ModelException
from src.classifier.logger import logging
import json, sys
import joblib


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception:
        raise ValueError("yaml file is empty")
    
@ensure_annotations
def write_yaml(filepath:Path, data:Any):
    """Write yaml file and return config box

    Args:
        filepath (Path): To save in yaml file path
        data (Any): data to save in yaml file

    Returns:
        ConfigBox: writern file path
    """
    try:
        os.makedirs(os.path.dirname(filepath),exist_ok=True)
        with open(filepath, 'w') as file:
            yaml.dump(data,file,default_flow_style=False)
    except Exception as e:
        raise ModelException(e,sys)
    
@ensure_annotations   
def create_directory(path_to_directory:list, verbose=True):
    """create list of directories

    Args:
        path_to_directory (list): list of path of directory
        verbose (bool, optional): Ingnoring if multiple directory is created Defaults to True.
    """
    try:
        for path in path_to_directory:
            os.makedirs(path,exist_ok=True)
            if verbose: 
                logging.info(f"Create directory {path}")
    except Exception as e:
        raise ModelException(e,sys)

@ensure_annotations
def save_json(path:str, data:dict):
    """Save Dict to JSON file

    Args:
        path (str): path to save dictionary in to json
        data (dict): dictionary to save

    Raises:
        ModelException: error
    """
    try:
        with open(path, 'w') as file:
            json.dump(data,file, indent=4)
            logging.info(f"Save json file {file}")
    except Exception as e:
        raise ModelException(e,sys)
    
    
@ensure_annotations
def load_json(path:str) -> ConfigBox:
    """To load a json file

    Args:
        path (str): file path there have json files

    Returns:
        ConfigBox: to file path
    """
    try:
        with open(path, 'r') as file:
            data = json.load(file)
            return ConfigBox(data)
    except Exception as e:
        raise ModelException(e,sys)