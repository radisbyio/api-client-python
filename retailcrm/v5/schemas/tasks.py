from datetime import date, datetime
from typing import Optional, Union

from pydantic import Field, field_serializer

from retailcrm.v5.enums import TasksStatuses
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme, RetailCrmResponse
from retailcrm.v5.schemas.shared import ApiKey, SerializedEntityCustomer, Task, User


class TagsFilter(BaseRetailCrmScheme):
    without: Optional[bool] = None
    attached: Optional[bool] = None


class TaskFilterData(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID задач")
    orderNumber: Optional[str] = Field(
        None, description="Номер заказа, связанного с задачей", max_length=255
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


class SerializedEntityOrder(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID заказа")
    externalId: Optional[str] = Field(None, description="Внешний ID заказа")
    number: Optional[str] = Field(None, description="Номер заказа")


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


class ResponseTasks(RetailCrmResponse):
    tasks: Optional[list[Task]] = Field(None, description="Задача")


class TaskHistoryFilterType(BaseRetailCrmScheme):
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


class TaskComment(BaseRetailCrmScheme):
    id: int = Field(description="ID комментария к задаче")
    creator: Optional[int] = Field(None, description="Автор комментария")
    text: str = Field("", description="Текст комментария к задаче")
    createdAt: Optional[datetime] = Field(description="Дата создания")
    updatedAt: Optional[datetime] = Field(description="Дата изменения")


class TaskHistory(BaseRetailCrmScheme):
    id: int = Field(description="Внутренний идентификатор записи в истории")
    createdAt: datetime = Field(description="Дата внесения изменения")
    created: Optional[bool] = Field(None, description="Признак создания сущности")
    source: Optional[str] = Field(None, description="Источник изменения")
    user: Optional[User] = Field(None, description="Пользователь")
    field: Optional[str] = Field(None, description="Имя изменившегося поля")
    oldValue: Optional[Union[str, int, dict, float]] = Field(
        None, description="Старое значение свойства"
    )
    newValue: Optional[Union[str, int, dict, float]] = Field(
        None, description="Новое значение свойства"
    )
    apiKey: Optional[ApiKey] = Field(
        None, description="Информация о ключе api, использовавшемся для этого изменения"
    )
    task: Optional[Task] = Field(None, description="Задача")
    comment: Optional[TaskComment] = Field(
        None, description="Комментарий пользователя к задаче"
    )


class ResponseTaskHistory(RetailCrmResponse):
    generatedAt: datetime = Field(description="Время формирования ответа")
    history: list[TaskHistory] = Field(default_factory=list, description="История")


class ResponseTaskResponse(RetailCrmResponse):
    task: Optional[Task] = Field(None, description="Задача")


class ResponseTaskCreate(RetailCrmResponse):
    id: Optional[int] = Field(None, description="ИД задачи")


class ResponseTaskComments(RetailCrmResponse):
    comments: list[TaskComment] = Field(
        default_factory=list, description="Комментарий пользователя к задаче"
    )
