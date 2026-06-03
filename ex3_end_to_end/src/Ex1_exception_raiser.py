from ex3_end_to_end.src.exception import CustomException

try:
    print("hello this is a calculator program")
    value = 50/0

except Exception as e:
    CustomException(e)
