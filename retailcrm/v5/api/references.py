from retailcrm.http_cilent import BaseHttpClient
from retailcrm.response import Response


class RetailCrmReferencesApi:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def cost_groups(self) -> Response:
        """
        **Получение списка групп расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-cost-groups
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/cost-groups",
        )

    async def cost_groups_edit(self, code: str, cost_group_json: str) -> Response:
        """
        **Редактирование группы расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-cost-groups-code-edit
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/reference/cost-groups/{code}/edit",
            data={"costGroup": cost_group_json},
        )

    async def cost_items(self) -> Response:
        """
        **Получение списка статей расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-cost-items
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/cost-items",
        )

    async def cost_items_edit(self, code: str, cost_item_json: str) -> Response:
        """
        **Редактирование статьи расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-cost-items-code-edit
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/reference/cost-items/{code}/edit",
            data={"costItem": cost_item_json},
        )

    async def countries(self) -> Response:
        """
        **Получение списка кодов доступных стран**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-countries
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/countries",
        )

    async def couriers(self) -> Response:
        """
        **Получение списка курьеров**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-couriers
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/couriers",
        )

    async def couriers_create(self, courier_json: str) -> Response:
        """
        **Создание курьера**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-couriers
        :return: Response
        """
        return await self._client.post(
            endpoint="/reference/couriers/create", data={"courier": courier_json}
        )

    async def couriers_edit(self, courier_id: str, courier_json: str) -> Response:
        """
        **Редактирование курьера**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-couriers-id-edit
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/reference/couriers/{courier_id}/edit",
            data={"courier": courier_json},
        )

    async def status_groups(self) -> Response:
        """
        **Получение списка групп статусов заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-status-groups
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/status-groups",
        )

    async def statuses(self) -> Response:
        """
        **Получение списка статусов заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-statuses
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/statuses",
        )
