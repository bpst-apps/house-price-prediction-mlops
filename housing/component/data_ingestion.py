# Importing required packages
import os
import sys
from housing.logger import logging
from housing.exception import HousingException
from housing.entity.config_entity import DataIngestionConfig


class DataIngestion:

    def __int__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data ingestion log started.{'='*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HousingException(e, sys) from e