import os
import pandas as pd
import numpy as np
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

from ex4_end_to_end.src import utils
from ex4_end_to_end.src.logger import logging
from ex4_end_to_end.src.exception import CustomException



@dataclass
class DataTransformationConfig:
    # here we are creating one pickle file, pickle file is used to serialize in python.
    # so that we can save an object onto disk  and read back whenever required.
    preprocessor_obj_file_path = os.path.join('artifact', "preprocessor.pkl")


class DataTransformation:
    def __int__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
            this function is responsible for data transformation.
        '''
        try:
            numeric_feature_columns = ["writing score", "reading score"]
            category_feature_columns = [
                "gender",
                "race/ethnicity",
                "parental level of education",
                "lunch",
                "test preparation course"
            ]

            numeric_feature_pipeline = Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="mean")),
                    ("scalar", StandardScaler())
                ]
            )

            category_feature_pipeline = Pipeline(
                [
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder())
                ]
            )

            logging.info("pipelines defined for the numeric and category fields.")
            logging.info("initializing the data transformation process.")

            preprocessor = ColumnTransformer(
                [
                    ("numeric_feature_pipeline", numeric_feature_pipeline, numeric_feature_columns),
                    ("category_feature_pipeline", category_feature_pipeline, category_feature_columns)
                ]
            )
            return preprocessor
        except Exception as e:
            raise CustomException(e)


    def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info(f"start reading the test and train data from csv")
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)
            logging.info(f"read the test and train data from csv")

            logging.info("target column extraction from train and test dataset process initiated")
            target_column_name = "math score"
            input_feature_train_df = train_data.drop([target_column_name], axis=1)
            target_feature_train_df = train_data[target_column_name]

            input_feature_test_df = test_data.drop([target_column_name], axis=1)
            target_feature_test_df = test_data[target_column_name]
            logging.info("target column extraction from train and test dataset process completed")

            logging.info("applying preprocessing pipeline on the objects")
            preprocessing_obj = self.get_data_transformer_object()

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)

            # we never apply fit_transform on the test data, because fit means learning for model, and if model learns from the test data
            # then this is called data leakage.
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            # save pre processor as pkl file.
            logging.info("saving the pre processor as pkl file")
            utils.save_preprocessor(preprocessing_obj, DataTransformationConfig.preprocessor_obj_file_path)
            logging.info("pre processor saved pkl file into disk")

            # Let's add target column also in above data frames or arrays.
            # np.c_ is used for the concating the array into the last column.
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            return train_arr, test_arr, DataTransformationConfig.preprocessor_obj_file_path
        except Exception as e:
            raise CustomException(e)

