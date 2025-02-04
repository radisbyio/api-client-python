from datetime import date, datetime, time
from typing import Optional, Union

from pydantic import Field, RootModel, field_serializer

from retailcrm.v5.enums import DeliveryStatusTypes, PrivilegeType, VatRateTypes
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas import BaseRetailCrmScheme, RetailCrmResponse
from retailcrm.v5.schemas.shared import (
    ApiKey,
    CodeValueModel,
    Contact,
    Customer,
    MGDialog,
    Order,
    OrderProduct,
    OrderProductProperties,
    Payment,
    PriceType,
    SerializedOrderDelivery,
    Source,
    User, FixExternalRow,
)


class DeliveryService(BaseRetailCrmScheme):
    name: str
    code: str = ""
    active: bool = False
    deliveryType: str = ""


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

    startDate_serializer = field_serializer("startDate")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    endDate_serializer = field_serializer("endDate")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class OrderFilterData(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID заказов")
    externalIds: Optional[list[str]] = Field(
        None, description="Массив externalID заказов"
    )
    numbers: Optional[list[str]] = Field(
        None,
        description="Массив номеров заказов (не более 100 номеров в одном запросе)",
    )
    customerId: Optional[int] = Field(None, description="Внутренний ID клиента")
    customerExternalId: Optional[str] = Field(None, description="Внешний ID клиента")
    customer: Optional[str] = Field(None, description="Клиент (ФИО или телефон)")
    customerType: Optional[str] = Field(None, description="Тип клиента")
    email: Optional[str] = Field(None, description="E-mail")
    managers: Optional[list[int]] = Field(None, description="Менеджеры")
    managerGroups: Optional[list[str]] = Field(None, description="Группы менеджеров")
    paymentStatuses: Optional[list[str]] = Field(None, description="Статусы оплаты")
    orderTypes: Optional[list[str]] = Field(None, description="Типы заказа")
    orderMethods: Optional[list[str]] = Field(None, description="Способы оформления")
    product: Optional[str] = Field(None, description="Товар (название или артикул)")
    extendedStatus: Optional[list[str]] = Field(None, description="Статус заказа")
    statusComment: Optional[str] = Field(None, description="")
    sites: Optional[list[str]] = Field(None, description="Магазины")
    vip: Optional[bool] = Field(None, description="Важный клиент")
    bad: Optional[bool] = Field(None, description="Плохой клиент")
    expired: Optional[bool] = Field(None, description="Заказ просрочен")
    call: Optional[bool] = Field(None, description="Требуется позвонить")
    online: Optional[bool] = Field(None, description="Клиент на сайте")
    paymentTypes: Optional[list[str]] = Field(None, description="Типы оплаты")
    deliveryStates: Optional[list[DeliveryStatusTypes]] = Field(
        None, description="Статусы оформления"
    )
    deliveryTypes: Optional[list[str]] = Field(None, description="Типы доставки")
    deliveryServices: Optional[list[str]] = Field(None, description="Службы доставки")
    countries: Optional[list[str]] = Field(None, description="Страны")
    region: Optional[str] = Field(None, description="Регион")
    city: Optional[str] = Field(None, description="Город")
    index: Optional[str] = Field(None, description="Почтовый индекс")
    metro: Optional[str] = Field(None, description="Метро")
    sourceName: Optional[str] = Field(None, description="Источник")
    mediumName: Optional[str] = Field(None, description="Канал")
    campaignName: Optional[str] = Field(None, description="Кампания")
    keywordName: Optional[str] = Field(None, description="Ключевое слово")
    adContentName: Optional[str] = Field(None, description="Содержание кампании")
    managerComment: Optional[str] = Field(None, description="Комментарий менеджера")
    customerComment: Optional[str] = Field(None, description="Комментарий клиента")
    trackNumber: Optional[str] = Field(
        None, description="Номер отправления в службе доставки"
    )
    deliveryExternalId: Optional[str] = Field(
        None, description="Идентификатор в службе доставки"
    )
    couriers: Optional[list[int]] = Field(None, description="Курьеры")
    contragentName: Optional[str] = Field(None, description="Полное наименование")
    contragentTypes: Optional[list[str]] = Field(None, description="Типы контрагента")
    contragentInn: Optional[str] = Field(None, description="ИНН")
    contragentKpp: Optional[str] = Field(None, description="КПП")
    contragentBik: Optional[str] = Field(None, description="БИК банка")
    contragentCorrAccount: Optional[str] = Field(None, description="Корр. счет банка")
    contragentBankAccount: Optional[str] = Field(None, description="Расчетный счет")
    companyName: Optional[str] = Field(None, description="Компания (название)")
    deliveryAddressNotes: Optional[str] = Field(
        None, description="Примечания к адресу доставки"
    )
    shipmentStores: Optional[list[str]] = Field(None, description="Склады отгрузки")
    shipped: Optional[bool] = Field(None, description="Отгружен")
    attachments: Optional[int] = Field(
        None, description="Прикрепленные объекты (вложения)"
    )
    receiptFiscalDocumentAttribute: Optional[str] = Field(
        None, description="Фискальный признак документа"
    )
    receiptStatus: Optional[str] = Field(None, description="Статус фискализации")
    receiptOperation: Optional[str] = Field(None, description="Операция фискализации")
    receiptOrderStatus: Optional[str] = Field(
        None, description="Статус полной фискализации"
    )
    mgChannels: Optional[list[int]] = Field(None, description="Каналы чатов")
    tasksCounts: Optional[int] = Field(None, description="Задачи")
    tags: Optional[list[str]] = Field(None, description="")
    attachedTags: Optional[list[str]] = Field(None, description="")
    createdAtFrom: Optional[date] = Field(
        None, description="Дата оформления заказа (от)"
    )
    createdAtTo: Optional[date] = Field(None, description="Дата оформления заказа (до)")
    fullPaidAtFrom: Optional[date] = Field(None, description="Дата полной оплаты (от)")
    fullPaidAtTo: Optional[date] = Field(None, description="Дата полной оплаты (до)")
    deliveryDateFrom: Optional[date] = Field(None, description="Дата доставки (от)")
    deliveryDateTo: Optional[date] = Field(None, description="Дата доставки (до)")
    statusUpdatedAtFrom: Optional[date] = Field(
        None, description="Дата последнего изменения статуса (от)"
    )
    statusUpdatedAtTo: Optional[date] = Field(
        None, description="Дата последнего изменения статуса (до)"
    )
    shipmentDateFrom: Optional[date] = Field(None, description="Дата отгрузки (от)")
    shipmentDateTo: Optional[date] = Field(None, description="Дата отгрузки (до)")
    firstWebVisitFrom: Optional[date] = Field(None, description="Первое посещение (от)")
    firstWebVisitTo: Optional[date] = Field(None, description="Первое посещение (до)")
    lastWebVisitFrom: Optional[date] = Field(
        None, description="Последнее посещение (от)"
    )
    lastWebVisitTo: Optional[date] = Field(None, description="Последнее посещение (до)")
    firstOrderFrom: Optional[date] = Field(None, description="Первый заказ (от)")
    firstOrderTo: Optional[date] = Field(None, description="Первый заказ (до)")
    lastOrderFrom: Optional[date] = Field(None, description="Последний заказ (от)")
    lastOrderTo: Optional[date] = Field(None, description="Последний заказ (до)")
    paidAtFrom: Optional[date] = Field(None, description="Дата оплаты (от)")
    paidAtTo: Optional[date] = Field(None, description="Дата оплаты (до)")
    deliveryTimeFrom: Optional[time] = Field(None, description="Время доставки (с)")
    deliveryTimeTo: Optional[time] = Field(None, description="Время доставки (до)")
    minPrice: Optional[int] = Field(None, description="Стоимость заказа (от)")
    maxPrice: Optional[int] = Field(None, description="Стоимость заказа (до)")
    minCostSumm: Optional[int] = Field(None, description="Сумма расходов (от)")
    maxCostSumm: Optional[int] = Field(None, description="Сумма расходов (до)")
    minPrepaySumm: Optional[int] = Field(None, description="Оплачено (от)")
    maxPrepaySumm: Optional[int] = Field(None, description="Оплачено (до)")
    minDeliveryCost: Optional[int] = Field(None, description="Стоимость доставки (от)")
    maxDeliveryCost: Optional[int] = Field(None, description="Стоимость доставки (до)")
    minDeliveryNetCost: Optional[int] = Field(
        None, description="Себестоимость доставки (от)"
    )
    maxDeliveryNetCost: Optional[int] = Field(
        None, description="Себестоимость доставки (до)"
    )
    minMarginSumm: Optional[int] = Field(
        None, description="Валовая прибыль заказа (от)"
    )
    maxMarginSumm: Optional[int] = Field(
        None, description="Валовая прибыль заказа (до)"
    )
    minPurchaseSumm: Optional[int] = Field(
        None, description="Закупочная стоимость заказа (от)"
    )
    maxPurchaseSumm: Optional[int] = Field(
        None, description="Закупочная стоимость заказа (до)"
    )
    customFields: Optional[dict] = Field(
        None, description="Фильтр по пользовательским полям"
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
    discountManualAmount: Optional[float] = Field(
        None, description="Денежная скидка на весь заказ (в валюте объекта)"
    )
    discountManualPercent: Optional[float] = Field(
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
    statusComment: Optional[str] = Field(
        None, description="Комментарий к последнему изменению статуса"
    )
    weight: Optional[float] = Field(None, description="Вес")
    length: Optional[int] = Field(None, description="Длина")
    width: Optional[int] = Field(None, description="Ширина")
    height: Optional[int] = Field(None, description="Высота")
    shipmentDate: Optional[datetime] = Field(None, description="Дата отгрузки")
    shipped: Optional[bool] = Field(None, description="Заказ отгружен")
    dialogId: Optional[MGDialog] = Field(
        None, description="Идентификатор диалога Чатов"
    )
    customFields: Optional[dict] = Field(
        None, description="Ассоциативный массив пользовательских полей"
    )
    orderType: Optional[str] = Field(None, description="Тип заказа")
    orderMethod: Optional[str] = Field(None, description="Способ оформления")
    customer: Optional[Customer] = Field(None, description="Клиент")
    contact: Optional[Contact] = Field(None, description="Контактное лицо")
    company: Optional[dict[str, Union[int, str]]] = Field(None, description="Компания")
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
    source: Optional[Source] = Field(None, description="Источник заказа")
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
    oldValue: Optional[str | int | float | dict] = Field(
        None, description="Старое значение свойства"
    )
    newValue: Optional[str | int | float | dict] = Field(
        None, description="Новое значение свойства"
    )
    apiKey: Optional[ApiKey] = Field(
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


class ResponseOrderHistory(RetailCrmResponse):
    generated_at: Optional[datetime] = Field(
        None, description="Время формирования ответа", validation_alias="generatedAt"
    )
    history: list[OrderHistory] = []





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


class SerializedOrderReference(RetailCrmResponse):
    id: Optional[int] = Field(None, description="Внутренний ID заказа")
