class InternalException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        
        
class ExternalException(Exception):
    def __init__(self, message: str, orig_exception: Exception):
        self.message = f"{message}: {orig_exception}"
        self.orig_exception = orig_exception
        super().__init__(self.message)
