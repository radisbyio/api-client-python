from datetime import date, datetime
from typing import Optional, Union

from pydantic import Field, RootModel, field_serializer

from retailcrm.v5.enums import VatRateTypes
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas import BaseRetailCrmScheme, RetailCrmResponse
from retailcrm.v5.schemas.references import SerializedDeliveryService
from retailcrm.v5.schemas.shared import (
    ApiKey,
    CodeValueModel,
    Contact,
    Customer,
    MGDialog,
    Order,
    OrderDeliveryAddress,
    OrderProduct,
    OrderProductProperties,
    Payment,
    PriceType,
    Source,
    TimeInterval,
    User,
)


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
    extraData: Optional[list[dict[str, str]]] = Field(
        None,
        description="Дополнительные данные доставки (deliveryDataField.code => значение)",
    )
    itemDeclaredValues: Optional[list[dict[str, Union[int, float]]]] = None
    packages: list[
        dict[str, Union[str, float, int, list[dict[str, Union[int, str]]]]]
    ] = Field(default_factory=list, description="Упаковки")


class DeliveryService(BaseRetailCrmScheme):
    name: str
    code: str = ""
    active: bool = False
    deliveryType: str = ""


# todo: update vatRate to enum
class SerializedOrderDelivery(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код типа доставки")
    data: Optional[GenericData] = Field(
        None, description="Данные службы доставки, подключенной через API"
    )
    service: Optional[SerializedDeliveryService] = Field(None)
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


class SerializedPayment(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(None, description="Внешний ID платежа")
    amount: float = Field(None, description="Сумма платежа (в валюте объекта)")
    paidAt: Optional[datetime] = Field(None, description="Дата оплаты")
    comment: Optional[str] = Field(None, description="Комментарий")
    type: Optional[str] = Field(None, description="Тип оплаты")
    status: Optional[str] = Field(None, description="Статус оплаты")

    paidAt_serializer = field_serializer("paidAt")(
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
    markingCodes: list[str] = Field(default_factory=list, description="Коды маркировки")
    initialPrice: Optional[float] = Field(
        None, description="Цена товара/SKU (в валюте объекта)"
    )
    discountManualAmount: Optional[float] = Field(
        0, description="Денежная скидка на единицу товара (в валюте объекта)"
    )
    discountManualPercent: Optional[float] = Field(
        0, description="Процентная скидка на единицу товара"
    )
    vatRate: VatRateTypes = Field(VatRateTypes.NONE, description="Ставка НДС")
    createdAt: Optional[datetime] = Field(
        None, description="Дата создания позиции в системе"
    )
    quantity: Optional[float] = Field(0, description="Количество")
    comment: str = Field("", description="Комментарий к позиции в заказе")
    properties: list[OrderProductProperties] = Field(
        default_factory=list, description="Дополнительные свойства позиции в заказе"
    )
    purchasePrice: float = Field(0, description="Закупочная цена (в базовой валюте)")
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


class OrderHistoryFilterV4Type(BaseRetailCrmScheme):
    orderId: Optional[int] = Field(None, description="ID заказа")
    sinceId: Optional[int] = Field(None, description="Начиная с ID истории заказов")
    externalId: Optional[str] = Field(None, description="Внешний ID заказа")
    startDate: Optional[datetime] = Field(None, description="Дата/время изменения (от)")
    endDate: Optional[datetime] = Field(None, description="Дата/время изменения (до)")


# todo: заполнить
class OrderFilterData(BaseRetailCrmScheme):
    ids: list[int] = Field([], description="Массив ID заказов")
    externalIds: list[str] = Field([], description="Массив externalID заказов")
    numbers: list[str] = Field([], description="Массив номеров заказов")
    customerId: Optional[int] = Field(None, description="Внутренний ID клиента")
    customerExternalId: Optional[str] = Field(None, description="Внешний ID клиента")
    customer: Optional[str] = Field(None, description="Клиент (ФИО или телефон)")
    customerType: Optional[str] = Field(None, description="Тип клиента")
    email: Optional[str] = Field(None, description="E-mail")
    createdAtFrom: Optional[date] = Field(
        None, description="Дата оформления заказа (от)"
    )
    orderTypes: list[str] = Field(default_factory=list, description="Типы заказа")
    extendedStatus: list[str] = Field(default_factory=list, description="Статус заказа")
    createdAtTo: Optional[date] = Field(None, description="Дата оформления заказа (до)")
    fullPaidAtFrom: Optional[date] = Field(None, description="Дата полной оплаты (от)")
    fullPaidAtTo: Optional[date] = Field(None, description="Дата полной оплаты (до)")
    deliveryDateFrom: Optional[date] = Field(None, description="Дата доставки (от)")
    deliveryDateTo: Optional[date] = Field(None, description="Дата доставки (до)")


class SerializedOrder(BaseRetailCrmScheme):
    number: str = ""
    externalId: str = ""
    privilegeType: str = ""
    countryIso: str = ""
    created_at: Optional[datetime] = Field(None, serialization_alias="createdAt")
    statusUpdatedAt: str = ""
    discountManualAmount: float = 0
    discountManualPercent: float = 0
    mark: int = 0
    markDatetime: str = ""
    lastName: str = ""
    firstName: str = ""
    patronymic: str = ""
    phone: str = ""
    additionalPhone: str = ""
    email: str = ""
    call: bool = False
    expired: bool = False
    customerComment: str = ""
    managerComment: str = ""
    # contragent: OrderContragent
    statusComment: str = ""
    weight: float = 0
    length: int = 0
    width: int = 0
    height: int = 0
    shipmentDate: str = ""
    shipped: bool = False
    dialogId: Optional[MGDialog] = None
    customFields: dict[str, str] = None
    orderType: str = ""
    orderMethod: str = ""
    customer: Optional[Customer] = None
    contact: Optional[Contact] = None
    company: Optional[dict[str, Union[int, str]]] = None
    managerId: int = 0
    status: str = ""
    items: list[SerializedOrderProduct] = None
    delivery: Optional[SerializedOrderDelivery] = None
    source: Optional[Source] = None
    shipmentStore: str = ""
    payments: list[SerializedPayment] = []
    loyaltyEventDiscountId: int = 0
    applyRound: bool = False
    isFromCart: bool = False
    clientId: str = ""

    created_at_serializer = field_serializer("created_at")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class SerializedOrderList(RootModel):
    root: list[SerializedOrder] = Field(default_factory=list)


class SerializedEntityOrder(BaseRetailCrmScheme):
    id: int = Field(0, description="Внутренний ID заказа")
    external_id: str = Field("", alias="externalId", description="Внешний ID заказа")
    number: str = Field("", description="Номер заказа")


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
    user: Optional[User] = Field(None, description="Пользователь")
    field: Optional[str] = Field(None, description="Имя изменившегося поля")
    old_value: Optional[str | int | float | dict] = Field(
        None, description="Старое значение свойства", validation_alias="oldValue"
    )
    new_value: Optional[str | int | float | dict] = Field(
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


class ResponseOrderHistory(RetailCrmResponse):
    generated_at: Optional[datetime] = Field(
        None, description="Время формирования ответа", validation_alias="generatedAt"
    )
    history: list[OrderHistory] = []


class FixExternalRow(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID")
    external_id: Optional[str] = Field(
        None, description="Внешний ID", validation_alias="externalId"
    )


class EntityWithExternalId(BaseRetailCrmScheme):
    external_id: Optional[str] = Field(
        None, description="Внешний ID (при наличии)", validation_alias="externalId"
    )


class ResponseOrdersUpload(RetailCrmResponse):
    uploaded_orders: list[FixExternalRow] = Field(
        [],
        description="Идентификаторы загруженных объектов",
        validation_alias="uploadedOrders",
    )
    failed_orders: list[FixExternalRow] = Field(
        [],
        description="Идентификаторы незагруженных объектов",
        validation_alias="failedOrders",
    )
    orders: list[Order] = Field([], description="Список заказов")


class ResponseEditOrder(RetailCrmResponse):
    id: Optional[int] = None
    order: Optional[Order] = None


class ResponseCreateOrderPayment(RetailCrmResponse):
    id: Optional[int] = 0


class ResponseEditOrderPayment(RetailCrmResponse):
    id: Optional[int] = 0


class ResponseDeleteOrderPayment(RetailCrmResponse):
    pass


class ResponseGetOrder(RetailCrmResponse):
    order: Optional[Order] = None


class ResponseOrders(RetailCrmResponse):
    orders: list[Order] = Field([], description="Список заказов")


# todo: заполнить
class CreateOrder(BaseRetailCrmScheme):
    id: int
    externalId: Optional[str] = None


# todo: заполнить
class ResponseCreateOrder(RetailCrmResponse):
    order: Optional[CreateOrder] = None
