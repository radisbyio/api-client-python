from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.enums.telephony import CallEventType, HangupStatus, CallUploadType, CallResult
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.shared.customer_phone import CustomerPhone
from retailcrm.v5.schemas.shared.source import SerializedSource

__all__ = ["SerializedCampaign", "WebAnalyticsData", "CallEvent", "CallUpload", "Manager", "Customer", "Links"]


class SerializedCampaign(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название рекламной кампании")
    code: Optional[str] = Field(None, description="Код рекламной кампании")


class WebAnalyticsData(BaseRetailCrmScheme):
    campaign: Optional[SerializedCampaign] = Field(None, description="Рекламная кампания")
    queryString: Optional[str] = Field(
        None, description="Поисковый запрос"
    )


class CallEvent(BaseRetailCrmScheme):
    phone: str | None = Field(None, description="Телефон")
    type: CallEventType | None = Field(None, description="Тип события")
    codes: Optional[list[str]] = Field(
        None, description="Добавочные коды менеджеров"
    )
    userIds: Optional[list[int]] = Field(
        default_factory=list, description="Массив ID пользователей"
    )
    site: Optional[str] = Field(
        None, description="Символьный код магазина, связанного с событием звонка"
    )
    hangupStatus: Optional[HangupStatus] = Field(
        None, description="Статус завершения звонка"
    )
    externalPhone: Optional[str] = Field(
        None, description="Внешний номер телефона"
    )
    callExternalId: Optional[str] = Field(
        None,
        description="External Id связанного с событием звонка",
    )
    webAnalyticsData: Optional[WebAnalyticsData] = Field(
        None, description="Данные веб-аналитики"
    )


class CallUpload(BaseRetailCrmScheme):
    date_: datetime | None = Field(None, description="Дата/время звонка в формате Y-m-d H:i:s", serialization_alias="date")
    type: CallUploadType | None  = Field(None, description="Тип звонка")
    phone: str | None = Field(None, description="Номер телефона")
    code: Optional[str] = Field(
        None, description="Внутренний номер пользователя, который обрабатывал звонок"
    )
    userId: Optional[int] = Field(
        None, description="Id пользователя, который обрабатывал звонок"
    )
    result: CallResult  | None = Field(None, description="Результат звонка")
    duration: Optional[int] = Field(
        None, description="Длительность звонка (в секундах)"
    )
    durationWaiting: Optional[int] = Field(
        None, description="Время ожидания ответа оператора (в секундах)"
    )
    externalId: str  | None = Field(None, description="ID звонка в АТС")
    recordUrl: Optional[str] = Field(
        None, description="Ссылка на запись звонка"
    )
    source: Optional[SerializedSource] = Field(None, description="Источник")
    externalPhone: Optional[str] = Field(
        None, description="Внешний номер телефона"
    )
    site: Optional[str] = Field(None, description="Символьный код магазина")
    clientId: Optional[str] = Field(None, description="Метка клиента Google Analytics")

    date_serializer = field_serializer("date_")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class Manager(BaseRetailCrmScheme):
    id: Optional[str] = Field(None, description="Id менеджера")
    first_name: Optional[str] = Field(None, description="Имя менеджера", alias="firstName")
    last_name: Optional[str] = Field(None, description="Фамилия менеджера", alias="lastName")
    patronymic: Optional[str] = Field(None, description="Отчество менеджера")
    email: Optional[str] = Field(None, description="Электронный адрес")
    code: Optional[str] = Field(None, description="Добавочный код менеджера в телефонии")


class Customer(BaseRetailCrmScheme):
    id: Optional[str] = Field(None, description="Id клиента")
    external_id: Optional[str] = Field(None, description="Идентификатор с внешнего сайта", alias="externalId")
    first_name: Optional[str] = Field(None, description="Имя клиента", alias="firstName")
    last_name: Optional[str] = Field(None, description="Фамилия клиента", alias="lastName")
    patronymic: Optional[str] = Field(None, description="Отчество клиента")
    email: Optional[str] = Field(None, description="Электронный адрес")
    phones: Optional[list[CustomerPhone]] = Field(default_factory=list, description="Телефоны клиента")


class Links(BaseRetailCrmScheme):
    new_order_link: Optional[str] = Field(None, description="Ссылка на страницу создания нового заказа", alias="newOrderLink")
    last_order_link: Optional[str] = Field(None, description="Ссылка на страницу последнего заказа", alias="lastOrderLink")
    new_customer_link: Optional[str] = Field(None, description="Ссылка на страницу создания нового клиента", alias="newCustomerLink")
    customer_link: Optional[str] = Field(None, description="Ссылка на страницу клиента", alias="customerLink")