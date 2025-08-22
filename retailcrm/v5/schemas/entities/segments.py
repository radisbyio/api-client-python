from datetime import datetime
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class Segment(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID сегмента")
    code: Optional[str] = Field(None, description="Символьный код")
    name: Optional[str] = Field(None, description="Название сегмента")
    createdAt: Optional[datetime] = Field(None, description="Дата создания сегмента")
    isDynamic: Optional[bool] = Field(
        None, description="Является ли сегмент автоматически пересчитываемым"
    )
    customersCount: Optional[int] = Field(
        None, description="Количество клиентов в сегменте"
    )
    active: Optional[bool] = Field(None, description="Активность сегмента")
