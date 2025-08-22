from datetime import datetime
from typing import Any, Optional

from pydantic import Field, field_validator, field_serializer

from retailcrm.v5.helpers import dict_validator, datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.customers import CustomerAddress, Subscription, CustomerTagLink
from retailcrm.v5.schemas.shared.history_api_key import HistoryApiKey
from retailcrm.v5.schemas.shared.history_user import HistoryUser


class EntityWithExternalIdNameOutput(BaseRetailCrmScheme):
    id: Optional[int] = Field(None)
    externalId: Optional[str] = Field(None)
    name: Optional[str] = Field(None)


class SerializedRelationAbstractCustomer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    browserId: Optional[str] = Field(None, description="Идентификатор устройства в Collector")
    site: Optional[str] = Field(None, description="Код магазина, необходим при передаче externalId")


class EntityWithExternalIdInput(BaseRetailCrmScheme):
    id: Optional[int] = Field(None)
    externalId: Optional[str] = Field(None)


class SerializedCustomerContactCompany(BaseRetailCrmScheme):
    company: Optional[EntityWithExternalIdInput] = Field(None, description="Компания")


class CustomerContactCompany(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID компании")
    company: Optional[EntityWithExternalIdNameOutput] = Field(None, description="	Компания")


class SerializedCustomerContact(BaseRetailCrmScheme):
    isMain: Optional[bool] = Field(None, description="Контактное лицо является основным для клиента")
    customer: Optional[SerializedRelationAbstractCustomer] = Field(None, description="Клиент")
    companies: Optional[list[SerializedCustomerContactCompany]] = Field(None, description="Компании контактного лица")


class SerializedCompanyContragent(BaseRetailCrmScheme):
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


class SerializedCompany(BaseRetailCrmScheme):
    isMain: Optional[bool] = Field(None, description="Компания является основной для клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID компании")
    active: Optional[bool] = Field(None, description="Активность")
    name: Optional[str] = Field(None, description="Наименование")
    brand: Optional[str] = Field(None, description="Бренд")
    site: Optional[str] = Field(None, description="Сайт компании")
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    contragent: Optional[SerializedCompanyContragent] = Field(None, description="Реквизиты")
    customFields: Optional[dict[str, Any]] = Field(None, description="Ассоциативный массив пользовательских полей")
    address: Optional[EntityWithExternalIdInput] = Field(None, description="Адрес")


class SerializedCustomerCorporate(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(None, description="Внешний ID корпоративного клиента")
    createdAt: Optional[datetime] = Field(None, description="Создан")
    vip: Optional[bool] = Field(None, description="Важный клиент")
    bad: Optional[bool] = Field(None, description="Плохой клиент")
    customFields: Optional[dict[str, Any]] = Field(None, description="Ассоциативный массив пользовательских полей")
    personalDiscount: Optional[float] = Field(None, description="Персональная скидка")
    discountCardNumber: Optional[str] = Field(None, description="Номер дисконтной карты")
    nickName: Optional[str] = Field(None, description="Наименование")
    managerId: Optional[int] = Field(None, description="Менеджер корпоративного клиента")
    customerContacts: Optional[list[SerializedCustomerContact]] = Field(None, alias="customerContacts", description="Контактные лица")
    companies: Optional[list[SerializedCompany]] = Field(None, description="Компании")
    addresses: Optional[list[CustomerAddress]] = Field(None, description="Адреса корпоративного клиента")


class CustomerContact(BaseRetailCrmScheme):
    isMain: Optional[bool] = Field(None)
    id: Optional[int] = Field(None)
    customer: Optional[SerializedRelationAbstractCustomer] = Field(None)
    companies: Optional[list[CustomerContactCompany]] = Field(None)


class CustomerCorporate(BaseRetailCrmScheme):
    type: Optional[str] = Field(None, description="Тип клиента")
    id: Optional[int] = Field(None, description="ID корпоративного клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID корпоративного клиента")
    mainAddress: Optional[EntityWithExternalIdNameOutput] = Field(None, description="Основной адрес корпоративного клиента")
    createdAt: Optional[datetime] = Field(None, description="Создан")
    managerId: Optional[int] = Field(None, description="Менеджер корпоративного клиента")
    vip: Optional[bool] = Field(None, description="Важный клиент")
    bad: Optional[bool] = Field(None, description="Плохой клиент")
    site: Optional[str] = Field(None, description="Магазин, с которого пришел клиент")
    tags: list[CustomerTagLink] = Field(default_factory=list)
    firstClientId: Optional[str] = Field(None, description="Первая метка клиента Google Analytics")
    lastClientId: Optional[str] = Field(None, description="Последняя метка клиента Google Analytics")
    customFields: Optional[dict[str, Any]] = Field(None, description="Ассоциативный массив пользовательских полей")
    personalDiscount: Optional[float] = Field(None, description="Персональная скидка")
    cumulativeDiscount: Optional[float] = Field(None, description="deprecated Накопительная скидка (Недоступно, начиная с 8 версии системы)")
    discountCardNumber: Optional[str] = Field(None, description="Номер дисконтной карты")
    avgMarginSumm: Optional[float] = Field(None, description="Средняя валовая прибыль по заказам корпоративного клиента (в базовой валюте)")
    marginSumm: Optional[float] = Field(None, description="LTV (в базовой валюте)")
    totalSumm: Optional[float] = Field(None, description="Общая сумма заказов (в базовой валюте)")
    averageSumm: Optional[float] = Field(None, description="Средняя сумма заказа (в базовой валюте)")
    ordersCount: Optional[int] = Field(None, description="Количество заказов")
    costSumm: Optional[float] = Field(None, description="Сумма расходов (в базовой валюте)")
    mainCustomerContact: Optional[CustomerContact] = Field(None, description="Основное контактное лицо")
    mainCompany: Optional[EntityWithExternalIdNameOutput] = Field(None, description="Основная компания")
    nickName: Optional[str] = Field(None, description="Наименование")



class SerializedCustomerAddress(BaseRetailCrmScheme):
    index: Optional[str] = Field(None, description="Индекс")
    countryIso: Optional[str] = Field(None, description="ISO код страны")
    region: Optional[str] = Field(None, description="Регион")
    regionId: Optional[int] = Field(None, description="Идентификатор региона в Geohelper")
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
    isMain: Optional[bool] = Field(None, description="Адрес является основным для клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID")
    name: Optional[str] = Field(None, description="Наменование адреса")




class CompanyContragent(BaseRetailCrmScheme):
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


class Company(BaseRetailCrmScheme):
    isMain: Optional[bool] = Field(None, description="Компания является основной для клиента")
    id: Optional[int] = Field(None, description="ID компании")
    externalId: Optional[str] = Field(None, description="Внешний ID компании")
    customer: Optional[SerializedRelationAbstractCustomer] = Field(None, description="Клиент")
    active: Optional[bool] = Field(None, description="Активность")
    name: Optional[str] = Field(None, description="Наименование")
    brand: Optional[str] = Field(None, description="Бренд")
    site: Optional[str] = Field(None, description="Сайт компании")
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    contragent: Optional[CompanyContragent] = Field(None, description="Реквизиты")
    address: Optional[CustomerAddress] = Field(None, description="Адрес")
    avgMarginSumm: Optional[float] = Field(None, description="Средняя валовая прибыль по заказам клиента (в базовой валюте)")
    marginSumm: Optional[float] = Field(None, description="LTV (в базовой валюте)")
    totalSumm: Optional[float] = Field(None, description="Общая сумма заказов (в базовой валюте)")
    averageSumm: Optional[float] = Field(None, description="Средняя сумма заказа (в базовой валюте)")
    costSumm: Optional[float] = Field(None, description="Сумма расходов (в базовой валюте)")
    ordersCount: Optional[int] = Field(None, description="Количество заказов")
    customFields: Optional[dict[str, Any]] = Field(None, description="Ассоциативный массив пользовательских полей")

    customFields_validator = field_validator("customFields", mode="before")(
        dict_validator()
    )
    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class CustomerAddressWithIsMain(CustomerAddress):
    isMain: Optional[bool] = Field(None, description="Адрес является основным для клиента")


class CustomerCorporateHistory(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний идентификатор записи в истории")
    createdAt: Optional[datetime] = Field(None, description="Дата внесения изменения")
    created: Optional[bool] = Field(None, description="Признак создания сущности")
    deleted: Optional[bool] = Field(None, description="Признак удаления сущности")
    source: Optional[str] = Field(None, description="Источник изменения")
    user: Optional[HistoryUser] = Field(None, description="Пользователь")
    field: Optional[str] = Field(None, description="Имя изменившегося поля")
    oldValue: Optional[Any] = Field(None, description="Старое значение свойства")
    newValue: Optional[Any] = Field(None, description="Новое значение свойства")
    apiKey: Optional[HistoryApiKey] = Field(None, description="Информация о ключе api, использовавшемся для этого изменения")
    customer: Optional[CustomerCorporate] = Field(None, description="Корпоративный клиент")
    address: Optional[CustomerAddressWithIsMain] = Field(None, description="Адрес клиента")
    combinedTo: Optional[CustomerCorporate] = Field(None, description="Информация о клиенте, который получился после объединения с текущим клиентом")
    subscription: Optional[Subscription] = Field(None, description="Категория подписки")
    customerContact: Optional[CustomerContact] = Field(None, alias="customerContact", description="Контактное лицо")
    company: Optional[Company] = Field(None, description="Компания")

