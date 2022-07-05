# Importing required packages
from collections import namedtuple

# Define data ingestion artifact
DataIngestionArtifact = namedtuple(
    'DataIngestionArtifact',
    ['train_file_path', 'test_file_path', 'is_ingested', 'message']
)

# Define data validation artifact
DataValidationArtifact = namedtuple(
    'DataValidationArtifact',
    ['schema_file_path', 'report_file_path', 'report_page_file_path', 'is_validated', 'message']
)

# Define data transformation artifact
DataTransformationArtifact = namedtuple(
    'DataTransformationArtifact',
    ['is_transformed', 'message', 'transformed_train_file_path', 'transformed_test_file_path',
     'preprocessed_object_file_path']
)
