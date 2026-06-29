from typing import Dict
from fastapi import APIRouter
from ex4_end_to_end.src.api.services.student_service import StudentService
from ex4_end_to_end.src.logger import logging

student_router = APIRouter(
    prefix="/students",
    tags=["Student"]
)

student_service = StudentService()


@student_router.get("")
def home():
    logging.info("Request hits at controller level")
    return student_service.home()


@student_router.get("/student-json-data")
def with_json_type_response():
    logging.info("Request hits at controller level")
    return student_service.with_json_type_response()


@student_router.post("/data-post")
def data_post(request_data: Dict):  # here Dict is required otherwise FastAPI consider this request_data as a query parameter.
    logging.info("Request hits at controller level")
    return student_service.data_post(request_data)
