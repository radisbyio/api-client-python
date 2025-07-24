from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_serializer

from retailcrm.v5.enums.user_statuses import UserStatuses
from retailcrm.v5.helpers import bool_flag_serializer, datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme, RetailCrmResponse


class Group(BaseModel):
    id: int | None = Field(None, description="ID группы")
    name: str | None = Field(None, description="Наименование")
    signatureTemplate: Optional[str] = Field(None, description="Шаблон для подписи")
    code: str | None = Field(None, description="Код")
    isManager: bool | None = Field(None, description="Обрабатывают заказы")
    isDeliveryMen: bool | None = Field(None, description="Группа отвечает за доставку")
    deliveryTypes: Optional[list[str]] = Field(
        None, description="Типы доставок, за которые отвечает группа"
    )
    breakdownOrderTypes: Optional[list[str]] = Field(
        None,
        description="Типы тех заказов, которые распределяются на менеджеров данной группы",
    )
    breakdownSites: Optional[list[str]] = Field(
        None,
        description="Магазины, заказов которых распределяются на менеджеров данной группы",
    )
    breakdownOrderMethods: Optional[list[str]] = Field(
        None,
        description="Способы оформления тех заказов, которые распределяются на менеджеров данной группы",
    )
    grantedOrderTypes: Optional[list[str]] = Field(
        None,
        description="Типы заказов, которые видны менеджерам данной группы, если доступ ограничен",
    )
    grantedSites: Optional[list[str]] = Field(
        None, description="Магазины, заказы которых видны менеджерам данной группы"
    )


class UserGroupsResponse(RetailCrmResponse):
    groups: list[Group] = Field(
        default_factory=list, description="Группа пользователей"
    )


class ApiUserFilter(BaseRetailCrmScheme):
    email: Optional[str] = Field(None, description="Email пользователя", max_length=255)
    status: Optional[UserStatuses] = Field(
        None,
        description="Статус пользователя в системе. При использовании фильтра `filter[status]` в выборку попадают только пользователи, у которых в поле `online` указано значение `true`.",
    )
    online: Optional[bool] = Field(None, description="Пользователь онлайн")
    active: Optional[bool] = Field(None, description="Активность пользователя")
    isManager: Optional[bool] = Field(None, description="Является менеджером")
    isAdmin: Optional[bool] = Field(None, description="Является администратором")
    groups: Optional[list[str]] = Field(None, description="Группы пользователя")
    createdAtFrom: Optional[datetime] = Field(
        None, description="Дата создания пользователя (от)"
    )
    createdAtTo: Optional[datetime] = Field(
        None, description="Дата создания пользователя (до)"
    )

    createdAtFrom_serializer = field_serializer("createdAtFrom")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    createdAtTo_serializer = field_serializer("createdAtTo")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    online_serializer = field_serializer("online")(bool_flag_serializer())
    active_serializer = field_serializer("active")(bool_flag_serializer())
    isManager_serializer = field_serializer("isManager")(bool_flag_serializer())
    isAdmin_serializer = field_serializer("isAdmin")(bool_flag_serializer())


class SerializedGroups(BaseRetailCrmScheme):
    id: int | None = Field(None, description="ID группы")
    name: str | None = Field(None, description="Название группы")
    code: str | None = Field(None, description="Код группы")


class SerializedUser(BaseRetailCrmScheme):
    id: int| None = Field(None, description="ID пользователя")
    createdAt: datetime | None= Field(None, description="Дата создания пользователя")
    active: bool| None = Field(None, description="Активность")
    email: Optional[str] = Field(None, description="Электронный адрес")
    firstName: str| None = Field(None , description="Имя пользователя")
    lastName: str| None = Field(None, description="Фамилия пользователя")
    patronymic: str| None= Field(None, description="Отчество пользователя")
    position: Optional[str] = Field(None, description="Должность")
    photoUrl: Optional[str] = Field(None, description="URL фотографии")
    phone: Optional[str] = Field(None, description="Телефон")
    status: Optional[str] = Field(None, description="Статус пользователя в системе")
    online: bool | None = Field(None, description="Пользователь онлайн")
    isAdmin: bool | None = Field(None, description="Является администратором")
    isManager: bool | None = Field(None, description="Является менеджером")
    groups: Optional[list[SerializedGroups]] = Field(
        default_factory=list, description="Группы пользователя"
    )
    mgUserId: Optional[int] = Field(None, description="ID MessageGateway пользователя")
    senderEmail: Optional[str] = Field(
        None, description="Адрес отправителя для менеджера"
    )
    senderName: Optional[str] = Field(None, description="Имя отправителя")
    language: Optional[str] = Field(None, description="Язык интерфейса")
