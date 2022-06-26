# Importing required packages
import os
import sys
import yaml
from housing.exception import HousingException

# Function to read yaml based configuration file
def read_yaml_file(file_path: str) -> dict:
    """

    Args:
        file_path (str): _description_

    Raises:
        HousingException: _description_

    Returns:
        dict: _description_
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e