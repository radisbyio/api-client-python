from typing import Optional

from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.tasks import TaskFilter, SerializedTask, TaskHistoryFilter
from retailcrm.v5.schemas.requests.tasks import FilterTasksRequest, CreateTaskRequest, FilterTasksHistoryRequest, \
    GetTaskCommentsRequest, EditTaskRequest
from retailcrm.v5.schemas.responses.tasks import FilterTasksResponse, CreateTaskResponse, FilterTaskHistoryResponse, \
    GetTaskResponse, GetTaskCommentsResponse

__all__ = ["TasksApiResource"]


class TasksApiResource(ApiResource):
    async def filter(
        self, filter_obj: TaskFilter | None = None, limit: int = 20, page: int = 1
    ) -> FilterTasksResponse:
        """
        **Получение списка задач**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-tasks

        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_obj: Фильтр
        :return: FilterTasksResponse
        """

        request = FilterTasksRequest(limit=limit, page=page, filter_obj=filter_obj)
        response = await self._client.get(
            endpoint="/tasks",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, FilterTasksResponse)

    async def create(
        self, task: SerializedTask, site: str | None = None
    ) -> CreateTaskResponse:
        """
        **Создание задачи**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-tasks-create

        :param task:
        :param site: Символьный код магазина
        :return: CreateTaskResponse
        """

        request = CreateTaskRequest(task=task, site=site)
        response = await self._client.get(
            endpoint="/tasks/create",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CreateTaskResponse)

    async def history(
        self, filter_obj: TaskHistoryFilter | None = None, limit: int = 20, page: int = 1
    ) -> FilterTaskHistoryResponse:
        """
        **Получение истории изменения задач**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-tasks-history

        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_obj: Фильтр
        :return: FilterTaskHistoryResponse
        """

        request = FilterTasksHistoryRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.post(
            endpoint="/tasks/history",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, FilterTaskHistoryResponse)

    async def get(self, task_id: int) -> GetTaskResponse:
        """
        **Получение информации о задаче**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-tasks-id

        :param task_id: ID задачи
        :return: GetTaskResponse
        """

        response = await self._client.get(
            endpoint=f"/tasks/{task_id}",
        )
        return self._process_response(response, GetTaskResponse)

    async def comments(
        self, task_id: int, limit: int = 20, page: int = 1
    ) -> GetTaskCommentsResponse:
        """
        **Получение комментариев к задаче**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-tasks-id-comments

        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param task_id: ID задачи
        :return: GetTaskCommentsResponse
        """

        request = GetTaskCommentsRequest(limit=limit, page=page)
        response = await self._client.get(
            endpoint=f"/tasks/{task_id}/comments",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, GetTaskCommentsResponse)

    async def edit(
        self, task_id: int, task: SerializedTask, site: Optional[str] = None
    ) -> SuccessResponse:
        """
        **Редактирование задачи**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-tasks-id-edit

        :param task_id: ID задачи
        :param task: Задача
        :param site: Код магазина
        :return: SuccessResponse
        """

        request = EditTaskRequest(task=task, site=site)
        response = await self._client.post(
            endpoint=f"/tasks/{task_id}/edit",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, SuccessResponse)
