import decimal

from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.api.orders import RetailCrmOrdersApi
from retailcrm.v5.enums import CombineTechniqueTypes, IdTypes
from retailcrm.v5.schemas import (
    ResponseCreateOrder,
    ResponseCreateOrderPayment,
    ResponseDeleteOrderPayment,
    ResponseEditOrder,
    ResponseEditOrderPayment,
    ResponseGetOrder,
    ResponseOrderHistory,
    ResponseOrders,
    ResponseOrdersUpload,
    OrderRetrieveResponse,
    SerializedEntityOrder, LoyaltyApplyResponse, LoyaltyCancelBonusOperationsResponse,
)
from retailcrm.v5.schemas.orders import (
    OrderFilterData,
    OrderHistoryFilterV4Type,
    SerializedOrder,
    SerializedOrderList,
    SerializedOrderReference,
    SerializedPayment,
)
from retailcrm.v5.utils import pydantic_to_nested_dict


class OrdersController:
    def __init__(self, client: BaseHttpClient):
        self._api = RetailCrmOrdersApi(client) # TODO: Remove
        self._client = client

    async def get(self, order_id: int | str, site: str | None = None, by: IdTypes | str = IdTypes.EXTERNAL_ID) -> OrderRetrieveResponse:
        """
        Получение информации о заказе.
        Для доступа к методу необходимо разрешение order_read.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-orders-externalId
        :param order_id: Внутренний или внешний ИД заказа
        :param site: Код магазина
        :param by: Указывается, что передается в параметре id: внутренний (by=id) или внешний (by=externalId) ID платежа. По умолчанию externalId.
        :return: Response
        """
        params = {}
        if site is not None:
            params["site"] = site
        if by is not None:
            params["by"] = by

        response = await self._client.get(
            endpoint=f"orders/{order_id}", params=params,
        )

        response_obj = OrderRetrieveResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def edit(
        self,
        order_id: int | str,
        order: SerializedOrder,
        site: str | None = None,
        by: IdTypes | str = IdTypes.EXTERNAL_ID
    ) -> ResponseEditOrder:
        params = {}
        if site is not None:
            params["site"] = site
        if by is not None:
            params["by"] = by
        data = {
            "order": order.model_dump_json(exclude_none=True, by_alias=True),
        }

        response =  await self._client.post(
            endpoint=f"/orders/{order_id}/edit",
            params=params,
            data=data,
        )
        response_obj = ResponseEditOrder.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(
                response.status_code, response_obj.errorMsg, response_obj.errors
            )
        return response_obj

    async def loyalty_apply(
        self,
        order_entity: SerializedEntityOrder,
        site: str,
        bonuses: decimal.Decimal,
    ) -> LoyaltyApplyResponse:
        """
        Применение бонусов по программе лояльности

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-loyalty-apply
        """
        json_data = {
            "site": site,
            "bonus": bonuses,
            "order": order_entity.model_dump_json(exclude_none=True, by_alias=True),
        }
        response = await self._client.post(
            endpoint="/orders/loyalty/apply",
            data=json_data
        )
        response_obj = LoyaltyApplyResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def loyalty_cancel_bonus_operations(
        self,
        order_entity: SerializedEntityOrder,
        site: str,
    ) -> LoyaltyCancelBonusOperationsResponse:
        json_data = {
            "site": site,
            "order": order_entity.model_dump_json(exclude_none=True, by_alias=True),
        }
        response = await self._client.post(
            endpoint="/orders/loyalty/cancel-bonus-operations",
            data=json_data
        )
        response_obj = LoyaltyCancelBonusOperationsResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def create_order(
        self, order: SerializedOrder, site: str
    ) -> ResponseCreateOrder:
        response = await self._api.create(
            order_json=order.model_dump_json(exclude_unset=True, by_alias=True),
            site=site,
        )
        response_obj = ResponseCreateOrder.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(
                response.status_code, response_obj.errorMsg, response_obj.errors
            )
        return response_obj

    async def upload(
        self, orders: SerializedOrderList, site: str
    ) -> ResponseOrdersUpload:
        if len(orders.root) > 50:
            raise ValueError("Too many orders, only 50 are allowed")
        response = await self._api.upload(
            orders_json=orders.model_dump_json(exclude_unset=True, by_alias=True),
            site=site,
        )
        response_obj = ResponseOrdersUpload.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def get_order_by_id(
        self, order_id: str, site: str, id_type: IdTypes = IdTypes.EXTERNAL_ID
    ) -> ResponseGetOrder:
        response = await self._api.get_by_id(
            order_id=order_id, by=id_type.value, site=site
        )
        response_obj = ResponseGetOrder.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def get_orders(
        self, filter_obj: OrderFilterData, limit: int = 20, page: int = 1
    ) -> ResponseOrders:
        response = await self._api.get_all(
            filter_dict=pydantic_to_nested_dict(filter_obj, "filter"),
            limit=limit,
            page=page,
        )
        response_obj = ResponseOrders.model_validate_json(response.body)
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
        response = await self._api.edit(
            order_json=order.model_dump_json(exclude_unset=True, by_alias=True),
            order_id=order_id,
            by=id_type.value,
            site=site,
        )
        response_obj = ResponseEditOrder.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(
                response.status_code, response_obj.errorMsg, response_obj.errors
            )
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
            raise RetailCrmApiError(
                response.status_code, response_obj.errorMsg, response_obj.errors
            )
        return response_obj

    async def payment_delete(self, payment_id: str) -> ResponseDeleteOrderPayment:
        response = await self._api.payment_delete(payment_id=payment_id)
        response_obj = ResponseDeleteOrderPayment.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def get_orders_history(
        self, filter_obj: OrderHistoryFilterV4Type, limit: int = 20, page: int = 1
    ) -> ResponseOrderHistory:
        response = await self._api.history(
            filter_dict=pydantic_to_nested_dict(filter_obj, "filter"),
            limit=limit,
            page=page,
        )
        response_obj = ResponseOrderHistory.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def combine(
        self,
        order: SerializedOrderReference,
        result_order: SerializedOrderReference,
        technique: CombineTechniqueTypes,
    ):
        response = await self._api.combine(
            order_json=order.model_dump_json(exclude_unset=True, by_alias=True),
            result_order_json=result_order.model_dump_json(
                exclude_unset=True, by_alias=True
            ),
            technique=technique.value,
        )
        response_obj = ResponseOrderHistory.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj
