from pydantic import Field, field_serializer

from retailcrm.v5.helpers import list_to_json_serializer
from retailcrm.v5.schemas import BaseRetailCrmScheme

from retailcrm.v5.schemas.entities.telephony import CallEvent, CallUpload

__all__ = ["CallEventRequest", "CallsUploadRequest", "ManagerRequest", "MgTelephonyMakeCallUrlRequest", "MgTelephonyPersonalAccountUrlRequest", "MgTelephonyChangeUserStatusUrlRequest"]




class CallEventRequest(BaseRetailCrmScheme):
    event: CallEvent = Field(None, description="Событие звонка")


class CallsUploadRequest(BaseRetailCrmScheme):
    calls: list[CallUpload] = Field(
        None, description="Массив звонков для загрузки (до 50 звонков)"
    )

    calls_serializer = field_serializer("calls")(list_to_json_serializer())

class ManagerRequest(BaseRetailCrmScheme):
    phone: str | None = Field(None, description="Телефон")
    details: str | None = Field(None, description="Детальная информация")
    ignoreStatus: str | None = Field(None, description="Игнорировать статус менеджера")


class MgTelephonyChangeUserStatusUrlRequest(BaseRetailCrmScheme):
    code: str | None = Field(None, description="Добавочный код менеджера")
    userId: str | None = Field(None, description="Id пользователя")
    clientId: str | None = Field(None, description="Id клиента")
    status: str | None = Field(None, description="Статус пользователя в системе")


class MgTelephonyMakeCallUrlRequest(BaseRetailCrmScheme):
    code: str | None = Field(None, description="Добавочный код менеджера")
    phone: str | None = Field(None, description="Телефон")
    clientId: str | None = Field(None, description="Id клиента")
    userId: str | None = Field(None, description="Id пользователя")
    externalPhone: str | None = Field(None, description="Внешний номер телефона")


class MgTelephonyPersonalAccountUrlRequest(BaseRetailCrmScheme):
    clientId: str | None = Field(None, description="Id клиента")
