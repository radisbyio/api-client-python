from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.callbacks.entities.payments import Result
from retailcrm.v5.schemas.entities.payments import ModuleRefund


class PaymentCreateCallbackResponse(SuccessResponse):
    result: Optional[Result] = Field(
        None, description="JSON с информацией о созданном платеже"
    )


class PaymentRefundCallbackResponse(SuccessResponse):
    result: Optional[ModuleRefund] = Field(None, description="JSON с данными возврата")
