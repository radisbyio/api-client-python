from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class CostFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="ID расходов")
    costItems: Optional[list[str]] = Field(
        None, description="Массив символьных кодов статей расходов"
    )
    sites: Optional[list[str]] = Field(
        None, description="Массив символьных кодов магазинов, связанных с расходами"
    )
    createdBy: Optional[list[int]] = Field(
        None, description="Массив ID пользователей, создавших расход"
    )
    orderNumber: Optional[str] = Field(
        None, description="Номер заказа связанного с расходом"
    )
    costGroups: Optional[list[str]] = Field(
        None, description="Массив символьных кодов групп расходов"
    )
    users: Optional[list[int]] = Field(
        None, description="Массив ID пользователей, связанных с расходами"
    )
    comment: Optional[str] = Field(None, description="Комментарий")
    orderIds: Optional[list[int]] = Field(
        None, description="Массив внутренних ID заказов"
    )
    orderExternalIds: Optional[list[str]] = Field(
        None, description="Массив внешних ID заказов"
    )
    createdAtFrom: Optional[datetime] = Field(
        None, description="Дата создания расхода (от)"
    )
    createdAtTo: Optional[datetime] = Field(
        None, description="Дата создания расхода (до)"
    )
    dateFrom: Optional[datetime] = Field(None, description="Период расхода (от)")
    dateTo: Optional[datetime] = Field(None, description="Период расхода (до)")
    minSumm: Optional[int] = Field(None, description="Минимальная сумма расхода")
    maxSumm: Optional[int] = Field(None, description="Максимальная сумма расхода")

    createdAtFrom_serializer = field_serializer("createdAtFrom")(
        datetime_serializer("%Y-%m-%d")
    )
    createdAtTo_serializer = field_serializer("createdAtTo")(
        datetime_serializer("%Y-%m-%d")
    )
    dateFrom_serializer = field_serializer("dateFrom")(datetime_serializer("%Y-%m-%d"))
    dateTo_serializer = field_serializer("dateTo")(datetime_serializer("%Y-%m-%d"))
