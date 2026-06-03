import pandas as pd
import numpy as np
from pandas import DataFrame
from sklearn.linear_model import Lasso, Ridge, LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from ex3_end_to_end.src.logger import logging
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from catboost import CatBoostRegressor

# in this dataset we have these columns
# gender","race/ethnicity","parental level of education","lunch","test preparation course","math score","reading score","writing score"
# we need to check how the scores are effected by the gender, test_preparation, etc.

df = pd.read_csv("../../data_files/StudentsPerformance.csv")


# Step-1: let's first check the null values in the dataset and if exist then remove
def check_and_clear_null_values(data_frame: DataFrame):
    logging.info("=============entered into the check_and_clear_null_values method================")
    # this is how we can check for individual columns
    #print(data_frame["gender"].isna())

    logging.debug(data_frame.isna().sum())
    return data_frame


# Step-2: checking duplicate records
def check_and_remove_duplicate(data_frame: DataFrame):
    logging.info("=============entered into the check_and_remove_duplicate method================")
    logging.debug(data_frame.duplicated())

    # checking if duplicate record exists then that should be removed.
    if data_frame.duplicated().sum() > 0:
        data_frame.drop_duplicates()

    return data_frame


def print_data_info(data_frame: DataFrame):
    logging.info("=============entered into the print_data_info method================")
    logging.debug(data_frame.info())


def describe_data_frame(data_frame: DataFrame):
    logging.info("=============entered into the describe_data_info method================")
    logging.debug(data_frame.describe())


def explore_data_frame(data_frame: DataFrame):
    logging.info("=============entered into the explore_data_frame method================ \n\n\n")

    for column in data_frame.columns:
        possible_values = data_frame[column].unique()
        logging.info(f"column: {column} \n Possible values: {possible_values.tolist()} \n\n")


def add_total_and_average_marks(data_frame: DataFrame):
    logging.info("=============entered into the add_total_and_average_marks method================ \n\n\n")
    data_frame["total"] = data_frame["math score"] + data_frame["reading score"] + data_frame["writing score"]
    data_frame["average"] = data_frame["total"] / 3
    logging.debug(data_frame)
    return data_frame


def column_transformation(data_frame: DataFrame):
    # we will predict this so this is our Y
    x = data_frame.drop("math score", axis=1)

    # fetch numeric value column and non numeric value column
    numeric_features = x.select_dtypes(exclude=["object", "str"]).columns
    non_numeric_features = x.select_dtypes(include=["object", "str"]).columns

    one_hot_encoder = OneHotEncoder()
    standard_scaler = StandardScaler()

    transformer = ColumnTransformer([
        ("OneHotEncoder", one_hot_encoder, non_numeric_features),
        ("StandardScaler", standard_scaler, numeric_features)
    ])

    print(type(transformer))
    return transformer.fit_transform(x)


def evaluate_model(true, predicted):
    mae = mean_absolute_error(true, predicted)
    mse = mean_squared_error(true, predicted)
    rmse = np.sqrt(mean_squared_error(true, predicted))
    r2_squar = r2_score(true, predicted)
    return mae, rmse, r2_squar


df = check_and_clear_null_values(df)
df = check_and_remove_duplicate(df)
print_data_info(df)
describe_data_frame(df)
explore_data_frame(df)
x = column_transformation(df)
y = df["math score"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print(x_train.shape)
print(x_test.shape)

models = {
    "Linear Regression": LinearRegression(),
    "Lasso": Lasso(),
    "Ridge": Ridge(),
    "K-Neighbor": KNeighborsRegressor(),
    "Decision Tree": DecisionTreeRegressor(),
    "CatBoosting Regressor": CatBoostRegressor()
}

model_list = []
r2_list = []

for i in range(len(list(models))):
    model = list(models.values())[i]
    model.fit(x_train, y_train) # train the model

    # Make predictions
    y_train_pred = model.predict(x_train)
    y_test_pred = model.predict(x_test)

    # evaluate Train the Test dataset
    model_train_mae, model_train_mse, model_train_r2 = evaluate_model(y_train, y_train_pred)
    model_test_mae, model_test_mse, model_test_r2 = evaluate_model(y_test, y_test_pred)

    print(list(models.keys())[i])
    model_list.append(list(models.keys())[i])

    print("model performance for training set")
    print("- Root Mean Squared Error: {:.4f}".format(model_train_mse))
    print("- Mean Absolute Error: {:.4f}".format(model_train_mae))
    print("- R2 Score: {:.4f}".format(model_train_r2))
    print("------------------------------------------------------------")
    print("model performance for test set")
    print("- Root Mean Squared Error: {:.4f}".format(model_test_mse))
    print("- Mean Absolute Error: {:.4f}".format(model_test_mae))
    print("- R2 Score: {:.4f}".format(model_test_r2))

    r2_list.append(model_train_r2)
    print('='*35)
    print("\n")
