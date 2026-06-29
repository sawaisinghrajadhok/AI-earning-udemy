from typing import Dict

from fastapi import APIRouter


welcome_router = APIRouter(
    prefix="/welcome",
    tags=["Welcome"]
)


@welcome_router.get("")
def home():
    return "Welcome to the fast welcome api"


@welcome_router.get("/welcome-json-data")
def with_json_type_response():
    return {
        'name': 'sawai',
        'age': 30,
        'gender': 'M'
    }


@welcome_router.post("/data-post")
def data_post(request_data: Dict):  # here Dict is required otherwise FastAPI consider this request_data as a query parameter.
    print('data received in the request body: ', request_data)
    return request_data
