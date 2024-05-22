class RetailCrmException(Exception):
    pass


class RetailCrmTimeoutException(RetailCrmException):
    def __str__(self):
        return "Timeout exception"


class RetailCrmApiError(RetailCrmException):
    def __init__(self, status_code: int, error_msg: str):
        self.status_code = status_code
        self.error_msg = error_msg

    def __str__(self) -> str:
        return f"{self.status_code} - {self.error_msg}"


class RetailCrmUnauthorizedError(RetailCrmException):
    def __str__(self):
        return "Invalid api key"
