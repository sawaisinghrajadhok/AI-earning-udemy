to run this project first execute the DataIngestion.py class this will train the model and generate the model.pkl and preprocessor.pkl files

after that run the FastAPI using this command: /PycharmProjects/AI-learning$ uvicorn ex4_end_to_end.src.api.main:app --reload

then pass the data to predict using the api mentioned in the postman collection.txt file

