from retailcrm.v5.enums.orders import CombineTechniqueTypes
from retailcrm.v5.resources.base import ApiResource


__all__ = ["OrdersApiResource"]

from retailcrm.v5.schemas import SuccessResponse
from retailcrm.v5.schemas.entities.orders import SerializedOrderReference, SerializedOrder

from retailcrm.v5.schemas.filters.orders import OrdersFilter, OrderHistoryFilterV4Type
from retailcrm.v5.schemas.base import IdTypesLiteral
from retailcrm.v5.schemas.requests.orders import OrdersFilterRequest, OrdersGetRequest, OrdersCombineRequest, \
    OrdersCreateRequest, FixExternalIdsRequest, OrdersHistoryRequest
from retailcrm.v5.schemas.responses.orders import OrdersFilterResponse, OrderGetResponse, OrdersCreateResponse, \
    OrdersHistoryResponse
from retailcrm.v5.schemas.shared.fix_external_row import FixExternalRow


class OrdersApiResource(ApiResource):
    async def filter(
            self, filter_obj: OrdersFilter, limit: int = 20, page: int = 1
    ) -> OrdersFilterResponse:
        """
        **Получение списка заказов, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-orders
        :param filter_obj: Объект фильтра
        :param limit: Количество заказов на странице (по умолчанию 20)
        :param page: Номер страницы с результатами (по умолчанию 1)
        :return: OrdersFilterResponse
        """
        request = OrdersFilterRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint="/orders",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, OrdersFilterResponse)

    async def combine(
        self,
        order: SerializedOrderReference,
        result_order: SerializedOrderReference,
        technique: CombineTechniqueTypes,
    ) -> SuccessResponse:
        """
        **Объединение заказов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-combine
        :param order: Объект исходного заказа
        :param result_order: Объект результирующего заказа
        :param technique: Техника объединения
        :return: OrdersCombineResponse
        """
        request = OrdersCombineRequest(
            order=order, resultOrder=result_order, technique=technique
        )
        response = await self._client.post(
            endpoint="/orders/combine",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, SuccessResponse)

    async def create(
        self, order: SerializedOrder, site: str
    ) -> OrdersCreateResponse:
        """
        **Создание заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-create
        :param order: Объект заказа
        :param site: Код магазина
        :return: OrdersCreateResponse
        """
        request = OrdersCreateRequest(order=order, site=site)
        response = await self._client.post(
            endpoint="/orders/create",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, OrdersCreateResponse)

    async def fix_external_ids(self, orders: list[FixExternalRow]) -> SuccessResponse:
        """
        Массовая запись внешних ID заказов
        Данный метод полезен в случае обратной синхронизации заказов, которые исходно оформлены в системе.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-fix-external-ids

        :param orders: Идентификаторы загруженных объектов
        :return: SuccessResponse
        """
        request = FixExternalIdsRequest(orders=orders)

        response = await self._client.post(
            endpoint=f"/orders/fix-external-ids",
            json_str=request.model_dump(exclude_none=True, by_alias=True)
        )

        return self._process_response(response, SuccessResponse)

    async def history(
        self, filter_obj: OrderHistoryFilterV4Type | None = None, limit: int = 20, page: int = 1
    ) -> OrdersHistoryResponse:
        """
        **Получение истории изменений по заказам**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-orders-history
        :param filter_obj: Объект фильтра
        :param limit: Количество заказов на странице (по умолчанию 20)
        :param page: Номер страницы с результатами (по умолчанию 1)
        :return: OrdersHistoryResponse
        """
        request = OrdersHistoryRequest(filter=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint="/orders/history",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, OrdersHistoryResponse)


    async def get(self, order_id: int | str, site: str | None = None, by: IdTypesLiteral | str = "externalId") -> OrderGetResponse:
        """
        Получение информации о заказе.
        Для доступа к методу необходимо разрешение order_read.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-orders-externalId
        :param order_id: Внутренний или внешний ИД заказа
        :param site: Код магазина
        :param by: Указывается, что передается в параметре id: внутренний (by=id) или внешний (by=externalId) ID платежа. По умолчанию externalId.
        :return: OrderRetrieveResponse
        """
        request = OrdersGetRequest(site=site, by=by)
        response = await self._client.get(
            endpoint=f"/orders/{order_id}",
            params=request.model_dump(exclude_none=True, by_alias=True)
        )
        return self._process_response(response, OrderGetResponse)

    async def edit(
        self,
        order_id: int | str,
        order: SerializedOrder,
        site: str | None = None,
        by: IdTypes | str = "externalId"
    ) -> OrdersEditResponse:
        """
        **Редактирование заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-externalId-edit
        :param order_id: Внутренний или внешний ИД заказа
        :param order: Объект заказа
        :param site: Код магазина
        :param by: Указывается, что передается в параметре id: внутренний (by=id) или внешний (by=externalId) ID платежа. По умолчанию externalId.
        :return: OrdersEditResponse
        """
        request = OrdersEditRequest(order=order, site=site, by=by)
        response =  await self._client.post(
            endpoint=f"/orders/{order_id}/edit",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, OrdersEditResponse)

    async def loyalty_apply(
        self,
        order_entity: SerializedEntityOrder,
        site: str,
        bonuses: decimal.Decimal,
    ) -> LoyaltyApplyResponse:
        """
        Применение бонусов по программе лояльности

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-loyalty-apply
        :param order_entity: Объект заказа
        :param site: Код магазина
        :param bonuses: Количество бонусов для применения
        :return: LoyaltyApplyResponse
        """
        request = LoyaltyApplyRequest(order=order_entity, site=site, bonus=bonuses)
        response = await self._client.post(
            endpoint="/orders/loyalty/apply",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True)
        )
        return self._process_response(response, LoyaltyApplyResponse)

    async def loyalty_cancel_bonus_operations(
        self,
        order_entity: SerializedEntityOrder,
        site: str,
    ) -> LoyaltyCancelBonusOperationsResponse:
        """
        Отмена операций с бонусами по программе лояльности

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-loyalty-cancel-bonus-operations
        :param order_entity: Объект заказа
        :param site: Код магазина
        :return: LoyaltyCancelBonusOperationsResponse
        """
        request = LoyaltyCancelBonusOperationsRequest(order=order_entity, site=site)
        response = await self._client.post(
            endpoint="/orders/loyalty/cancel-bonus-operations",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True)
        )
        return self._process_response(response, LoyaltyCancelBonusOperationsResponse)



    async def upload(
        self, orders: SerializedOrderList, site: str
    ) -> OrdersUploadResponse:
        """
        **Массовая загрузка заказов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-upload
        :param orders: Список заказов
        :param site: Код магазина
        :return: OrdersUploadResponse
        """
        if len(orders.root) > 50:
            raise ValueError("Too many orders, only 50 are allowed")
        request = OrdersUploadRequest(orders=orders, site=site)
        response = await self._client.post(
            endpoint="/orders/upload",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, OrdersUploadResponse)



    async def payment_create(
        self, payment: SerializedPayment, site: str
    ) -> OrdersPaymentCreateResponse:
        """
        **Создание платежа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-payments-create
        :param payment: Объект платежа
        :param site: Код магазина
        :return: OrdersPaymentCreateResponse
        """
        request = OrdersPaymentCreateRequest(payment=payment, site=site)
        response = await self._client.post(
            endpoint="/orders/payments/create",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, OrdersPaymentCreateResponse)

    async def payment_edit(
        self,
        payment_id: str,
        payment: SerializedPayment,
        site: str,
        by: IdTypes = "externalId",
    ) -> OrdersPaymentEditResponse:
        """
        **Редактирование платежа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-payments-externalId-edit
        :param payment_id: Внутренний или внешний ИД платежа
        :param payment: Объект платежа
        :param site: Код магазина
        :param by: Указывается, что передается в параметре id: внутренний (by=id) или внешний (by=externalId) ID платежа. По умолчанию externalId.
        :return: OrdersPaymentEditResponse
        """
        request = OrdersPaymentEditRequest(payment=payment, site=site, by=by)
        response = await self._client.post(
            endpoint=f"/orders/payments/{payment_id}/edit",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, OrdersPaymentEditResponse)

    async def payment_delete(self, payment_id: str) -> OrdersPaymentDeleteResponse:
        """
        **Удаление платежа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-payments-externalId-delete
        :param payment_id: Внутренний или внешний ИД платежа
        :return: OrdersPaymentDeleteResponse
        """
        response = await self._client.post(
            endpoint=f"/orders/payments/{payment_id}/delete"
        )
        return self._process_response(response, OrdersPaymentDeleteResponse)



