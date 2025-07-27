from datetime import datetime
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas import SuccessResponse
from retailcrm.v5.schemas.entities.tasks import Task, TaskHistory, TaskComment

__all__ = ["FilterTasksResponse", "CreateTaskResponse", "FilterTaskHistoryResponse", "GetTaskResponse", "GetTaskCommentsResponse"]


class FilterTasksResponse(SuccessResponse):
    tasks: list[Task] = Field(None, description="Задача")


class CreateTaskResponse(SuccessResponse):
    id: Optional[int] = Field(None, description="ИД задачи")


class FilterTaskHistoryResponse(SuccessResponse):
    generatedAt: datetime = Field(description="Время формирования ответа")
    history: list[TaskHistory] = Field(default_factory=list, description="История")


class GetTaskResponse(SuccessResponse):
    task: Optional[Task] = Field(None, description="Задача")


class GetTaskCommentsResponse(SuccessResponse):
    comments: list[TaskComment] = Field(
        default_factory=list, description="Комментарий пользователя к задаче"
    )
