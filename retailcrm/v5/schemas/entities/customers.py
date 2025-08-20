import decimal
from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer, field_validator

from retailcrm.v5.helpers import datetime_serializer, dict_validator
from retailcrm.v5.schemas import BaseRetailCrmScheme
from retailcrm.v5.schemas.shared.customer_phone import CustomerPhone
from retailcrm.v5.schemas.shared.source import SerializedSource


class MGChannel(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID канала")
    externalId: Optional[int] = Field(None, description="Внешний ID канала")
    allowedSendByPhone: Optional[bool] = Field(None, description="Можно ли писать первыми в этот канал по номеру телефона")
    type: Optional[str] = Field(None, description="Тип канала")
    active: Optional[bool] = Field(False, description="Активность канала")
    name: Optional[str] = Field(None, description="Название канала")

class MGCustomer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID клиента")
    externalId: Optional[int] = Field(
        None, description="Внешний ID MessageGateway клиента"
    )
    mgChannel: Optional[MGChannel] = Field(None, description="MessageGateway канал")


class CustomerTagLink(BaseRetailCrmScheme):
    name: Optional[str] = Field(None)
    colorCode: Optional[str] = Field(None)
    attached: Optional[bool] = Field(None)


class CustomerAddress(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID адреса")
    index: Optional[str] = Field(None, description="Индекс")
    countryIso: Optional[str] = Field(
        None, description="ISO код страны (ISO 3166-1 alpha-2)"
    )
    region: Optional[str] = Field(None, description="Регион")
    regionId: Optional[int] = Field(
        None, description="Идентификатор региона в Geohelper"
    )
    city: Optional[str] = Field(None, description="Город")
    cityId: Optional[int] = Field(None, description="Идентификатор города в Geohelper")
    cityType: Optional[str] = Field(None, description="Тип населенного пункта")
    street: Optional[str] = Field(None, description="Улица")
    streetId: Optional[int] = Field(None, description="Идентификатор улицы в Geohelper")
    streetType: Optional[str] = Field(None, description="Тип улицы")
    building: Optional[str] = Field(None, description="Дом")
    flat: Optional[str] = Field(None, description="Номер квартиры/офиса")
    floor: Optional[int] = Field(None, description="Этаж")
    block: Optional[int] = Field(None, description="Подъезд")
    house: Optional[str] = Field(None, description="Строение")
    housing: Optional[str] = Field(None, description="Корпус")
    metro: Optional[str] = Field(None, description="Метро")
    notes: Optional[str] = Field(None, description="Примечания к адресу")
    text: Optional[str] = Field(None, description="Адрес в текстовом виде")
    externalId: Optional[str] = Field(None, description="Внешний ID")
    name: Optional[str] = Field(None, description="Наменование адреса")


class EntityWithExternalIdNameOutput(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID")
    externalId: Optional[str] = Field(None, description="Внешний ID")
    name: Optional[str] = Field(None, description="Название")


class Customer(BaseRetailCrmScheme):
    type: Optional[str] = Field(None, description="Тип клиента")
    id: Optional[int] = Field(None, description="ID клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    isContact: Optional[bool] = Field(
        None, description="Клиент является контактным лицом (создан как контактное лицо и на него нет оформленных заказов)",
    )
    createdAt: Optional[datetime] = Field(None, description="Создан")
    managerId: Optional[int] = Field(None, description="Менеджер клиента")
    vip: Optional[bool] = Field(None, description="Важный клиент")
    bad: Optional[bool] = Field(None, description="Плохой клиент")
    site: Optional[str] = Field(None, description="Магазин, с которого пришел клиент")
    tags: list[CustomerTagLink] = Field(default_factory=list, description="Теги")
    firstClientId: Optional[str] = Field(
        None, description="Первая метка клиента Google Analytics"
    )
    lastClientId: Optional[str] = Field(
        None, description="Последняя метка клиента Google Analytics"
    )
    customFields: dict = Field(
        default_factory=dict, description="Ассоциативный массив пользовательских полей"
    )
    discountCardNumber: Optional[str] = Field(
        None, description="Номер дисконтной карты"
    )
    avgMarginSumm: float | None = Field(
        None, description="Средняя валовая прибыль по заказам клиента (в базовой валюте)"
    )
    marginSumm: Optional[decimal.Decimal] = Field(None, description="LTV (в базовой валюте)")
    totalSumm: Optional[decimal.Decimal] = Field(None, description="Общая сумма заказов (в базовой валюте)")
    averageSumm: Optional[decimal.Decimal] = Field(None, description="Средняя сумма заказа (в базовой валюте)")
    ordersCount: int = Field(None, description="Количество заказов")
    costSumm: Optional[decimal.Decimal] = Field(None, description="Сумма расходов (в базовой валюте)")
    address: Optional[CustomerAddress] = Field(None, description="Адрес клиента")
    maturationTime: Optional[int] = Field(
        None, description="Время «созревания», в секундах"
    )
    firstName: str = Field("", description="Имя")  # todo: remove default
    lastName: str = Field("", description="Фамилия")
    patronymic: str = Field("", description="Отчество")
    sex: str = Field("", description="Пол, возможные значения: male, female")
    presumableSex: Optional[str] = Field(
        None, description="Предполагаемый пол на основе ФИО"
    )
    email: str = Field(None, description="Адрес электронной почты")
    phones: list[CustomerPhone] = Field(default_factory=list, description="Телефоны")
    birthday: Optional[datetime] = Field(None, description="День рождения")
    source: Optional[SerializedSource] = Field(None, description="Источник клиента")
    mgCustomers: list[MGCustomer] = Field([], description="Клиенты MessageGateway")
    photoUrl: Optional[str] = Field(None, description="URL фотографии")
    contragentType: str = Field(
        "",
        description="Тип контрагента: физ. лицо individual, юр. лицо legal-entity, ИП enterpreneur",
    )
    legalName: str = Field(
        "",
        description="Наименование юр.лица или ИП, передается в случае фиск. на стороне модуля для юр .лица",
    )
    inn: str = Field(
        "",
        description="ИНН клиента, передается в случае фискализации на стороне модуля для юр. лиц и ИП",
        alias="INN",
    )

    # TODO: Временно до создания CorporateCustomer
    nickName: str | None = Field(None, description="Наименование")
    mainCompany: EntityWithExternalIdNameOutput | None = Field(None, description="Основная компания")
    phone: str | None = Field(None, description="Номер телефона")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )

    customFields_validator = field_validator("customFields", mode="before")(
        dict_validator()
    )