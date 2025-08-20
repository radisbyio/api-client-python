from datetime import datetime
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
    "DeliveryService",
    "SerializedDeliveryService",
    "PaymentType",
]





class ResponseStatuses(RetailCrmResponse):
    statuses: dict[str, Status] = Field(
        default_factory=list, description="Статусы заказа"
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


















class ResponseSites(RetailCrmResponse):
    sites: dict[str, Site] = Field(default_factory=dict)



class SerializedOrderProductStatus(BaseModel):
    name: Optional[str] = Field(None)
    code: Optional[str] = Field(None)
    type: Optional[str] = Field(None)
    ordering: Optional[int] = Field(None)
    active: Optional[bool] = Field(None)
    cancelStatus: Optional[bool] = Field(None)
    orderStatusByProductStatus: Optional[str] = Field(None)
    orderStatusForProductStatus: Optional[str] = Field(None)














class Currency(BaseModel):
    id: int = Field(description="ID")
    code: str = Field(description="Код валюты")
    isBase: bool = Field(False, description="Является базовой валютой")
    isAutoConvert: bool = Field(False, description="Автоматическая конвертация валюты")
    autoConvertExtraPercent: Optional[int] = Field(
        None, description="Наценка в % при автоматической конвертации"
    )
    manualConvertNominal: Optional[int] = Field(
        None, description="Номинал валюты при ручной конвертации"
    )
    manualConvertValue: Optional[float] = Field(
        None, description="Курс валюты при ручной конвертации"
    )


class ResponseCurrencies(RetailCrmResponse):
    currencies: list[Currency] = Field(default_factory=list, description="Валюта")


class SerializedCurrency(BaseModel):
    code: Optional[str] = Field(None, description="Код валюты")
    isAutoConvert: Optional[bool] = Field(
        None, description="Автоматическая конвертация валюты"
    )
    autoConvertExtraPercent: Optional[int] = Field(
        None, description="Наценка в % при автоматической конвертации"
    )
    manualConvertNominal: Optional[int] = Field(
        None, description="Номинал валюты при ручной конвертации"
    )
    manualConvertValue: Optional[float] = Field(
        None, description="Курс валюты при ручной конвертации"
    )


class ResponseCurrenciesCreate(RetailCrmResponse):
    id: Optional[int] = Field(None, description="Внутренний ID созданного объекта")













class ResponseDeliveryTypes(RetailCrmResponse):
    deliveryTypes: dict[str, DeliveryType] = Field(
        default_factory=dict, description="Тип доставки"
    )


# TODO: Stores
# TODO: Units
