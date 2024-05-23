from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.api.customers import RetailCrmCustomersApi
from retailcrm.v5.schemas.requests.customers import CustomerFilterData
from retailcrm.v5.schemas.responses.customers import ResponseCustomers


class CustomersController:
    def __init__(self, client: BaseHttpClient):
        self._api = RetailCrmCustomersApi(client)

    async def customers(
        self, filter_data: CustomerFilterData, limit: int = 20, page: int = 1
    ) -> ResponseCustomers:
        response = await self._api.customers(
            filter_json=filter_data.model_dump_json(exclude_unset=True, by_alias=True),
            limit=limit,
            page=page,
        )
        response_obj = ResponseCustomers.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj
