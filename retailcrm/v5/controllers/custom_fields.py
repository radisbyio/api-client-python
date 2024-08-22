from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.api.custom_fields import RetailCrmCustomFieldsApi
from retailcrm.v5.schemas.custom_fields import (
    CustomDictionariesResponse,
    CustomDictionaryFilter,
    CustomFieldFilter,
    CustomFieldsResponse,
)
from retailcrm.v5.utils import pydantic_to_nested_dict


class CustomFieldsController:
    def __init__(self, client: BaseHttpClient):
        self._api = RetailCrmCustomFieldsApi(client)

    async def custom_fields(
        self, filter_data: CustomFieldFilter, limit: int = 20, page: int = 1
    ) -> CustomFieldsResponse:
        response = await self._api.get_all(
            filter_dict=pydantic_to_nested_dict(filter_data, "filter"),
            limit=limit,
            page=page,
        )
        response_obj = CustomFieldsResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def dictionaries(
        self, filter_data: CustomDictionaryFilter, limit: int = 20, page: int = 1
    ) -> CustomDictionariesResponse:
        response = await self._api.dictionaries(
            filter_dict=pydantic_to_nested_dict(filter_data, "filter"),
            limit=limit,
            page=page,
        )
        response_obj = CustomDictionariesResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj
