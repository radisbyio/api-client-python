class RetailCrmException(Exception):
    pass


class RetailCrmTimeoutException(RetailCrmException):
    def __str__(self):
        return "Timeout exception"


class RetailCrmApiError(RetailCrmException):
    def __init__(self, status_code: int, error_msg: str, errors: dict = None):
        self.status_code = status_code
        self.error_msg = error_msg
        self.errors = errors or {}

    def __str__(self) -> str:
        if self.errors:
            return f"{self.error_msg} - {self.errors or str()}"
        return f"{self.error_msg}"


class RetailCrmUnauthorizedError(RetailCrmException):
    def __str__(self):
        return "Invalid api key"
