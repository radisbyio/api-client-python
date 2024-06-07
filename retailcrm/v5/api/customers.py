from retailcrm.http_cilent import BaseHttpClient
from retailcrm.response import Response


class RetailCrmCustomersApi:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def customers(self, filter: dict, limit: int = 20, page: int = 1) -> Response:
        """
        **Получение списка клиентов, удовлетворяющих заданному фильтру**
        Результат возвращается постранично. В поле pagination содержится информация о постраничной разбивке.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers
        :param filter: Словарь полей фильтра
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :return: Response
        """
        return await self._client.get(
            endpoint=f"/customers",
            params={"limit": limit, "page": page, **filter},
        )
