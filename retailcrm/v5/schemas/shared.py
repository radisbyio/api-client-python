import decimal
from datetime import date, datetime, time
from decimal import Decimal
from typing import Any, Optional, TypeVar

from pydantic import Field, field_serializer, field_validator

from retailcrm.v5.enums import (
    DiscountTypes,
    PaymentMethods,
    PaymentObjects,
    PrivilegeType,
    VatRateTypes,
)
from retailcrm.v5.enums.country_code_iso3166 import CountryCodeIso3166
from retailcrm.v5.enums.currency import Currency
from retailcrm.v5.helpers import (
    datetime_serializer,
    dict_validator,
    payments_validator,
    time_serializer,
)
from retailcrm.v5.schemas.base import BaseRetailCrmScheme

__all__ = [
    "ApiKey",
    "Item",
    "Customer",
    "MGCustomer",
    "CustomerAddress",
    "CustomerPhone",
    "CustomerTagLink",
    "MGChannel",
    "OrderProduct",
    "Payment",
    "Order",
    "Package",
    "DeclaredValueItem",
    "SerializedSource",
    "Courier",
    "CourierPhone",
    "Source",
    "PriceType",
    "Offer",
    "CodeValueModel",
    "Contact",
    "OrderDeliveryAddress",
    "OrderProductProperties",
    "TimeInterval",
    "Task",
    "User",
    "SerializedEntityCustomer",
    "SerializedOrderDelivery",
    "SerializedEntityOrder",
    "SerializedCustomerAddress",
    "FixExternalRow"
]

DeliveryType = TypeVar("DeliveryType")





class EntityWithExternalIdInput(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID")
    externalId: Optional[str] = Field(None, description="Внешний ID")

class Item(BaseRetailCrmScheme):
    name: str = Field("", description="Наименование")
    price: float = Field(0, description="Цена")
    quantity: float = Field(0, description="Количество")
    measurementUnit: str = Field("шт.", description="Единица измерения")
    vat: VatRateTypes = Field(VatRateTypes.NONE, description="Ставка НДС")
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





class SerializedCustomerAddress(BaseRetailCrmScheme):
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
    isMain: Optional[bool] = Field(None, description="Адрес является основным для клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID")
    name: Optional[str] = Field(None, description="Наменование адреса")






# TODO: Remove
class SerializedSource(BaseRetailCrmScheme):
    source: str = Field("", description="Источник")
    medium: str = Field("", description="Канал")
    campaign: str = Field("", description="Кампания")
    keyword: str = Field("", description="Ключевое слово")
    content: str = Field("", description="Содержание кампании")


class Customer(BaseRetailCrmScheme):
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
    marginSumm: float = Field(0, description="LTV (в базовой валюте)")
    totalSumm: float = Field(0, description="Общая сумма заказов (в базовой валюте)")
    averageSumm: float = Field(0, description="Средняя сумма заказа (в базовой валюте)")
    ordersCount: int = Field(0, description="Количество заказов")
    costSumm: float = Field(0, description="Сумма расходов (в базовой валюте)")
    address: Optional[CustomerAddress] = Field(None, description="Адрес клиента")
    maturationTime: Optional[int] = Field(
        0, description="Время «созревания», в секундах"
    )
    firstName: str = Field("", description="Имя")  # todo: remove default
    lastName: str = Field("", description="Фамилия")
    patronymic: str = Field("", description="Отчество")
    sex: str = Field("", description="Пол, возможные значения: male, female")
    presumableSex: Optional[str] = Field(
        None, description="Предполагаемый пол на основе ФИО"
    )
    email: str = Field("", description="Адрес электронной почты")
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


class CodeValueModel(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код")
    value: Optional[str] = Field(None, description="Значение")



































# todo: заполнить
class CompanyContragent(BaseRetailCrmScheme):
    contragentType: Optional[str] = Field(None)
    legalName: Optional[str] = Field(None)
    legalAddress: Optional[str] = Field(None)
    INN: Optional[str] = Field(None)
    OKPO: Optional[str] = Field(None)
    KPP: Optional[str] = Field(None)
    OGRN: Optional[str] = Field(None)
    OGRNIP: Optional[str] = Field(None)
    certificateNumber: Optional[str] = Field(None)
    certificateDate: Optional[datetime] = Field(None)
    BIK: Optional[str] = Field(None)
    bank: Optional[str] = Field(None)
    bankAddress: Optional[str] = Field(None)
    corrAccount: Optional[str] = Field(None)
    bankAccount: Optional[str] = Field(None)

















# todo: update vatRate to enum


# todo: заполнить
class OrderContragent(BaseRetailCrmScheme):
    contragentType: Optional[str] = Field(None)
    legalName: Optional[str] = Field(None)
    legalAddress: Optional[str] = Field(None)
    INN: Optional[str] = Field(None)
    OKPO: Optional[str] = Field(None)
    KPP: Optional[str] = Field(None)
    OGRN: Optional[str] = Field(None)
    OGRNIP: Optional[str] = Field(None)
    certificateNumber: Optional[str] = Field(None)
    certificateDate: Optional[datetime] = Field(None)
    BIK: Optional[str] = Field(None)
    bank: Optional[str] = Field(None)
    bankAddress: Optional[str] = Field(None)
    corrAccount: Optional[str] = Field(None)
    bankAccount: Optional[str] = Field(None)


# TODO: Изменить float на Decimal





class Contact(BaseRetailCrmScheme):
    id: int | None = None
    externalId: str | None = None
    browserId: str | None = None
    site: str | None = None


class Source(BaseRetailCrmScheme):
    source: str = ""
    medium: str = ""
    campaign: str = ""
    keyword: str = ""
    content: str = ""





class ApiKey(BaseRetailCrmScheme):
    current: Optional[bool] = Field(
        None,
        description="Изменение было сделано с помощью ключа, используемого в данный момент",
    )
    id: Optional[int] = Field(None, description="ID API-ключа")


class User(BaseRetailCrmScheme):
    id: int = Field(description="ID пользователя")




class Loyalty(BaseRetailCrmScheme):
    levels: list[LoyaltyLevel] = Field(
        default_factory=list, description="Уровни программы лояльности"
    )
    active: Optional[bool] = Field(None, description="Активна")
    blocked: Optional[bool] = Field(None, description="Заблокирована")
    currency: Optional[str] = Field(None, description="Валюта")
    id: Optional[int] = Field(None, description="ID программы лояльности")
    name: Optional[str] = Field(None, description="Название программы лояльности")
    confirmSmsCharge: Optional[bool] = Field(
        None, description="Подтверждать списание по СМС"
    )
    confirmSmsRegistration: Optional[bool] = Field(
        None, description="Подтверждать участие по СМС"
    )
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    activatedAt: Optional[datetime] = Field(None, description="Дата запуска")
    deactivatedAt: Optional[datetime] = Field(None, description="Дата остановки")
    blockedAt: Optional[datetime] = Field(None, description="Дата блокировки")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    activatedAt_serializer = field_serializer("activatedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    deactivatedAt_serializer = field_serializer("deactivatedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    blockedAt_serializer = field_serializer("blockedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class LoyaltyAccount(BaseRetailCrmScheme):
    active: Optional[bool] = Field(None, description="Признак активности участия")
    id: Optional[int] = Field(None, description="ID участия")
    loyalty: Optional[Loyalty] = Field(None, description="Программа лояльности")
    customer: Optional[Customer] = Field(None, description="Клиент")
    phoneNumber: Optional[str] = Field(None, description="Номер телефона")
    cardNumber: Optional[str] = Field(None, description="Номер карты")
    amount: Optional[float] = Field(None, description="Количество активных бонусов")
    ordersSum: Optional[float] = Field(
        None, description="Сумма покупок (в валюте объекта)"
    )
    nextLevelSum: Optional[float] = Field(
        None, description="Необходимая сумма покупок для перехода на след уровень"
    )
    level: Optional[LoyaltyLevel] = Field(None, description="Уровень участия")
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    activatedAt: Optional[datetime] = Field(None, description="Дата активации участия")
    confirmedPhoneAt: Optional[datetime] = Field(
        None, description="Дата верификации номера телефона"
    )
    lastCheckId: Optional[str] = Field(None, description="ID последней СМС-верификации")
    status: Optional[str] = Field(
        None,
        description="Статус участия. Возможные значения: not_confirmed, activated, deactivated",
    )
    customFields: Optional[dict] = Field(
        None, description="Ассоциативный массив пользовательских полей"
    )

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    activatedAt_serializer = field_serializer("activatedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    confirmedPhoneAt_serializer = field_serializer("confirmedPhoneAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    customFields_validator = field_validator("customFields", mode="before")(
        dict_validator()
    )


class SerializedLoyaltyOrder(BaseRetailCrmScheme):
    bonusesCreditTotal: decimal.Decimal | None = Field(None, description="Количество начисленных бонусов")
    bonusesChargeTotal: decimal.Decimal | None = Field(None, description="Количество списанных бонусов")
    currency: str | None = Field(None, description="Валюта")
    privilegeType: PrivilegeType | None = Field(
        None,
        description="Тип привилегии. Возможные значения: none, personal_discount, loyalty_level, loyalty_event",
    )
    totalSumm: decimal.Decimal | None = Field(
        None, description="Общая сумма с учетом скидки (в валюте объекта)"
    )
    personalDiscountPercent: decimal.Decimal | None = Field(
        None, description="Персональная скидка на заказ"
    )
    loyaltyAccount: LoyaltyAccount = Field(
        None, description="Участие в программе лояльности"
    )
    loyaltyLevel: LoyaltyLevel| None = Field(
        None, description="Уровень участия в программе лояльности"
    )
    loyaltyEventDiscount: LoyaltyEventDiscount| None = Field(
        None, description="Скидка по событию программы лояльности"
    )
    customer: Customer | None = Field(None, description="Клиент")
    delivery: SerializedOrderDelivery | None = Field(
        None, description="Данные о доставке"
    )
    site: str | None = Field(None, description="Магазин")
    items: list[OrderProduct] = Field(default_factory=list, description="Позиция в заказе")
