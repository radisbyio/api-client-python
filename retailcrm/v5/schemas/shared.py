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
    "MGDialog",
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


class EntityWithExternalIdNameOutput(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID")
    externalId: Optional[str] = Field(None, description="Внешний ID")
    name: Optional[str] = Field(None, description="Название")


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


class CustomerTagLink(BaseRetailCrmScheme):
    name: str = Field("")
    colorCode: str = Field("")
    attached: bool = Field(False)


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


class CustomerPhone(BaseRetailCrmScheme):
    number: str | None = Field(None, description="Номер телефона")


class MGChannel(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID канала")
    externalId: Optional[int] = Field(None, description="Внешний ID канала")
    type: Optional[str] = Field(None, description="Тип канала")
    active: Optional[bool] = Field(False, description="Активность канала")
    name: Optional[str] = Field(None, description="Название канала")


class MGCustomer(BaseRetailCrmScheme):
    id: int = Field(description="ID клиента")
    externalId: Optional[int] = Field(
        None, description="Внешний ID MessageGateway клиента"
    )
    mgChannel: Optional[MGChannel] = Field(None, description="MessageGateway канал")


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
    phones: list[CustomerPhone] = Field([], description="Телефоны")
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


class Unit(BaseRetailCrmScheme):
    code: str = Field(description="Символьный код")
    name: str = Field(description="Название")
    sym: str = Field(description="Краткое обозначение")


class LoyaltyLevel(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID уровня")
    name: str | None = Field(None, description="Название уровня")
    sum: decimal.Decimal | None = Field(None, description="Сумма, необходимая для перехода на данный уровень (в валюте объекта)")
    privilegeSize: int | None = Field(None, description="Размер скидки, процент или курс начисления бонусов для товаров по обычной цене (в валюте объекта)")
    privilegeSizePromo: int | None = Field(None, description="Размер скидки, процент или курс начисления бонусов для акционных товаров (в валюте объекта)")


# todo: заполнить
class LoyaltyEventDiscount(BaseRetailCrmScheme):
    id: int


class PackageItemOrderProduct(BaseRetailCrmScheme):
    id: int = Field(description="ID позиции в заказе")
    externalId: Optional[str] = Field(
        None, description="[deprecated] Внешний ID позиции в заказе"
    )
    externalIds: list[CodeValueModel] = Field(
        [], description="Внешние идентификаторы позиции в заказе"
    )


class PackageItem(BaseRetailCrmScheme):
    offerId: Optional[str] = Field(None, description="Идентификатор оффера в системе")
    externalId: Optional[str] = Field(
        None, description="Идентификатор торгового предложения в магазине"
    )
    xmlId: Optional[str] = Field(
        None, description="Идентификатор торгового предложения в складской системе"
    )
    name: Optional[str] = Field(None, description="Наименование товара")
    declaredValue: Optional[float] = Field(
        None, description="Объявленная стоимость за единицу товара"
    )
    cod: Optional[float] = Field(
        None, description="Наложенный платеж за единицу товара"
    )
    vatRate: Optional[VatRateTypes] = Field(
        None, description='Ставка НДС ("none" - НДС не облагается)'
    )
    quantity: Optional[float] = Field(None, description="Количество товара в упаковке")
    unit: Optional[Unit] = Field(None, description="Единица измерения товара")
    cost: Optional[float] = Field(
        None, description="Стоимость товара (с учетом скидок)"
    )
    markingCodes: Optional[list[str]] = Field(
        None, description="Коды маркировки (формат кода маркировки)"
    )
    properties: Optional[list] = Field(
        None, description="Свойства товара"
    )  # todo: уточнить тип данных
    weight: Optional[float] = Field(
        None, description="Вес товара (может быть null для услуг)"
    )


class Package(BaseRetailCrmScheme):
    packageId: Optional[str] = Field(None, description="Идентификатор упаковки")
    weight: Optional[float] = Field(None, description="Вес г.")
    width: Optional[int] = Field(None, description="Ширина мм.")
    length: Optional[int] = Field(None, description="Длина мм.")
    height: Optional[int] = Field(None, description="Высота мм.")
    items: list[PackageItem] = Field(default_factory=list, description="Содержимое упаковки")


# todo: заполнить
class DeclaredValueItem(BaseRetailCrmScheme):
    orderProduct: Optional[PackageItemOrderProduct] = Field(None)
    value: Optional[float] = Field(None)


class TimeInterval(BaseRetailCrmScheme):
    from_: Optional[time] = Field(
        None, description='Время "с"', serialization_alias="from"
    )
    to: Optional[time] = Field(None, description='Время "до"')
    custom: Optional[str] = Field(
        "", description="Временной диапазон в свободной форме"
    )

    from_serializer = field_serializer("from_")(time_serializer("%H:%M"))
    to_serializer = field_serializer("to")(time_serializer("%H:%M"))


class LinkedOrder(BaseRetailCrmScheme):
    id: int = Field(description="ID связанного заказа")
    number: Optional[str] = Field(None, description="Номер связанного заказа")
    externalId: Optional[str] = Field(None, description="Внешний ID связанного заказа")


class OrderLink(BaseRetailCrmScheme):
    order: Optional[LinkedOrder] = Field(None, description="Связанный заказ")
    createdAt: Optional[datetime] = Field(
        None, description="Дата/время создания связи с заказом"
    )
    comment: Optional[str] = Field(None, description="Комментарий")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class OrderProductPriceItem(BaseRetailCrmScheme):
    price: float = Field(
        0,
        description="Итоговая цена c учетом всех скидок на товар и заказ (в валюте объекта)",
    )
    quantity: float = Field(0, description="Количество товара по заданной цене")


class AbstractDiscount(BaseRetailCrmScheme):
    type: DiscountTypes = Field(description="Тип скидки")
    amount: float = Field(0, description="Сумма скидки")


class PriceType(BaseRetailCrmScheme):
    code: str = Field(description="Код типа цены")


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


# todo: заполнить
class SerializedEntityCustomer(BaseRetailCrmScheme):
    site: Optional[str] = Field(None)
    id: Optional[int] = Field(None, description="Внутренний ID клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    type: Optional[str] = Field(None)


class SerializedEntityOrder(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID заказа")
    externalId: Optional[str] = Field(None, description="Внешний ID заказа")
    number: Optional[str] = Field(None, description="Номер заказа")


# todo: заполнить
class Company(BaseRetailCrmScheme):
    id: Optional[int] = Field(None)
    externalId: Optional[str] = Field(None)
    customer: Optional[SerializedEntityCustomer] = Field(None)
    active: Optional[bool] = Field(None)
    name: Optional[str] = Field(None)
    brand: Optional[str] = Field(None)
    site: Optional[str] = Field(None)
    createdAt: Optional[datetime] = Field(None)
    contragent: Optional[CompanyContragent] = Field(None)
    address: Optional[CustomerAddress] = Field(None)
    avgMarginSumm: Optional[float] = Field(None)
    marginSumm: Optional[float] = Field(None)
    totalSumm: Optional[float] = Field(None)
    averageSumm: Optional[float] = Field(None)
    costSumm: Optional[float] = Field(None)
    ordersCount: Optional[int] = Field(None)
    customFields: dict = Field({})

    customFields_validator = field_validator("customFields", mode="before")(
        dict_validator()
    )


class OrderProductProperties(BaseRetailCrmScheme):
    code: Optional[str] = Field(
        None,
        description="Код свойства (не обязательное поле, код может передаваться в ключе свойства)",
    )
    name: Optional[str] = Field(None, description="Имя свойства")
    value: Optional[str] = Field(None, description="Значение свойства")


class OrderProduct(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID позиции в заказе")
    externalIds: list[CodeValueModel] = Field(
        default_factory=list, description="Внешние идентификаторы позиции в заказе"
    )
    discounts: list[AbstractDiscount] = Field(default_factory=list, description="Массив скидок")
    offer: Optional["Offer"] = Field(None, description="Торговое предложение")
    ordering: Optional[int] = Field(None, description="Порядок")
    properties: dict = Field(default_factory=dict, description="Дополнительные свойства позиции в заказе")

    bonusesChargeTotal: Optional[Decimal] = Field(
        None, description="Количество списанных бонусов"
    )
    bonusesCreditTotal: Optional[float] = Field(
        None, description="Количество начисленных бонусов"
    )
    markingCodes: list[str] = Field(default_factory=list, description="Коды маркировки")
    priceType: Optional[PriceType] = Field(None, description="Тип цены")
    initialPrice: Optional[Decimal] = Field(
        None, description="Цена товара/SKU (в валюте объекта)"
    )
    discountTotal: Optional[Decimal] = Field(
        None,
        description="Итоговая денежная скидка на единицу товара c учетом всех скидок на товар и заказ (в валюте объекта)",
    )
    prices: list[OrderProductPriceItem] = Field(
        default_factory=list, description="Набор итоговых цен реализации с указанием количества"
    )
    vatRate: Optional[str] = Field(None, description="Ставка НДС")
    createdAt: Optional[datetime] = Field(
        None, description="Дата создания позиции в системе"
    )
    quantity: Optional[Decimal] = Field(None, description="Количество")
    status: Optional[str] = Field(None, description="Статус позиции в заказе")
    comment: str = Field("", description="Комментарий к позиции в заказе")
    isCanceled: bool = Field(
        False, description="Данная позиция в заказе является отменной"
    )
    purchasePrice: Decimal | None = Field(None, description="Закупочная цена (в базовой валюте)")

    properties_validator = field_validator("properties", mode="before")(
        dict_validator()
    )
    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class Offer(BaseRetailCrmScheme):
    id: Optional[int] = Field(description="ID торгового предложения")
    externalId: Optional[str] = Field(
        "", description="ID торгового предложения в магазине"
    )
    xmlId: Optional[str] = Field(
        "", description="ID торгового предложения в складской системе"
    )
    properties: dict[str, Any] = Field({}, description="Свойства SKU")
    displayName: Optional[str] = Field("", description="Название SKU")
    name: Optional[str] = Field("", description="")
    article: Optional[str] = Field("", description="Артикул")
    vatRate: Optional[str] = Field(None, description="Ставка НДС")
    unit: Optional[Unit] = Field(None, description="Единица измерения")
    barcode: Optional[str] = Field("", description="Символьный код")

    properties_validator = field_validator("properties", mode="before")(
        dict_validator()
    )


class Payment(BaseRetailCrmScheme):
    id: int = Field(description="Внутренний ID")
    type: str = Field(None, description="Тип оплаты")
    external_id: Optional[str] = Field(
        None, description="Внешний ID платежа", validation_alias="externalId"
    )
    status: Optional[str] = Field(None, description="Статус оплаты")
    amount: float = Field(0, description="Сумма платежа (в валюте объекта)")
    paidAt: Optional[datetime] = Field(None, description="Дата оплаты")
    comment: Optional[str] = Field(None, description="Комментарий")

    order: SerializedEntityOrder | None = Field(None, description="Заказ")

    paidAt_serializer = field_serializer("paidAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class OrderDeliveryAddress(BaseRetailCrmScheme):
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


# TODO: make itemDeclaredValues
# TODO: make packages
class GenericData(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(
        None, description="Идентификатор в службе доставки"
    )
    trackNumber: Optional[str] = Field(
        None, description="Номер отправления (поле deprecated на запись)"
    )
    locked: bool = Field(False, description="Не синхронизировать со службой доставки")
    tariff: Optional[str] = Field(None, description="Код тарифа")
    pickuppointId: Optional[str] = Field(
        None, description="Идентификатор пункта самовывоза"
    )
    payerType: Optional[str] = Field(None, description="	Плательщик за доставку")
    shipmentpointId: Optional[str] = Field(
        None, description="Идентификатор терминала отгрузки"
    )
    extraData: Optional[dict[str, Any]] = Field(
        None,
        description="Дополнительные данные доставки (deliveryDataField.code => значение)",
    )
    itemDeclaredValues: Optional[list[dict[str, int | float]]] = None
    packages: list[dict[str, str | float | int | list[dict[str, int | str]]]] = Field(
        default_factory=list, description="Упаковки"
    )


# todo: update vatRate to enum
class SerializedOrderDelivery(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код типа доставки")
    data: Optional[GenericData] = Field(
        None, description="Данные службы доставки, подключенной через API"
    )
    # service: Optional[SerializedDeliveryService] = Field(None)  # todo realize
    cost: Optional[float] = Field(None, description="Стоимость доставки")
    netCost: Optional[float] = Field(None, description="Себестоимость доставки")
    date_: Optional[date] = Field(
        None, description="Дата доставки", serialization_alias="date"
    )
    time: Optional[TimeInterval] = Field(
        None, description="Информация о временном диапазоне"
    )
    address: Optional[OrderDeliveryAddress] = Field(None, description="Адрес доставки")
    vatRate: Optional[str] = Field(None, description="Ставка НДС")


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
class Order(BaseRetailCrmScheme):
    id: int | None = Field(None, description="ID заказа")
    externalId: str | None = Field(None, description="Внешний ID заказа")
    number: str | None = Field(None, description="Номер заказа")
    site: str | None = Field(None, description="Магазин")
    status: str | None = Field(None, description="Статус заказа")
    statusComment: str | None = Field(None, description="Комментарий к статусу доставки")
    managerId: int | None = Field(
        None, description="Менеджер, прикрепленный к заказу"
    )
    bonusesCreditTotal: float = Field(None, description="Количество начисленных бонусов")
    bonusesChargeTotal: float = Field(None, description="Количество списанных бонусов")
    summ: float = Field(None, description="Сумма по товарам (в валюте объекта)")
    currency: Currency | None = Field(None, description="Валюта")
    orderType: str = Field(None, description="Тип заказа")
    orderMethod: str = Field(None, description="Способ оформления")
    privilegeType: PrivilegeType = Field(
        PrivilegeType.NONE, description="Тип привилегии"
    )
    countryIso: CountryCodeIso3166 | None = Field(None, description="ISO код страны (ISO 3166-1 alpha-2)")
    createdAt: Optional[datetime] = Field(None, description="Дата оформления заказа")
    statusUpdatedAt: Optional[datetime] = Field(
        None, description="Дата последнего изменения статуса"
    )
    totalSumm: Decimal = Field(
        None, description="Общая сумма с учетом скидки (в валюте объекта)"
    )
    prepaySum: Decimal = Field(None, description="Оплаченная сумма (в валюте объекта)")
    purchaseSumm: Decimal = Field(
        None, description="Общая стоимость закупки (в базовой валюте)"
    )
    personalDiscountPercent: Optional[Decimal] = Field(
        None, description="Персональная скидка на заказ"
    )
    loyaltyLevel: Optional[LoyaltyLevel] = Field(
        None, description="Уровень участия в программе лояльности"
    )
    loyaltyEventDiscount: Optional[LoyaltyEventDiscount] = Field(
        None, description="Скидка по событию программы лояльности"
    )
    mark: Optional[int] = Field(None, description="Оценка заказа")
    markDatetime: Optional[datetime] = Field(
        None, description="Дата и время получение оценки от покупателя"
    )
    lastName: Optional[str] = Field(None, description="Фамилия")
    firstName: Optional[str] = Field(None, description="Имя")
    patronymic: Optional[str] = Field(None, description="Отчество")
    phone: Optional[str] = Field(None, description="Телефон")
    additionalPhone: Optional[str] = Field(None, description="Дополнительный телефон")
    email: Optional[str] = Field(None, description="E-mail")
    call: bool = Field(None, description="Требуется позвонить")
    expired: bool = Field(None, description="Просрочен")
    customerComment: Optional[str] = Field(None, description="")
    managerComment: Optional[str] = Field(None, description="")
    customer: Optional[Customer] = Field(None, description="Клиент")
    contact: Optional[Customer] = Field(None, description="Контактное лицо")
    company: Optional[Company] = Field(None, description="Компания")
    contragent: Optional[OrderContragent] = Field(None, description="Реквизиты")
    delivery: Optional[SerializedOrderDelivery] = Field(
        None, description="Данные о доставке"
    )
    source: Optional[SerializedSource] = Field(None, description="Источник заказа")
    items: list[OrderProduct] = Field([], description="Позиция в заказе")
    fullPaidAt: Optional[datetime] = Field(None, description="Дата полной оплаты")
    payments: dict[str, Payment] = Field(default_factory=dict, description="Платежи")
    fromApi: bool = Field(False, description="Заказ поступил через API")
    weight: Optional[Decimal] = Field(None, description="Вес")
    length: Optional[int] = Field(None, description="Длина")
    width: Optional[int] = Field(None, description="Ширина")
    height: Optional[int] = Field(None, description="Высота")
    shipmentStore: Optional[str] = Field(None, description="Склад отгрузки")
    shipmentDate: Optional[datetime] = Field(None, description="Дата отгрузки")
    shipped: bool = Field(False, description="Заказ отгружен")
    links: list[OrderLink] = Field(None, description="Связь заказов")
    customFields: dict = Field({}, validation_alias="customFields")
    client_id: Optional[str] = Field(None, validation_alias="clientId")

    customFields_validator = field_validator("customFields", mode="before")(
        dict_validator()
    )
    payments_validator = field_validator("payments", mode="before")(
        payments_validator()
    )

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    statusUpdatedAt_serializer = field_serializer("statusUpdatedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    markDatetime_serializer = field_serializer("markDatetime")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    fullPaidAt_serializer = field_serializer("fullPaidAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    shipmentDate_serializer = field_serializer("shipmentDate")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class CourierPhone(BaseRetailCrmScheme):
    number: str = Field("", description="Номер телефона")


class Courier(BaseRetailCrmScheme):
    id: int = Field(description="ID курьера")
    firstName: str = Field("", description="Имя")
    lastName: str = Field("", description="Фамилия")
    patronymic: str = Field("", description="Отчество")
    active: bool = Field(False, description="Признак активности")
    email: str = Field("", description="Электронная почта")
    phone: Optional[CourierPhone] = Field(None, description="Контактный телефон")
    description: str = Field("", description="Примечание")


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


class AbstractCustomer(BaseRetailCrmScheme):
    type: str = Field(description="Тип клиента")
    id: int = Field(description="ID клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    site: Optional[str] = Field(None, description="Магазин, с которого пришел клиент")


class Task(BaseRetailCrmScheme):
    id: int = Field(description="ID задачи")
    text: str = Field("", description="Текст задачи")
    commentary: str = Field("", description="Комментарий к задаче")
    datetime_: Optional[datetime] = Field(
        None, description="Время выполнения задачи", validation_alias="datetime"
    )
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    complete: bool = Field(False, description="Признак выполнения задачи")
    creator: Optional[int] = Field(None, description="Автор задачи")
    performer: Optional[int] = Field(None, description="Исполнитель задачи")
    performerType: Optional[str] = Field(None, description="Тип исполнителя задачи")
    customer: Optional[AbstractCustomer] = Field(
        None, description="Клиент, к которому привязана задача"
    )
    order: Optional[Order] = Field(
        None, description="Заказ, к которому привязана задача"
    )
    phone: Optional[str] = Field(None, description="Телефон связанный с задачей")
    phoneSite: Optional[str] = Field(
        None, description="Магазин, связанный с задачей на перезвон"
    )
    completedAt: Optional[datetime] = Field(None, description="Время завершения задачи")


class ApiKey(BaseRetailCrmScheme):
    current: Optional[bool] = Field(
        None,
        description="Изменение было сделано с помощью ключа, используемого в данный момент",
    )
    id: Optional[int] = Field(None, description="ID API-ключа")


class User(BaseRetailCrmScheme):
    id: int = Field(description="ID пользователя")


class MGDialog(BaseRetailCrmScheme):
    pass  # TODO: reailize if need


class FixExternalRow(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID")
    external_id: Optional[str] = Field(
        None, description="Внешний ID", validation_alias="externalId"
    )


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
