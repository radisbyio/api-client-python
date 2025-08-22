import decimal

from retailcrm import RetailCrmApiError
from retailcrm.v5.enums.orders import CombineTechniqueTypes
from retailcrm.v5.resources.base import ApiResource

__all__ = ["OrdersApiResource"]

from retailcrm.v5.schemas.base import (
    ErrorResponse,
    IdResponse,
    IdTypesLiteral,
    SuccessResponse,
)
from retailcrm.v5.schemas.entities.orders import (
    SerializedOrder,
    SerializedOrderLink,
    SerializedOrderReference,
    SerializedPayment,
)
from retailcrm.v5.schemas.filters.orders import OrderHistoryFilterV4Type, OrdersFilter
from retailcrm.v5.schemas.requests.orders import (
    FixExternalIdsRequest,
    LoyaltyApplyRequest,
    LoyaltyCancelBonusOperationsRequest,
    OrderLinkCreateRequest,
    OrdersCombineRequest,
    OrdersCreateRequest,
    OrdersDeliveryCancelRequest,
    OrdersEditRequest,
    OrdersFilterRequest,
    OrdersGetRequest,
    OrdersHistoryRequest,
    OrdersPaymentCreateRequest,
    OrdersPaymentEditRequest,
    OrdersPlatesPrintRequest,
    OrdersUploadRequest,
)
from retailcrm.v5.schemas.responses.orders import (
    LoyaltyApplyResponse,
    LoyaltyCancelBonusOperationsResponse,
    OrderGetResponse,
    OrdersCreateResponse,
    OrdersFilterResponse,
    OrdersHistoryResponse,
    OrdersPaymentCreateResponse,
)
from retailcrm.v5.schemas.shared.fix_external_row import FixExternalRow
from retailcrm.v5.schemas.shared.order import SerializedEntityOrder


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
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, SuccessResponse)

    async def create(self, order: SerializedOrder, site: str) -> OrdersCreateResponse:
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
            content=request.model_dump_json(exclude_none=True, by_alias=True),
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
            content=request.model_dump(exclude_none=True, by_alias=True),
        )

        return self._process_response(response, SuccessResponse)

    async def history(
        self,
        filter_obj: OrderHistoryFilterV4Type | None = None,
        limit: int = 20,
        page: int = 1,
    ) -> OrdersHistoryResponse:
        """
        **Получение истории изменений по заказам**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-orders-history
        :param filter_obj: Объект фильтра
        :param limit: Количество заказов на странице (по умолчанию 20)
        :param page: Номер страницы с результатами (по умолчанию 1)
        :return: OrdersHistoryResponse
        """
        request = OrdersHistoryRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint="/orders/history",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, OrdersHistoryResponse)

    async def links_create(
        self, link: SerializedOrderLink, site: str = None
    ) -> OrdersHistoryResponse:
        """
        **Создание связи между заказами**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-links-create

        :param filter_obj: Объект фильтра
        :param limit: Количество заказов на странице (по умолчанию 20)
        :param page: Номер страницы с результатами (по умолчанию 1)
        :return: OrdersHistoryResponse
        """
        request = OrderLinkCreateRequest(link=link, site=site)
        response = await self._client.get(
            endpoint="/orders/links/create",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, OrdersHistoryResponse)

    async def loyalty_apply(
        self,
        order: SerializedEntityOrder,
        site: str,
        bonuses: decimal.Decimal,
    ) -> LoyaltyApplyResponse:
        """
        Применение бонусов по программе лояльности

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-loyalty-apply
        :param order: Объект заказа
        :param site: Код магазина
        :param bonuses: Количество бонусов для применения
        :return: LoyaltyApplyResponse
        """
        request = LoyaltyApplyRequest(order=order, site=site, bonuses=bonuses)
        response = await self._client.post(
            endpoint="/orders/loyalty/apply",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, LoyaltyApplyResponse)

    async def loyalty_cancel_bonus_operations(
        self,
        order: SerializedEntityOrder,
        site: str,
    ) -> LoyaltyCancelBonusOperationsResponse:
        """
        Отмена операций с бонусами по программе лояльности

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-loyalty-cancel-bonus-operations
        :param order: Объект заказа
        :param site: Код магазина
        :return: LoyaltyCancelBonusOperationsResponse
        """
        request = LoyaltyCancelBonusOperationsRequest(order=order, site=site)
        response = await self._client.post(
            endpoint="/orders/loyalty/cancel-bonus-operations",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, LoyaltyCancelBonusOperationsResponse)

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
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, OrdersPaymentCreateResponse)

    async def payment_edit(
        self,
        payment_id: str,
        payment: SerializedPayment,
        site: str,
        by: IdTypesLiteral | str = "externalId",
    ) -> IdResponse:
        """
        **Редактирование платежа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-payments-externalId-edit
        :param payment_id: Внутренний или внешний ИД платежа
        :param payment: Объект платежа
        :param site: Код магазина
        :param by: Указывается, что передается в параметре id: внутренний (by=id) или внешний (by=externalId) ID платежа. По умолчанию externalId.
        :return: IdResponse
        """
        request = OrdersPaymentEditRequest(payment=payment, site=site, by=by)
        response = await self._client.post(
            endpoint=f"/orders/payments/{payment_id}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, IdResponse)

    async def payment_delete(self, payment_id: int) -> SuccessResponse:
        """
        **Удаление платежа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-payments-externalId-delete
        :param payment_id: 	Внутренний ID удаляемого платежа
        :return: SuccessResponse
        """
        response = await self._client.post(
            endpoint=f"/orders/payments/{payment_id}/delete"
        )
        return self._process_response(response, SuccessResponse)

    async def upload(self, orders: list[SerializedOrder], site: str) -> SuccessResponse:
        """
        **Массовая загрузка заказов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-upload
        :param orders: Список заказов
        :param site: Код магазина
        :return: SuccessResponse
        """
        if len(orders) > 50:
            raise ValueError("Too many orders, only 50 are allowed")
        request = OrdersUploadRequest(orders=orders, site=site)
        response = await self._client.post(
            endpoint="/orders/upload",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, SuccessResponse)

    async def get(
        self,
        order_id: int | str,
        site: str | None = None,
        by: IdTypesLiteral | str = "externalId",
    ) -> OrderGetResponse:
        """
        Получение информации о заказе.
        Для доступа к методу необходимо разрешение order_read.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-orders-externalId
        :param order_id: Внутренний или внешний ИД заказа
        :param site: Код магазина
        :param by: Указывается, что передается в параметре id: внутренний (by=id) или внешний (by=externalId) ID платежа. По умолчанию externalId.
        :return: OrderGetResponse
        """
        request = OrdersGetRequest(site=site, by=by)
        response = await self._client.get(
            endpoint=f"/orders/{order_id}",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, OrderGetResponse)

    async def edit(
        self,
        order_id: int | str,
        order: SerializedOrder,
        site: str | None = None,
        by: IdTypesLiteral | str = "externalId",
    ) -> SuccessResponse:
        """
        **Редактирование заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-externalId-edit
        :param order_id: Внутренний или внешний ИД заказа
        :param order: Объект заказа
        :param site: Код магазина
        :param by: Указывается, что передается в параметре id: внутренний (by=id) или внешний (by=externalId) ID платежа. По умолчанию externalId.
        :return: SuccessResponse
        """
        request = OrdersEditRequest(order=order, site=site, by=by)
        response = await self._client.post(
            endpoint=f"/orders/{order_id}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, SuccessResponse)

    async def delivery_cancel(
        self, order_id: int | str, force: bool, by: IdTypesLiteral | str = "externalId"
    ) -> SuccessResponse:
        """
        **Отмена интеграционной доставки**

        Метод позволяет отменить интеграционную доставку у конкретного заказа.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-externalId-edit

        :param order_id: Внутренний или внешний ИД заказа
        :param force: Если значение true - доставка будет помечена как отменённая, даже если не удалось её отменить в стороннем сервисе. Если false, то в случае ошибки от сервера службы доставки - отмена прерывается.
        :param by: Указывается, что передается в параметре id: внутренний (by=id) или внешний (by=externalId) ID платежа. По умолчанию externalId.
        :return: SuccessResponse
        """
        request = OrdersDeliveryCancelRequest(by=by, force=force)
        response = await self._client.post(
            endpoint=f"/orders/{order_id}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, SuccessResponse)

    async def plates_print(
        self,
        order_id: int | str,
        plate_id: int,
        site: str | None = None,
        by: IdTypesLiteral | str = "externalId",
    ) -> bytes:
        """
        **Редактирование заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-externalId-edit
        :param plate_id: ID печатной формы
        :param order_id: Внутренний или внешний ИД заказа
        :param site: Код магазина
        :param by: Указывается, что передается в параметре id: внутренний (by=id) или внешний (by=externalId) ID платежа. По умолчанию externalId.
        :return: SuccessResponse
        """
        request = OrdersPlatesPrintRequest(site=site, by=by)
        response = await self._client.post(
            endpoint=f"/orders/{order_id}/plates/{plate_id}/print",
            content=request.model_dump(exclude_none=True, by_alias=True),
        )
        if response.status_code >= 400:
            error_response = ErrorResponse.model_validate_json(response.content)
            raise RetailCrmApiError(
                status_code=response.status_code,
                error_msg=error_response.errorMsg,
                errors=error_response.errors,
                response=error_response,
            )

        return response.content
