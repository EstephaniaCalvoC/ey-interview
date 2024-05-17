from exceptions import CustomException
from logging import logger

def handle_error(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except CustomException as e:
            e.log_error()
        except Exception as e:
            logger.error(e)
    return wrapper