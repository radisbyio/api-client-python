from retailcrm import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.api.references import RetailCrmReferencesApi
from retailcrm.v5.schemas.references import ResponseStatuses, ResponseStatusGroups
from dataclasses import dataclass


@dataclass(slots=True)
class ReferencesController:
    _api: RetailCrmReferencesApi

    def __init__(self, client: BaseHttpClient):
        self._api = RetailCrmReferencesApi(client)

    async def status_groups(self) -> ResponseStatusGroups:
        response = await self._api.status_groups()
        response_obj = ResponseStatusGroups.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def statuses(self) -> ResponseStatuses:
        response = await self._api.statuses()
        response_obj = ResponseStatuses.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj
