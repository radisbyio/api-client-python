from datetime import datetime

from pydantic import Field, field_serializer, RootModel

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme, RetailCrmResponse
from retailcrm.v5.schemas.shared import SerializedEntityOrder, SerializedEntityCustomer, SerializedSource


class ClientId(BaseRetailCrmScheme):
    value: str = Field(..., description="Значение добавляемого clientId")
    createdAt: datetime | None = Field(None, description="Дата добавления clientId")
    site: str | None = Field(None, description="Символьный код магазина")
    order: SerializedEntityOrder | None = Field(None, description="Заказ")
    customer: SerializedEntityCustomer | None = Field(None, description="Клиент")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class ClientIdsUploadList(RootModel):
    root: list[ClientId] = Field(default_factory=list)


class ClientIdsUploadResponse(RetailCrmResponse):
    failedClientIds: list[ClientId] = Field(default_factory=list, description="")


class Source(BaseRetailCrmScheme):
    source: str | None = Field(None, description="Источник")
    medium: str | None = Field(None, description="Канал")
    campaign: str | None = Field(None, description="Кампания")
    keyword: str | None = Field(None, description="Ключевое слово")
    content: str | None = Field(None, description="Содержание кампании")
    clientId: str | None = Field(
        None, description="clientId веб-аналитики, к которому будет привязан источник"
    )
    site: str | None = Field(
        None, description="Символьный код магазина, в котором ищется заказ или клиент"
    )
    order: SerializedEntityOrder | None = Field(None, description="Заказ")
    customer: SerializedEntityCustomer | None = Field(None, description="Клиент")


class SourcesUploadList(RootModel):
    root: list[Source] = Field(default_factory=list)


class SourcesUploadResponse(RetailCrmResponse):
    failedSources: list[Source] = Field(default_factory=list, description="Массив источников для загрузки")


class Page(BaseRetailCrmScheme):
    url: str = Field(..., description="URL страницы")
    title: str | None = Field(None, description="Заголовок страницы")
    countViews: int | None = Field(
        None, description="Количество просмотров страницы"
    )
    timeOnPage: int | None = Field(
        None, description="Время, проведенное на странице в миллисекундах"
    )


class Visit(BaseRetailCrmScheme):
    createdAt: datetime = Field(
        ..., description="Дата-время начала визита", validation_alias="createdAt"
    )
    visitLength: int | str = Field(None, description="Длительность визита в секундах")
    exitPage: str | None = Field(None, description="Страница выхода")
    landingPage: str | None = Field(None, description="Страница входа")
    pageViews: int | None = Field(
        None, description="Количество страниц, просмотренных в ходе визита"
    )
    pageDepth: int | None = Field(None, description="Глубина просмотра")
    customer: SerializedEntityCustomer | None = Field(None, description="Клиент")
    source: SerializedSource | None = Field(None, description="Данные по источнику клиента")
    pages: list[Page] = Field(default_factory=list, description="Массив страниц для загрузки")
    clientId: str | None = Field(
        None, description="clientId веб-аналитики, к которому будет привязан визит"
    )
    site: str | None = Field(
        None, description="Символьный код магазина, в котором ищутся страницы или клиент"
    )
    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class VisitUploadList(RootModel):
    root: list[Visit] = Field(default_factory=list, description="Массив визитов для загрузки")


class VisitsUploadResponse(RetailCrmResponse):
    failedVisits: list[Visit] = Field(default_factory=list, description="Массив визитов для загрузки")
