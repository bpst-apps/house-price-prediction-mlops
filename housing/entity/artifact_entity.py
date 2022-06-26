# Importing required packages
from collections import namedtuple

# Definr data ingestion artifact
DataIngestionArtifact = namedtuple(
    'DataIngestionArtifact',
    ['train_file_path', 'test_file_path', 'is_ingested', 'message']
)