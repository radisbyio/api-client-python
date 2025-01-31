from datetime import datetime

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas import BaseRetailCrmScheme, RetailCrmResponse


class SmsVerification(BaseRetailCrmScheme):
    createdAt: datetime | None = Field(None, description="Дата создания")
    expiredAt: datetime | None = Field(None, description="Дата окончания срока жизни")
    verifiedAt: datetime | None = Field(None, description="Дата успешной верификации")
    checkId: str | None = Field(None, description="Идентификатор проверки кода")
    actionType: str | None = Field(None, description="Тип действия")


    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    expiredAt_serializer = field_serializer("expiredAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    verifiedAt_serializer = field_serializer("verifiedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class SmsVerificationConfirm(BaseRetailCrmScheme):
    code: str = Field(..., description="Проверочный код")
    checkId: str = Field(..., description="Идентификатор проверки кода")


class VerificationConfirmResponse(RetailCrmResponse):
    verification: SmsVerification | None = None