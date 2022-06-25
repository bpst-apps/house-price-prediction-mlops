# Importing required packages
from flask import Flask
from housing.logger import logging
from housing.exception import HousingException


# Create flask application
app = Flask(__name__)


# Create home route
@app.route('/', methods=['GET', 'POST'])
def index():
    logging.info('testing our logging module implementation')
    return 'CI/CD pipeline has been successfully established'


# Run flask application
if __name__ == '__main__':
    app.run()

