from datetime import datetime
from typing import Optional, Callable, Any, List

from pydantic import BaseModel, Field, field_validator
from pydantic_core.core_schema import ValidationInfo

from retailcrm.v5.schemas.base import RetailCrmResponse


def dict_validator() -> Callable[[Any, ValidationInfo], dict]:
    def validator(v, info: ValidationInfo) -> dict:
        if isinstance(v, dict):
            return v
        if isinstance(v, list) and not v:
            return {}
        else:
            raise ValueError("Not empty list")

    return validator


class CreateOrder(BaseModel):
    id: int
    externalId: Optional[str] = None


class ResponseCreateOrder(RetailCrmResponse):
    order: Optional[CreateOrder] = None


class LoyaltyLevel(BaseModel):
    id: Optional[int] = Field(None)
    name: str = Field("")


class LoyaltyEventDiscount(BaseModel):
    id: int


class CustomerContragent(BaseModel):
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


class Customer(BaseModel):
    type: Optional[str] = Field(None)
    id: Optional[int] = Field(None)
    externalId: Optional[str] = Field(None)
    isContact: Optional[bool] = Field(None)
    createdAt: Optional[datetime] = Field(None)
    managerId: Optional[int] = Field(None)
    vip: Optional[bool] = Field(None)
    bad: Optional[bool] = Field(None)
    site: Optional[str] = Field(None)
    contragent: Optional[CustomerContragent] = Field(None)
    tags: Optional[List["CustomerTagLink"]] = Field(None)
    firstClientId: Optional[str] = Field(None)
    lastClientId: Optional[str] = Field(None)
    customFields: Optional[dict] = Field(None)
    personalDiscount: Optional[float] = Field(None)
    cumulativeDiscount: Optional[float] = Field(None)
    discountCardNumber: Optional[str] = Field(None)
    avgMarginSumm: Optional[float] = Field(None)
    marginSumm: Optional[float] = Field(None)
    totalSumm: Optional[float] = Field(None)
    averageSumm: Optional[float] = Field(None)
    ordersCount: Optional[int] = Field(None)
    costSumm: Optional[float] = Field(None)
    address: Optional["CustomerAddress"] = Field(None)
    maturationTime: Optional[int] = Field(None)
    firstName: Optional[str] = Field(None)
    lastName: Optional[str] = Field(None)
    patronymic: Optional[str] = Field(None)
    sex: Optional[str] = Field(None)
    presumableSex: Optional[str] = Field(None)
    email: Optional[str] = Field(None)
    emailMarketingUnsubscribedAt: Optional[datetime] = Field(None)
    phones: Optional[List["CustomerPhone"]] = Field(None)
    birthday: Optional[datetime] = Field(None)
    source: Optional["SerializedSource"] = Field(None)
    mgCustomers: Optional[List["MGCustomer"]] = Field(None)
    photoUrl: Optional[str] = Field(None)

    custom_fields_validator = field_validator("customFields", mode="before")(
        dict_validator()
    )


class CodeValueModel(BaseModel):
    code: Optional[str] = Field(None, description="Код")
    value: Optional[str] = Field(None, description="Значение")


class Unit(BaseModel):
    code: Optional[str]
    name: Optional[str]
    sym: Optional[str]


class PriceType(BaseModel):
    code: Optional[str]


class CustomerTagLink(BaseModel):
    name: Optional[str]
    colorCode: Optional[str]
    attached: Optional[bool]


class CustomerAddress(BaseModel):
    id: Optional[int] = Field(None)
    index: Optional[str] = Field(None)
    countryIso: Optional[str] = Field(None)
    region: Optional[str] = Field(None)
    regionId: Optional[int] = Field(None)
    city: Optional[str] = Field(None)
    cityId: Optional[int] = Field(None)
    cityType: Optional[str] = Field(None)
    street: Optional[str] = Field(None)
    streetId: Optional[int] = Field(None)
    streetType: Optional[str] = Field(None)
    building: Optional[str] = Field(None)
    flat: Optional[str] = Field(None)
    floor: Optional[int] = Field(None)
    block: Optional[int] = Field(None)
    house: Optional[str] = Field(None)
    housing: Optional[str] = Field(None)
    metro: Optional[str] = Field(None)
    notes: Optional[str] = Field(None)
    text: Optional[str] = Field(None)
    externalId: Optional[str] = Field(None)
    name: Optional[str] = Field(None)


class CustomerPhone(BaseModel):
    number: str


class SerializedSource(BaseModel):
    source: Optional[str] = Field(None)
    medium: Optional[str] = Field(None)
    campaign: Optional[str] = Field(None)
    keyword: Optional[str] = Field(None)
    content: Optional[str] = Field(None)


class MGCustomer(BaseModel):
    id: int
    externalId: Optional[int] = Field(None)
    mgChannel: "MGChannel"


class MGChannel(BaseModel):
    id: Optional[int] = Field(None)
    externalId: Optional[int] = Field(None)
    type: Optional[str] = Field(None)
    active: Optional[bool] = Field(None)
    name: Optional[str] = Field(None)


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


class SerializedEntityCustomer(BaseModel):
    site: Optional[str] = Field(None)
    id: Optional[int] = Field(None)
    externalId: Optional[str] = Field(None)
    type: Optional[str] = Field(None)


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


class GenericData(BaseModel):
    externalId: Optional[str] = Field(None)


class CourierData(BaseModel):
    externalId: Optional[str] = Field(None)
    trackNumber: Optional[str] = Field(None)
    status: Optional[str] = Field(None)
    locked: Optional[bool] = Field(None)
    pickuppointAddress: Optional[str] = Field(None)
    days: Optional[str] = Field(None)
    statusText: Optional[str] = Field(None)
    statusDate: Optional[datetime] = Field(None)
    tariff: Optional[str] = Field(None)
    tariffName: Optional[str] = Field(None)
    pickuppointId: Optional[str] = Field(None)
    pickuppointSchedule: Optional[str] = Field(None)
    pickuppointPhone: Optional[str] = Field(None)
    payerType: Optional[str] = Field(None)
    statusComment: Optional[str] = Field(None)
    cost: Optional[float] = Field(None)
    minTerm: Optional[int] = Field(None)
    maxTerm: Optional[int] = Field(None)
    shipmentpointId: Optional[str] = Field(None)
    shipmentpointName: Optional[str] = Field(None)
    shipmentpointAddress: Optional[str] = Field(None)
    shipmentpointSchedule: Optional[str] = Field(None)
    shipmentpointPhone: Optional[str] = Field(None)
    shipmentpointCoordinateLatitude: Optional[str] = Field(None)
    shipmentpointCoordinateLongitude: Optional[str] = Field(None)
    pickuppointName: Optional[str] = Field(None)
    pickuppointCoordinateLatitude: Optional[str] = Field(None)
    pickuppointCoordinateLongitude: Optional[str] = Field(None)
    extraData: Optional[dict] = Field(None)
    itemDeclaredValues: Optional[List["DeclaredValueItem"]] = Field(None)
    packages: Optional[List["Package"]] = Field(None)


class NewPostData(BaseModel):
    externalId: Optional[str] = Field(None)
    trackNumber: Optional[str] = Field(None)
    status: Optional[str] = Field(None)
    locked: Optional[bool] = Field(None)
    pickuppointAddress: Optional[str] = Field(None)
    days: Optional[str] = Field(None)
    statusText: Optional[str] = Field(None)
    statusDate: Optional[datetime] = Field(None)
    tariff: Optional[str] = Field(None)
    tariffName: Optional[str] = Field(None)
    pickuppointId: Optional[str] = Field(None)
    pickuppointSchedule: Optional[str] = Field(None)
    pickuppointPhone: Optional[str] = Field(None)
    payerType: Optional[str] = Field(None)
    statusComment: Optional[str] = Field(None)
    cost: Optional[float] = Field(None)
    minTerm: Optional[int] = Field(None)
    maxTerm: Optional[int] = Field(None)
    shipmentpointId: Optional[str] = Field(None)
    shipmentpointName: Optional[str] = Field(None)
    shipmentpointAddress: Optional[str] = Field(None)
    shipmentpointSchedule: Optional[str] = Field(None)
    shipmentpointPhone: Optional[str] = Field(None)
    shipmentpointCoordinateLatitude: Optional[str] = Field(None)
    shipmentpointCoordinateLongitude: Optional[str] = Field(None)
    pickuppointName: Optional[str] = Field(None)
    pickuppointCoordinateLatitude: Optional[str] = Field(None)
    pickuppointCoordinateLongitude: Optional[str] = Field(None)
    extraData: Optional[dict] = Field(None)
    itemDeclaredValues: Optional[List["DeclaredValueItem"]] = Field(None)
    packages: Optional[List["Package"]] = Field(None)


class DDeliveryData(BaseModel):
    externalId: Optional[str] = Field(None)
    trackNumber: Optional[str] = Field(None)
    status: Optional[str] = Field(None)
    locked: Optional[bool] = Field(None)
    pickuppointAddress: Optional[str] = Field(None)
    days: Optional[str] = Field(None)
    statusText: Optional[str] = Field(None)
    statusDate: Optional[datetime] = Field(None)
    tariff: Optional[str] = Field(None)
    tariffName: Optional[str] = Field(None)
    pickuppointId: Optional[str] = Field(None)
    pickuppointSchedule: Optional[str] = Field(None)
    pickuppointPhone: Optional[str] = Field(None)
    payerType: Optional[str] = Field(None)
    statusComment: Optional[str] = Field(None)
    cost: Optional[float] = Field(None)
    minTerm: Optional[int] = Field(None)
    maxTerm: Optional[int] = Field(None)
    shipmentpointId: Optional[str] = Field(None)
    shipmentpointName: Optional[str] = Field(None)
    shipmentpointAddress: Optional[str] = Field(None)
    shipmentpointSchedule: Optional[str] = Field(None)
    shipmentpointPhone: Optional[str] = Field(None)
    shipmentpointCoordinateLatitude: Optional[str] = Field(None)
    shipmentpointCoordinateLongitude: Optional[str] = Field(None)
    pickuppointName: Optional[str] = Field(None)
    pickuppointCoordinateLatitude: Optional[str] = Field(None)
    pickuppointCoordinateLongitude: Optional[str] = Field(None)
    extraData: Optional[dict] = Field(None)
    itemDeclaredValues: Optional[List["DeclaredValueItem"]] = Field(None)
    packages: Optional[List["Package"]] = Field(None)


class KazPostData(BaseModel):
    externalId: Optional[str] = Field(None)
    trackNumber: Optional[str] = Field(None)
    status: Optional[str] = Field(None)
    locked: Optional[bool] = Field(None)
    pickuppointAddress: Optional[str] = Field(None)
    days: Optional[str] = Field(None)
    statusText: Optional[str] = Field(None)
    statusDate: Optional[datetime] = Field(None)
    tariff: Optional[str] = Field(None)
    tariffName: Optional[str] = Field(None)
    pickuppointId: Optional[str] = Field(None)
    pickuppointSchedule: Optional[str] = Field(None)
    pickuppointPhone: Optional[str] = Field(None)
    payerType: Optional[str] = Field(None)
    statusComment: Optional[str] = Field(None)
    cost: Optional[float] = Field(None)
    minTerm: Optional[int] = Field(None)
    maxTerm: Optional[int] = Field(None)
    shipmentpointId: Optional[str] = Field(None)
    shipmentpointName: Optional[str] = Field(None)
    shipmentpointAddress: Optional[str] = Field(None)
    shipmentpointSchedule: Optional[str] = Field(None)
    shipmentpointPhone: Optional[str] = Field(None)
    shipmentpointCoordinateLatitude: Optional[str] = Field(None)
    shipmentpointCoordinateLongitude: Optional[str] = Field(None)
    pickuppointName: Optional[str] = Field(None)
    pickuppointCoordinateLatitude: Optional[str] = Field(None)
    pickuppointCoordinateLongitude: Optional[str] = Field(None)
    extraData: Optional[dict] = Field(None)
    itemDeclaredValues: Optional[List["DeclaredValueItem"]] = Field(None)
    packages: Optional[List["Package"]] = Field(None)


class OrderDeliveryAddress(BaseModel):
    index: Optional[str] = Field(None)
    countryIso: Optional[str] = Field(None)
    region: Optional[str] = Field(None)
    regionId: Optional[int] = Field(None)
    city: Optional[str] = Field(None)
    cityId: Optional[int] = Field(None)
    cityType: Optional[str] = Field(None)
    street: Optional[str] = Field(None)
    streetId: Optional[int] = Field(None)
    streetType: Optional[str] = Field(None)
    building: Optional[str] = Field(None)
    flat: Optional[str] = Field(None)
    floor: Optional[int] = Field(None)
    block: Optional[int] = Field(None)
    house: Optional[str] = Field(None)
    housing: Optional[str] = Field(None)
    metro: Optional[str] = Field(None)
    notes: Optional[str] = Field(None)
    text: Optional[str] = Field(None)


class DeclaredValueItem(BaseModel):
    orderProduct: "PackageItemOrderProduct" = Field(None)
    value: Optional[float] = Field(None)


class PackageItemOrderProduct(BaseModel):
    id: Optional[int] = Field(None)
    externalId: Optional[str] = Field(None)
    externalIds: Optional[List[CodeValueModel]] = Field(None)
    quantity: Optional[float] = Field(None)


class Package(BaseModel):
    packageId: Optional[str] = Field(None)
    weight: Optional[float] = Field(None)
    length: Optional[int] = Field(None)
    width: Optional[int] = Field(None)
    height: Optional[int] = Field(None)
    items: List["PackageItem"] = []


class PackageItem(BaseModel):
    orderProduct: "PackageItemOrderProduct" = Field(None)
    quantity: Optional[float] = Field(None)


class TimeInterval(BaseModel):
    from_: Optional[datetime] = Field(None, alias="from")
    to: Optional[datetime] = Field(None)


class LinkedOrder(BaseModel):
    id: Optional[int] = Field(None)
    number: Optional[str] = Field(None)
    externalId: Optional[str] = Field(None)


class OrderLink(BaseModel):
    order: Optional[LinkedOrder] = Field(None)
    createdAt: Optional[datetime] = Field(None)
    comment: Optional[str] = Field(None)


class OrderProductPriceItem(BaseModel):
    price: Optional[float] = Field(None)
    quantity: Optional[float] = Field(None)


class AbstractDiscount(BaseModel):
    type: Optional[str] = Field(
        None,
        description="Тип скидки. Возможные значения:  <br>`manual_order` - Разовая скидка на заказ;  <br>`manual_product` - Дополнительная скидка на товар;  <br>`loyalty_level` - Скидка по уровню программы лояльности;  <br>`loyalty_event` - Скидка по событию программы лояльности;  <br>`personal` - Персональная скидка;  <br>`bonus_charge` - Списание бонусов ПЛ;  <br>`round` - Скидка от округления",
    )
    amount: Optional[float] = Field(None, description="Сумма скидки")


class OrderProduct(BaseModel):
    id: Optional[int] = Field(None, description="ID позиции в заказе")
    externalId: Optional[str] = Field(None)
    external_ids: list[CodeValueModel] = Field(
        [],
        description="Внешние идентификаторы позиции в заказе",
        validation_alias="externalIds",
    )
    discounts: list[AbstractDiscount] = Field([], description="Массив скидок")
    offer: Optional["Offer"] = Field(None, description="Торговое предложение")
    ordering: Optional[int] = Field(None, description="Порядок")
    properties: dict = Field({}, description="Дополнительные свойства позиции в заказе")

    bonusesChargeTotal: Optional[float] = Field(None)
    bonusesCreditTotal: Optional[float] = Field(None)
    markingCodes: Optional[List[str]] = Field(None)
    externalIds: Optional[List[CodeValueModel]] = Field(None)
    priceType: Optional[PriceType] = Field(None)
    initialPrice: Optional[float] = Field(None)
    discountTotal: Optional[float] = Field(None)
    prices: Optional[List[OrderProductPriceItem]] = Field(None)
    vatRate: Optional[str] = Field(None)
    createdAt: Optional[datetime] = Field(None)
    quantity: Optional[float] = Field(None)
    status: Optional[str] = Field(None)
    comment: Optional[str] = Field(None)
    isCanceled: Optional[bool] = Field(None)
    purchasePrice: Optional[float] = Field(None)

    properties_validator = field_validator("properties", mode="before")(
        dict_validator()
    )


class Offer(BaseModel):
    id: Optional[int] = Field(None, description="ID торгового предложения")
    external_id: Optional[str] = Field(
        None,
        description="ID торгового предложения в магазине",
        validation_alias="externalId",
    )
    xml_id: Optional[str] = Field(
        None,
        description="ID торгового предложения в складской системе",
        validation_alias="xmlId",
    )
    properties: dict[str, Any] = Field({}, description="Свойства SKU")

    displayName: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    article: Optional[str] = Field(None)
    vatRate: Optional[str] = Field(None)
    unit: Optional[Unit] = Field(None)
    barcode: Optional[str] = Field(None)

    properties_validator = field_validator("properties", mode="before")(
        dict_validator()
    )


class Payment(BaseModel):
    id: Optional[int] = Field(None, description="Внутренний ID")
    type: Optional[str] = Field(None, description="Тип оплаты")
    external_id: Optional[str] = Field(
        None, description="Внешний ID платежа", validation_alias="externalId"
    )
    status: Optional[str] = Field(None)
    amount: Optional[float] = Field(None)
    paidAt: Optional[datetime] = Field(None)
    comment: Optional[str] = Field(None)


class SerializedOrderDelivery(BaseModel):
    code: Optional[str] = Field(None)
    integrationCode: Optional[str] = Field(None)
    # data: "OrderDeliveryData"
    # service: "SerializedDeliveryService"
    cost: Optional[float] = Field(None)
    netCost: Optional[float] = Field(None)
    date: Optional[datetime] = Field(None)
    time: Optional[TimeInterval] = Field(None)
    address: Optional[OrderDeliveryAddress] = Field(None)
    vatRate: Optional[str] = Field(None)


class Order(BaseModel):
    id: int = Field(0, description="ID заказа")
    external_id: str = Field(
        "", description="Внешний ID заказа", validation_alias="externalId"
    )
    number: str = Field("", description="Номер заказа")
    site: str = Field("", description="Магазин")
    status: str = Field("", description="Статус заказа")
    status_comment: Optional[str] = Field(
        None, description="", validation_alias="statusComment"
    )
    manager_id: Optional[int] = Field(
        None,
        description="Менеджер, прикрепленный к заказу",
        validation_alias="managerId",
    )
    bonuses_credit_total: float = Field(
        0,
        description="Количество начисленных бонусов",
        validation_alias="bonusesCreditTotal",
    )
    bonuses_charge_total: float = Field(
        0,
        description="Количество списанных бонусов",
        validation_alias="bonusesChargeTotal",
    )
    summ: float = Field(0, description="Сумма по товарам (в валюте объекта)")
    currency: str = Field("", description="Валюта")
    order_type: str = Field("Тип заказа", description="", validation_alias="orderType")
    order_method: str = Field(
        "", description="Способ оформления", validation_alias="orderMethod"
    )
    privilege_type: str = Field(
        "none",
        description="Тип привилегии",
        examples=["none", "personal_discount", "loyalty_level", "loyalty_event"],
        validation_alias="privilegeType",
    )
    country_iso: str = Field(
        "",
        description="ISO код страны (ISO 3166-1 alpha-2)",
        validation_alias="countryIso",
    )
    created_at: Optional[datetime] = Field(
        None, description="Дата оформления заказа", validation_alias="createdAt"
    )
    status_updated_at: Optional[datetime] = Field(
        None,
        description="Дата последнего изменения статуса",
        validation_alias="statusUpdatedAt",
    )
    total_summ: float = Field(
        0,
        description="Общая сумма с учетом скидки (в валюте объекта)",
        validation_alias="totalSumm",
    )
    prepay_sum: float = Field(
        0,
        description="Оплаченная сумма (в валюте объекта)",
        validation_alias="prepaySum",
    )
    purchase_summ: float = Field(
        0,
        description="Общая стоимость закупки (в базовой валюте)",
        validation_alias="purchaseSumm",
    )
    personal_discount_percent: Optional[float] = Field(
        None,
        description="Персональная скидка на заказ",
        validation_alias="personalDiscountPercent",
    )
    loyalty_level: Optional[LoyaltyLevel] = Field(
        None,
        description="Уровень участия в программе лояльности",
        validation_alias="loyaltyLevel",
    )
    loyalty_event_discount: Optional[LoyaltyEventDiscount] = Field(
        None,
        description="Скидка по событию программы лояльности",
        validation_alias="loyaltyEventDiscount",
    )
    mark: Optional[int] = Field(None, description="Оценка заказа")
    mark_datetime: Optional[datetime] = Field(
        None,
        description="Дата и время получение оценки от покупателя",
        validation_alias="markDatetime",
    )
    last_name: Optional[str] = Field(None, validation_alias="lastName")
    first_name: Optional[str] = Field("", validation_alias="firstName")
    patronymic: Optional[str] = Field(None)
    phone: Optional[str] = Field(None)
    additional_phone: Optional[str] = Field(None, validation_alias="additionalPhone")
    email: Optional[str] = Field(None)
    call: bool = Field(False)
    expired: bool = Field(False)
    customer_comment: Optional[str] = Field(None, validation_alias="customerComment")
    manager_comment: Optional[str] = Field(None, validation_alias="managerComment")
    customer: Optional[Customer] = Field(None)
    contact: Optional[Customer] = Field(None)
    company: Optional[Company] = Field(None)
    contragent: Optional[OrderContragent] = Field(None)
    delivery: Optional[SerializedOrderDelivery] = Field(None)
    source: Optional[SerializedSource] = Field(None)
    items: list[OrderProduct] = Field([])
    full_paid_at: Optional[datetime] = Field(None, validation_alias="fullPaidAt")
    payments: list["Payment"] = Field([])
    from_api: bool = Field(False, validation_alias="fromApi")
    weight: float = 0
    length: int = 0
    width: int = 0
    height: int = 0
    shipment_store: Optional[str] = Field(None, validation_alias="shipmentStore")
    shipment_date: Optional[datetime] = Field(None, validation_alias="shipmentDate")
    shipped: bool = False
    links: list[OrderLink] = Field(None)
    custom_fields: dict = Field({}, validation_alias="customFields")
    client_id: Optional[str] = Field(None, validation_alias="clientId")

    custom_fields_validator = field_validator("custom_fields", mode="before")(
        dict_validator()
    )


class User(BaseModel):
    id: int = Field(description="ID пользователя")


class ApiKey(BaseModel):
    current: Optional[bool] = Field(
        None,
        description="Изменение было сделано с помощью ключа, используемого в данный момент",
    )
    id: Optional[int] = Field(None, description="ID API-ключа")


class OrderHistory(BaseModel):
    id: Optional[int] = Field(
        None, alias="id", description="Внутренний идентификатор записи в истории"
    )
    created_at: Optional[datetime] = Field(
        None, description="Дата внесения изменения", validation_alias="createdAt"
    )
    created: Optional[bool] = Field(None, description="Признак создания сущности")
    deleted: Optional[bool] = Field(None, description="Признак удаления сущности")
    source: Optional[str] = Field(None, description="Источник изменения")
    user: Optional[User] = Field(None, description="Пользователь")
    field: Optional[str] = Field(None, description="Имя изменившегося поля")
    old_value: Optional[str | int | datetime | dict] = Field(
        None, description="Старое значение свойства", validation_alias="oldValue"
    )
    new_value: Optional[str | int | datetime | dict] = Field(
        None, description="Новое значение свойства", validation_alias="newValue"
    )
    api_key: Optional[ApiKey] = Field(
        None,
        description="Информация о ключе api, использовавшемся для этого изменения",
        validation_alias="apiKey",
    )
    order: Optional[Order] = Field(None, description="Заказ")
    item: Optional[OrderProduct] = Field(None, description="Позиция в заказе")
    payment: Optional[Payment] = Field(None, description="Платёж")
    combined_to: Optional[Order] = Field(
        None,
        description="Информация о заказе который получился после объединения с текущим заказом",
        validation_alias="combinedTo",
    )
    ancestor: Optional[Order] = Field(
        None, description="Информация о заказе из которого был создан текущий заказ"
    )


class ResponseGetOrder(RetailCrmResponse):
    order: Optional[Order] = None


class ResponseOrders(RetailCrmResponse):
    orders: list[Order] = Field([], description="Список заказов")


class ResponseEditOrder(RetailCrmResponse):
    id: Optional[int] = None
    order: Optional[Order] = None


class ResponseCreateOrderPayment(RetailCrmResponse):
    id: Optional[int] = 0


class ResponseEditOrderPayment(RetailCrmResponse):
    id: Optional[int] = 0


class ResponseOrderHistory(RetailCrmResponse):
    generated_at: Optional[datetime] = Field(
        None, description="Время формирования ответа", validation_alias="generatedAt"
    )
    history: list[OrderHistory] = []


class ResponseDeleteOrderPayment(RetailCrmResponse):
    pass


class ResponseOrdersHistory(RetailCrmResponse):
    generated_at: Optional[datetime] = Field(
        None,
    )
