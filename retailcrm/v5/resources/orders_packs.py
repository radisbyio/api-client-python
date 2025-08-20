from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas import SuccessResponse
from retailcrm.v5.schemas.base import IdResponse
from retailcrm.v5.schemas.entities.orders_packs import SerializedOrderProductPack
from retailcrm.v5.schemas.filters.orders_packs import OrderProductPackFilter, OrderProductPackHistoryFilterType
from retailcrm.v5.schemas.requests.orders_packs import OrdersProductsPacksFilterRequest, OrdersPacksCreateRequest, \
    OrdersPacksEditRequest, OrdersProductsPacksHistoryFilterRequest
from retailcrm.v5.schemas.responses.orders_packs import OrderProductPackFilterResponse, OrderProductPackResponse, \
    OrderProductPackHistoryListResponse

__all__ = ["OrdersPacksApiResource"]


class OrdersPacksApiResource(ApiResource):
    async def filter(
            self, filter_obj: OrderProductPackFilter | None, limit: int = 20, page: int = 1
    ) -> OrderProductPackFilterResponse:
        """
        **Получение списка паков, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-orders-packs

        :param filter_obj:
        :param limit: Получение списка паков, удовлетворяющих заданному фильтру
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :return: OrderProductPackListResponse
        """

        request = OrdersProductsPacksFilterRequest(
            limit=limit, page=page, filter_obj=filter_obj
        )
        response = await self._client.get(
            endpoint="/api/v5/orders/packs",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, OrderProductPackFilterResponse)

    async def create(self, pack: SerializedOrderProductPack) -> IdResponse:
        """
        **Создание пака**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-packs-create
        :param pack:
        :return: IdResponse
        """

        request = OrdersPacksCreateRequest(pack=pack)
        response = await self._client.post(
            endpoint="/api/v5/orders/packs/create",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, IdResponse)

    async def history(
            self, filter_obj: OrderProductPackHistoryFilterType | None, limit: int = 20, page: int = 1
    ) -> OrderProductPackHistoryListResponse:
        """
        **Получение истории комплектации заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-orders-packs

        :param filter_obj:
        :param limit: Получение списка паков, удовлетворяющих заданному фильтру
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :return: OrderProductPackHistoryListResponse
        """

        request = OrdersProductsPacksHistoryFilterRequest(
            limit=limit, page=page, filter_obj=filter_obj
        )
        response = await self._client.get(
            endpoint="/api/v5/orders/packs/history",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, OrderProductPackHistoryListResponse)

    async def get(self, pack_id: int) -> OrderProductPackResponse:
        """
        **Получение информации о паке**
        :param pack_id:
        :return: OrderProductPackResponse
        """

        response = await self._client.get(
            endpoint=f"/api/v5/orders/packs/{pack_id}",
        )

        return self._process_response(response, OrderProductPackResponse)

    async def delete(self, pack_id: int) -> SuccessResponse:
        """
        **Получение информации о паке**
        :param pack_id:
        :return: OrderProductPackResponse
        """

        response = await self._client.post(
            endpoint=f"/api/v5/orders/packs/{pack_id}",
        )

        return self._process_response(response, SuccessResponse)

    async def edit(self, pack_id: int, pack: SerializedOrderProductPack) -> OrderProductPackResponse:
        """
        **Редактирование пака**
        :param pack_id:
        :param pack:
        :return: OrderProductPackResponse
        """
        request = OrdersPacksEditRequest(pack=pack)

        response = await self._client.post(
            endpoint=f"/api/v5/orders/packs/{pack_id}/edit",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )

        return self._process_response(response, OrderProductPackResponse)