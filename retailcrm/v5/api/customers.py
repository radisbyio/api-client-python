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

    async def get_by_id(self, client_id: str | int, site: str = None, by: str = None) -> Response:
        """
        **Получение информации о клиенте**
        Метод возвращает полную информацию по клиенту.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers
        :param client_id: Словарь полей фильтра
        :param site: Код магазина
        :param by:
        :return: Response
        """
        params = {}
        if site is not None:
            params["site"] = site
        if by is not None:
            params["by"] = by
        return await self._client.get(
            endpoint=f"/customers/{client_id}",
            params=params,
        )


    async def create(self, customer_json: str, site: str) -> Response:
        """
        **Создание клиента**
        Метод создает клиента и возвращает внутренний ID созданного клиента.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-create
        :param customer_json: Json строка
        :param site: Символьный код магазина
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/customers/create",
            params={"site": site},
            data={"customer": customer_json},
        )

    async def edit(self, customer_id: str, customer_json: str, site: str = None, by: str = None) -> Response:
        """
        **Редактирование клиента**
        Метод создает клиента и возвращает внутренний ID созданного клиента.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-create
        :param customer_id: Идентификатор пользователя
        :param by:
        :param customer_json: Json строка
        :param site: Символьный код магазина
        :return: Response
        """
        params = {}
        if site is not None:
            params["site"] = site
        if by is not None:
            params["by"] = by

        return await self._client.post(
            endpoint=f"/customers/{customer_id}/edit",
            params=params,
            data={"customer": customer_json},
        )
