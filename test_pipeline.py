# Importing required packages
from housing.logger import logging
from housing.pipeline.pipeline import Pipeline


def main():
    try:
        pipeline = Pipeline()
        pipeline.execute()
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == "__main__":
    main()
