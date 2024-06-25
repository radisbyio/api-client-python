from retailcrm.http_cilent import BaseHttpClient
from retailcrm.response import Response


class RetailCrmReferencesApi:
    def __init__(self, client: BaseHttpClient):
        self._client = client

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
