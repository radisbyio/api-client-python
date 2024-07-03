from typing import Optional

from pydantic import BaseModel, Field

from retailcrm.v5.schemas.base import RetailCrmResponse
from retailcrm.v5.schemas.shared import Courier, CourierPhone, SerializedSource

__all__ = [
    "Status",
    "ResponseStatuses",
    "StatusGroup",
    "ResponseStatusGroups",
    "CostGroup",
    "ResponseCostGroups",
    "SerializedCostGroup",
    "CostItem",
    "ResponseCostItems",
    "SerializedCostItem",
    "ResponseCostItems",
    "ResponseCountries",
    "ResponseCouriers",
    "SerializedCourier",
]


class Status(BaseModel):
    name: str = Field(description="Название")
    code: str = Field(description="Символьный код")
    active: bool = Field(False, description="Статус активности")
    ordering: int = Field(description="Порядок")
    group: str = Field(description="Группа статусов, к которой относится статус")


class ResponseStatuses(RetailCrmResponse):
    statuses: dict[str, Status] = Field(
        default_factory=list, description="Статусы заказа"
    )


class StatusGroup(BaseModel):
    name: str = Field(description="Название")
    code: str = Field(description="Символьный код")
    active: bool = Field(False, description="Статус активности")
    ordering: int = Field(description="Порядок")
    process: bool = Field(
        False, description="Является или нет процессным состоянием заказа"
    )
    statuses: list[str] = Field(
        default_factory=list,
        description="Статусы заказов, которые входят в данную группу",
    )


class ResponseStatusGroups(RetailCrmResponse):
    statusGroups: dict[str, StatusGroup] = Field(
        default_factory=list, description="Группа статусов"
    )


class CostGroup(BaseModel):
    code: str = Field(description="Символьный код группы расходов")
    name: str = Field(description="Название группы расходов")
    ordering: int = Field(description="Порядок")
    active: bool = Field(False, description="Активность")
    color: str = Field(description="Цвет")


class ResponseCostGroups(RetailCrmResponse):
    costGroups: list[CostGroup] = Field(
        default_factory=list, description="Группа расходов"
    )


class SerializedCostGroup(BaseModel):
    code: Optional[str] = Field(None, description="Символьный код группы расходов")
    name: Optional[str] = Field(None, description="Название группы расходов")
    ordering: Optional[int] = Field(None, description="Порядок")
    active: Optional[bool] = Field(None, description="Активность")
    color: Optional[str] = Field(
        None,
        description="Цвет",
        examples=[
            "#19976e",
            "#4191ff",
            "#6ce0b9",
            "#8453df",
            "#8a96a6",
            "#bc6b01",
            "#c7cdd4",
            "#ef8e06",
            "#ff8e87",
            "#ffd298",
        ],
    )


class CostItem(BaseModel):
    source: Optional[SerializedSource] = Field(
        None, description="Данные по источнику клиента"
    )
    code: str = Field(description="Символьный код статьи расходов")
    name: str = Field(description="Название статьи расходов")
    group: str = Field(description="Символьный код группы расходов")
    ordering: int = Field(description="Порядок")
    active: bool = Field(False, description="Активность")
    appliesToOrders: bool = Field(False, description="Относится к расходам по заказам")
    type: str = Field(description="Тип расхода")
    appliesToUsers: bool = Field(
        False, description="Относится к расходам по пользователям"
    )


class ResponseCostItems(RetailCrmResponse):
    costItems: list[CostItem] = Field([], description="Статьи расходов")


class SerializedCostItem(BaseModel):
    code: Optional[str] = Field(None, description="Символьный код статьи расходов")
    name: Optional[str] = Field(None, description="Название статьи расходов")
    ordering: Optional[int] = Field(None, description="Порядок")
    active: bool = Field(False, description="Активность")
    appliesToOrders: bool = Field(False, description="Относится к расходам по заказам")
    appliesToUsers: bool = Field(
        False, description="Относится к расходам по пользователям"
    )
    group: Optional[str] = Field(None, description="Символьный код группы расходов")
    source: Optional[SerializedSource] = Field(
        None, description="Данные по источнику клиента"
    )
    type: Optional[str] = Field(None, description="Тип расхода")


class ResponseCountries(RetailCrmResponse):
    countriesIso: list[str] = Field(
        default_factory=list,
        description="Список ISO 3166-1 alpha-2 кодов активных стран",
    )


class ResponseCouriers(RetailCrmResponse):
    couriers: list[Courier] = Field(default_factory=list, description="Курьеры")


class SerializedCourier(BaseModel):
    firstName: Optional[str] = Field(None, description="Имя")
    lastName: Optional[str] = Field(None, description="Фамилия")
    patronymic: Optional[str] = Field(None, description="Отчество")
    active: Optional[bool] = Field(None, description="Признак активности")
    email: Optional[str] = Field(None, description="Электронная почта")
    description: Optional[str] = Field(None, description="Примечание")
    phone: Optional[CourierPhone] = Field(None, description="Контактный телефон")
