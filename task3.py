class BaseCustomException(Exception):
    def __init__(self, message, error_code=501):
        self.message = message
        self.error_code = error_code

    def __str__(self):
        return f"Error Code: {self.error_code}\nMessage: {self.message}"


class LevelError(BaseCustomException):
    def __str__(self):
        print(self.message)
        return "False"


class AccessError(BaseCustomException):
    pass

class IOUserError(BaseCustomException):
    pass
