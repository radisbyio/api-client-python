from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas import BaseRetailCrmScheme
from retailcrm.v5.schemas.callbacks.entities.payments import Result
from retailcrm.v5.schemas.entities.payments import ModuleRefund


class PaymentCreateCallbackResponse(BaseRetailCrmScheme):
    result: Optional[Result] = Field(
        None, description="JSON с информацией о созданном платеже"
    )


class PaymentRefundCallbackResponse(BaseRetailCrmScheme):
    result: Optional[ModuleRefund] = Field(None, description="JSON с данными возврата")
