from retailcrm.http_cilent import BaseHttpClient
from retailcrm.response import Response


class RetailCrmUsersApi:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def user_groups(self, limit: int = 20, page: int = 1) -> Response:
        """
        **Получение списка групп пользователей**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-user-groups
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :return: Response
        """
        return await self._client.get(
            endpoint="/user-groups",
            params={
                "limit": limit,
                "page": page,
            },
        )

    async def users(
        self, filter_dict: dict, limit: int = 20, page: int = 1
    ) -> Response:
        """
        **Получение списка пользователей, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-users
        :param filter_dict: Фильтр
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :return: Response
        """
        return await self._client.get(
            endpoint="/users",
            params={"limit": limit, "page": page, **filter_dict},
        )

    async def user(self, user_id: int) -> Response:
        """
        **Получение информации о пользователе**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-users-id
        :param user_id: ID пользователя
        :return: Response
        """
        return await self._client.get(
            endpoint=f"/users/{user_id}",
        )

    async def user_set_status(self, user_id: int, status: str) -> Response:
        """
        **Смена статуса пользователя**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-users-id-status
        :param user_id: ID пользователя
        :param status: Статус пользователя в системе.
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/users/{user_id}/status",
            params={"status": status},
        )
