from typing import TypeVar

from retailcrm import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.response import Response
from retailcrm.v5.schemas.base import ErrorResponse, SuccessResponse

T = TypeVar("T", bound=SuccessResponse)


class ApiResource:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    def _process_response(self, response: Response, schema: type[T]) -> T:
        response_obj = schema.model_validate_json(response.body)
        if response.status_code >= 400:
            error_response = ErrorResponse.model_validate_json(response.body)
            raise RetailCrmApiError(
                status_code=response.status_code,
                error_msg=error_response.errorMsg,
                errors=error_response.errors,
                response=error_response,
            )
        return response_obj
