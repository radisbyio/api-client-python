from typing import Optional

from retailcrm.http_cilent import BaseHttpClient
from retailcrm.response import Response


class RetailCrmTasksApi:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def get_all(
        self, filter_dict: dict, limit: int = 20, page: int = 1
    ) -> Response:
        """
        **Получение списка задач**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-tasks

        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_dict: Фильтр
        :return: Response object
        """
        return await self._client.get(
            endpoint="/tasks",
            params={"limit": limit, "page": page, **filter_dict},
        )

    async def create(
        self,
        task_json: str,
        site: str = None,
    ) -> Response:
        """
        **Создание задачи**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-tasks-create

        :param task_json: Task json for creation
        :param site: (optional) Site code
        :return: Response object
        """
        payload = {
            "site": site,
            "task": task_json,
        }
        if site:
            payload["site"] = site

        return await self._client.post(
            endpoint="/tasks/create",
            data=payload,
        )

    async def history(
        self, filter_dict: dict, limit: int = 20, page: int = 1
    ) -> Response:
        """
        **Получение истории изменения задач**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-tasks-history

        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_dict: Фильтр
        :return: Response object
        """
        return await self._client.get(
            endpoint="/tasks/history",
            params={"limit": limit, "page": page, **filter_dict},
        )

    async def get_by_id(self, task_id: int) -> Response:
        """
        **Получение информации о задаче**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-tasks-id

        :param task_id: ID задачи
        :return: Response object
        """
        return await self._client.get(
            endpoint=f"/tasks/{task_id}",
        )

    async def comments(self, task_id: int, limit: int, page: int) -> Response:
        """
        **Получение комментариев к задаче**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-tasks-id-comments

        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param task_id: ID задачи
        :return: Response object
        """
        return await self._client.get(
            endpoint=f"/tasks/{task_id}/comments", params={"limit": limit, "page": page}
        )

    async def edit(
        self,
        task_id: int,
        task_json: str,
        site: Optional[str] = None,
    ) -> Response:
        """
        POST /api/v5/tasks/{id}/edit
        Редактирование задачи

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-tasks-id-edit

        :param task_id: ID задачи
        :param task_json: Task json
        :param site: Код магазина
        :return: Response object
        """
        payload = {"task": task_json}
        if site:
            payload["site"] = site

        return await self._client.post(
            endpoint=f"/tasks/{task_id}/edit",
            data=payload,
        )
