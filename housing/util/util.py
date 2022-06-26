#===========================================================================
#                                  util.py
#  @author         :  Bhanu Pratap Singh
#  @email          :  bpst.work@gmail.com
#  @repo           :  https://github.com/bpst-apps/house-price-prediction-mlops
#  @createdOn      :  26 June, 2022
#  @description    :  Collection of util function needed by project
#===========================================================================
# Importing required packages
import os
import sys
import yaml
from housing.exception import HousingException
 
#===========================================================================
# *                           read_yaml_file
# Function to read yaml based configuration file
# @param file_path str    
# @return dict
#===========================================================================
def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e