import sys
import logging 

def error_message_detail(error: Exception, error_detail:sys)-> str:
    """Extracts the error message and details from an exception."""
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename 

    line_number = exc_tb.tb_lineno

    error_message = f"Error occurred in script: [{file_name}] at line number: [{line_number}] with message: [{str(error)}]"
    logging.error(error_message)
    return error_message


class MyException(Exception):
    """Custom exception class that inherits from the built-in Exception class."""
    
    def __init__(self, error_message: str, error_detail: sys):
        """Initializes the custom exception with an error message and details."""
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        """Returns the string representation of the custom exception."""
        return self.error_message