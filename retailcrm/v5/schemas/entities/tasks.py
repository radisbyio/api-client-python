from datetime import date, datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.enums.task import TasksStatuses
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.shared.customer import (
    AbstractCustomer,
    SerializedEntityCustomer,
)
from retailcrm.v5.schemas.shared.history_api_key import HistoryApiKey
from retailcrm.v5.schemas.shared.history_user import HistoryUser
from retailcrm.v5.schemas.shared.order import AbstractOrder, SerializedEntityOrder

__all__ = [
    "TagsFilter",
    "TaskFilter",
    "Task",
    "TaskComment",
    "TaskHistory",
    "SerializedTask",
    "TaskHistoryFilter",
]


class TagsFilter(BaseRetailCrmScheme):
    without: Optional[bool] = None
    attached: Optional[bool] = None


class TaskFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID задач")
    orderNumber: Optional[str] = Field(
        None, description="Номер заказа, связанного с задачей"
    )
    customer: Optional[str] = Field(None, description="Клиент, связанный с задачей")
    performers: Optional[list[int]] = Field(None, description="Исполнители задачи")
    status: Optional[TasksStatuses] = Field(None, description="Статус задачи")
    creators: Optional[list[int]] = Field(None, description="Авторы задачи")
    text: Optional[str] = Field(None, description="Текст задачи")
    tagsFilter: Optional[TagsFilter] = None
    tags: Optional[list[str]] = Field(None, description="Теги")
    attachedTags: Optional[list[str]] = Field(None, description="Прикрепленные теги")
    createdAtFrom: Optional[date] = Field(None, description="Дата создания задачи (с)")
    createdAtTo: Optional[date] = Field(None, description="Дата создания задачи (до)")
    dateFrom: Optional[date] = Field(None, description="Дата выполнения задачи (с)")
    dateTo: Optional[date] = Field(None, description="Дата выполнения задачи (до)")
    completedAtFrom: Optional[date] = Field(
        None, description="Фактическая дата выполнения (с)"
    )
    completedAtTo: Optional[date] = Field(
        None, description="Фактическая дата выполнения (до)"
    )


class Task(BaseRetailCrmScheme):
    id: int | None = Field(None, description="ID задачи")
    text: str | None = Field(None, description="Текст задачи")
    commentary: str | None = Field(None, description="Комментарий к задаче")
    datetime_: Optional[datetime] = Field(
        None, description="Время выполнения задачи", validation_alias="datetime"
    )
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    complete: bool = Field(False, description="Признак выполнения задачи")
    creator: Optional[int] = Field(None, description="Автор задачи")
    performer: Optional[int] = Field(None, description="Исполнитель задачи")
    performerType: Optional[str] = Field(None, description="Тип исполнителя задачи")
    customer: Optional[AbstractCustomer] = Field(
        None, description="Клиент, к которому привязана задача"
    )
    order: Optional[AbstractOrder] = Field(
        None, description="Заказ, к которому привязана задача"
    )
    phone: Optional[str] = Field(None, description="Телефон связанный с задачей")
    phoneSite: Optional[str] = Field(
        None, description="Магазин, связанный с задачей на перезвон"
    )
    completedAt: Optional[datetime] = Field(None, description="Время завершения задачи")


class TaskComment(BaseRetailCrmScheme):
    id: int | None = Field(None, description="ID комментария к задаче")
    creator: Optional[int] = Field(None, description="Автор комментария")
    text: str | None = Field(None, description="Текст комментария к задаче")
    createdAt: Optional[datetime] = Field(description="Дата создания")
    updatedAt: Optional[datetime] = Field(description="Дата изменения")


class TaskHistory(BaseRetailCrmScheme):
    id: int = Field(description="Внутренний идентификатор записи в истории")
    createdAt: datetime = Field(description="Дата внесения изменения")
    created: Optional[bool] = Field(None, description="Признак создания сущности")
    source: Optional[str] = Field(None, description="Источник изменения")
    user: Optional[HistoryUser] = Field(None, description="Пользователь")
    field: Optional[str] = Field(None, description="Имя изменившегося поля")
    oldValue: Optional[str | int | dict | float] = Field(
        None, description="Старое значение свойства"
    )
    newValue: Optional[str | int | dict | float] = Field(
        None, description="Новое значение свойства"
    )
    apiKey: Optional[HistoryApiKey] = Field(
        None, description="Информация о ключе api, использовавшемся для этого изменения"
    )
    task: Optional[Task] = Field(None, description="Задача")
    comment: Optional[TaskComment] = Field(
        None, description="Комментарий пользователя к задаче"
    )


class SerializedTask(BaseRetailCrmScheme):
    text: Optional[str] = Field(None, description="Текст задачи")
    commentary: Optional[str] = Field(None, description="Комментарий к задаче")
    datetime_: Optional[datetime] = Field(
        None, description="Время выполнения задачи", serialization_alias="datetime"
    )
    complete: Optional[bool] = Field(None, description="Признак выполнения задачи")
    customer: Optional[SerializedEntityCustomer] = Field(
        None, description="Клиент, к которому привязана задача"
    )
    performerId: Optional[int] = Field(None, description="Исполнитель задачи")
    order: Optional[SerializedEntityOrder] = Field(
        None, description="Заказ, к которому привязана задача"
    )
    phone: Optional[str] = Field(None, description="Телефон связанный с задачей")
    phoneSite: Optional[str] = Field(
        None, description="Магазин, связанный с задачей на перезвон"
    )

    datetime_serializer = field_serializer("datetime_")(
        datetime_serializer("%Y-%m-%d %H:%M")
    )


class TaskHistoryFilter(BaseRetailCrmScheme):
    taskId: Optional[int] = Field(None, description="ID задачи")
    sinceId: Optional[int] = Field(None, description="Начиная с ID истории задач")
    startDate: Optional[datetime] = Field(None, description="Дата/время изменения (от)")
    endDate: Optional[datetime] = Field(None, description="Дата/время изменения (от)")

    startDate_serializer = field_serializer("startDate")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    endDate_serializer = field_serializer("endDate")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
