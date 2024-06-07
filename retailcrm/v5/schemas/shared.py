from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_serializer, field_validator

from retailcrm.v5.enums import PaymentMethods, PaymentObjects, VatTypes
from retailcrm.v5.schemas.validators import dict_validator

from retailcrm.v5.serializers import datetime_serializer

__all__ = [
    "Item",
    "Customer",
    "MGCustomer",
    "CustomerAddress",
    "CustomerPhone",
    "CustomerTagLink",
    "MGChannel",
]


class Item(BaseModel):
    name: str = Field("", description="Наименование")
    price: float = Field(0, description="Цена")
    quantity: float = Field(0, description="Количество")
    measurementUnit: str = Field("шт.", description="Единица измерения")
    vat: VatTypes = Field(VatTypes.NONE, description="Ставка НДС")
    paymentMethod: PaymentMethods = Field(
        PaymentMethods.FULL_PREPAYMENT, description="Признак способа расчета"
    )
    paymentObject: PaymentObjects = Field(
        PaymentObjects.COMMODITY, description="Признак предмета расчета"
    )
    productCode: str = Field(
        "", description="Код маркировки в шестнадцатеричном представлении"
    )
    markingCode: str = Field("", description="Код маркировки")


class CustomerTagLink(BaseModel):
    name: str = Field("")
    colorCode: str = Field("")
    attached: bool = Field(False)


class CustomerAddress(BaseModel):
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


class CustomerPhone(BaseModel):
    number: str = Field("", description="Номер телефона")


class MGChannel(BaseModel):
    id: Optional[int] = Field(None, description="ID канала")
    externalId: Optional[int] = Field(None, description="Внешний ID канала")
    type: Optional[str] = Field(None, description="Тип канала")
    active: Optional[bool] = Field(False, description="Активность канала")
    name: Optional[str] = Field(None, description="Название канала")


class MGCustomer(BaseModel):
    id: int = Field(description="ID клиента")
    externalId: Optional[int] = Field(
        None, description="Внешний ID MessageGateway клиента"
    )
    mgChannel: Optional[MGChannel] = Field(None, description="MessageGateway канал")


class SerializedSource(BaseModel):
    source: str = Field("", description="Источник")
    medium: str = Field("", description="Канал")
    campaign: str = Field("", description="Кампания")
    keyword: str = Field("", description="Ключевое слово")
    content: str = Field("", description="Содержание кампании")


class Customer(BaseModel):
    type: Optional[str] = Field(None, description="Тип клиента")
    id: Optional[int] = Field(None, description="ID клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    isContact: bool = Field(
        False,
        description="Клиент является контактным лицом (создан как контактное лицо и на него нет оформленных заказов)",
    )
    createdAt: Optional[datetime] = Field(None, description="Создан")
    managerId: Optional[int] = Field(None, description="Менеджер клиента")
    vip: Optional[bool] = Field(None, description="Важный клиент")
    bad: Optional[bool] = Field(None, description="Плохой клиент")
    site: Optional[str] = Field(None, description="Магазин, с которого пришел клиент")
    tags: list[CustomerTagLink] = Field([], description="Теги")
    firstClientId: Optional[str] = Field(
        None, description="Первая метка клиента Google Analytics"
    )
    lastClientId: Optional[str] = Field(
        None, description="Последняя метка клиента Google Analytics"
    )
    customFields: dict = Field(
        {}, description="Ассоциативный массив пользовательских полей"
    )
    discountCardNumber: Optional[str] = Field(
        None, description="Номер дисконтной карты"
    )
    avgMarginSumm: float = Field(
        "", description="Средняя валовая прибыль по заказам клиента (в базовой валюте)"
    )
    marginSumm: float = Field(0, description="LTV (в базовой валюте)")
    totalSumm: float = Field(0, description="Общая сумма заказов (в базовой валюте)")
    averageSumm: float = Field(0, description="Средняя сумма заказа (в базовой валюте)")
    ordersCount: int = Field(0, description="Количество заказов")
    costSumm: float = Field(0, description="Сумма расходов (в базовой валюте)")
    address: Optional[CustomerAddress] = Field(None, description="Адрес клиента")
    maturationTime: Optional[int] = Field(
        0, description="Время «созревания», в секундах"
    )
    firstName: str = Field(description="Имя")
    lastName: str = Field("", description="Фамилия")
    patronymic: str = Field("", description="Отчество")
    sex: str = Field("", description="Пол, возможные значения: male, female")
    presumableSex: Optional[str] = Field(
        None, description="Предполагаемый пол на основе ФИО"
    )
    email: str = Field("", description="Адрес электронной почты")
    phones: list[CustomerPhone] = Field([], description="Телефоны")
    birthday: Optional[datetime] = Field(None, description="День рождения")
    source: Optional[SerializedSource] = Field(None, description="Источник клиента")
    mgCustomers: list["MGCustomer"] = Field([], description="Клиенты MessageGateway")
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

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )

    customFields_validator = field_validator("customFields", mode="before")(
        dict_validator()
    )
