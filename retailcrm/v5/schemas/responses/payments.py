from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.payments import ApiCheckResponseResult, ApiCreateInvoiceRequest, PaymentInvoice


class CheckResponsePayment(SuccessResponse):
    result: Optional[ApiCheckResponseResult] = Field(
        None, description="Объект с результатом проверки"
    )


class CreateInvoiceResponsePayment(SuccessResponse):
    result: Optional[ApiCreateInvoiceRequest] = Field(
        None, description="JSON с данными созданного инвойса"
    )

class InvoiceImportResponse(SuccessResponse):
    invoice: Optional[PaymentInvoice] = Field(None)


class InvoiceResponse(SuccessResponse):
    invoice: Optional[InvoiceDetails] = Field(None)