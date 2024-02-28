import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads the yaml and returns

    Args:
        path_to_yaml (Path): path like input

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as f:
            content = yaml.safe_load(f)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        return e
    
@ensure_annotations
def create_directory(path_to_directories: list,verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        verbose (bool, optional): ignore if multiple directories to be created. Defaults to False.
    """
    for path in path_to_directories:
        if not os.path.exists(path):
            os.makedirs(path,exists_ok=True)
            if verbose:
                logger.info(f"Created directory: {path}")
        else:
            if verbose:
                logger.info(f"Directory: {path} already exists")
                
@ensure_annotations
def get_size(path: Path)-> str:
    """get the size of the file in KB
    Args:
    path (Path): path to the file
    
    Returns:
    str: size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"

