from logging import logger

class CustomException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        
    def log_error(self):
        logger.error(self.message)


class LoadFileException(CustomException):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        
        
