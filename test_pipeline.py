# Importing required packages
from housing.logger import logging
from housing.exception import HousingException
from housing.pipeline.pipeline import Pipeline


# Define main function
def main():
    try:
        pipeline = Pipeline()
        pipeline.execute()
    except Exception as e:
        logging.error(f'{e}')
        
        
if __name__ == '__main__':
    main()