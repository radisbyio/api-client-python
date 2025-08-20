from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_serializer

from retailcrm.v5.enums import RefundStatuses
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import RetailCrmResponse
from retailcrm.v5.schemas.shared import Customer, Item

__all__ = [
    "ApiCheckRequest",
    "ApiCheckResponseResult",
    "PaymentCheckResponse",
    "ApiCreateInvoiceRequest",
    "ApiCreateInvoiceResponseResult",
    "PaymentCreateInvoiceResponse",
    "ApiUpdateInvoiceRequest",
    "ModuleRefund",
    "PaymentUpdateInvoiceResponse",
]



"""
    Callbacks
"""


class ModuleApiRequest(BaseModel):
    paymentId: Optional[str] = Field(
        "", description="Внутренний идентификатор оплаты в модуле"
    )
    amount: Optional[float] = Field(
        0, description="Итоговая сумма, которая спишется с клиента"
    )


class PaymentApproveCallbackResponse(BaseModel):
    pass


class PaymentCancelCallbackResponse(BaseModel):
    pass


class Create(BaseModel):
    shopId: Optional[str] = Field(description="ID магазина")
    invoiceUuid: Optional[str] = Field(
        description="Идентификатор инвойса в системе(UUID). Все обращения к API системы совершаются через этот ID."
    )
    invoiceType: Optional[str] = Field(
        description="Тип инвойса. Возможные значения: link"
    )
    amount: Optional[float] = Field(description="Сумма в выбранной валюте")
    currency: Optional[str] = Field(description="Код валюты в формате ISO-4217")
    orderNumber: Optional[str] = Field(description="Номер заказа")
    orderId: Optional[int] = Field(description="Внутренний ID заказа")
    siteUrl: Optional[str] = Field("", description="URL магазина")
    returnUrl: Optional[str] = Field(
        "",
        description="URL, на который вернется пользователь после подтверждения или отмены платежа",
    )
    items: list[Item] = Field([], description="Список товаров")
    customer: Customer


class PaymentCreateResult(BaseModel):
    paymentId: str = Field("", description="Внутренний идентификатор оплаты в модуле")
    invoiceUrl: str = Field("", description="Ссылка на страницу оплаты для покупателя")
    cancellable: bool = Field(False, description="Признак возможности отмены платежа")


class PaymentCreateCallbackResponse(BaseModel):
    result: Optional[PaymentCreateResult] = Field(
        None, description="JSON с информацией о созданном платеже"
    )


class PaymentRefundCallbackResponse(BaseModel):
    result: Optional[ModuleRefund] = Field(None, description="JSON с данными возврата")
