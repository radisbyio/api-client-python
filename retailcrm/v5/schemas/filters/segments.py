from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.schemas import BaseRetailCrmScheme
from retailcrm.v5.helpers import datetime_serializer


class SegmentsFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID сегментов")
    name: Optional[str] = Field(None, description="Название сегмента", max_length=255)
    isTree: Optional[bool] = Field(None)
    active: Optional[bool] = Field(None, description="Активность")
    date_from: Optional[datetime] = Field(None, alias="dateFrom", description="Дата создания (от)")
    date_to: Optional[datetime] = Field(None, alias="dateTo", description="Дата создания (до)")
    min_customers_count: Optional[int] = Field(None, alias="minCustomersCount", description="Число клиентов (от)")
    max_customers_count: Optional[int] = Field(None, alias="maxCustomersCount", description="Число клиентов (до)")
    type: Optional[str] = Field(None, description="Тип сегмента", pattern="^(dynamic|static)$")

    date_from_serializer = field_serializer("date_from")(datetime_serializer("%Y-%m-%d"))
    date_to_serializer = field_serializer("date_to")(datetime_serializer("%Y-%m-%d"))
