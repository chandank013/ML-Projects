# import sys
# import logging


# def error_message_detail(error,error_detail:sys):
#     _,_,exc_tb=error_detail.exc_info()
#     file_name=exc_tb.tb_frame.f_code.co_filename
#     error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
#     file_name,exc_tb.tb_lineno,str(error)

#     )
#     return error_message


# class CustomException(Exception):
#     def __init__(self, error_message,error_detail:sys):
#         super().__init__(error_message)
#         self.error_message=error_message_detail(error_message,error_detail=error_detail)

#     def __str__(self):
#         return self.error_message
    


    
# if __name__=="__main__":

#     try:
#         x = 1 / 0
#     except Exception as e:
#         logging.info("Division by zero is not possible")
#         raise CustomException(e, sys)


import sys
import logging
import os
from datetime import datetime


def error_message_detail(error, error_detail):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "<unknown file>"
    line_number = exc_tb.tb_lineno if exc_tb else "?"
    return (
        f"Error occurred in python script name [{file_name}] "
        f"line number [{line_number}] "
        f"error message [{error}]"
    )


class CustomException(Exception):
    def __init__(self, error, error_detail):
        super().__init__(str(error))  # keep base Exception behavior
        self.error_message = error_message_detail(error, error_detail)

    def __str__(self):
        return self.error_message


if __name__ == "__main__":
    # Create logs folder if it doesn’t exist
    logs_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(logs_dir, exist_ok=True)

    # Log file name with timestamp
    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

    # Configure logging
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s - %(message)s",
    )
