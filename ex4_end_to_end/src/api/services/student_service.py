from typing import Dict


class StudentService:

    def data_post(self, request_data: Dict):  # here Dict is required otherwise FastAPI consider this request_data as a query parameter.
        print('data received in the request body: ', request_data)
        return request_data


    def home(self):
        return "Welcome to the flask student api"


    def with_json_type_response(self):
        return {
            'name': 'sawai',
            'age': 30,
            'gender': 'M'
        }
