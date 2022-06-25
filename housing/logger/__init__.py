# Importing required packages
import os
import logging
from datetime import datetime


# Define login variables
LOG_DIR = 'housing_logs'
CURRENT_TIMESTAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
LOG_FILENAME = f'log_{CURRENT_TIMESTAMP}.log'


# Create log directory
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILENAME)

# Configure logging module
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='w',
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)