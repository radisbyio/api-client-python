from datetime import datetime
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas import BaseRetailCrmScheme


class Segment(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID сегмента")
    code: Optional[str] = Field(None, description="Символьный код")
    name: Optional[str] = Field(None, description="Название сегмента")
    created_at: Optional[datetime] = Field(None, alias="createdAt", description="Дата создания сегмента")
    is_dynamic: Optional[bool] = Field(None, alias="isDynamic", description="Является ли сегмент автоматически пересчитываемым")
    customers_count: Optional[int] = Field(None, alias="customersCount", description="Количество клиентов в сегменте")
    active: Optional[bool] = Field(None, description="Активность сегмента")