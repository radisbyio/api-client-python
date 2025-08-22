from datetime import datetime
from typing import Optional, Any, Literal

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.delivery import StatusInfo
from retailcrm.v5.schemas.entities.orders import Unit, TimeInterval




class Tariff(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код тарифа")
    name: Optional[str] = Field(None, description="Название тарифа")
    description: Optional[str] = Field(None, description="Описание тарифа")
    type: Optional[Literal["courier", "selfDelivery"]] = Field(None, description="Тип тарифа (Возможные значения: courier - курьерская доставка, selfDelivery - самовывоз)")

class ResponseAutocompleteItem(BaseRetailCrmScheme):
    value: Optional[str] = Field(None, description="Значение")
    label: Optional[str] = Field(None, description="Наименование")
    description: Optional[str] = Field(None, description="Не обязательное поле. Подсказка для опции - выводится мелким шрифтом под именем опции")


class RequestShipmentDelete(BaseRetailCrmScheme):
    shipmentId: Optional[str] = Field(None, description="Идентификатор отгрузки в службе доставки")
    extraData: dict[str, Any] = Field(default_factory=dict, description="Дополнительные данные отгрузки (shipmentDataField.code => значение)")


class ResponseShipmentSave(BaseRetailCrmScheme):
    shipmentId: Optional[str] = Field(None, description="Идентификатор отгрузки в службе доставки")
    extraData: dict[str, Any] = Field(default_factory=dict, description="Дополнительные данные отгрузки")

class DeliveryAddress(BaseRetailCrmScheme):
    index: Optional[str] = Field(None, description="Индекс")
    countryIso: Optional[str] = Field(None, description="ISO код страны (ISO 3166-1 alpha-2)")
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
    terminal: Optional[str] = Field(None, description="Код терминала отгрузки/доставки")


class Store(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код")
    name: Optional[str] = Field(None, description="Название")


class PackageItem(BaseRetailCrmScheme):
    offerId: Optional[str] = Field(None, description="Идентификатор оффера в системе")
    externalId: Optional[str] = Field(None, description="Идентификатор торгового предложения в магазине")
    xmlId: Optional[str] = Field(None, description="Идентификатор торгового предложения в складской системе")
    name: Optional[str] = Field(None, description="Наименование товара")
    declaredValue: Optional[float] = Field(None, description="Объявленная стоимость за единицу товара")
    cod: Optional[float] = Field(None, description="Наложенный платеж за единицу товара")
    vatRate: Optional[str] = Field(None, description="Ставка НДС ('none' - НДС не облагается)")
    quantity: Optional[float] = Field(None, description="Количество товара в упаковке")
    unit: Optional[Unit] = Field(None, description="Единица измерения товара")
    cost: Optional[float] = Field(None, description="Стоимость товара (с учетом скидок)")
    markingCodes: list[str] = Field(default_factory=list, description="Коды маркировки (формат кода маркировки)")
    properties: list[list[str]] = Field(default_factory=list, description="Свойства товара")
    weight: Optional[float] = Field(None, description="Вес товара (может быть null для услуг)")


class Package(BaseRetailCrmScheme):
    packageId: Optional[str] = Field(None, description="Идентификатор упаковки")
    weight: Optional[float] = Field(None, description="Вес г.")
    width: Optional[int] = Field(None, description="Ширина мм.")
    length: Optional[int] = Field(None, description="Длина мм.")
    height: Optional[int] = Field(None, description="Высота мм.")
    items: list[PackageItem] = Field(default_factory=list, description="Содержимое упаковки")


class ExtraDataValue(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код поля")
    value: Optional[str] = Field(None, description="Значение поля")


class RequestCalculate(BaseRetailCrmScheme):
    shipmentAddress: Optional[DeliveryAddress] = Field(None, description="Адрес отгрузки")
    store: Optional[Store] = Field(None, description="Склад отгрузки")
    deliveryAddress: Optional[DeliveryAddress] = Field(None, description="Адрес доставки")
    packages: list[Package] = Field(default_factory=list, description="Набор упаковок")
    declaredValue: Optional[float] = Field(None, description="Объявленная стоимость")
    cod: Optional[float] = Field(None, description="Сумма наложенного платежа по заказу")
    payerType: Optional[str] = Field(None, description="Плательщик за доставку (receiver или sender)")
    shipmentDate: Optional[datetime] = Field(None, description="Дата отгрузки")
    deliveryDate: Optional[datetime] = Field(None, description="Дата доставки")
    deliveryTime: Optional[TimeInterval] = Field(None, description="Время доставки")
    currency: Optional[str] = Field(None, description="Код валюты")
    extraData: list[ExtraDataValue] = Field(default_factory=list, description="Дополнительные данные доставки (deliveryDataField.code => значение)")


class Coordinates(BaseRetailCrmScheme):
    latitude: Optional[str] = Field(None, description="Широта")
    longitude: Optional[str] = Field(None, description="Долгота")


class Terminal(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код терминала")
    cost: Optional[float] = Field(None, description="Стоимость доставки до терминала (указывается в случае если она отличается от стандартной стоимости по тарифу)")
    name: Optional[str] = Field(None, description="Наименование терминала")
    description: Optional[str] = Field(None, description="Описание терминала")
    address: Optional[str] = Field(None, description="Адрес")
    schedule: Optional[str] = Field(None, description="Режим работы")
    phone: Optional[str] = Field(None, description="Телефон")
    extraData: Optional[dict[str, Any]] = Field(None, description="Дополнительные данные (deliveryDataField.code => значение)")
    coordinates: Optional[Coordinates] = Field(None, description="Координаты")


class ResponseCalculate(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код тарифа")
    group: Optional[str] = Field(None, description="Группа тарифов")
    name: Optional[str] = Field(None, description="Наименование тарифа")
    type: Optional[str] = Field(None, description="Тип тарифа (courier - курьерская доставка или selfDelivery - самовывоз)")
    description: Optional[str] = Field(None, description="Описание")
    cost: Optional[float] = Field(None, description="Стоимость доставки (Если не передана, то тариф будет выводиться, но не будет доступен для выбора) (в валюте объекта)")
    minTerm: Optional[int] = Field(None, description="Минимальный срок доставки")
    maxTerm: Optional[int] = Field(None, description="Максимальный срок доставки")
    extraData: Optional[dict[str, Any]] = Field(None, description="Дополнительные данные доставки (deliveryDataField.code => значение)")
    extraDataAvailable: Optional[list[str]] = Field(None, description="Массив кодов полей, которые должны отображаться в карточке заказа. Если не передан будут отображаться все поля с дополнительными данными доставки.")
    pickuppointList: list[Terminal] = Field(default_factory=list, description="Терминал отгрузки/получения")


class RequestDelete(BaseRetailCrmScheme):
    deliveryId: Optional[str] = Field(None, description="Идентификатор доставки в службе доставки")


class ResponseLoadDeliveryData(BaseRetailCrmScheme):
    trackNumber: Optional[str] = Field(None, description="Трек номер (если установлена опция configuration[allowTrackNumber])")
    cost: Optional[float] = Field(None, description="Стоимость доставки")
    shipmentDate: Optional[datetime] = Field(None, description="Дата отгрузки")
    deliveryDate: Optional[datetime] = Field(None, description="Дата доставки")
    deliveryTime: Optional[TimeInterval] = Field(None, description="Время доставки")
    tariff: Optional[str] = Field(None, description="Код тарифа")
    tariffName: Optional[str] = Field(None, description="Наименование тарифа")
    payerType: Optional[str] = Field(None, description="Плательщик за доставку (receiver или sender)")
    status: Optional[StatusInfo] = Field(None, description="Статус доставки")
    extraData: Optional[dict[str, Any]] = Field(None, description="Дополнительные данные доставки (deliveryDataField.code => значение)")
    shipmentAddress: Optional[DeliveryAddress] = Field(None, description="Адрес отгрузки")
    deliveryAddress: Optional[DeliveryAddress] = Field(None, description="Адрес доставки")


class RequestPrint(BaseRetailCrmScheme):
    entityType: Optional[str] = Field(None, description="Тип сущности для печатной формы (order - печатная форма для заказа (по умолчанию), shipment - печатная форма для отгрузки. Значение совпадает со значением integrationModule[integrations][delivery][plateList][][type] выбранной печатной формы)")
    type: Optional[str] = Field(None, description="Код типа печатной формы")
    deliveryIds: list[list[str]] = Field(default_factory=list, description="Массив идентификаторов доставок в службе доставки ([['56376', '798645']])")


class Point(BaseRetailCrmScheme):
    latitude: Optional[float] = Field(None, description="Широта")
    longitude: Optional[float] = Field(None, description="Долгота")


class StoreAddress(BaseRetailCrmScheme):
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
    coordinates: Optional[Point] = Field(None, description="Координаты точки")


class StoreWorkTime(BaseRetailCrmScheme):
    startTime: Optional[str] = Field(None, description="Время начала работы склада (в формате H:i)")
    endTime: Optional[str] = Field(None, description="Время окончания работы склада (в формате H:i)")
    lunchStartTime: Optional[str] = Field(None, description="Время начала перерыва (в формате H:i)")
    lunchEndTime: Optional[str] = Field(None, description="Время окончания перерыва (в формате H:i)")


class SerializedStoreWeekOpeningHours(BaseRetailCrmScheme):
    mo: list[StoreWorkTime] = Field(default_factory=list, description="Время работы склада в понедельник")
    tu: list[StoreWorkTime] = Field(default_factory=list, description="Время работы склада во вторник")
    we: list[StoreWorkTime] = Field(default_factory=list, description="Время работы склада в среду")
    th: list[StoreWorkTime] = Field(default_factory=list, description="Время работы склада в четверг")
    fr: list[StoreWorkTime] = Field(default_factory=list, description="Время работы склада в пятницу")
    sa: list[StoreWorkTime] = Field(default_factory=list, description="Время работы склада в субботу")
    su: list[StoreWorkTime] = Field(default_factory=list, description="Время работы склада в воскресенье")


class Contragent(BaseRetailCrmScheme):
    type: Optional[str] = Field(None, description="Тип контрагента")
    legalName: Optional[str] = Field(None, description="Полное наименование")
    legalAddress: Optional[str] = Field(None, description="Адрес регистрации")
    INN: Optional[str] = Field(None, description="ИНН")
    OKPO: Optional[str] = Field(None, description="ОКПО")
    KPP: Optional[str] = Field(None, description="КПП")
    OGRN: Optional[str] = Field(None, description="ОГРН")
    OGRNIP: Optional[str] = Field(None, description="ОГРНИП")


class Manager(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Идентификатор менеджера")
    lastName: Optional[str] = Field(None, description="Фамилия")
    firstName: Optional[str] = Field(None, description="Имя")
    patronymic: Optional[str] = Field(None, description="Отчество")
    phone: Optional[str] = Field(None, description="Телефон")
    email: Optional[str] = Field(None, description="E-mail")


class PaymentType(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код")
    name: Optional[str] = Field(None, description="Название")


class SaveDeliveryData(BaseRetailCrmScheme):
    shipmentAddress: Optional[DeliveryAddress] = Field(None, description="Адрес отгрузки")
    deliveryAddress: Optional[DeliveryAddress] = Field(None, description="Адрес доставки")
    codPaymentType: Optional[PaymentType] = Field(None, description="Тип оплаты для наложенного платежа")
    withCod: Optional[bool] = Field(None, description="Доставка наложенным платежом")
    cod: Optional[float] = Field(None, description="Величина наложенного платежа за услуги доставки")
    cost: Optional[float] = Field(None, description="Стоимость доставки (указывается в накладной в случае предоплаты)")
    vatRate: Optional[str] = Field(None, description="Ставка НДС на услугу доставки ('none' - НДС не облагается)")
    tariff: Optional[str] = Field(None, description="Код тарифа")
    payerType: Optional[str] = Field(None, description="Плательщик за услуги доставки (receiver или sender)")
    shipmentDate: Optional[datetime] = Field(None, description="Дата отгрузки")
    deliveryDate: Optional[datetime] = Field(None, description="Дата доставки")
    deliveryTime: Optional[TimeInterval] = Field(None, description="Время доставки ('custom' не ипользуется)")
    extraData: list[ExtraDataValue] = Field(default_factory=list, description="Дополнительные данные доставки (deliveryDataField.code => значение)")


class DeliveryCustomer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Идентификатор покупателя")
    last_name: Optional[str] = Field(None, alias="lastName", description="Фамилия")
    first_name: Optional[str] = Field(None, alias="firstName", description="Имя")
    patronymic: Optional[str] = Field(None, description="Отчество")
    email: Optional[str] = Field(None, description="Адрес электронной почты")
    phone: Optional[str] = Field(None, description="Номер телефона")
    contragent: Optional[Contragent] = Field(None, description="Данные контрагента")


class RequestSave(BaseRetailCrmScheme):
    deliveryId: Optional[str] = Field(None, description="Идентификатор доставки в службе доставки. Передается если требуется отредактировать уже оформленную доставку")
    order: Optional[str] = Field(None, description="Внутренний ID заказа")
    orderNumber: Optional[str] = Field(None, description="Номер заказа")
    site: Optional[str] = Field(None, description="Код магазина")
    siteName: Optional[str] = Field(None, description="Наименование магазина")
    store: Optional[Store] = Field(None, description="Склад отгрузки")
    legalEntity: Optional[str] = Field(None, description="Наименование юридического лица продавца")
    customer: Optional[DeliveryCustomer] = Field(None, description="Покупатель")
    manager: Optional[Manager] = Field(None, description="Менеджер, работающий с покупателем")
    packages: list[Package] = Field(default_factory=list, description="Набор упаковок")
    delivery: Optional[SaveDeliveryData] = Field(None, description="Данные доставки")
    currency: Optional[str] = Field(None, description="Код валюты")


class ResponseSave(BaseRetailCrmScheme):
    deliveryId: Optional[str] = Field(None, description="Идентификатор доставки в службе доставки")
    trackNumber: Optional[str] = Field(None, description="Трек номер (если установлена опция configuration[allowTrackNumber])")
    cost: Optional[float] = Field(None, description="Стоимость доставки")
    status: Optional[str] = Field(None, description="Код статуса доставки")
    extraData: Optional[dict[str, Any]] = Field(None, description="Дополнительные данные доставки (deliveryDataField.code => значение)")

class ShipmentOrder(BaseRetailCrmScheme):
    deliveryId: Optional[str] = Field(None, description="Идентификатор оформленной доставки в службе доставки")
    packages: list[Package] = Field(default_factory=list, description="Упаковки")

class RequestShipmentSave(BaseRetailCrmScheme):
    shipmentId: Optional[str] = Field(None,
                                      description="Идентификатор отгрузки в службе доставки. Передается если требуется отредактировать уже оформленную отгрузку")
    manager: Optional[Manager] = Field(None, description="Менеджер ответственный за отгрузку")
    date: Optional[datetime] = Field(None, description="Дата отгрузки")
    time: Optional[TimeInterval] = Field(None, description="Время отгрузки")
    address: Optional[DeliveryAddress] = Field(None, description="Адрес отгрузки")
    store: Optional[str] = Field(None, description="Склад отгрузки")
    orders: list[ShipmentOrder] = Field(default_factory=list, description="Заказы в составе отгрузки")
    comment: Optional[str] = Field(None, description="Комментарий")
    extraData: list[ExtraDataValue] = Field(default_factory=list,
                                            description="Дополнительные данные отгрузки (shipmentDataField.code => значение)")