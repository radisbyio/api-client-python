from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, field_validator, Field, field_serializer

from retailcrm.v5.enums import ContragentTypes, SexTypes
from retailcrm.v5.helpers import dict_validator, datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme, RetailCrmResponse
from retailcrm.v5.schemas.shared import Customer, CustomerAddress, CustomerPhone, SerializedSource, MGCustomer


class CustomerFilterCustomerSubscriptionData(BaseModel):
    channel: Optional[str] = Field(None, description="Канал категории подписки")
    subscription: Optional[str] = Field(None, description="Код категории подписки")
    subscribed: Optional[bool] = Field(None, description="Флаг подписки")


class CustomerFilterData(BaseRetailCrmScheme):
    ids: Optional[List[int]] = Field(None, description="Массив ID клиентов")
    externalIds: Optional[List[str]] = Field(None, description="Массив externalID клиентов")
    name: Optional[str] = Field(None, description="Клиент")
    city: Optional[str] = Field(None, description="Город")
    region: Optional[str] = Field(None, description="Регион")
    sites: Optional[List[str]] = Field(None, description="Магазины")
    managers: Optional[List[int]] = Field(None, description="Менеджеры")
    managerGroups: Optional[List[str]] = Field(None, description="Группы менеджеров")
    notes: Optional[str] = Field(None, description="Заметки")
    vip: Optional[bool] = Field(None, description="Важный клиент")
    bad: Optional[bool] = Field(None, description="Плохой клиент")
    discountCardNumber: Optional[str] = Field(None, description="Номер дисконтной карты")
    attachments: Optional[int] = Field(None, description="Прикрепленные объекты (вложения)")
    tasksCounts: Optional[int] = Field(None, description="Задачи")
    email: Optional[str] = Field(None, description="E-mail")
    contragentName: Optional[str] = Field(None, description="Полное наименование")
    contragentTypes: Optional[List[ContragentTypes]] = Field(None,
                                                             description="Типы контрагента")  # Несостыковка в документации
    contragentInn: Optional[str] = Field(None, description="ИНН")
    contragentKpp: Optional[str] = Field(None, description="КПП")
    contragentBik: Optional[str] = Field(None, description="БИК банка")
    contragentCorrAccount: Optional[str] = Field(None, description="Корр. счет банка")
    contragentBankAccount: Optional[str] = Field(None, description="Расчетный счет")
    classSegment: Optional[str] = Field(None, description="Сегмент", )
    minOrdersCount: Optional[int] = Field(None, description="Количество заказов (от)")
    maxOrdersCount: Optional[int] = Field(None, description="Количество заказов (до)")
    minAverageSumm: Optional[int] = Field(None, description="Средний чек (от)")
    maxAverageSumm: Optional[int] = Field(None, description="Средний чек (до)")
    minTotalSumm: Optional[int] = Field(None, description="Сумма по заказам (от)")
    maxTotalSumm: Optional[int] = Field(None, description="Сумма по заказам (до)")
    minCostSumm: Optional[int] = Field(None, description="Сумма расходов по заказам (от)")
    maxCostSumm: Optional[int] = Field(None, description="Сумма расходов по заказам (до)")
    dateFrom: Optional[date] = Field(None, description="Дата регистрации (от)")
    dateTo: Optional[date] = Field(None, description="Дата регистрации (до)")
    firstOrderFrom: Optional[date] = Field(None, description="Первый заказ (от)")
    firstOrderTo: Optional[date] = Field(None, description="Первый заказ (до)")
    lastOrderFrom: Optional[date] = Field(None, description="Последний заказ (от)")
    lastOrderTo: Optional[date] = Field(None, description="Последний заказ (до)")
    customFields: Optional[dict] = Field(None, description="Пользовательские поля")
    sex: Optional[SexTypes] = Field(None, description="Пол")
    isContact: Optional[bool] = Field(None, description="Клиент является контактным лицом")
    subscriptions: Optional[List[CustomerFilterCustomerSubscriptionData]] = Field(None,
                                                                                  description="Фильтр по подпискам пользователя")
    online: Optional[bool] = Field(None, description="Клиент на сайте")
    segment: Optional[str] = Field(None, description="Сегмент")
    commentary: Optional[str] = Field(None, description="Комментарий оператора")
    browserId: Optional[str] = Field(
        None, description="Идентификатор устройства в Collector"
    )
    mgChannels: Optional[List[int]] = Field(None, description="Каналы чатов")
    sourceName: Optional[str] = Field(None, description="Источник")
    mediumName: Optional[str] = Field(None, description="Канал")
    campaignName: Optional[str] = Field(None, description="Кампания")
    keywordName: Optional[str] = Field(None, description="Ключевое слово")
    adContentName: Optional[str] = Field(None, description="Содержание кампании")
    tags: Optional[List[str]] = Field(None, description="Теги")
    attachedTags: Optional[List[str]] = Field(
        None, description="Список прикреплённых тегов (или)"
    )
    countries: Optional[List[str]] = Field(None, description="Страны")
    abandonedCart: Optional[bool] = Field(None, description="")
    emailMarketingUnsubscribed: Optional[bool] = Field(
        None, description="`deprecated` Отписан от email рассылок"
    )
    mgCustomerId: Optional[str] = Field(
        None, description="Идентификатор клиента MessageGateway"
    )
    firstWebVisitFrom: Optional[date] = Field(None, description="Первое посещение (от)")
    firstWebVisitTo: Optional[date] = Field(None, description="Первое посещение (до)")
    lastWebVisitFrom: Optional[date] = Field(None, description="Последнее посещение (от)")
    lastWebVisitTo: Optional[date] = Field(None, description="Последнее посещение (до)")

    customFields_validator = field_validator("customFields", mode="before")(
        dict_validator()
    )


class ResponseCustomersFilter(RetailCrmResponse):
    customers: list[Customer] = Field(default_factory=list, description="Клиенты")


class CustomerContragent(BaseRetailCrmScheme):
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


class SerializedCustomer(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    isContact: Optional[bool] = Field(
        None,
        description="Клиент является контактным лицом (создан как контактное лицо и на него нет оформленных заказов)",
    )
    createdAt: Optional[datetime] = Field(None, description="Создан")
    vip: Optional[bool] = Field(None, description="Важный клиент")
    bad: Optional[bool] = Field(None, description="Плохой клиент")
    contragent: Optional[CustomerContragent] = Field(
        None,
        description="`deprecated` Реквизиты (Поля объекта следует использовать только при неактивированной функциональности \"Корпоративные клиенты\")",
    )
    customFields: Optional[dict] = Field(
        None, description="Ассоциативный массив пользовательских полей"
    )
    personalDiscount: Optional[float] = Field(None, description="Персональная скидка")
    discountCardNumber: Optional[str] = Field(None, description="Номер дисконтной карты")
    address: Optional[CustomerAddress] = Field(None, description="Адрес клиента")
    firstName: Optional[str] = Field(None, description="Имя")
    lastName: Optional[str] = Field(None, description="Фамилия")
    patronymic: Optional[str] = Field(None, description="Отчество")
    email: Optional[str] = Field(None, description="E-mail")
    emailMarketingUnsubscribedAt: Optional[datetime] = Field(
        None, description="`deprecated` Дата отписки от email рассылок"
    )
    phones: Optional[List[CustomerPhone]] = Field(None, description="Телефоны")
    birthday: Optional[date] = Field(None, description="День рождения")
    photoUrl: Optional[str] = Field(None, description="URL фотографии")
    managerId: Optional[int] = Field(None, description="Менеджер клиента")
    sex: Optional[str] = Field(None, description="Пол")
    source: Optional[SerializedSource] = Field(None, description="Источник клиента")
    mgCustomerId: Optional[MGCustomer] = Field(
        None, description="Идентификатор клиента MessageGateway"
    )
    subscribed: Optional[bool] = Field(
        None, description="Статус подписки на маркетинговые рассылки писем"
    )
    tags: Optional[List[str]] = Field(None, description="Теги")
    attachedTag: Optional[str] = Field(None, description="Прикреплённый тег")
    browserId: Optional[str] = Field(None, description="Идентификатор устройства в Collector")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )

    customFields_validator = field_validator("customFields", mode="before")(
        dict_validator()
    )


class ResponseCustomerCreate(RetailCrmResponse):
    id: Optional[int] = Field(None, description="Внутренний ID созданного клиента")
