import os
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from ex4_end_to_end.src.exception import CustomException


def save_preprocessor(preprocessing_obj, preprocessor_obj_file_path):
    try:
        print(preprocessor_obj_file_path)
        with open(preprocessor_obj_file_path, "wb") as file_obj:
            # dill is the new library used to store the files.
            dill.dump(preprocessing_obj, file_obj)
    except Exception as e:
        raise CustomException(e)


def evaluate_models(x_train, x_test, y_train, y_test, models: dict, hyper_params):
    try:
        reports = {}
        for i in range(len(list(models.values()))):
            model = list(models.values())[i]
            hyper_param = hyper_params[list(hyper_params.keys())[i]]

            gs = GridSearchCV(model, hyper_param, cv=3)
            gs.fit(x_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(x_train, y_train) # train model

            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            reports[list(models.keys())[i]] = test_model_score

        return reports
    except Exception as e:
        raise CustomException(e)


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e)




def load_pkl_file(file_path):
    try:
        print("====================================================")
        print("loading this file ", file_path)
        with open(file_path, "rb") as file_obj:
            obj = dill.load(file_obj)
            print("data type ============================================", type(obj))
            print(obj)
            return obj
    except Exception as e:
        raise CustomException(e)


