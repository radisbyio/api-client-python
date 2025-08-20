from datetime import datetime
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas import SuccessResponse
from retailcrm.v5.schemas.base import PaginatedResponse
from retailcrm.v5.schemas.entities.orders import Order, OrderHistory


class OrdersFilterResponse(PaginatedResponse):
    orders: list[Order] = Field(default_factory=list, description="Заказ")


class OrderGetResponse(SuccessResponse):
    order: Optional[Order] = Field(None, description="Заказ")


class OrdersCreateResponse(SuccessResponse):
    order: Optional[Order] = Field(None, description="Заказ")



class OrdersHistoryResponse(PaginatedResponse):
    generated_at: Optional[datetime] = Field(
        None, description="Время формирования ответа", validation_alias="generatedAt"
    )
    history: list[OrderHistory] = Field(default_factory=list)