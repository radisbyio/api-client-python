from dataclasses import dataclass

from retailcrm import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.api.tasks import RetailCrmTasksApi
from retailcrm.v5.schemas.base import RetailCrmResponse
from retailcrm.v5.schemas.tasks import (
    SerializedTask,
    TaskCommentsResponse,
    TaskFilterData,
    TaskHistoryFilterType,
    TaskHistoryResponse,
    TaskResponse,
    TasksResponse,
)
from retailcrm.v5.utils import pydantic_to_nested_dict

__all__ = ["TasksController"]


@dataclass(slots=True)
class TasksController:
    _api: RetailCrmTasksApi

    def __init__(self, client: BaseHttpClient):
        self._api = RetailCrmTasksApi(client)

    async def get_all(
        self, filter_obj: TaskFilterData, limit: int = 20, page: int = 1
    ) -> TasksResponse:
        response = await self._api.get_all(
            pydantic_to_nested_dict(filter_obj, "filter"), limit, page
        )
        response_obj = TasksResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def create(self, task: SerializedTask, site: str = None) -> RetailCrmResponse:
        response = await self._api.create(
            task_json=task.model_dump_json(exclude_none=True, by_alias=True), site=site
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def history(
        self, filter_obj: TaskHistoryFilterType, limit: int = 20, page: int = 1
    ) -> TaskHistoryResponse:
        response = await self._api.history(
            filter_dict=pydantic_to_nested_dict(filter_obj, "filter"),
            limit=limit,
            page=page,
        )
        response_obj = TaskHistoryResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def get_by_id(self, task_id: int) -> TaskResponse:
        response = await self._api.get_by_id(task_id)
        response_obj = TaskResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def comments(
        self, task_id: int, limit: int = 20, page: int = 1
    ) -> TaskCommentsResponse:
        response = await self._api.comments(task_id, limit, page)
        response_obj = TaskCommentsResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def edit(
        self, task_id: int, task: SerializedTask, site: str = None
    ) -> RetailCrmResponse:
        response = await self._api.edit(
            task_id, task.model_dump_json(exclude_unset=True, by_alias=True), site
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj
