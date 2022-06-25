# Importing required packages
import sys
import yaml
from housing.exception import HousingException


def read_yaml_file(file_path: str) -> dict:

    """
    Reads a YAML file and returns the contents as a dictionary.

    Raises:
        HousingException: raise custom housing exception

    Returns:
        dict: housing configuration as a dictionary
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e, sys) from e