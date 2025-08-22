from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class SegmentsFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID сегментов")
    name: Optional[str] = Field(None, description="Название сегмента")
    isTree: Optional[bool] = Field(None)
    active: Optional[bool] = Field(None, description="Активность")
    dateFrom: Optional[datetime] = Field(None, description="Дата создания (от)")
    dateTo: Optional[datetime] = Field(None, description="Дата создания (до)")
    minCustomersCount: Optional[int] = Field(None, description="Число клиентов (от)")
    maxCustomersCount: Optional[int] = Field(None, description="Число клиентов (до)")
    type: Optional[str] = Field(
        None, description="Тип сегмента", pattern="^(dynamic|static)$"
    )

    dateFrom_serializer = field_serializer("dateFrom")(datetime_serializer("%Y-%m-%d"))
    dateTo_serializer = field_serializer("dateTo")(datetime_serializer("%Y-%m-%d"))
