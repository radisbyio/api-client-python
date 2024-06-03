from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.utils import pydantic_to_nested_dict
from retailcrm.v5.api.orders import RetailCrmOrdersApi
from retailcrm.v5.enums import IdTypes
from retailcrm.v5.schemas.requests.orders import SerializedOrder, SerializedPayment, OrderHistoryFilterV4Type
from retailcrm.v5.schemas.responses.orders import (
    ResponseCreateOrder,
    ResponseCreateOrderPayment,
    ResponseDeleteOrderPayment,
    ResponseEditOrder,
    ResponseEditOrderPayment,
    ResponseGetOrder, ResponseOrderHistory,
)


class OrdersController:
    def __init__(self, client: BaseHttpClient):
        self._api = RetailCrmOrdersApi(client)

    async def create_order(
            self, order: SerializedOrder, site: str
    ) -> ResponseCreateOrder:
        response = await self._api.order_create(
            order_json=order.model_dump_json(exclude_unset=True, by_alias=True),
            site=site,
        )
        response_obj = ResponseCreateOrder.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def get_order(
            self, order_id: str, site: str, id_type: IdTypes = IdTypes.EXTERNAL_ID
    ) -> ResponseGetOrder:
        response = await self._api.order(order_id=order_id, by=id_type.value, site=site)
        response_obj = ResponseGetOrder.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def get_orders(
            self, filter: object, limit: int = 20, page: int = 1
    ) -> ResponseGetOrder:
        response = await self._api.orders(
            filter_json=filter.model_dump_json(exclude_unset=True, by_alias=True),
            limit=limit,
            page=page,
        )
        response_obj = ResponseGetOrder.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def edit_order(
            self,
            order_id: str,
            order: SerializedOrder,
            site: str,
            id_type: IdTypes = IdTypes.EXTERNAL_ID,
    ) -> ResponseEditOrder:
        response = await self._api.order_edit(
            order_json=order.model_dump_json(exclude_unset=True, by_alias=True),
            order_id=order_id,
            by=id_type.value,
            site=site,
        )
        response_obj = ResponseEditOrder.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def payment_create(
            self, payment: SerializedPayment, site: str
    ) -> ResponseCreateOrderPayment:
        response = await self._api.payment_create(
            payment_json=payment.model_dump_json(exclude_unset=True, by_alias=True),
            site=site,
        )
        response_obj = ResponseCreateOrderPayment.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def payment_edit(
            self,
            payment_id: str,
            payment: SerializedPayment,
            site: str,
            id_type: IdTypes = IdTypes.EXTERNAL_ID,
    ) -> ResponseEditOrderPayment:
        response = await self._api.payment_edit(
            payment_id=payment_id,
            payment_json=payment.model_dump_json(exclude_unset=True, by_alias=True),
            by=id_type.value,
            site=site,
        )
        response_obj = ResponseEditOrderPayment.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def payment_delete(self, payment_id: str) -> ResponseDeleteOrderPayment:
        response = await self._api.payment_delete(payment_id=payment_id)
        response_obj = ResponseDeleteOrderPayment.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def orders_history(self, filter_obj: OrderHistoryFilterV4Type, limit: int = 20,
                             page: int = 1) -> ResponseOrderHistory:
        response = await self._api.orders_history(
            filter_dict=pydantic_to_nested_dict(filter_obj, "filter"),
            limit=limit,
            page=page,
        )
        response_obj = ResponseOrderHistory.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj
