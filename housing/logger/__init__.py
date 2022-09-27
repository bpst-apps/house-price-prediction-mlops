# Importing required packages
import os
import logging
import pandas as pd
from datetime import datetime

from housing.constant import get_current_timestamp

# Define logging directory
LOG_DIR = 'app_logs'


def get_log_file_name():
    return f"log_{get_current_timestamp()}.log"


# Define current timestamp
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

# Define log file name
LOG_FILE_NAME = get_log_file_name()

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


def get_log_dataframe(file_path):
    data = []
    with open(file_path) as log_file:
        for line in log_file.readlines():
            data.append(line.split("^;"))

    log_df = pd.DataFrame(data)
    columns = ["Time stamp", "Log Level", "line number", "file name",
               "function name", "message"]
    log_df.columns = columns

    log_df["log_message"] = log_df['Time stamp'].astype(str) + ":$" + log_df["message"]
    return log_df[["log_message"]]
