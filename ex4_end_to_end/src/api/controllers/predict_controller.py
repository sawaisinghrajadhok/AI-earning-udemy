from typing import Dict
from fastapi import APIRouter
import pandas as pd

from ex4_end_to_end.src import utils
from ex4_end_to_end.src.exception import CustomException
from ex4_end_to_end.src.pipeline.predict_pipeline import PredictPipeline

predict_router = APIRouter(
    prefix="/predict",
    tags=["Predict"]
)


def get_data_as_data_frame(request_data: Dict):
    df = pd.DataFrame([request_data])
    print("data as data frame: ", df)
    return df


@predict_router.post("")
def predict(request_data: Dict):
    try:
        print("request data: ", request_data)
        features = get_data_as_data_frame(request_data)
        predict_pipeline = PredictPipeline()
        model = predict_pipeline.load_model_file()
        preprocessor = predict_pipeline.load_preprocessor_file()
        scaled_data = preprocessor.transform(features)
        prediction = model.predict(scaled_data)
        return {"prediction": float(prediction[0])}
    except Exception as e:
        raise CustomException(e)

