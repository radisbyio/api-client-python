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
    SerializedCourier, ResponseOrderMethod, SerializedOrderMethod, SerializedOrderType, ResponseOrderTypes,
    SerializedPaymentStatus, ResponsePaymentStatuses, ResponsePaymentTypes, SerializedPaymentType, ResponsePriceTypes,
    SerializedPriceType, ResponseProductStatuses, SerializedOrderProductStatus, ResponseSites, SerializedSite,
    ResponseSitesEdit,
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

    # TODO: Realize legal-entities
    # TODO: Realize legal-entities edit
    # TODO: Realize mg-channels

    async def order_methods(self) -> ResponseOrderMethod:
        response = await self._api.order_methods()
        response_obj = ResponseOrderMethod.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def order_methods_edit(
            self, code: str, order_method: SerializedOrderMethod
    ) -> RetailCrmResponse:
        response = await self._api.order_methods_edit(
            code=code, order_method_json=order_method.model_dump_json(exclude_unset=True)
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def order_types(self) -> ResponseOrderTypes:
        response = await self._api.order_types()
        response_obj = ResponseOrderTypes.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def order_types_edit(
            self, code: str, order_type: SerializedOrderType
    ) -> RetailCrmResponse:
        response = await self._api.order_types_edit(
            code=code, order_type_json=order_type.model_dump_json(exclude_unset=True)
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def payment_statuses(self) -> ResponsePaymentStatuses:
        response = await self._api.payment_statuses()
        response_obj = ResponsePaymentStatuses.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def payment_statuses_edit(
            self, code: str, payment_status: SerializedPaymentStatus
    ) -> RetailCrmResponse:
        response = await self._api.payment_statuses_edit(
            code=code, payment_status_json=payment_status.model_dump_json(exclude_unset=True)
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def payment_types(self) -> ResponsePaymentTypes:
        response = await self._api.payment_types()
        response_obj = ResponsePaymentTypes.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def payment_types_edit(
            self, code: str, payment_type: SerializedPaymentType
    ) -> RetailCrmResponse:
        response = await self._api.payment_types_edit(
            code=code, payment_type_json=payment_type.model_dump_json(exclude_unset=True)
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def price_types(self) -> ResponsePriceTypes:
        response = await self._api.price_types()
        response_obj = ResponsePriceTypes.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def price_types_edit(
            self, code: str, price_type: SerializedPriceType
    ) -> RetailCrmResponse:
        response = await self._api.price_types_edit(
            code=code, price_type_json=price_type.model_dump_json(exclude_unset=True)
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def product_statuses(self) -> ResponseProductStatuses:
        response = await self._api.product_statuses()
        response_obj = ResponseProductStatuses.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def product_statuses_edit(
            self, code: str, product_status: SerializedOrderProductStatus
    ) -> RetailCrmResponse:
        response = await self._api.product_statuses_edit(
            code=code, product_status_json=product_status.model_dump_json(exclude_unset=True)
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def sites(self) -> ResponseSites:
        response = await self._api.sites()
        response_obj = ResponseSites.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def sites_edit(
            self, code: str, site: SerializedSite
    ) -> ResponseSitesEdit:
        response = await self._api.sites_edit(
            code=code, sites_json=site.model_dump_json(exclude_unset=True)
        )
        response_obj = ResponseSitesEdit.model_validate_json(response.body)
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

    # TODO: Realize stores
    # TODO: Realize stores edit
    # TODO: Realize units
