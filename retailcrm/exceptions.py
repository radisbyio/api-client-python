from typing import Optional

from retailcrm.v5.schemas.base import ErrorResponse


class RetailCrmException(Exception):
    pass


class RetailCrmTimeoutException(RetailCrmException):
    def __str__(self):
        return "Timeout exception"


class RetailCrmUnauthorizedError(RetailCrmException):
    def __str__(self):
        return "Invalid api key"


class RetailCrmApiError(RetailCrmException):
    def __init__(
        self,
        status_code: int,
        error_msg: str | None = None,
        errors: Optional[dict] = None,
        response: ErrorResponse = None,
    ):
        self.status_code = status_code
        self.error_msg = error_msg
        self.errors = errors or {}
        self.response = response

    def __str__(self) -> str:
        if self.errors:
            return f"{self.error_msg} - {self.errors or str()}"
        return f"{self.error_msg}"
