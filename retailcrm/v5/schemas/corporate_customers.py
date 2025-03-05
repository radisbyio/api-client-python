from datetime import datetime
from typing import Optional, Union

from pydantic import Field, field_serializer, field_validator

from retailcrm.v5.helpers import datetime_serializer, dict_validator
from retailcrm.v5.schemas.base import BaseRetailCrmScheme, RetailCrmResponse
from retailcrm.v5.schemas.customers import CustomerAddress, CustomerContragent
from retailcrm.v5.schemas.shared import ApiKey, User, CustomerTagLink, Customer, SerializedEntityCustomer, \
    EntityWithExternalIdNameOutput, EntityWithExternalIdInput


class Subscription(BaseRetailCrmScheme):
    id: int
    channel: str = Field(...)
    name: str = Field(...)
    code: str = Field(...)
    active: bool = Field(False)
    autoSubscribe: bool = Field(False)
    ordering: int = Field(...)


class CustomerSubscription(BaseRetailCrmScheme):
    subscription: Subscription
    subscribed: bool = Field(False)
    changedAt: Optional[datetime] = None


class CustomerCorporateApiFilterData(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID клиентов")
    externalIds: Optional[list[str]] = Field(None, description="Массив externalID клиентов")
    name: Optional[str] = Field(None, description="Клиент")
    city: Optional[str] = Field(None, description="Город")
    region: Optional[str] = Field(None, description="Регион")
    sites: Optional[list[str]] = Field(None, description="Магазины")
    managers: Optional[list[int]] = Field(None, description="Менеджеры")
    managerGroups: Optional[list[str]] = Field(None, description="Группы менеджеров")
    notes: Optional[str] = Field(None, description="Заметки")
    vip: Optional[bool] = Field(None, description="Важный клиент")
    bad: Optional[bool] = Field(None, description="Плохой клиент")
    discountCardNumber: Optional[str] = Field(None, description="Номер дисконтной карты")
    attachments: Optional[int] = Field(None, description="Прикрепленные объекты (вложения)")
    tasksCounts: Optional[int] = Field(None, description="Задачи")
    email: Optional[str] = Field(None, description="E-mail")
    contragentName: Optional[str] = Field(None, description="Полное наименование")
    contragentTypes: Optional[list[str]] = Field(None, description="Типы контрагента")
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
    minCostSumm: Optional[int] = Field(None, description="Сумма расходов по заказам (от)")
    maxCostSumm: Optional[int] = Field(None, description="Сумма расходов по заказам (до)")
    dateFrom: Optional[datetime] = Field(None, description="Дата регистрации (от)")
    dateTo: Optional[datetime] = Field(None, description="Дата регистрации (до)")
    firstOrderFrom: Optional[datetime] = Field(None, description="Первый заказ (от)")
    firstOrderTo: Optional[datetime] = Field(None, description="Первый заказ (до)")
    lastOrderFrom: Optional[datetime] = Field(None, description="Последний заказ (от)")
    lastOrderTo: Optional[datetime] = Field(None, description="Последний заказ (до)")
    customFields: Optional[dict] = Field(None, description="Пользовательские поля")
    nickName: Optional[list[str]] = Field(None, description="Наименование")
    contactName: Optional[str] = Field(None, description="ФИО или телефон")
    addressName: Optional[str] = Field(None, description="Название адреса")
    phone: Optional[str] = Field(None, description="Телефон")
    companyCustomFields: Optional[dict] = Field(None, description="Пользовательские поля компании")  # Assuming dict
    contactIds: Optional[list[int]] = Field(None, description="Массив ID контактных лиц")
    companyName: Optional[str] = Field(None, description="Название компании")

    dateFrom_serializer = field_serializer("dateFrom")(datetime_serializer("%Y-%m-%d"))
    dateTo_serializer = field_serializer("dateTo")(datetime_serializer("%Y-%m-%d"))
    firstOrderFrom_serializer = field_serializer("firstOrderFrom")(datetime_serializer("%Y-%m-%d"))
    firstOrderTo_serializer = field_serializer("firstOrderTo")(datetime_serializer("%Y-%m-%d"))
    lastOrderFrom_serializer = field_serializer("lastOrderFrom")(datetime_serializer("%Y-%m-%d"))
    lastOrderTo_serializer = field_serializer("lastOrderTo")(datetime_serializer("%Y-%m-%d"))

    customFields_validator = field_validator("customFields", mode="before")(dict_validator())
    companyCustomFields_validator = field_validator("companyCustomFields", mode="before")(dict_validator())


class SerializedRelationAbstractCustomer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    browserId: Optional[str] = Field(None, description="Идентификатор устройства в Collector")
    site: Optional[str] = Field(None, description="Код магазина, необходим при передаче externalId")


class CustomerContact(BaseRetailCrmScheme):
    id: int = Field(description="ID контакта")
    customer: SerializedRelationAbstractCustomer = Field(description="Клиент")
    companies: Optional[list["CustomerContactCompany"]] = Field(None, description="Компании контактного лица")


class CustomerCorporate(BaseRetailCrmScheme):
    type: str = Field(description="Тип клиента")
    id: int = Field(description="ID корпоративного клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID")
    nickName: Optional[str] = Field(None, description="Наименование")
    mainAddress: Optional[EntityWithExternalIdNameOutput] = Field(None, description="Основной адрес")
    createdAt: Optional[datetime] = Field(None, description="Создан")
    managerId: Optional[int] = Field(None, description="Менеджер")
    vip: Optional[bool] = Field(None, description="Важный клиент")
    bad: Optional[bool] = Field(None, description="Плохой клиент")
    site: Optional[str] = Field(None, description="Магазин")
    tags: list[CustomerTagLink] = Field([], description="Теги")

    firstClientId: Optional[str] = Field(None, description="Первая метка клиента Google Analytics")
    lastClientId: Optional[str] = Field(None, description="Последняя метка клиента Google Analytics")

    customFields: dict = Field(default_factory=dict, description="Пользовательские поля")
    personalDiscount: Optional[float] = Field(None, description="Персональная скидка")
    cumulativeDiscount: Optional[float] = Field(None, description="Накопительная скидка")
    discountCardNumber: Optional[str] = Field(None, description="Номер дисконтной карты")

    avgMarginSumm: Optional[float] = Field(None, description="Средняя маржа")
    marginSumm: Optional[float] = Field(None, description="LTV")
    totalSumm: Optional[float] = Field(None, description="Выручка")
    averageSumm: Optional[float] = Field(None, description="Средний чек")

    ordersCount: Optional[int] = Field(None, description="Количество заказов")
    costSumm: Optional[float] = Field(None, description="Сумма расходов")

    mainCustomerContact: Optional[CustomerContact] = Field(None, description="Основной контакт")
    mainCompany: Optional[EntityWithExternalIdNameOutput] = Field(None, description="Основная компания")
    createdAt_serializer = field_serializer("createdAt")(datetime_serializer("%Y-%m-%d %H:%M:%S"))
    customFields_validator = field_validator("customFields", mode="before")(dict_validator())


class SerializedCustomerContactCompany(BaseRetailCrmScheme):
    company: EntityWithExternalIdInput = Field(description="Компания")


class SerializedCustomerContact(BaseRetailCrmScheme):
    isMain: bool = Field(False, description="Основной контакт")
    customer: SerializedRelationAbstractCustomer = Field(description="Клиент")
    companies: Optional[list[SerializedCustomerContactCompany]] = Field(None, description="Компании контактного лица")


class SerializedCompanyContragent(CustomerContragent):
    # Inherits all fields from CustomerContragent
    pass


class SerializedCompany(BaseRetailCrmScheme):
    isMain: bool = Field(False, description="Основная компания")
    externalId: Optional[str] = Field(None, description="Внешний ID компании")
    active: Optional[bool] = Field(None, description="Активность")
    name: Optional[str] = Field(None, description="Наименование")
    brand: Optional[str] = Field(None, description="Бренд")
    site: Optional[str] = Field(None, description="Сайт компании")
    createdAt: Optional[datetime] = Field(None, description="Дата создания")

    contragent: Optional[SerializedCompanyContragent] = Field(None, description="Реквизиты")
    customFields: Optional[dict] = Field(None, description="Ассоциативный массив пользовательских полей")
    address: Optional[CustomerAddress] = Field(None, description="Адрес")

    createdAt_serializer = field_serializer("createdAt")(datetime_serializer("%Y-%m-%d %H:%M:%S"))

    customFields_validator = field_validator("customFields", mode="before")(dict_validator())


class SerializedRelationAbstractCustomerWithGa(SerializedRelationAbstractCustomer):
    gaClientId: Optional[str] = Field(None, description="Метка клиента Google Analytics")


class SerializedRelationOffer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID торгового предложения")
    externalId: Optional[str] = Field(None, description="Внешний ID торгового предложения")
    xmlId: Optional[str] = Field(None, description="ID торгового предложения в складской системе")


class SerializedCartItem(BaseRetailCrmScheme):
    quantity: float = Field(description="Количество")
    price: float = Field(description="Цена (в валюте объекта)")
    offer: SerializedRelationOffer = Field(description="Торговое предложение")


class SerializedRelationOrder(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID заказа")
    externalId: Optional[str] = Field(None, description="Внешний ID заказа")
    number: Optional[str] = Field(None, description="Номер заказа")


class SerializedCart(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(None, description="Внешний ID корзины")
    droppedAt: Optional[datetime] = Field(None, description="Дата/время, когда корзина стала брошенной")
    clearedAt: Optional[datetime] = Field(None, description="Дата/время очистки корзины", )
    customer: SerializedRelationAbstractCustomerWithGa = Field(description="Клиент")
    items: list[SerializedCartItem] = Field([], description="Товары в корзине")
    order: Optional[SerializedRelationOrder] = Field(None, description="Заказ, созданный из корзины")
    link: Optional[str] = Field(None, description="Ссылка")

    droppedAt_serializer = field_serializer("droppedAt")(datetime_serializer("%Y-%m-%d %H:%M:%S"))

    clearedAt_serializer = field_serializer("clearedAt")(datetime_serializer("%Y-%m-%d %H:%M:%S"))


class CustomerContactCompany(BaseRetailCrmScheme):
    id: int = Field(description="ID компании")
    company: EntityWithExternalIdNameOutput = Field(description="Компания")


class ResponseCustomersCorporateGetAll(RetailCrmResponse):
    customersCorporate: list[CustomerCorporate] = Field(default_factory=list, description="Корпоративные клиенты")


class SerializedCustomerCorporate(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(None, description="Внешний ID")

    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    managerId: Optional[int] = Field(None, description="ID менеджера")

    vip: Optional[bool] = Field(None, description="Важный клиент")
    bad: Optional[bool] = Field(None, description="Плохой клиент")

    customFields: Optional[dict] = Field(default_factory=dict, description="Пользовательские поля")
    personalDiscount: Optional[float] = Field(None, description="Персональная скидка")
    discountCardNumber: Optional[str] = Field(None, description="Номер карты")
    nickName: Optional[str] = Field(None, description="Наименование")
    customerContacts: Optional[list[SerializedCustomerContact]] = Field(None, description="Контактные лица")
    companies: Optional[list[SerializedCompany]] = Field(None, description="Компании")
    addresses: Optional[list[CustomerAddress]] = Field(None, description="Адреса")
    createdAt_serializer = field_serializer("createdAt")(datetime_serializer("%Y-%m-%d %H:%M:%S"))
    customFields_validator = field_validator("customFields", mode="before")(dict_validator())


class ResponseCustomerCorporateCreate(RetailCrmResponse):
    id: Optional[int] = Field(None, description="ID корпоративного клиента")


class CustomerCorporateWithCompanyLinksOutput(BaseRetailCrmScheme):
    id: int = Field(description="ID")
    isMain: bool = Field(description="Основная")


class CustomerWithContragentOutput(BaseRetailCrmScheme):
    id: int = Field(description="ID")

    externalId: Optional[str] = Field(None, description="Внешний ID")

    contragent: Optional[CustomerContragent] = Field(None, description="Контрагент")
    customFields: dict = Field(default_factory=dict, description="Пользовательские поля")

    personalDiscount: Optional[float] = Field(None, description="Персональная скидка")
    cumulativeDiscount: Optional[float] = Field(None, description="Накопительная скидка")

    marginSumm: Optional[float] = Field(None, description="LTV")
    totalSumm: Optional[float] = Field(None, description="Выручка")
    averageSumm: Optional[float] = Field(None, description="Средний чек")

    ordersCount: Optional[int] = Field(None, description="Количество заказов")
    costSumm: Optional[float] = Field(None, description="Сумма расходов")

    customFields_validator = field_validator("customFields", mode="before")(dict_validator())


class CustomerContactOutput(BaseRetailCrmScheme):
    id: int = Field(description="ID")
    isMain: Optional[bool] = Field(None, description="Основной контакт")
    customer: Optional[CustomerWithContragentOutput] = Field(None, description="Клиент")


class CustomerCorporateOutput(BaseRetailCrmScheme):
    id: int = Field(description="ID")
    nickName: str = Field("", description="Наименование")


class CompanyOutput(BaseRetailCrmScheme):
    id: int = Field(description="ID")

    externalId: Optional[str] = Field(None, description="Внешний ID")
    active: bool = Field(False, description="Активность")
    name: str = Field("", description="Наименование")

    brand: Optional[str] = Field(None, description="Бренд")
    site: Optional[str] = Field(None, description="Сайт компании")

    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    contragent: Optional[CustomerContragent] = Field(None, description="Контрагент")
    address: Optional[CustomerAddress] = Field(None, description="Адрес")
    avgMarginSumm: Optional[float] = Field(None, description="Средняя маржа")
    marginSumm: Optional[float] = Field(None, description="LTV")
    totalSumm: Optional[float] = Field(None, description="Выручка")
    averageSumm: Optional[float] = Field(None, description="Средний чек")

    ordersCount: Optional[int] = Field(None, description="Количество заказов")
    costSumm: Optional[float] = Field(None, description="Сумма расходов")

    customFields: dict = Field(default_factory=dict, description="Пользовательские поля")

    createdAt_serializer = field_serializer("createdAt")(datetime_serializer("%Y-%m-%d %H:%M:%S"))
    customFields_validator = field_validator("customFields", mode="before")(dict_validator())


class FixExternalRow(BaseRetailCrmScheme):
    id: int = Field(description="ID")
    externalId: str = Field(description="Внешний ID")


class EntityWithExternalId(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(None, description="Внешний ID")


class CustomerHistory(BaseRetailCrmScheme):
    id: int = Field(description="ID")
    createdAt: datetime = Field(description="Дата создания")
    created: Optional[bool] = Field(None, description="Создан")
    deleted: Optional[bool] = Field(None, description="Удален")
    source: Optional[str] = Field(None, description="Источник")
    user: Optional[User] = Field(None, description="Пользователь")
    field: Optional[str] = Field(None, description="Поле")
    oldValue: Optional[Union[str, int, float, dict, list]] = Field(None, description="Старое значение")
    newValue: Optional[Union[str, int, float, dict, list]] = Field(None, description="Новое значение")
    apiKey: Optional[ApiKey] = Field(None, description="Ключ API")
    customer: Optional[Customer] = Field(None, description="Клиент")
    address: Optional[CustomerAddress] = Field(None, description="Адрес")
    combinedTo: Optional[Customer] = Field(None, description="Объединен с")
    subscription: Optional[Subscription] = Field(None, description="Подписка")  # Requires forward reference


class CustomerHistoryFilterV4Type(BaseRetailCrmScheme):
    customerId: Optional[int] = Field(None, description="ID клиента")
    sinceId: Optional[int] = Field(None, description="ID истории (от)")
    customerExternalId: Optional[str] = Field(None, description="Внешний ID клиента")
    startDate: Optional[datetime] = Field(None, description="Дата начала")
    endDate: Optional[datetime] = Field(None, description="Дата окончания")


class CustomerAddressWithIsMain(CustomerAddress):
    isMain: bool = Field(False, description="Основной")


class CustomerNote(BaseRetailCrmScheme):
    id: int = Field(...)
    text: str = Field(...)
    createdAt: datetime = Field(...)
    managerId: Optional[int] = None
    customer: SerializedEntityCustomer = None


class CustomerCorporateHistory(BaseRetailCrmScheme):
    id: int = Field(description="ID")
    createdAt: datetime = Field(description="Дата создания")
    created: Optional[bool] = Field(None, description="Создан")
    deleted: Optional[bool] = Field(None, description="Удален")
    source: Optional[str] = Field(None, description="Источник")
    user: Optional[User] = Field(None, description="Пользователь")
    field: Optional[str] = Field(None, description="Поле")
    oldValue: Optional[Union[str, int, float, dict, list]] = Field(None, description="Старое значение")
    newValue: Optional[Union[str, int, float, dict, list]] = Field(None, description="Новое значение")
    apiKey: Optional[ApiKey] = Field(None, description="Ключ API")
    customer: Optional[CustomerCorporate] = Field(None, description="Клиент")
    address: Optional[CustomerAddressWithIsMain] = Field(None, description="Адрес")
    combinedTo: Optional[CustomerCorporate] = Field(None, description="Объединен с")
    subscription: Optional[Subscription] = Field(None, description="Подписка")
    customerContact: Optional[CustomerContactOutput] = Field(None, description="Контактное лицо")
    company: Optional[CompanyOutput] = Field(None, description="Компания")


class GetByIdCustomerCorporateResponse(RetailCrmResponse):
    customerCorporate: Optional[CustomerCorporate] = Field(None, description="Корпоративный клиент")


class ResponseCustomerCorporateEdit(RetailCrmResponse):
    id: Optional[int] = Field(None, description="ID корпоративного клиента")
