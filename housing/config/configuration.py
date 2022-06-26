# Importing required packages
import os
import sys
from housing.constant import *
from housing.logger import logging
from housing.util.util import read_yaml_file
from housing.exception import HousingException

from housing.entity.config_entity import (DataIngestionConfig, DataValidationConfig, DataTransformationConfig, 
                                          ModelTrainerConfig, ModelEvaluationConfig, ModelPusherConfig,
                                          TrainingPipelineConfig)


class Configuration:
    
    def __init__(self, 
                 config_file_path: str = CONFIG_FILE_PATH,
                 current_timestamp: str = CURRENT_TIMESTAMP
                 ) -> None:
        try:
            # set yaml configuration file information
            self.config_info  = read_yaml_file(file_path=config_file_path)
            
            # Set training pipeline configuration
            self.training_pipeline_config = self.get_training_pipeline_config()
            
            # Set current timestamp information
            self.timestamp = current_timestamp
        except Exception as e:
            raise HousingException(e,sys) from e
    
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            # Get artifact directory path
            artifact_dir = self.training_pipeline_config.artifact_dir
            
            # Define data ingestion artifact directory path
            data_ingestion_artifact_dir=os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.timestamp
            )
            
            # Set data ingestion info with data ingestion configuration key
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            
            # Set dataset download url key in configuration
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            
            # Define tgz file download directory path
            tgz_download_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]
            )
            
            # Define raw data directory path
            raw_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )
            
            # Define ingested data directory path
            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY]
            )
            
            # Define ingested train data directory path
            ingested_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
            )
            
            # Define ingested test data directory path
            ingested_test_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            )
            
            # Define ingestion data configuration
            data_ingestion_config = DataIngestionConfig(
                dataset_download_url=dataset_download_url, 
                tgz_download_dir=tgz_download_dir, 
                raw_data_dir=raw_data_dir, 
                ingested_train_dir=ingested_train_dir, 
                ingested_test_dir=ingested_test_dir
            )
            
            logging.info(f"data ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            # Initialize schema file path variable
            schema_file_path = None
            
            # Define data validation configuration
            data_validation_config = DataValidationConfig(
                schema_file_path=schema_file_path
            )
            
            return data_validation_config
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e
    
    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            # Getting training file configuration
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            
            # Get artifact directory
            artifact_dir = os.path.join(
                ROOT_DIR,
                training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            # Define training pipeline configuration
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"training pipeline config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e