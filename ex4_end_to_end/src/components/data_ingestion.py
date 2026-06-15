import os
import sys
from dataclasses import dataclass
import pandas as pd
from pandas import DataFrame

from ex4_end_to_end.src.components.model_trainer import ModelTrainer
from ex4_end_to_end.src.logger import logging
from ex4_end_to_end.src.exception import  CustomException
from sklearn.model_selection import train_test_split
from data_transformation import DataTransformationConfig, DataTransformation

# so the data ingestion component should have below configured path to decide where need to store the train.csv
# test data and raw data.


# dataclass annotation is used generate boilerplate code that python needs to store the data into a class.
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact', "train.csv")
    test_data_path: str = os.path.join('artifact', "test.csv")
    raw_data_path: str = os.path.join('artifact', "raw_data.csv")


class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv("../../data_files/StudentsPerformance.csv")
            logging.info(f"data source read successfully and converted into the df, storing the raw data in: "
                         f"{DataIngestionConfig.raw_data_path}")

            # os.path.dirname() this method returns directory path from the given path, ex:
            # /home/sawai/python/file.txt   it means it will remove the last file name and return the directory as: /home/sawai/python
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.data_ingestion_config.raw_data_path, header=True, index=False)
            logging.info(f"raw data stored successfully at this path: {self.data_ingestion_config.raw_data_path}")

            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

            logging.info(f"storing train data at: {self.data_ingestion_config.train_data_path}")
            train_data.to_csv(self.data_ingestion_config.train_data_path)
            logging.info(f"train data stored successfully at: {self.data_ingestion_config.train_data_path}")

            logging.info(f"storing test data at: {self.data_ingestion_config.test_data_path}")
            test_data.to_csv(self.data_ingestion_config.test_data_path)
            logging.info(f"test data stored successfully at: {self.data_ingestion_config.test_data_path}")

            return (
                self.data_ingestion_config.raw_data_path,
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path,
            )

        except Exception as exc:
            logging.error(f"operation failed due to: {exc}")
            raise CustomException(exc)


if __name__ == '__main__':
    obj = DataIngestion()
    raw_data_path, train_data_path, test_data_path = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, preprocessor_obj_file_path = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(train_arr, test_arr)

