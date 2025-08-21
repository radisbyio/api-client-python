import decimal
from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.enums import RefundStatuses
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class ApiCheckRequest(BaseRetailCrmScheme):
    invoiceUuid: Optional[str] = Field(None, description="UUID инвойса в системе")
    amount: Optional[decimal.Decimal] = Field(None, description="Сумма")
    currency: Optional[str] = Field(None, description="Код валюты в формате ISO-4217")

class ApiCheckResponseResult(BaseRetailCrmScheme):
    success: Optional[bool] = Field(None, description="Результат проверки (успешный/неуспешный)")
    errorMsg: Optional[str] = Field(
        None, description="Текст ошибки (в случае, если проверка не прошла)"
    )


class ApiCreateInvoiceRequest(BaseRetailCrmScheme):
    paymentId: Optional[int] = Field(None, description="Внутренний ID платежа")
    returnUrl: Optional[str] = Field(
        None,
        description="URL, на который вернется пользователь после подтверждения или отмены платежа",
    )

class ApiCreateInvoiceResponseResult(BaseRetailCrmScheme):
    link: Optional[str] = Field(None, description="Ссылка на страницу оплаты для покупателя")


class ModuleRefund(BaseRetailCrmScheme):
    id: Optional[str] = Field(
        None, description="Внутренний идентификатор возврата в модуле"
    )
    status: Optional[RefundStatuses] = Field(None, description="Статус возврата.")
    comment: Optional[str] = Field(None, description="Комментарий")
    amount: Optional[str] = Field(None, description="Сумма возврата")


class ApiUpdateInvoiceRequest(BaseRetailCrmScheme):
    invoiceUuid: Optional[str] = Field(None, description="UUID инвойса в системе")
    paymentId: Optional[str] = Field(
        None, description="Внутренний идентификатор оплаты в модуле (UUID)"
    )
    amount: Optional[decimal.Decimal] = Field(None, description="Сумма платежа")
    status: Optional[str] = Field(None, description="Код статуса оплаты")
    cancellationDetails: Optional[str] = Field(None, description="Причина отмены платежа")
    invoiceUrl: Optional[str] = Field(None, description="Ссылка на страницу оплаты для покупателя")
    paidAt: Optional[datetime] = Field(None, description="Дата и время оплаты")
    expiredAt: Optional[datetime] = Field(
        None,
        description="Дата и время, до которых платеж будет ожидать подтверждения или отмены (при двухстадийной оплате)",
    )
    refund: Optional[ModuleRefund] = Field(None, description="JSON с данными возврата")
    refundable: Optional[bool] = Field(None, description="Признак возможности возврата платежа")
    cancellable: Optional[bool] = Field(None, description="Признак возможности отмены платежа")

    paidAt_serializer = field_serializer("paidAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    expiredAt_serializer = field_serializer("expiredAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class ApiImportInvoicePaymentRefund(BaseRetailCrmScheme):
    external_id: Optional[str] = Field(None, alias="externalId", description="Внешний идентификатор возврата в модуле")
    status: Optional[str] = Field(None, description="Статус")
    comment: Optional[str] = Field(None, description="Комментарий")
    amount: Optional[decimal.Decimal] = Field(None, description="Сумма")
    created_at: Optional[datetime] = Field(None, alias="createdAt", description="Дата и время создания")

    created_at_serializer = field_serializer("created_at")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class ApiImportInvoiceRequest(BaseRetailCrmScheme):
    paymentId: Optional[int] = Field(None, description="Внутренний ID платежа")
    externalId: Optional[str] = Field(None, description="Внешний идентификатор оплаты в модуле")
    amount: Optional[decimal.Decimal] = Field(None, description="Сумма")
    currency: Optional[str] = Field(None, description="Код валюты в формате ISO-4217")
    status: Optional[str] = Field(None, description="Статус")
    createdAt: Optional[datetime] = Field(None, description="Дата и время создания")
    paidAt: Optional[datetime] = Field(None, description="Дата и время платежа")
    discountAmount: Optional[decimal.Decimal] = Field(None, description="Скидка")
    refunds: Optional[list[ApiImportInvoicePaymentRefund]] = Field(None, description="Данные возвратов")
    refundable: Optional[bool] = Field(None, description="Возможность сделать возврат")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    paidAt_serializer = field_serializer("paidAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )

class PaymentInvoice(BaseRetailCrmScheme):
    invoice_uuid: Optional[str] = Field(None, alias="invoiceUuid", description="UUID инвойса")


class PaymentRefund(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID возврата")
    status: Optional[str] = Field(None, description="Статус")
    external_id: Optional[str] = Field(None, alias="externalId", description="Внешний ID")
    comment: Optional[str] = Field(None, description="Комментарий")
    amount: Optional[decimal.Decimal] = Field(None, description="Сумма (в валюте объекта)")
    created_at: Optional[datetime] = Field(None, alias="createdAt", description="Дата и время создания")


class InvoiceDetails(BaseRetailCrmScheme):
    createdAt: Optional[datetime] = Field(None, description="Дата и время создания")
    customerId: Optional[int] = Field(None, description="ID покупателя")
    orderId: Optional[int] = Field(None, description="ID заказа")
    paymentId: Optional[int] = Field(None, description="Внутренний ID платежа")
    amount: Optional[str] = Field(None, description="Сумма")
    currency: Optional[str] = Field(None, description="Код валюты в формате ISO-4217")
    email: Optional[str] = Field(None, description="E-mail")
    phone: Optional[str] = Field(None, description="Телефон")
    status: Optional[str] = Field(None, description="Статус")
    statusMessage: Optional[str] = Field(None, description="Комментарий к статусу")
    externalId: Optional[str] = Field(None,
                                       description="Внутренний идентификатор оплаты в модуле")
    invoiceUuid: Optional[str] = Field(None, description="UUID инвойса")
    invoiceType: Optional[str] = Field(None, description="Тип инвойса")
    link: Optional[str] = Field(None, description="Ссылка на страницу оплаты для покупателя")
    errorMsg: Optional[str] = Field(None, description="Ошибка в ответе")
    paidAt: Optional[datetime] = Field(None, description="Дата и время платежа")
    expiredAt: Optional[datetime] = Field(None,
                                           description="Дата и время, до которого инвойс, находящийся в статусе waitingForCapture будет ожидать подтверждения/отмены")
    cancellationDetails: Optional[str] = Field(None,
                                                description="Причина отмены платежа")
    refundable: Optional[bool] = Field(None, description="Возможность сделать возврат")
    cancellable: Optional[bool] = Field(None, description="Возможность отменить платёж")
    refunds: Optional[list[PaymentRefund]] = Field(None, description="Данные возвратов")
    discount_amount: Optional[str] = Field(None, alias="discountAmount",
                                           description="Скидка (в валюте объекта)")