from retailcrm.http_cilent import BaseHttpClient
from retailcrm.response import Response


class RetailCrmOrdersApi:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def create_order(self, order_json: str, site: str) -> Response:
        """
        **Создание заказа**
        Для доступа к методу необходимо разрешение order_write.
        Метод создает заказ и возвращает внутренний ID созданного заказа.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-create
        :param order_json: string
        :param site: string
        :return: Response
        """
        return await self._client.post(
            endpoint="/orders/create",
            data={
                "site": site,
                "order": order_json,
            }
        )

    async def get_order(self, order_id: str, by: str, site: str) -> Response:
        """
        **Получение информации о заказе.**
        Для доступа к методу необходимо разрешение order_read.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-orders-externalId
        :param order_id: string
        :param by: string
        :param site: string
        :return: Response
        """
        return await self._client.get(
            endpoint=f"/orders/{order_id}",
            params={
                "by": by,
                "site": site,
            }
        )