from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.api.customers import RetailCrmCustomersApi
from retailcrm.v5.enums import IdTypes
from retailcrm.v5.schemas.customers import (
    CustomerFilterData,
    ResponseCustomerCreate,
    SerializedCustomer, GetByIdCustomerResponse, ResponseCustomerEdit,
)
from retailcrm.v5.schemas.customers import ResponseCustomersGetAll
from retailcrm.v5.utils import pydantic_to_nested_dict


class CustomersController:
    def __init__(self, client: BaseHttpClient):
        self._api = RetailCrmCustomersApi(client)

    async def customers(
            self, filter_data: CustomerFilterData, limit: int = 20, page: int = 1
    ) -> ResponseCustomersGetAll:
        filter_params = pydantic_to_nested_dict(filter_data, "filter")
        response = await self._api.customers(
            filter=filter_params,
            limit=limit,
            page=page,
        )
        response_obj = ResponseCustomersGetAll.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def get_by_id(self, customer_id: str, site: str = None,
                        by: IdTypes = IdTypes.EXTERNAL_ID) -> GetByIdCustomerResponse:
        response = await self._api.get_by_id(
            customer_id, site, by.value
        )
        response_obj = GetByIdCustomerResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def create(
            self, customer: SerializedCustomer, site: str
    ) -> ResponseCustomerCreate:
        response = await self._api.create(
            customer_json=customer.model_dump_json(exclude_unset=True, by_alias=True),
            site=site,
        )
        response_obj = ResponseCustomerCreate.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(
                response.status_code, response_obj.errorMsg, response_obj.errors
            )
        return response_obj

    async def edit(self, customer_id: str, customer: SerializedCustomer, site: str = None, by: IdTypes = IdTypes.EXTERNAL_ID) -> ResponseCustomerEdit:
        response = await self._api.edit(
            customer_id, customer.model_dump_json(exclude_none=True, by_alias=True), site, by.value
        )
        response_obj = ResponseCustomerEdit.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj
