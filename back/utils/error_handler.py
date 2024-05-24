from functools import wraps
from utils.exceptions import InternalException, ExternalException


def log_error(logger):
    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except InternalException as e:
                e.log_error()
                raise e
            except ExternalException as e:
                logger.error(e.message)
                raise e.original_exception

        return wrapper

    return decorator
