from fastapi import FastAPI
from .controllers.welcome_controller import welcome_router
from .controllers.student_controller import student_router
from .controllers.predict_controller import predict_router

app = FastAPI()

app.include_router(welcome_router)
app.include_router(student_router)
app.include_router(predict_router)
