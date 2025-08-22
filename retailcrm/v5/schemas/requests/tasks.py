from typing import Optional

from pydantic import BaseModel, Field, field_serializer, model_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.entities.tasks import (
    SerializedTask,
    TaskFilter,
    TaskHistoryFilter,
)
from retailcrm.v5.utils import pydantic_to_nested_dict

__all__ = [
    "FilterTasksRequest",
    "CreateTaskRequest",
    "FilterTasksHistoryRequest",
    "GetTaskCommentsRequest",
    "EditTaskRequest",
]


class FilterTasksRequest(BaseModel):
    filter_obj: TaskFilter | None = Field(serialization_alias="filter")
    limit: int
    page: int

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter"),
        }


class CreateTaskRequest(BaseModel):
    task: SerializedTask
    site: str = None

    task = field_serializer("task")(to_json_serializer())


class FilterTasksHistoryRequest(BaseModel):
    filter_obj: TaskHistoryFilter | None = Field(serialization_alias="filter")
    limit: int
    page: int

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter"),
        }


class GetTaskCommentsRequest(BaseModel):
    limit: int
    page: int


class EditTaskRequest(BaseModel):
    task: SerializedTask
    site: Optional[str] = (None,)

    task = field_serializer("task")(to_json_serializer())
