# Importing required packages
from setuptools import setup, find_packages
from typing import List

# Declaring variables for setup function
PROJECT_NAME = 'housing=predictor'
PROJECT_VERSION = '0.0.1'
PROJECT_AUTHOR = 'Bhanu'
PROJECT_DESCRIPTION = 'House Price Prediction Project'


# Function to get list of project requirements
def get_requirement_list() -> List[str]:
    """
    Description: This function is going to return list of requirements
    mentioned in requirements.txt file

    :return: List of name of libraries
    """
    with open('requirements.txt', 'r') as requirement_file:
        return requirement_file.readlines()


setup(
    name=PROJECT_NAME,
    version=PROJECT_VERSION,
    author=PROJECT_AUTHOR,
    description=PROJECT_DESCRIPTION,
    packages=find_packages(),
    install_requires=['flask', 'sklearn', 'gunicorn', 'pandas', 'numpy']
    # install_requires=get_requirement_list()
)