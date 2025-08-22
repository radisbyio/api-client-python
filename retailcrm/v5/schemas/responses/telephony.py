from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.telephony import Customer, Links, Manager


class CallEventResponse(SuccessResponse):
    notExistCodes: Optional[list[str]] = Field(
        None, description="Массив добавочных кодов, которые отсутствуют в системе"
    )
    notExistUsers: Optional[list[int]] = Field(
        None, description="Массив userId, которые отсутствуют в системе"
    )


class CallsUploadResponse(SuccessResponse):
    processedCallsCount: Optional[int] = Field(
        None, description="Количество успешно обработанных звонков"
    )
    duplicateCalls: Optional[list[str]] = Field(
        None, description="Массив externalId, которые уже присутствуют в системе"
    )


class ManagerResponse(SuccessResponse):
    manager: Optional[Manager] = Field(None, description="Менеджер")
    customer: Optional[Customer] = Field(None, description="Клиент")
    links: Optional[Links] = Field(None, description="Ссылки")
