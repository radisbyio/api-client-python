from retailcrm.http_cilent import BaseHttpClient
from retailcrm.response import Response


class RetailCrmCustomFieldsApi:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def get_all(self, filter_dict: dict, limit: int = 20, page: int = 1) -> Response:
        """
        **Получение списка пользовательских полей, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-custom-fields
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_dict: Фильтр
        :return: Response
        """
        return await self._client.get(
            endpoint="/custom-fields",
            params={
                "limit": limit,
                "page": page,
                **filter_dict,
            },
        )

    async def dictionaries(self, filter_dict: dict, limit: int = 20, page: int = 1) -> Response:
        """
        **Получение списка справочников, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-custom-fields-dictionaries
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_dict: Фильтр
        :return: Response
        """
        return await self._client.get(
            endpoint="/custom-fields/dictionaries",
            params={
                "limit": limit,
                "page": page,
                **filter_dict,
            },
        )
