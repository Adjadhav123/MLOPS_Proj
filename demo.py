from src.logger import logging

logging.info("Creating necessary directories and files as per the template...")
logging.debug("This is a debug message to trace the execution flow.")
logging.warning("This is a warning message to indicate a potential issue.")


from src.logger import configure_logger
from src.exception import MyException 
import os 
import sys 

try:
    a=1+'z'
except Exception as e:
    logging.info(e)
    raise MyException(e,sys) from e 
