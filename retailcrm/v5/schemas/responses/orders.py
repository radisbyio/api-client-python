from datetime import datetime
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import PaginatedResponse, IdTypesLiteral, SuccessResponse
from retailcrm.v5.schemas.entities.loyalty import SmsVerification
from retailcrm.v5.schemas.entities.orders import Order, OrderHistory, SerializedLoyaltyOrder, SerializedPayment


class OrdersFilterResponse(PaginatedResponse):
    orders: list[Order] = Field(default_factory=list, description="Заказ")


class OrderGetResponse(SuccessResponse):
    order: Optional[Order] = Field(None, description="Заказ")


class OrdersCreateResponse(SuccessResponse):
    order: Optional[Order] = Field(None, description="Заказ")



class OrdersHistoryResponse(PaginatedResponse):
    generatedAt: Optional[datetime] = Field(
        None, description="Время формирования ответа"
    )
    history: list[OrderHistory] = Field(default_factory=list)


class LoyaltyApplyResponse(SuccessResponse):
    order: SerializedLoyaltyOrder | None = Field(None)
    verification: SmsVerification | None = Field(None, description="SMS-верификация")


class LoyaltyCancelBonusOperationsResponse(SuccessResponse):
    order: Order | None = Field(None, description="Заказ")


class OrdersPaymentCreateResponse(SuccessResponse):
    payment: Optional[SerializedPayment] = Field(None)
