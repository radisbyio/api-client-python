from datetime import datetime
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.shared.order import SerializedEntityOrder
from retailcrm.v5.schemas.shared.source import SerializedSource


class CostsOrder(BaseRetailCrmScheme):
    id: int | None = Field(None, description="ID заказа")
    externalId: str | None = Field(None, description="Внешний ID заказа")
    number: str | None = Field(None, description="Номер заказа")


class Cost(BaseRetailCrmScheme):
    currency: Optional[str] = Field(None, description="Валюта")
    source: Optional[SerializedSource] = Field(None, description="Данные по источнику клиента")
    id: Optional[int] = Field(None, description="ID расхода")
    dateFrom: Optional[datetime] = Field(None, description="Дата (от)")
    dateTo: Optional[datetime] = Field(None, description="Дата (до)")
    summ: Optional[float] = Field(None, description="Сумма (в базовой валюте)")
    costItem: Optional[str] = Field(None, description="Код статьи расхода")
    comment: Optional[str] = Field(None, description="Комментарий")
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    createdBy: Optional[str] = Field(None, description="ID пользователя, создавшего расход")
    order: Optional[CostsOrder] = Field(None, description="Заказ")
    userId: Optional[int] = Field(None, description="ID пользователя, связанного с расходом")
    sites: list[str] = Field(default_factory=list, description="Символьные коды магазинов, по которым понесён расход")


class SerializedCost(BaseRetailCrmScheme):
    dateFrom: Optional[datetime] = Field(None, description="Дата (от)")
    dateTo: Optional[datetime] = Field(None, description="Дата (до)")
    summ: Optional[float] = Field(None, description="Сумма (в базовой валюте)")
    comment: Optional[str] = Field(None, description="Комментарий")
    costItem: Optional[str] = Field(None, description="Код статьи расхода")
    order: Optional[SerializedEntityOrder] = Field(None, description="Заказ")
    userId: Optional[int] = Field(None, description="ID пользователя, связанного с расходом")
    sites: Optional[list[str]] = Field(None, description="Символьные коды магазинов, по которым понесён расход")
    source: Optional[SerializedSource] = Field(None, description="Данные по источнику клиента")