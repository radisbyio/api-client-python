from datetime import datetime, time
from typing import Optional, Any

from pydantic import BaseModel, Field, field_serializer, field_validator

from retailcrm.v5.enums import (
    PaymentMethods,
    PaymentObjects,
    VatRateTypes,
    PrivilegeType,
    DiscountTypes,
)
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
    "OrderProduct",
    "Payment",
    "Order",
    "Package",
    "DeclaredValueItem"
]


class Item(BaseModel):
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


class CodeValueModel(BaseModel):
    code: Optional[str] = Field(None, description="Код")
    value: Optional[str] = Field(None, description="Значение")


class Unit(BaseModel):
    code: str = Field(description="Символьный код")
    name: str = Field(description="Название")
    sym: str = Field(description="Краткое обозначение")


# todo: заполнить
class LoyaltyLevel(BaseModel):
    id: Optional[int] = Field(None)
    name: str = Field("")


# todo: заполнить
class LoyaltyEventDiscount(BaseModel):
    id: int


class PackageItemOrderProduct(BaseModel):
    id: int = Field(description="ID позиции в заказе")
    externalId: Optional[str] = Field(
        None, description="[deprecated] Внешний ID позиции в заказе"
    )
    externalIds: list[CodeValueModel] = Field(
        [], description="Внешние идентификаторы позиции в заказе"
    )


# todo: заполнить
class PackageItem(BaseModel):
    orderProduct: PackageItemOrderProduct = Field(None, description="Позиция в заказе")
    quantity: Optional[float] = Field(0, description="Количество товара в упаковке")


# todo: заполнить
class Package(BaseModel):
    packageId: Optional[str] = Field(None)
    weight: Optional[float] = Field(None)
    length: Optional[int] = Field(None)
    width: Optional[int] = Field(None)
    height: Optional[int] = Field(None)
    items: list[PackageItem] = []


# todo: заполнить
class DeclaredValueItem(BaseModel):
    orderProduct: Optional[PackageItemOrderProduct] = Field(None)
    value: Optional[float] = Field(None)


class TimeInterval(BaseModel):
    from_: Optional[time] = Field(None, description='Время "с"', alias="from")
    to: Optional[time] = Field(None, description='Время "до"')
    custom: Optional[str] = Field(
        "", description="Временной диапазон в свободной форме"
    )


class LinkedOrder(BaseModel):
    id: int = Field(description="ID связанного заказа")
    number: Optional[str] = Field(None, description="Номер связанного заказа")
    externalId: Optional[str] = Field(None, description="Внешний ID связанного заказа")


class OrderLink(BaseModel):
    order: Optional[LinkedOrder] = Field(None, description="Связанный заказ")
    createdAt: Optional[datetime] = Field(
        None, description="Дата/время создания связи с заказом"
    )
    comment: Optional[str] = Field(None, description="Комментарий")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class OrderProductPriceItem(BaseModel):
    price: float = Field(
        0,
        description="Итоговая цена c учетом всех скидок на товар и заказ (в валюте объекта)",
    )
    quantity: float = Field(0, description="Количество товара по заданной цене")


class AbstractDiscount(BaseModel):
    type: DiscountTypes = Field(description="Тип скидки")
    amount: float = Field(0, description="Сумма скидки")


class PriceType(BaseModel):
    code: str = Field(description="Код типа цены")


# todo: заполнить
class OrderContragent(BaseModel):
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
class CompanyContragent(BaseModel):
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
class SerializedEntityCustomer(BaseModel):
    site: Optional[str] = Field(None)
    id: Optional[int] = Field(None)
    externalId: Optional[str] = Field(None)
    type: Optional[str] = Field(None)


# todo: заполнить
class Company(BaseModel):
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
    customFields: Optional[dict] = Field(None)


class OrderProduct(BaseModel):
    id: Optional[int] = Field(description="ID позиции в заказе")
    externalIds: list[CodeValueModel] = Field(
        [], description="Внешние идентификаторы позиции в заказе"
    )
    discounts: list[AbstractDiscount] = Field([], description="Массив скидок")
    offer: Optional["Offer"] = Field(None, description="Торговое предложение")
    ordering: Optional[int] = Field(None, description="Порядок")
    properties: dict = Field({}, description="Дополнительные свойства позиции в заказе")

    bonusesChargeTotal: Optional[float] = Field(
        0, description="Количество списанных бонусов"
    )
    bonusesCreditTotal: Optional[float] = Field(
        0, description="Количество начисленных бонусов"
    )
    markingCodes: list[str] = Field([], description="Коды маркировки")
    priceType: Optional[PriceType] = Field(None, description="Тип цены")
    initialPrice: Optional[float] = Field(
        0, description="Цена товара/SKU (в валюте объекта)"
    )
    discountTotal: Optional[float] = Field(
        0,
        description="Итоговая денежная скидка на единицу товара c учетом всех скидок на товар и заказ (в валюте объекта)",
    )
    prices: list[OrderProductPriceItem] = Field(
        [], description="Набор итоговых цен реализации с указанием количества"
    )
    vatRate: VatRateTypes = Field(VatRateTypes.NONE, description="Ставка НДС")
    createdAt: Optional[datetime] = Field(
        None, description="Дата создания позиции в системе"
    )
    quantity: Optional[float] = Field(0, description="Количество")
    status: Optional[str] = Field(None, description="Статус позиции в заказе")
    comment: str = Field("", description="Комментарий к позиции в заказе")
    isCanceled: bool = Field(
        False, description="Данная позиция в заказе является отменной"
    )
    purchasePrice: float = Field(0, description="Закупочная цена (в базовой валюте)")

    properties_validator = field_validator("properties", mode="before")(
        dict_validator()
    )
    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class Offer(BaseModel):
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
    vatRate: VatRateTypes = Field(VatRateTypes.NONE, description="Ставка НДС")
    unit: Optional[Unit] = Field(None, description="Единица измерения")
    barcode: Optional[str] = Field("", description="Символьный код")

    properties_validator = field_validator("properties", mode="before")(
        dict_validator()
    )


class Payment(BaseModel):
    id: int = Field(description="Внутренний ID")
    type: str = Field(None, description="Тип оплаты")
    external_id: Optional[str] = Field(
        None, description="Внешний ID платежа", validation_alias="externalId"
    )
    status: Optional[str] = Field(None, description="Статус оплаты")
    amount: float = Field(0, description="Сумма платежа (в валюте объекта)")
    paidAt: Optional[datetime] = Field(None, description="Дата оплаты")
    comment: Optional[str] = Field(None, description="Комментарий")

    paidAt_serializer = field_serializer("paidAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class OrderDeliveryAddress(BaseModel):
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


class SerializedOrderDelivery(BaseModel):
    code: str = Field(None, description="Код типа доставки")
    integrationCode: Optional[str] = Field(
        None, description="Интеграционный код типа доставки"
    )
    # data: "OrderDeliveryData"
    # service: "SerializedDeliveryService"
    cost: float = Field(0, description="Стоимость доставки")
    netCost: float = Field(0, description="Себестоимость доставки")
    date: Optional[datetime] = Field(None, description="Дата доставки")
    time: Optional[TimeInterval] = Field(
        None, description="Информация о временном диапазоне"
    )
    address: Optional[OrderDeliveryAddress] = Field(None, description="Адрес доставки")
    vatRate: Optional[str] = Field(None, description="Ставка НДС")

    date_serializer = field_serializer("date")(datetime_serializer("%Y-%m-%d %H:%M:%S"))


class Order(BaseModel):
    id: int = Field(0, description="ID заказа")
    externalId: str = Field(
        "",
        description="Внешний ID заказа",
    )
    number: str = Field("", description="Номер заказа")
    site: str = Field("", description="Магазин")
    status: str = Field("", description="Статус заказа")
    statusComment: Optional[str] = Field(
        None,
        description="Комментарий к статусу доставки",
    )
    managerId: Optional[int] = Field(
        None, description="Менеджер, прикрепленный к заказу"
    )
    bonusesCreditTotal: float = Field(0, description="Количество начисленных бонусов")
    bonusesChargeTotal: float = Field(0, description="Количество списанных бонусов")
    summ: float = Field(0, description="Сумма по товарам (в валюте объекта)")
    currency: str = Field("", description="Валюта")
    orderType: str = Field("", description="Тип заказа")
    orderMethod: str = Field("", description="Способ оформления")
    privilegeType: PrivilegeType = Field(
        PrivilegeType.NONE, description="Тип привилегии"
    )
    countryIso: str = Field("", description="ISO код страны (ISO 3166-1 alpha-2)")
    createdAt: Optional[datetime] = Field(None, description="Дата оформления заказа")
    statusUpdatedAt: Optional[datetime] = Field(
        None, description="Дата последнего изменения статуса"
    )
    totalSumm: float = Field(
        0, description="Общая сумма с учетом скидки (в валюте объекта)"
    )
    prepaySum: float = Field(0, description="Оплаченная сумма (в валюте объекта)")
    purchaseSumm: float = Field(
        0, description="Общая стоимость закупки (в базовой валюте)"
    )
    personalDiscountPercent: Optional[float] = Field(
        0, description="Персональная скидка на заказ"
    )
    loyaltyLevel: Optional[LoyaltyLevel] = Field(
        None, description="Уровень участия в программе лояльности"
    )
    loyaltyEventDiscount: Optional[LoyaltyEventDiscount] = Field(
        None,
        description="Скидка по событию программы лояльности",
    )
    mark: Optional[int] = Field(None, description="Оценка заказа")
    markDatetime: Optional[datetime] = Field(
        None, description="Дата и время получение оценки от покупателя"
    )
    lastName: Optional[str] = Field("Фамилия")
    firstName: Optional[str] = Field("Имя")
    patronymic: Optional[str] = Field("", description="Отчество")
    phone: Optional[str] = Field("", description="Телефон")
    additionalPhone: Optional[str] = Field("", description="Дополнительный телефон")
    email: Optional[str] = Field(None, description="E-mail")
    call: bool = Field(False, description="Требуется позвонить")
    expired: bool = Field(False, description="Просрочен")
    customerComment: Optional[str] = Field("", description="")
    managerComment: Optional[str] = Field("", description="")
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
    payments: dict[str, "Payment"] = Field({}, description="Платежи")
    fromApi: bool = Field(False, description="Заказ поступил через API")
    weight: Optional[float] = Field(None, description="Вес")
    length: Optional[int] = Field(None, description="Длина")
    width: Optional[int] = Field(None, description="Ширина")
    height: Optional[int] = Field(None, description="Высота")
    shipmentStore: Optional[str] = Field(None, description="Склад отгрузки")
    shipmentDate: Optional[datetime] = Field(None, description="Дата отгрузки")
    shipped: bool = Field(False, description="Заказ отгружен")
    links: list[OrderLink] = Field(None, description="Связь заказов")
    custom_fields: dict = Field({}, validation_alias="customFields")
    client_id: Optional[str] = Field(None, validation_alias="clientId")

    custom_fields_validator = field_validator("custom_fields", mode="before")(
        dict_validator()
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
