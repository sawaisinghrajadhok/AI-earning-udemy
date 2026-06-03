import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(), "logs")
os.makedirs(log_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)
logging.basicConfig(
    format="[ %(asctime)s ] - %(filename)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),  # Used to print in the file
        logging.StreamHandler()                # used to print on the console.
    ]

)

logging.info("Logging has started . . . .")

