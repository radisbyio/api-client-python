from datetime import datetime

from pydantic import BaseModel, Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.entities.transports import ChatDevice, ChatLastVisit, ChatUtm

__all__ = ["MgTransportOnlineResponse", "MgTransportVisitsResponse"]


class MgTransportOnlineResponse(BaseModel):
    lastOnline: datetime | None = Field(
        None, description="Дата последнего онлайн-статуса пользователя"
    )

    lastOnline_serializer = field_serializer("lastOnline")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class MgTransportVisitsResponse(BaseModel):
    lastVisit: ChatLastVisit | None = Field(
        None, description="Данные последнего посещения"
    )
    countVisits: int | None = Field(None, description="Количество посещений")
    device: ChatDevice | None = Field(
        None, description="Информация об устройстве пользователя"
    )
    country: str | None = Field(None, description="Страна пользователя")
    utm: ChatUtm | None = Field(None, description="UTM-метки пользователя")
    city: str | None = Field(None, description="Город пользователя")
