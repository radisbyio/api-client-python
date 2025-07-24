from datetime import datetime

from pydantic import BaseModel, Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer


class ChatVisitedPage(BaseModel):
    dateTime: datetime | None = Field(None, description="Дата и время посещения страницы")
    url: str | None = Field(None, description="URL страницы")
    title: str | None | None = Field(None, description="Заголовок страницы")

    dateTime_serializer = field_serializer("dateTime")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class ChatLastVisit(BaseModel):
    source: str | None = Field(None, description="Источник визита")
    createdAt: datetime | None = Field(None, description="Дата начала визита")
    endedAt: datetime | None = Field(None, description="Дата окончания визита")
    duration: int | None = Field(None, description="Продолжительность визита в секундах")
    pages: list[ChatVisitedPage] = Field(default_factory=list, description="Посещенные страницы")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    endedAt_serializer = field_serializer("endedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class ChatUtm(BaseModel):
    source: str | None = Field(None, description="Значение метки utm_source")
    medium: str | None = Field(None, description="Значение метки utm_medium")
    campaign: str | None = Field(None, description="Значение метки utm_campaign")


class ChatDevice(BaseModel):
    lang: str | None = Field(None, description="Язык на устройстве пользователя (в формате en_US)")
    browser: str | None = Field(None, description="Информация об устройстве пользователя")
    os: str | None = Field(None, description="Тип ОС пользователя")
