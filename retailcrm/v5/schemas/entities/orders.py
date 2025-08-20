import decimal
from datetime import datetime, date, time
from typing import Optional, Any

from pydantic import field_serializer, field_validator, Field

from retailcrm.v5.enums import PrivilegeType, DiscountTypes
from retailcrm.v5.enums.country_code_iso3166 import CountryCodeIso3166
from retailcrm.v5.enums.currency import Currency
from retailcrm.v5.helpers import datetime_serializer, dict_validator, payments_validator, time_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.customers import Customer
from retailcrm.v5.schemas.entities.customers_corporate import Company
from retailcrm.v5.schemas.entities.loyalty import LoyaltyEventDiscount, LoyaltyLevel, LoyaltyAccount
from retailcrm.v5.schemas.shared.code_value_model import CodeValueModel
from retailcrm.v5.schemas.shared.entity_with_external_id import EntityWithExternalIdInput
from retailcrm.v5.schemas.shared.history_api_key import HistoryApiKey
from retailcrm.v5.schemas.shared.history_user import HistoryUser
from retailcrm.v5.schemas.shared.order import SerializedEntityOrder
from retailcrm.v5.schemas.shared.source import SerializedSource


class SerializedOrderReference(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID заказа")


class SerializedOrderLink(BaseRetailCrmScheme):
    comment: Optional[str] = Field(None, description="Комментарий")
    orders: Optional[list[SerializedEntityOrder]] = Field(None, description="Заказ")


class AbstractDiscount(BaseRetailCrmScheme):
    type: Optional[DiscountTypes] = Field(None, description="Тип скидки")
    amount: Optional[decimal.Decimal] = Field(None, description="Сумма скидки")


class OrderProductProperties(BaseRetailCrmScheme):
    code: Optional[str] = Field(
        None, description="Код свойства (не обязательное поле, код может передаваться в ключе свойства)",
    )
    name: Optional[str] = Field(None, description="Имя свойства")
    value: Optional[str] = Field(None, description="Значение свойства")


class PriceType(BaseRetailCrmScheme):
    code: str = Field(description="Код типа цены")


class OrderProductPriceItem(BaseRetailCrmScheme):
    price: Optional[decimal.Decimal] = Field(
        None, description="Итоговая цена c учетом всех скидок на товар и заказ (в валюте объекта)",
    )
    quantity: Optional[decimal.Decimal] = Field(None, description="Количество товара по заданной цене")


class Unit(BaseRetailCrmScheme):
    code: Optional[str] = Field(description="Символьный код")
    name: Optional[str] = Field(description="Название")
    sym: Optional[str] = Field(description="Краткое обозначение")


class Offer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID торгового предложения")
    externalId: Optional[str] = Field(
        None, description="ID торгового предложения в магазине"
    )
    xmlId: Optional[str] = Field(
        None, description="ID торгового предложения в складской системе"
    )
    properties: dict[str, Any] = Field(default_factory=dict, description="Свойства SKU")
    displayName: Optional[str] = Field(None, description="Название SKU")
    name: Optional[str] = Field(None, description="")
    article: Optional[str] = Field(None, description="Артикул")
    vatRate: Optional[str] = Field(None, description="Ставка НДС")
    unit: Optional[Unit] = Field(None, description="Единица измерения")
    barcode: Optional[str] = Field(None, description="Символьный код")

    properties_validator = field_validator("properties", mode="before")(
        dict_validator()
    )


class OrderProduct(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID позиции в заказе")
    externalIds: list[CodeValueModel] = Field(
        default_factory=list, description="Внешние идентификаторы позиции в заказе"
    )
    discounts: list[AbstractDiscount] = Field(default_factory=list, description="Массив скидок")
    offer: Optional[Offer] = Field(None, description="Торговое предложение")
    ordering: Optional[int] = Field(None, description="Порядок")
    properties: dict = Field(default_factory=dict, description="Дополнительные свойства позиции в заказе")

    bonusesChargeTotal: Optional[decimal.Decimal] = Field(
        None, description="Количество списанных бонусов"
    )
    bonusesCreditTotal: Optional[decimal.Decimal] = Field(
        None, description="Количество начисленных бонусов"
    )
    markingCodes: list[str] = Field(default_factory=list, description="Коды маркировки")
    priceType: Optional[PriceType] = Field(None, description="Тип цены")
    initialPrice: Optional[decimal.Decimal] = Field(
        None, description="Цена товара/SKU (в валюте объекта)"
    )
    discountTotal: Optional[decimal.Decimal] = Field(
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
    quantity: Optional[decimal.Decimal] = Field(None, description="Количество")
    status: Optional[str] = Field(None, description="Статус позиции в заказе")
    comment: str = Field("", description="Комментарий к позиции в заказе")
    isCanceled: bool = Field(
        False, description="Данная позиция в заказе является отменной"
    )
    purchasePrice: Optional[decimal.Decimal] | None = Field(None, description="Закупочная цена (в базовой валюте)")

    properties_validator = field_validator("properties", mode="before")(
        dict_validator()
    )
    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class SerializedOrderProductOffer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID торгового предложения")
    externalId: Optional[str] = Field(
        None, description="Внешний ID торгового предложения"
    )
    xmlId: Optional[str] = Field(
        None, description="ID торгового предложения в складской системе"
    )


class SerializedOrderProduct(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(None)
    markingCodes: list[str] = Field(default_factory=list, description="Коды маркировки")
    initialPrice: Optional[decimal.Decimal] = Field(
        None, description="Цена товара/SKU (в валюте объекта)"
    )
    discountManualAmount: Optional[decimal.Decimal] = Field(
        None, description="Денежная скидка на единицу товара (в валюте объекта)"
    )
    discountManualPercent: Optional[decimal.Decimal] = Field(
        None, description="Процентная скидка на единицу товара"
    )
    vatRate: Optional[str] = Field(None, description="Ставка НДС")
    createdAt: Optional[datetime] = Field(
        None, description="Дата создания позиции в системе"
    )
    quantity: Optional[decimal.Decimal] = Field(None, description="Количество")
    comment: Optional[str] = Field(None, description="Комментарий к позиции в заказе")
    properties: list[OrderProductProperties] = Field(
        default_factory=list, description="Дополнительные свойства позиции в заказе"
    )
    purchasePrice: decimal.Decimal = Field(None, description="Закупочная цена (в базовой валюте)")
    ordering: Optional[int] = Field(None, description="Порядок")
    offer: Optional[SerializedOrderProductOffer] = Field(
        None, description="Торговое предложение"
    )
    productName: Optional[str] = Field(None, description="Название товара")
    status: Optional[str] = Field(None, description="Статус позиции в заказе")
    priceType: Optional[PriceType] = Field(None, description="Тип цены")
    externalIds: list[CodeValueModel] = Field(
        default_factory=list, description="Внешние идентификаторы позиции в заказе"
    )

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class LinkedOrder(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID связанного заказа")
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

class Payment(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID")
    type: Optional[str] = Field(None, description="Тип оплаты")
    external_id: Optional[str] = Field(
        None, description="Внешний ID платежа", validation_alias="externalId"
    )
    status: Optional[str] = Field(None, description="Статус оплаты")
    amount: Optional[decimal.Decimal] = Field(None, description="Сумма платежа (в валюте объекта)")
    paidAt: Optional[datetime] = Field(None, description="Дата оплаты")
    comment: Optional[str] = Field(None, description="Комментарий")

    order: Optional[SerializedEntityOrder] = Field(None, description="Заказ")

    paidAt_serializer = field_serializer("paidAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class SerializedPayment(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(None, description="Внешний ID платежа")
    amount: Optional[decimal.Decimal] = Field(None, description="Сумма платежа (в валюте объекта)")
    paidAt: Optional[datetime] = Field(None, description="Дата оплаты")
    comment: Optional[str] = Field(None, description="Комментарий")
    type: Optional[str] = Field(None, description="Тип оплаты")
    status: Optional[str] = Field(None, description="Статус оплаты")

    order: SerializedEntityOrder | None = Field(None, description="Заказ")

    paidAt_serializer = field_serializer("paidAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class OrderContragent(BaseRetailCrmScheme):
    contragentType: Optional[str] = Field(None, description="Тип контрагента")
    legalName: Optional[str] = Field(None, description="Полное наименование")
    legalAddress: Optional[str] = Field(None, description="Адрес регистрации")
    INN: Optional[str] = Field(None, description="ИНН")
    OKPO: Optional[str] = Field(None, description="ОКПО")
    KPP: Optional[str] = Field(None, description="КПП")
    OGRN: Optional[str] = Field(None, description="ОГРН")
    OGRNIP: Optional[str] = Field(None, description="ОГРНИП")
    certificateNumber: Optional[str] = Field(None, description="Номер свидетельства")
    certificateDate: Optional[datetime] = Field(None, description="Дата свидетельства")
    BIK: Optional[str] = Field(None, description="БИК")
    bank: Optional[str] = Field(None, description="Банк")
    bankAddress: Optional[str] = Field(None, description="Адрес банка")
    corrAccount: Optional[str] = Field(None, description="Корр. счёт")
    bankAccount: Optional[str] = Field(None, description="Расчётный счёт")

    certificateDate_serializer = field_serializer("certificateDate")(
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


class TimeInterval(BaseRetailCrmScheme):
    from_: Optional[time] = Field(
        None, description='Время "с"', serialization_alias="from"
    )
    to: Optional[time] = Field(None, description='Время "до"')
    custom: Optional[str] = Field(
        None, description="Временной диапазон в свободной форме"
    )

    from_serializer = field_serializer("from_")(time_serializer("%H:%M"))
    to_serializer = field_serializer("to")(time_serializer("%H:%M"))


class PackageItemOrderProduct(BaseRetailCrmScheme):
    id: int = Field(description="ID позиции в заказе")
    externalId: Optional[str] = Field(
        None, description="[deprecated] Внешний ID позиции в заказе"
    )
    externalIds: list[CodeValueModel] = Field(
        default_factory=list, description="Внешние идентификаторы позиции в заказе"
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
    declaredValue: Optional[decimal.Decimal] = Field(
        None, description="Объявленная стоимость за единицу товара"
    )
    cod: Optional[decimal.Decimal] = Field(
        None, description="Наложенный платеж за единицу товара"
    )
    vatRate: Optional[str] = Field(
        None, description='Ставка НДС ("none" - НДС не облагается)'
    ) # TODO: Уточнить значение
    quantity: Optional[decimal.Decimal] = Field(None, description="Количество товара в упаковке")
    unit: Optional[Unit] = Field(None, description="Единица измерения товара")
    cost: Optional[decimal.Decimal] = Field(
        None, description="Стоимость товара (с учетом скидок)"
    )
    markingCodes: Optional[list[str]] = Field(
        None, description="Коды маркировки (формат кода маркировки)"
    )
    properties: Optional[Any] = Field(
        None, description="Свойства товара"
    )  # todo: уточнить тип данных
    weight: Optional[decimal.Decimal] = Field(
        None, description="Вес товара (может быть null для услуг)"
    )


class Package(BaseRetailCrmScheme):
    packageId: Optional[str] = Field(None, description="Идентификатор упаковки")
    weight: Optional[decimal.Decimal] = Field(None, description="Вес г.")
    width: Optional[int] = Field(None, description="Ширина мм.")
    length: Optional[int] = Field(None, description="Длина мм.")
    height: Optional[int] = Field(None, description="Высота мм.")
    items: list[PackageItem] = Field(default_factory=list, description="Содержимое упаковки")


class DeclaredValueItem(BaseRetailCrmScheme):
    orderProduct: PackageItemOrderProduct | None = Field(None, description="Позиция в заказе")
    value: decimal.Decimal | None = Field(None, description="Объявленная стоимость товара")


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
    itemDeclaredValues: Optional[list[DeclaredValueItem]] = Field(default_factory=list)
    packages: list[Package] = Field(
        default_factory=list, description="Упаковки"
    )


class SerializedOrderDelivery(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код типа доставки")
    data: Optional[GenericData] = Field(
        None, description="Данные службы доставки, подключенной через API"
    )
    # service: Optional[SerializedDeliveryService] = Field(None)  # todo realize
    cost: Optional[decimal.Decimal] = Field(None, description="Стоимость доставки")
    netCost: Optional[decimal.Decimal] = Field(None, description="Себестоимость доставки")
    date_: Optional[date] = Field(
        None, description="Дата доставки", serialization_alias="date"
    )
    time: Optional[TimeInterval] = Field(
        None, description="Информация о временном диапазоне"
    )
    address: Optional[OrderDeliveryAddress] = Field(None, description="Адрес доставки")
    vatRate: Optional[str] = Field(None, description="Ставка НДС")



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
    bonusesCreditTotal: Optional[decimal.Decimal] = Field(None, description="Количество начисленных бонусов")
    bonusesChargeTotal: Optional[decimal.Decimal] = Field(None, description="Количество списанных бонусов")
    summ: Optional[decimal.Decimal] = Field(None, description="Сумма по товарам (в валюте объекта)")
    currency: Currency | None = Field(None, description="Валюта")
    orderType: str = Field(None, description="Тип заказа")
    orderMethod: str = Field(None, description="Способ оформления")
    privilegeType: Optional[PrivilegeType] = Field(None, description="Тип привилегии")
    countryIso: CountryCodeIso3166 | None = Field(None, description="ISO код страны (ISO 3166-1 alpha-2)")
    createdAt: Optional[datetime] = Field(None, description="Дата оформления заказа")
    statusUpdatedAt: Optional[datetime] = Field(
        None, description="Дата последнего изменения статуса"
    )
    totalSumm: Optional[decimal.Decimal] = Field(
        None, description="Общая сумма с учетом скидки (в валюте объекта)"
    )
    prepaySum: Optional[decimal.Decimal] = Field(None, description="Оплаченная сумма (в валюте объекта)")
    purchaseSumm: Optional[decimal.Decimal] = Field(
        None, description="Общая стоимость закупки (в базовой валюте)"
    )
    personalDiscountPercent: Optional[decimal.Decimal] = Field(
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
    items: list[OrderProduct] = Field(default_factory=list, description="Позиция в заказе")
    fullPaidAt: Optional[datetime] = Field(None, description="Дата полной оплаты")
    payments: dict[str, Payment] = Field(default_factory=dict, description="Платежи")
    fromApi: bool = Field(False, description="Заказ поступил через API")
    weight: Optional[decimal.Decimal] = Field(None, description="Вес")
    length: Optional[int] = Field(None, description="Длина")
    width: Optional[int] = Field(None, description="Ширина")
    height: Optional[int] = Field(None, description="Высота")
    shipmentStore: Optional[str] = Field(None, description="Склад отгрузки")
    shipmentDate: Optional[datetime] = Field(None, description="Дата отгрузки")
    shipped: Optional[bool] = Field(None, description="Заказ отгружен")
    links: list[OrderLink] = Field(default_factory=list, description="Связь заказов")
    customFields: dict[str, Any] = Field(default_factory=dict)
    clientId: Optional[str] = Field(None)

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


class SerializedOrder(BaseRetailCrmScheme):
    number: Optional[str] = Field(None, description="Номер заказа")
    externalId: Optional[str] = Field(None, description="Внешний ID заказа")
    privilegeType: Optional[PrivilegeType] = Field(
        PrivilegeType.NONE, description="Тип привилегии"
    )
    countryIso: Optional[str] = Field(
        None, description="ISO код страны (ISO 3166-1 alpha-2)"
    )
    createdAt: Optional[datetime] = Field(None, description="Дата оформления заказа")
    statusUpdatedAt: Optional[datetime] = Field(
        None, description="Дата последнего изменения статуса"
    )
    discountManualAmount: Optional[decimal.Decimal] = Field(
        None, description="Денежная скидка на весь заказ (в валюте объекта)"
    )
    discountManualPercent: Optional[decimal.Decimal] = Field(
        None, description="Процентная скидка на весь заказ"
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
    call: Optional[bool] = Field(None, description="Требуется позвонить")
    expired: Optional[bool] = Field(None, description="Просрочен")
    customerComment: Optional[str] = Field(None, description="Комментарий клиента")
    managerComment: Optional[str] = Field(None, description="Комментарий оператора")
    contragent: Optional[OrderContragent] = Field(None, description="Реквизиты")
    statusComment: Optional[str] = Field(
        None, description="Комментарий к последнему изменению статуса"
    )
    weight: Optional[decimal.Decimal] = Field(None, description="Вес")
    length: Optional[int] = Field(None, description="Длина")
    width: Optional[int] = Field(None, description="Ширина")
    height: Optional[int] = Field(None, description="Высота")
    shipmentDate: Optional[datetime] = Field(None, description="Дата отгрузки")
    shipped: Optional[bool] = Field(None, description="Заказ отгружен")
    dialogId: Optional[Any] = Field(
        None, description="Идентификатор диалога Чатов"
    ) # TODO: Уточнить
    customFields: Optional[dict] = Field(
        None, description="Ассоциативный массив пользовательских полей"
    )
    orderType: Optional[str] = Field(None, description="Тип заказа")
    orderMethod: Optional[str] = Field(None, description="Способ оформления")
    customer: Optional[Customer] = Field(None, description="Клиент")
    contact: Optional[Customer] = Field(None, description="Контактное лицо")
    company: Optional[EntityWithExternalIdInput] = Field(None, description="Компания")
    managerId: Optional[int] = Field(
        None, description="Менеджер, прикрепленный к заказу"
    )
    status: Optional[str] = Field(None, description="Статус заказа")
    items: Optional[list[SerializedOrderProduct]] = Field(
        None, description="Позиции в заказе"
    )
    delivery: Optional[SerializedOrderDelivery] = Field(
        None, description="Данные о доставке"
    )
    source: Optional[SerializedSource] = Field(None, description="Источник заказа")
    shipmentStore: Optional[str] = Field(None, description="Склад отгрузки")
    payments: Optional[list[SerializedPayment]] = Field(None, description="Платежи")
    loyaltyEventDiscountId: Optional[int] = Field(
        None, description="ID скидки по событию программы лояльности"
    )
    applyRound: Optional[bool] = Field(
        None, description="Применять настройку округления стоимости заказа"
    )
    isFromCart: Optional[bool] = Field(None, description="Заказ создан из корзины")
    clientId: Optional[str] = Field(None, description="Метка клиента Google Analytics")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    statusUpdatedAt_serializer = field_serializer("statusUpdatedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    markDatetime_serializer = field_serializer("markDatetime")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    shipmentDate_serializer = field_serializer("shipmentDate")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )

class OrderHistory(BaseRetailCrmScheme):
    id: Optional[int] = Field(
        None, alias="id", description="Внутренний идентификатор записи в истории"
    )
    created_at: Optional[datetime] = Field(
        None, description="Дата внесения изменения", validation_alias="createdAt"
    )
    created: Optional[bool] = Field(None, description="Признак создания сущности")
    deleted: Optional[bool] = Field(None, description="Признак удаления сущности")
    source: Optional[str] = Field(None, description="Источник изменения")
    user: Optional[HistoryUser] = Field(None, description="Пользователь")
    field: Optional[str] = Field(None, description="Имя изменившегося поля")
    oldValue: Optional[str | int | float | dict] = Field(
        None, description="Старое значение свойства"
    )
    newValue: Optional[str | int | float | dict] = Field(
        None, description="Новое значение свойства"
    )
    apiKey: Optional[HistoryApiKey] = Field(
        None, description="Информация о ключе api, использовавшемся для этого изменения"
    )
    order: Optional[Order] = Field(None, description="Заказ")
    item: Optional[OrderProduct] = Field(None, description="Позиция в заказе")
    payment: Optional[Payment] = Field(None, description="Платёж")
    combinedTo: Optional[Order] = Field(
        None,
        description="Информация о заказе который получился после объединения с текущим заказом",
    )
    ancestor: Optional[Order] = Field(
        None, description="Информация о заказе из которого был создан текущий заказ"
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