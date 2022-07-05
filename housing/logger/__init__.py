# Importing required packages
import os
import logging
from datetime import datetime

# Define logging directory
LOG_DIR = 'app_logs'

# Define current timestamp
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

# Define log file name
LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"

# Create logging directory if not exits
os.makedirs(LOG_DIR, exist_ok=True)

# Define log file path
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

# Define logging basic configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    filemode='w',
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)