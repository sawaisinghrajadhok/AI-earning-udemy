import os
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor
from ex4_end_to_end.src import utils
from ex4_end_to_end.src.exception import CustomException
from ex4_end_to_end.src.logger import logging

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifact", "model.pkl")


class ModelTrainer:
    def __int__(self):
        model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            # split input and target columns from the test and train data

            x_train, x_test, y_train, y_test = (
                train_array[:, :-1],
                test_array[:, :-1],
                train_array[:, -1],
                test_array[:, -1]
            )


            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbors Regression": KNeighborsRegressor(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting": CatBoostRegressor(verbose=False),
                "AdaBoost": AdaBoostRegressor()
            }

            model_reports = utils.evaluate_models(x_train, x_test, y_train, y_test, models)
            logging.info(f"Model name with r2 score {model_reports}")

            # finding best model score
            best_model_score = max(model_reports.values())

            # finding best model name on basis of the score
            best_model_name = list(model_reports.keys())[
                list(model_reports.values()).index(best_model_score)
            ]

            logging.info(f"Best model name: {best_model_name} with score: {best_model_score}")

            # if best model score is < .6 then this no model is best fit for this
            if best_model_score < 0.6:
                logging.info(f"No model is perfect for given dataset.")
            else:
                logging.info(f"Storing model into the model.pkl file")
                best_model = model_reports[best_model_name]
                utils.save_object(ModelTrainerConfig.trained_model_file_path, best_model)
                logging.info(f"model file stored successfully at: {ModelTrainerConfig.trained_model_file_path}")
        except Exception as e:
            raise CustomException(e)

