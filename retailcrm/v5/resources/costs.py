from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.costs import SerializedCost
from retailcrm.v5.schemas.filters.costs import CostFilter
from retailcrm.v5.schemas.requests.costs import (
    CostCreateRequest,
    CostEditRequest,
    CostsDeleteRequest,
    CostsFilterRequest,
    CostsUploadRequest,
)
from retailcrm.v5.schemas.responses.costs import (
    CostCreateResponse,
    CostEditResponse,
    CostGetResponse,
    CostsDeleteResponse,
    CostsFilterResponse,
    CostsUploadResponse,
)


class CostsApiResource(ApiResource):
    async def filter(
        self, filter_obj: CostFilter | None = None, limit: int = 20, page: int = 1
    ) -> CostsFilterResponse:
        """
        **Получение списка расходов, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-costs

        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: CostsFilterResponse
        """
        request = CostsFilterRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint="/costs",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CostsFilterResponse)

    async def create(
        self, cost: SerializedCost, site: str | None = None
    ) -> CostCreateResponse:
        """
        **Создание расхода**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-costs-create
        :param cost: Данные по расходу.
        :param site: Символьный код магазина. Указывается в случае привязки к заказу по externalId или number.
        :return: CostCreateResponse
        """
        request = CostCreateRequest(cost=cost, site=site)
        response = await self._client.post(
            endpoint="/costs/create",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CostCreateResponse)

    async def delete_multiple(self, ids: list[int]) -> CostsDeleteResponse:
        """
        **Пакетное удаление расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-costs-delete
        :param ids: Идентификаторы удаляемых расходов.
        :return: CostsDeleteResponse
        """
        request = CostsDeleteRequest(ids=ids)
        response = await self._client.post(
            endpoint="/costs/delete",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CostsDeleteResponse)

    async def upload(self, costs: list[SerializedCost]) -> CostsUploadResponse:
        """
        **Пакетная загрузка расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-costs-upload
        :param costs: Данные по расходам.
        :return: CostsUploadResponse
        """
        if len(costs) > 50:
            raise ValueError("Too many costs, only 50 are allowed")
        request = CostsUploadRequest(costs=costs)
        response = await self._client.post(
            endpoint="/costs/upload",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CostsUploadResponse)

    async def get(self, cost_id: str) -> CostGetResponse:
        """
        **Получение информации о расходе**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-costs-id
        :param cost_id: ID расхода.
        :return: CostGetResponse
        """
        response = await self._client.get(
            endpoint=f"/costs/{cost_id}",
        )
        return self._process_response(response, CostGetResponse)

    async def delete(self, cost_id: str) -> SuccessResponse:
        """
        **Удаление расхода**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-costs-id-delete
        :param cost_id: ID расхода.
        :return: SuccessResponse
        """
        response = await self._client.post(
            endpoint=f"/costs/{cost_id}/delete",
        )
        return self._process_response(response, SuccessResponse)

    async def edit(
        self, cost_id: str, cost: SerializedCost, site: str | None = None
    ) -> CostEditResponse:
        """
        **Редактирование расхода**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-costs-id-edit
        :param cost_id: ID расхода.
        :param cost: Данные по расходу.
        :param site: Символьный код магазина. Указывается в случае привязки к заказу по externalId или number.
        :return: CostEditResponse
        """
        request = CostEditRequest(cost=cost, site=site)
        response = await self._client.post(
            endpoint=f"/costs/{cost_id}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CostEditResponse)
