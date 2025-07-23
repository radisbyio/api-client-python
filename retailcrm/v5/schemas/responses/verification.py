from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.verification import SmsVerification


class VerificationConfirmResponse(SuccessResponse):
    verification: SmsVerification | None = None