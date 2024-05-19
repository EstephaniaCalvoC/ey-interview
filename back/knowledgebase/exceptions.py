from utils.exceptions import InternalException


class NoFilesToLoadException(InternalException):
    def __init__(self, local_path: str):
        super().__init__(f"No files into {local_path}")