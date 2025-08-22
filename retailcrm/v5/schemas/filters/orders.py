from datetime import date, datetime, time
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.enums import DeliveryStatusTypes
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class OrdersFilter(BaseRetailCrmScheme):
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
