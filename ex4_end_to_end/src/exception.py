import logging
import sys
# this below import will work because whenever we import some module in python
# then python create one variable with that name, so in logger class we import the logging and it creates one variable
# there, so now we are able to import like this:
from ex4_end_to_end.src.logger import logging



def error_message_details(error):
    # this argument error and sys.exc_info will refer same exception
    # this is a good practice to pass error as an argument
    # we can use the error argument to print the exact error and use the sys for line number and class name, etc.

    exc_type, exc_value, exc_traceback = sys.exc_info()
    file_name = exc_traceback.tb_frame.f_code.co_filename
    line_number = exc_traceback.tb_lineno

    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(file_name, line_number, error)

    logging.info(error_message)
    #logging.exception(exc_traceback)
    # or we can use this below also
    logging.error(exc_traceback, exc_info=True)
    return error_message


class CustomException(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)
        # below line will create dynamic instance variable.
        self.error_message = error_message_details(error_message)

    def __str__(self):
        return self.error_message
