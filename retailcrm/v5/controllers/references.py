from dataclasses import dataclass

from retailcrm import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.api.references import RetailCrmReferencesApi
from retailcrm.v5.schemas.base import RetailCrmResponse
from retailcrm.v5.schemas.references import (
    ResponseCostGroups,
    ResponseCostItems,
    ResponseCountries,
    ResponseCouriers,
    ResponseStatuses,
    ResponseStatusGroups,
    SerializedCostGroup,
    SerializedCostItem,
    SerializedCourier,
)


@dataclass(slots=True)
class ReferencesController:
    _api: RetailCrmReferencesApi

    def __init__(self, client: BaseHttpClient):
        self._api = RetailCrmReferencesApi(client)

    async def cost_groups(self) -> ResponseCostGroups:
        response = await self._api.cost_groups()
        response_obj = ResponseCostGroups.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def cost_groups_edit(
        self, code: str, cost_group: SerializedCostGroup
    ) -> RetailCrmResponse:
        response = await self._api.cost_groups_edit(
            code=code, cost_group_json=cost_group.model_dump_json(exclude_unset=True)
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def cost_items(self) -> ResponseCostItems:
        response = await self._api.cost_items()
        response_obj = ResponseCostItems.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def cost_items_edit(
        self, code: str, cost_item: SerializedCostItem
    ) -> RetailCrmResponse:
        response = await self._api.cost_items_edit(
            code=code, cost_item_json=cost_item.model_dump_json(exclude_unset=True)
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def countries(self) -> ResponseCountries:
        response = await self._api.countries()
        response_obj = ResponseCountries.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def couriers(self) -> ResponseCouriers:
        response = await self._api.couriers()
        response_obj = ResponseCouriers.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def couriers_create(self, courier: SerializedCourier) -> RetailCrmResponse:
        response = await self._api.couriers_create(
            courier_json=courier.model_dump_json(exclude_unset=True)
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def couriers_edit(
        self, courier_id: int, courier: SerializedCourier
    ) -> RetailCrmResponse:
        response = await self._api.couriers_edit(
            courier_id=courier_id,
            courier_json=courier.model_dump_json(exclude_unset=True),
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

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
