from datetime import datetime
from typing import Any, Literal, Optional

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class CustomerFilterCustomerSubscriptionData(BaseRetailCrmScheme):
    channel: Optional[str] = Field(None, description="Канал категории подписки")
    subscription: Optional[str] = Field(None, description="Код категории подписки")
    subscribed: Optional[bool] = Field(None, description="Флаг подписки")


class CustomerFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID клиентов")
    externalIds: Optional[list[str]] = Field(
        None, description="Массив externalID клиентов"
    )
    name: Optional[str] = Field(None, description="Клиент")
    city: Optional[str] = Field(None, description="Город")
    region: Optional[str] = Field(None, description="Регион")
    sites: Optional[list[str]] = Field(None, description="Магазины")
    managers: Optional[list[int]] = Field(None, description="Менеджеры")
    managerGroups: Optional[list[str]] = Field(None, description="Группы менеджеров")
    notes: Optional[str] = Field(None, description="Заметки")
    vip: Optional[bool] = Field(None, description="Важный клиент")
    bad: Optional[bool] = Field(None, description="Плохой клиент")
    discountCardNumber: Optional[str] = Field(
        None, description="Номер дисконтной карты"
    )
    attachments: Optional[Literal[1, 2, 3]] = Field(
        None, description="Прикрепленные объекты (вложения)"
    )
    tasksCounts: Optional[Literal[1, 2, 3]] = Field(None, description="Задачи")
    email: Optional[str] = Field(None, description="E-mail")
    contragentName: Optional[str] = Field(None, description="Полное наименование")
    contragentTypes: Optional[
        list[Literal["enterpreneur", "individual", "legal-entity"]]
    ] = Field(None, description="Типы контрагента")
    contragentInn: Optional[str] = Field(None, description="ИНН")
    contragentKpp: Optional[str] = Field(None, description="КПП")
    contragentBik: Optional[str] = Field(None, description="БИК банка")
    contragentCorrAccount: Optional[str] = Field(None, description="Корр. счет банка")
    contragentBankAccount: Optional[str] = Field(None, description="Расчетный счет")
    classSegment: Optional[str] = Field(None, description="Сегмент")
    minOrdersCount: Optional[int] = Field(None, description="Количество заказов (от)")
    maxOrdersCount: Optional[int] = Field(None, description="Количество заказов (до)")
    minAverageSumm: Optional[int] = Field(None, description="Средний чек (от)")
    maxAverageSumm: Optional[int] = Field(None, description="Средний чек (до)")
    minTotalSumm: Optional[int] = Field(None, description="Сумма по заказам (от)")
    maxTotalSumm: Optional[int] = Field(None, description="Сумма по заказам (до)")
    minCostSumm: Optional[int] = Field(
        None, description="Сумма расходов по заказам (от)"
    )
    maxCostSumm: Optional[int] = Field(
        None, description="Сумма расходов по заказам (до)"
    )
    dateFrom: Optional[datetime] = Field(None, description="Дата регистрации (от)")
    dateTo: Optional[datetime] = Field(None, description="Дата регистрации (до)")
    firstOrderFrom: Optional[datetime] = Field(None, description="Первый заказ (от)")
    firstOrderTo: Optional[datetime] = Field(None, description="Первый заказ (до)")
    lastOrderFrom: Optional[datetime] = Field(None, description="Последний заказ (от)")
    lastOrderTo: Optional[datetime] = Field(None, description="Последний заказ (до)")
    customFields: Optional[dict[str, Any]] = Field(
        None, description="Пользовательские поля"
    )
    sex: Optional[
        Literal["female", "female_with_presumable", "male", "male_with_presumable"]
    ] = Field(None, description="Пол")
    isContact: Optional[bool] = Field(
        None, description="Клиент является контактным лицом"
    )
    subscriptions: Optional[list[CustomerFilterCustomerSubscriptionData]] = Field(
        None, description="Фильтр по подпискам пользователя"
    )
    online: Optional[bool] = Field(None, description="Клиент на сайте")
    segment: Optional[str] = Field(None, description="Сегмент")
    commentary: Optional[str] = Field(None, description="Комментарий оператора")
    browserId: Optional[str] = Field(
        None, description="Идентификатор устройства в Collector"
    )
    mgChannels: Optional[list[int]] = Field(None, description="Каналы чатов")
    sourceName: Optional[str] = Field(None, description="Источник")
    mediumName: Optional[str] = Field(None, description="Канал")
    campaignName: Optional[str] = Field(None, description="Кампания")
    keywordName: Optional[str] = Field(None, description="Ключевое слово")
    adContentName: Optional[str] = Field(None, description="Содержание кампании")
    tags: Optional[list[str]] = Field(None, description="Теги")
    attachedTags: Optional[list[str]] = Field(
        None, description="Список прикреплённых тегов (или)"
    )
    countries: Optional[list[str]] = Field(None, description="Страны")
    abandonedCart: Optional[bool] = Field(None)
    emailMarketingUnsubscribed: Optional[bool] = Field(
        None, description="deprecated Отписан от email рассылок"
    )
    mgCustomerId: Optional[str] = Field(
        None, description="Идентификатор клиента MessageGateway"
    )
    firstWebVisitFrom: Optional[datetime] = Field(
        None, description="Первое посещение (от)"
    )
    firstWebVisitTo: Optional[datetime] = Field(
        None, description="Первое посещение (до)"
    )
    lastWebVisitFrom: Optional[datetime] = Field(
        None, description="Последнее посещение (от)"
    )
    lastWebVisitTo: Optional[datetime] = Field(
        None, description="Последнее посещение (до)"
    )

    dateFrom_serializer = field_serializer("dateFrom")(datetime_serializer("%Y-%m-%d"))
    dateTo_serializer = field_serializer("dateTo")(datetime_serializer("%Y-%m-%d"))
    firstOrderFrom_serializer = field_serializer("firstOrderFrom")(
        datetime_serializer("%Y-%m-%d")
    )
    firstOrderTo_serializer = field_serializer("firstOrderTo")(
        datetime_serializer("%Y-%m-%d")
    )
    lastOrderFrom_serializer = field_serializer("lastOrderFrom")(
        datetime_serializer("%Y-%m-%d")
    )
    lastOrderTo_serializer = field_serializer("lastOrderTo")(
        datetime_serializer("%Y-%m-%d")
    )
    firstWebVisitFrom_serializer = field_serializer("firstWebVisitFrom")(
        datetime_serializer("%Y-%m-%d")
    )
    firstWebVisitTo_serializer = field_serializer("firstWebVisitTo")(
        datetime_serializer("%Y-%m-%d")
    )
    lastWebVisitFrom_serializer = field_serializer("lastWebVisitFrom")(
        datetime_serializer("%Y-%m-%d")
    )
    lastWebVisitTo_serializer = field_serializer("lastWebVisitTo")(
        datetime_serializer("%Y-%m-%d")
    )


class CustomerHistoryFilterV4Type(BaseRetailCrmScheme):
    customerId: Optional[int] = Field(None, description="ID клиента")
    sinceId: Optional[int] = Field(None, description="Начиная с ID истории клиентов")
    customerExternalId: Optional[str] = Field(None, description="Внешний ID клиента")
    startDate: Optional[datetime] = Field(None, description="Дата/время изменения (от)")
    endDate: Optional[datetime] = Field(None, description="Дата/время изменения (до)")

    startDate_serializer = field_serializer("startDate")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    endDate_serializer = field_serializer("endDate")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class CustomerNoteFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="ID заметок")
    customerIds: Optional[list[int]] = Field(None, description="Внутренние ID клиентов")
    customerExternalIds: Optional[list[str]] = Field(
        None, description="Внешние ID клиентов"
    )
    managerIds: Optional[list[int]] = Field(None, description="ID менеджеров")
    text: Optional[str] = Field(None, description="Текст заметки")
    createdAtFrom: Optional[str] = Field(None, description="Дата/время создания (от)")
    createdAtTo: Optional[str] = Field(None, description="Дата/время создания (до)")
