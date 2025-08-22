import decimal
from datetime import datetime
from typing import Any, Literal, Optional

from pydantic import Field, field_serializer, field_validator

from retailcrm.v5.helpers import datetime_serializer, dict_validator
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.shared.customer_phone import CustomerPhone
from retailcrm.v5.schemas.shared.history_api_key import HistoryApiKey
from retailcrm.v5.schemas.shared.history_user import HistoryUser
from retailcrm.v5.schemas.shared.source import SerializedSource


class MGChannel(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID канала")
    externalId: Optional[int] = Field(None, description="Внешний ID канала")
    allowedSendByPhone: Optional[bool] = Field(
        None, description="Можно ли писать первыми в этот канал по номеру телефона"
    )
    type: Optional[str] = Field(None, description="Тип канала")
    active: Optional[bool] = Field(False, description="Активность канала")
    name: Optional[str] = Field(None, description="Название канала")


class MGCustomer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID клиента")
    externalId: Optional[int] = Field(
        None, description="Внешний ID MessageGateway клиента"
    )
    mgChannel: Optional[MGChannel] = Field(None, description="MessageGateway канал")


class CustomerTagLink(BaseRetailCrmScheme):
    name: Optional[str] = Field(None)
    colorCode: Optional[str] = Field(None)
    attached: Optional[bool] = Field(None)


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


class EntityWithExternalIdNameOutput(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID")
    externalId: Optional[str] = Field(None, description="Внешний ID")
    name: Optional[str] = Field(None, description="Название")


class Customer(BaseRetailCrmScheme):
    type: Optional[str] = Field(None, description="Тип клиента")
    id: Optional[int] = Field(None, description="ID клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    isContact: Optional[bool] = Field(
        None,
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
        None,
        description="Средняя валовая прибыль по заказам клиента (в базовой валюте)",
    )
    marginSumm: Optional[decimal.Decimal] = Field(
        None, description="LTV (в базовой валюте)"
    )
    totalSumm: Optional[decimal.Decimal] = Field(
        None, description="Общая сумма заказов (в базовой валюте)"
    )
    averageSumm: Optional[decimal.Decimal] = Field(
        None, description="Средняя сумма заказа (в базовой валюте)"
    )
    ordersCount: int = Field(None, description="Количество заказов")
    costSumm: Optional[decimal.Decimal] = Field(
        None, description="Сумма расходов (в базовой валюте)"
    )
    address: Optional[CustomerAddress] = Field(None, description="Адрес клиента")
    maturationTime: Optional[int] = Field(
        None, description="Время «созревания», в секундах"
    )
    firstName: str = Field("", description="Имя")  # todo: remove default
    lastName: str = Field("", description="Фамилия")
    patronymic: str = Field("", description="Отчество")
    sex: str = Field("", description="Пол, возможные значения: male, female")
    presumableSex: Optional[str] = Field(
        None, description="Предполагаемый пол на основе ФИО"
    )
    email: str = Field(None, description="Адрес электронной почты")
    phones: list[CustomerPhone] = Field(default_factory=list, description="Телефоны")
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
    mainCompany: EntityWithExternalIdNameOutput | None = Field(
        None, description="Основная компания"
    )
    phone: str | None = Field(None, description="Номер телефона")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )

    customFields_validator = field_validator("customFields", mode="before")(
        dict_validator()
    )


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


class Segment(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID сегмента")
    code: Optional[str] = Field(None, description="Символьный код")
    name: Optional[str] = Field(None, description="Название сегмента")
    createdAt: Optional[datetime] = Field(None, description="Дата создания сегмента")
    isDynamic: Optional[bool] = Field(
        None, description="Является ли сегмент автоматически пересчитываемым"
    )
    customersCount: Optional[int] = Field(
        None, description="Количество клиентов в сегменте"
    )
    active: Optional[bool] = Field(None, description="Активность сегмента")


class Subscription(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID категории подписки")
    channel: Optional[str] = Field(None, description="Канал")
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    active: Optional[bool] = Field(None, description="Статус активности")
    autoSubscribe: Optional[bool] = Field(
        None, description="Автоматически подписывать новых клиентов"
    )
    ordering: Optional[int] = Field(None)


class CustomerSubscription(BaseRetailCrmScheme):
    subscription: Optional[Subscription] = Field(None, description="Категория подписки")
    subscribed: Optional[bool] = Field(None, description="Активность подписки")
    changedAt: Optional[datetime] = Field(
        None, description="Дата изменения флага активности"
    )


class SerializedCustomerReference(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID клиента")


class SerializedEntityCustomer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    type: Optional[str] = Field(None, description="Тип клиента")
    site: Optional[str] = Field(None, description="Символьный код магазина")


class CustomerAddressWithIsMain(CustomerAddress):
    isMain: Optional[bool] = Field(None, description="Адрес клиента является основным")


class CustomerHistory(BaseRetailCrmScheme):
    id: Optional[int] = Field(
        None, description="Внутренний идентификатор записи в истории"
    )
    createdAt: Optional[datetime] = Field(None, description="Дата внесения изменения")
    created: Optional[bool] = Field(None, description="Признак создания сущности")
    deleted: Optional[bool] = Field(None, description="Признак удаления сущности")
    source: Optional[str] = Field(None, description="Источник изменения")
    user: Optional[HistoryUser] = Field(None, description="Пользователь")
    field: Optional[str] = Field(None, description="Имя изменившегося поля")
    oldValue: Optional[Any] = Field(None, description="Старое значение свойства")
    newValue: Optional[Any] = Field(None, description="Новое значение свойства")
    apiKey: Optional[HistoryApiKey] = Field(
        None,
        alias="apiKey",
        description="Информация о ключе api, использовавшемся для этого изменения",
    )
    customer: Optional[Customer] = Field(None, description="Клиент")
    address: Optional[CustomerAddressWithIsMain] = Field(
        None, description="Адрес клиента"
    )
    combinedTo: Optional[Customer] = Field(
        None,
        description="Информация о клиенте, который получился после объединения с текущим клиентом",
    )
    subscription: Optional[Subscription] = Field(None, description="Категория подписки")


class CustomerNote(BaseRetailCrmScheme):
    customer: Optional[SerializedEntityCustomer] = Field(None, description="Клиент")
    managerId: Optional[int] = Field(None, description="ID менеджера")
    id: Optional[int] = Field(None, description="ID заметки")
    text: Optional[str] = Field(None, description="Текст заметки")
    createdAt: Optional[datetime] = Field(None, description="Дата/время создания")


class EntityWithExternalId(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(None, description="Внешний ID (при наличии)")


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
        description="deprecated Реквизиты (Поля объекта следует использовать только при неактивированной функциональности 'Корпоративные клиенты')",
    )
    customFields: Optional[dict[str, Any]] = Field(
        None, description="Ассоциативный массив пользовательских полей"
    )
    personalDiscount: Optional[float] = Field(None, description="Персональная скидка")
    discountCardNumber: Optional[str] = Field(
        None, description="Номер дисконтной карты"
    )
    address: Optional[CustomerAddress] = Field(None, description="Адрес клиента")
    firstName: Optional[str] = Field(None, description="Имя")
    lastName: Optional[str] = Field(None, description="Фамилия")
    patronymic: Optional[str] = Field(None, description="Отчество")
    email: Optional[str] = Field(None, description="E-mail")
    emailMarketingUnsubscribedAt: Optional[datetime] = Field(
        None, description="deprecated Дата отписки от email рассылок"
    )
    phones: Optional[list[CustomerPhone]] = Field(None, description="Телефоны")
    birthday: Optional[datetime] = Field(None, description="День рождения")
    photoUrl: Optional[str] = Field(None, description="URL фотографии")
    managerId: Optional[int] = Field(None, description="Менеджер клиента")
    sex: Optional[str] = Field(None, description="Пол")
    source: Optional[SerializedSource] = Field(None, description="Источник клиента")
    mgCustomerId: Optional[MGCustomer] = Field(
        None, alias="mgCustomerId", description="Идентификатор клиента MessageGateway"
    )
    subscribed: Optional[bool] = Field(
        None, description="Статус подписки на маркетинговые рассылки писем"
    )
    tags: Optional[list[str]] = Field(None, description="Теги")
    attachedTag: Optional[str] = Field(None, description="Прикреплённый тег")
    browserId: Optional[str] = Field(
        None, description="Идентификатор устройства в Collector"
    )
    addTags: Optional[list[str]] = Field(None, description="Добавление тегов")
    removeTags: Optional[list[str]] = Field(None, description="Удаление тегов")


class SerializedCustomerNote(BaseRetailCrmScheme):
    managerId: Optional[int] = Field(None, description="Внутренний ID менеджера")
    text: str = Field(None, description="Текст заметки")
    customer: SerializedEntityCustomer = Field(None, description="Клиент")


class SerializedSubscription(BaseRetailCrmScheme):
    channel: Literal["email", "sms", "waba"] = Field(None, description="Канал подписки")
    subscription: Optional[str] = Field(None, description="Код категории подписки")
    active: bool = Field(None, description="Флаг подписки (подписан/отписан)")
    messageId: Optional[int] = Field(
        None, description="Идентификатор сообщения, с которым взаимодействовал клиент"
    )
