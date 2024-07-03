from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_serializer

from retailcrm.v5.enums import RefundStatuses
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import RetailCrmResponse
from retailcrm.v5.schemas.requests import Customer
from retailcrm.v5.schemas.shared import Item

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


class ApiCheckRequest(BaseModel):
    invoiceUuid: Optional[str] = Field(None, description="UUID инвойса в системе")
    amount: Optional[float] = Field(None, description="Сумма")
    currency: Optional[str] = Field(None, description="Код валюты в формате ISO-4217")


class ApiCheckResponseResult(RetailCrmResponse):
    success: bool = Field(False, description="Результат проверки (успешный/неуспешный)")
    error_msg: str = Field(
        "", description="Текст ошибки (в случае, если проверка не прошла)"
    )


class PaymentCheckResponse(RetailCrmResponse):
    result: Optional[ApiCheckResponseResult] = Field(
        None, description="Объект с результатом проверки"
    )


class ApiCreateInvoiceRequest(BaseModel):
    paymentId: Optional[int] = Field(None, description="Внутренний ID платежа")
    returnUrl: Optional[str] = Field(
        None,
        description="URL, на который вернется пользователь после подтверждения или отмены платежа",
    )


class ApiCreateInvoiceResponseResult(BaseModel):
    link: str = Field("", description="Ссылка на страницу оплаты для покупателя")


class PaymentCreateInvoiceResponse(RetailCrmResponse):
    result: Optional[ApiCreateInvoiceRequest] = Field(
        None, description="JSON с данными созданного инвойса"
    )


class ModuleRefund(BaseModel):
    id: Optional[str] = Field(
        None, description="Внутренний идентификатор возврата в модуле"
    )
    status: Optional[RefundStatuses] = Field(None, description="Статус возврата.")
    comment: Optional[str] = Field(None, description="Комментарий")
    amount: Optional[str] = Field(None, description="Сумма возврата")


class ApiUpdateInvoiceRequest(BaseModel):
    invoiceUuid: str = Field("", description="UUID инвойса в системе")
    paymentId: str = Field(
        "", description="Внутренний идентификатор оплаты в модуле (UUID)"
    )
    amount: float = Field(0, description="Сумма платежа")
    status: str = Field("", description="Код статуса оплаты")
    cancellationDetails: str = Field("", description="Причина отмены платежа")
    invoiceUrl: str = Field("", description="Ссылка на страницу оплаты для покупателя")
    paidAt: Optional[datetime] = Field(None, description="Дата и время оплаты")
    expiredAt: Optional[datetime] = Field(
        None,
        description="Дата и время, до которых платеж будет ожидать подтверждения или отмены (при двухстадийной оплате)",
    )
    refund: Optional[ModuleRefund] = Field(None, description="JSON с данными возврата")
    refundable: bool = Field(False, description="Признак возможности возврата платежа")
    cancellable: bool = Field(False, description="Признак возможности отмены платежа")

    paidAt_serializer = field_serializer("paidAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    expiredAt_serializer = field_serializer("expiredAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class PaymentUpdateInvoiceResponse(RetailCrmResponse):
    pass


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
