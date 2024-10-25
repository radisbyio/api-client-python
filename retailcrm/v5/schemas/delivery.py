from datetime import datetime, date
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.enums import VatRateTypes, DeliveryShipmentStatusTypes
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas import SerializedEntityOrder
from retailcrm.v5.schemas.base import BaseRetailCrmScheme, RetailCrmResponse
from retailcrm.v5.schemas.shared import (
    Courier,
    Package,
    TimeInterval,
)
from retailcrm.v5.schemas.references import PaymentType

__all__ = [
    "RequestStatusUpdateItem",
    "DeliveryShipmentFilterData",
    "DeliveryShipment",
    "ResponseAutocompleteItem",
    "RequestCalculate",
    "ResponseCalculate",
    "Terminal",
    "RequestDelete",
    "ResponseLoadDeliveryData",
    "RequestPrint",
    "RequestSave",
    "SaveDeliveryData",
    "ResponseSave",
    "RequestShipmentDelete",
    "RequestShipmentSave",
    "ResponseShipmentSave",
    "Tariff",
    "ShipmentOrder",
    "DeliveryTrackingResponse",
    "FilterDeliveryShipmentsResponse",
    "GetDeliveryShipmentResponse",
    "EditDeliveryShipmentsResponse",
    "CalculationResponse",
    "CreateDeliveryShipmentsResponse"
]


class DeliveryCalculation(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код типа доставки")
    available: Optional[bool] = Field(None, description="Тип доставки подходит по заданным условиям")
    vatRate: Optional[str] = Field(None, description="Ставка НДС")
    cost: Optional[str] = Field(None, description="Стоимость доставки")


class CalculationResponse(RetailCrmResponse):
    calculations: list[DeliveryCalculation] = Field(default_factory=list)


class StatusInfo(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Дата обновления статуса доставки")
    updatedAt: Optional[datetime] = Field(None, description="Дата обновления статуса доставки")
    comment: Optional[str] = Field(None, description="Комментарий к статусу")

    updatedAt_serializer = field_serializer("updatedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class RequestStatusUpdateItem(BaseRetailCrmScheme):
    deliveryId: str = Field(description="Идентификатор доставки в СД")
    trackNumber: Optional[str] = Field(
        None, description="Трек номер (если установлена опция `configuration[allowTrackNumber]`)"
    )
    cost: Optional[float] = Field(None, description="Стоимость доставки")
    history: Optional[list[StatusInfo]] = Field(
        None, description="История смены статусов доставки"
    )
    # TODO: Определить нужный тип и вид
    extraData: Optional[list] = Field(
        None,
        description="Массив дополнительных данных доставки (deliveryDataField.code => значение)",
    )


class DeliveryTrackingResponse(RetailCrmResponse):
    pass


class DeliveryShipmentFilterData(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Идентификаторы отгрузок")
    externalId: Optional[str] = Field(None, description="Внешний идентификатор отгрузки")
    orderNumber: Optional[str] = Field(
        None, description="Номер заказа в составе отгрузки"
    )
    deliveryTypes: Optional[list[str]] = Field(None, description="Типы доставки")
    managers: Optional[list[int]] = Field(None, description="Идентификаторы менеджеров")
    stores: Optional[list[str]] = Field(None, description="Склады")
    statuses: Optional[list[str]] = Field(None, description="Статусы")
    dateFrom: Optional[date] = Field(None, description="Дата отгрузки (с)")
    dateTo: Optional[date] = Field(None, description="Дата отгрузки (до)")


class DeliveryShipment(BaseRetailCrmScheme):
    integrationCode: Optional[str] = Field(None, description="Код интеграции")
    id: int = Field(description="Идентификатор отгрузки")
    externalId: Optional[str] = Field(
        None, description="Идентификатор отгрузки в службе доставки"
    )
    deliveryType: Optional[str] = Field(None, description="Тип доставки")
    store: Optional[str] = Field(None, description="Склад отгрузки")
    managerId: Optional[int] = Field(
        None, description="Менеджер, ответственный за отгрузку"
    )
    status: Optional[DeliveryShipmentStatusTypes] = Field(
        None,
        description="Статус отгрузки (Возможные значения created, processing, shipped, cancelled)",
    )
    date_: Optional[datetime] = Field(None, description="Дата отгрузки", serialization_alias="date")
    time: Optional[TimeInterval] = Field(None, description="Время отгрузки")
    comment: Optional[str] = Field(None, description="Комментарий")
    orders: Optional[list[SerializedEntityOrder]] = Field(
        default_factory=list, description="Заказы в составке отгрузки"
    )
    # TODO: Определить нужный тип и вид
    # TODO: Протестировать на создание и чтение
    extraData: Optional[list] = Field(
        default_factory=list,
        description="Дополнительные данные отгрузки (shipmentDataField.code => значение) (указывается только для отгрузок для типов доставок, интегрированных со службами доставки, подключенными через API)",
    )

    date_serializer = field_serializer("date_")(datetime_serializer("%Y-%m-%d %H:%M:%S"))


class FilterDeliveryShipmentsResponse(RetailCrmResponse):
    deliveryShipments: list[DeliveryShipment] = Field(default_factory=list,
                                                      description="Заявка на отгрузку в службу доставки")


class CreateDeliveryShipmentsResponse(RetailCrmResponse):
    id: Optional[int] = Field(None, description="Идентификатор отгрузки")
    status: Optional[DeliveryShipmentStatusTypes] = Field(None, description="Статус отгрузки")


class GetDeliveryShipmentResponse(RetailCrmResponse):
    deliveryShipment: Optional[DeliveryShipment] = Field(None, description="Заявка на отгрузку в службу доставки")


class EditDeliveryShipmentsResponse(RetailCrmResponse):
    id: Optional[int] = Field(None, description="Идентификатор отгрузки")
    status: Optional[DeliveryShipmentStatusTypes] = Field(None, description="Статус отгрузки")


### Callbacks


class ResponseAutocompleteItem(BaseRetailCrmScheme):
    value: str = Field(description="Значение")
    label: str = Field(description="Наименование")
    description: Optional[str] = Field(
        None, description="Не обязательное поле. Подсказка для опции - выводится мелким шрифтом под именем опции"
    )


class CallbackDeliveryAutocompleteResponse(BaseRetailCrmScheme):
    result: Optional[list[ResponseAutocompleteItem]] = Field(None, description="Массив значений")


class PackageItem(BaseRetailCrmScheme):
    offerId: Optional[str] = Field(None, description="Идентификатор оффера в системе")
    externalId: Optional[str] = Field(
        None, description="Идентификатор торгового предложения в магазине"
    )
    xmlId: Optional[str] = Field(
        None, description="Идентификатор торгового предложения в складской системе"
    )
    name: Optional[str] = Field(None, description="Наименование товара")
    declaredValue: Optional[float] = Field(
        None, description="Объявленная стоимость за единицу товара"
    )
    cod: Optional[float] = Field(
        None, description="Наложенный платеж за единицу товара"
    )
    vatRate: Optional[VatRateTypes] = Field(
        None, description='Ставка НДС ("none" - НДС не облагается)'
    )
    quantity: Optional[float] = Field(None, description="Количество товара в упаковке")
    unit: Optional[str] = Field(None, description="Единица измерения товара")
    cost: Optional[float] = Field(
        None, description="Стоимость товара (с учетом скидок)"
    )
    markingCodes: Optional[list[str]] = Field(
        None, description="Коды маркировки (формат кода маркировки)"
    )
    properties: Optional[dict] = Field(
        None, description="Свойства товара"
    )  # todo: уточнить тип данных
    weight: Optional[float] = Field(
        None, description="Вес товара (может быть null для услуг)"
    )


class Coordinates(BaseRetailCrmScheme):
    latitude: Optional[float] = Field(None, description="Широта")
    longitude: Optional[float] = Field(None, description="Долгота")


class Terminal(BaseRetailCrmScheme):
    code: str = Field(description="Код терминала")
    cost: Optional[float] = Field(
        None,
        description="Стоимость доставки до терминала (указывается в случае если она отличается от стандартной стоимости по тарифу)",
    )
    name: Optional[str] = Field(None, description="Наименование терминала")
    description: Optional[str] = Field(None, description="Описание терминала")
    address: Optional[str] = Field(None, description="Адрес")
    schedule: Optional[str] = Field(None, description="Режим работы")
    phone: Optional[str] = Field(None, description="Телефон")
    extraData: Optional[list] = Field(
        None, description="Дополнительные данные (deliveryDataField.code => значение)"
    )  # TODO Уточнить
    coordinates: Optional[Coordinates] = Field(None, description="Координаты")


class DeliveryAddress(BaseRetailCrmScheme):
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
    terminal: Optional[str] = Field(
        None, description="Код терминала отгрузки/доставки"
    )
    terminalData: Optional[Terminal] = Field(None, description="Данные терминала")


class Store(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код")
    name: Optional[str] = Field(None, description="Название")


class RequestCalculate(BaseRetailCrmScheme):
    shipmentAddress: Optional[DeliveryAddress] = Field(None, description="Адрес отгрузки")
    store: Optional[Store] = Field(None, description="Склад отгрузки")
    deliveryAddress: Optional[DeliveryAddress] = Field(
        None, description="Адрес доставки"
    )
    packages: Optional[list[Package]] = Field(None, description="Набор упаковок")
    declaredValue: Optional[float] = Field(None, description="Объявленная стоимость")
    cod: Optional[float] = Field(
        None, description="Сумма наложенного платежа по заказу"
    )
    payerType: Optional[str] = Field(
        None, description="Плательщик за доставку (receiver или sender)"
    )
    shipmentDate: Optional[datetime] = Field(
        None, description="Дата отгрузки", serialization_alias="shipmentDate"
    )
    deliveryDate: Optional[datetime] = Field(
        None, description="Дата доставки", serialization_alias="deliveryDate"
    )
    deliveryTime: Optional[TimeInterval] = Field(None, description="Время доставки")
    currency: Optional[str] = Field(None, description="Код валюты")
    extraData: Optional[list] = Field(
        None,
        description="Дополнительные данные доставки (deliveryDataField.code => значение)",
    )  # TODO: Уточнить

    shipmentDate_serializer = field_serializer("shipmentDate")(
        datetime_serializer("%Y-%m-%d")
    )
    deliveryDate_serializer = field_serializer("deliveryDate")(
        datetime_serializer("%Y-%m-%d")
    )


class ResponseCalculate(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код тарифа")
    group: Optional[str] = Field(None, description="Группа тарифов")
    name: Optional[str] = Field(None, description="Наименование тарифа")
    type: Optional[str] = Field(
        None,
        description="Тип тарифа (courier - курьерская доставка или selfDelivery - самовывоз)",
    )
    description: Optional[str] = Field(None, description="Описание")
    cost: Optional[float] = Field(
        None,
        description="Стоимость доставки (Если не передана, то тариф будет выводиться, но не будет доступен для выбора) (в валюте объекта)",
    )
    minTerm: Optional[int] = Field(None, description="Минимальный срок доставки")
    maxTerm: Optional[int] = Field(None, description="Максимальный срок доставки")
    extraData: Optional[list] = Field(
        None, description="Дополнительные данные доставки (deliveryDataField.code => значение)"
    )  # TODO: уточнить
    extraDataAvailable: Optional[list] = Field(
        None,
        description="Массив кодов полей, которые должны отображаться в карточке заказа. Если не передан будут отображаться все поля с дополнительными данными доставки.",
    )
    pickuppointlist: Optional[list[Terminal]] = Field(
        None, description="Терминал отгрузки/получения"
    )


class CallbackDeliveryCalculateResponse(BaseRetailCrmScheme):
    success: Optional[bool] = Field(None, description="Результат запроса (успешный/неуспешный)")
    result: Optional[list[ResponseCalculate]] = Field(None, description="Данные о стоимости доступных доставок")


class RequestDelete(BaseRetailCrmScheme):
    deliveryId: str = Field(description="Идентификатор доставки в службе доставки")


class CallbackDeliveryDeleteResponse(BaseRetailCrmScheme):
    success: Optional[bool] = Field(None, description="Результат запроса (успешный/неуспешный)")


class ResponseLoadDeliveryData(BaseRetailCrmScheme):
    trackNumber: Optional[str] = Field(
        None, description="Трек номер (если установлена опция configuration[allowTrackNumber])"
    )
    cost: Optional[float] = Field(None, description="Стоимость доставки")
    shipmentDate: Optional[datetime] = Field(None, description="Дата отгрузки")
    deliveryDate: Optional[datetime] = Field(None, description="Дата доставки")
    deliveryTime: Optional[TimeInterval] = Field(None, description="Время доставки")
    tariff: Optional[str] = Field(None, description="Код тарифа")
    tariffName: Optional[str] = Field(None, description="Наименование тарифа")
    payerType: Optional[str] = Field(
        None, description="Плательщик за доставку (receiver или sender)"
    )
    status: Optional[StatusInfo] = Field(None, description="Статус доставки")
    extraData: Optional[list] = Field(
        None, description="Дополнительные данные доставки (deliveryDataField.code => значение)"
    )
    shipmentAddress: Optional[DeliveryAddress] = Field(
        None, description="Адрес отгрузки"
    )
    deliveryAddress: Optional[DeliveryAddress] = Field(
        None, description="Адрес доставки"
    )


class CallbackDeliveryGetResponse(BaseRetailCrmScheme):
    success: Optional[bool] = Field(None, description="Результат запроса (успешный/неуспешный)")
    result: Optional[ResponseLoadDeliveryData] = Field(None, description="Данные доставки")
    errorMsg: Optional[str] = Field(None, description="Сообщение об ошибке")


class RequestPrint(BaseRetailCrmScheme):
    entityType: Optional[str] = Field(
        None,
        description='Тип сущности для печатной формы (order - печатная форма для заказа (по умолчанию), shipment - печатная форма для отгрузки. Значение совпадает со значением integrationModule[integrations][delivery][platelist][][type] выбранной печатной формы)',
    )
    type: Optional[str] = Field(None, description="Код типа печатной формы")
    deliveryIds: list[str] = Field(
        default_factory=list,
        description='Массив идентификаторов доставок в службе доставки ([["56376", "798645"]])'
    )


class Manager(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Идентификатор менеджера")
    lastName: Optional[str] = Field(None, description="Фамилия")
    firstName: Optional[str] = Field(None, description="Имя")
    patronymic: Optional[str] = Field(None, description="Отчество")
    phone: Optional[str] = Field(None, description="Телефон")
    email: Optional[str] = Field(None, description="E-mail")


class SaveDeliveryData(BaseRetailCrmScheme):
    shipmentAddress: Optional[DeliveryAddress] = Field(None, description="Адрес отгрузки")
    deliveryAddress: Optional[DeliveryAddress] = Field(
        None, description="Адрес доставки"
    )
    codPaymentType: Optional[PaymentType] = Field(
        None, description="Тип оплаты для наложенного платежа"
    )
    withCod: Optional[bool] = Field(
        None, description="Доставка наложенным платежом"
    )
    cod: Optional[float] = Field(
        None, description="Величина наложенного платежа за услуги доставки"
    )
    cost: Optional[float] = Field(
        None, description="Стоимость доставки (указывается в накладной в случае предоплаты)"
    )
    vatRate: Optional[VatRateTypes] = Field(
        None, description="Ставка НДС на услугу доставки (`none` - НДС не облагается)"
    )
    tariff: Optional[str] = Field(None, description="Код тарифа")
    payerType: Optional[str] = Field(
        None, description="Плательщик за услуги доставки (receiver или sender)"
    )
    shipmentDate: Optional[datetime] = Field(
        None, description="Дата отгрузки", serialization_alias="shipmentDate"
    )
    deliveryDate: Optional[datetime] = Field(
        None, description="Дата доставки", serialization_alias="deliveryDate"
    )
    deliveryTime: Optional[TimeInterval] = Field(
        None, description='Время доставки ("custom" не ипользуется)'
    )
    # extraData: Optional[list[ExtraDataValue]] = Field(
    extraData: Optional[list] = Field(
        None,
        description="Дополнительные данные доставки (deliveryDataField.code => значение)",
    )  # TODO: Уточнить

    shipmentDate_serializer = field_serializer("shipmentDate")(
        datetime_serializer("%Y-%m-%d")
    )
    deliveryDate_serializer = field_serializer("deliveryDate")(
        datetime_serializer("%Y-%m-%d")
    )


class RequestSave(BaseRetailCrmScheme):
    deliveryId: Optional[str] = Field(
        None,
        description="Идентификатор доставки в службе доставки. Передается если требуется отредактировать уже оформленную доставку"
    )
    order: Optional[str] = Field(None, description="Внутренний ID заказа")
    orderNumber: Optional[str] = Field(None, description="Номер заказа")
    site: Optional[str] = Field(None, description="Код магазина")
    siteName: Optional[str] = Field(None, description="Наименование магазина")
    store: Optional[Store] = Field(None, description="Склад отгрузки")
    legalEntity: Optional[str] = Field(
        None, description="Наименование юридического лица продавца"
    )
    customer: Optional[Courier] = Field(None, description="Покупатель")
    manager: Optional[Manager] = Field(
        None, description="Менеджер, работающий с покупателем"
    )
    packages: Optional[list[Package]] = Field(None, description="Набор упаковок")
    delivery: Optional[SaveDeliveryData] = Field(None, description="Данные доставки")
    currency: Optional[str] = Field(None, description="Код валюты")


class ResponseSave(BaseRetailCrmScheme):
    deliveryId: str = Field(description="Идентификатор доставки в службе доставки")
    trackNumber: Optional[str] = Field(
        None, description="Трек номер (если установлена опция configuration[allowTrackNumber])"
    )
    cost: Optional[float] = Field(None, description="Стоимость доставки")
    status: Optional[str] = Field(None, description="Код статуса доставки")
    extraData: Optional[list] = Field(
        None, description="Дополнительные данные доставки (deliveryDataField.code => значение)"
    )


class CallbackDeliverySaveResponse(BaseRetailCrmScheme):
    success: Optional[bool] = Field(None, description="Результат запроса (успешный/неуспешный)")
    result: Optional[ResponseSave] = Field(None, description="Данные доставки")


class RequestShipmentDelete(BaseRetailCrmScheme):
    shipmentId: str = Field(description="Идентификатор отгрузки в службе доставки")
    extraData: Optional[list] = Field(
        None, description="Дополнительные данные отгрузки (shipmentDataField.code => значение)"
    )  # TODO: Уточнить


class CallbackDeliveryShipmentDeleteResponse(BaseRetailCrmScheme):
    success: Optional[bool] = Field(None, description="Результат запроса (успешный/неуспешный)")


class CallbackDeliveryShipmentPointListResponse(BaseRetailCrmScheme):
    success: Optional[bool] = Field(None, description="Результат запроса (успешный/неуспешный)")
    result: Optional[list[Terminal]] = Field(default_factory=list, description="Данные доставки")


class ShipmentOrder(BaseRetailCrmScheme):
    deliveryId: str = Field(description="Идентификатор оформленной доставки в службе доставки")
    packages: Optional[list[Package]] = Field(None, description="Упаковки")


class RequestShipmentSave(BaseRetailCrmScheme):
    shipmentId: Optional[str] = Field(
        None,
        description="Идентификатор отгрузки в службе доставки. Передается если требуется отредактировать уже оформленную отгрузку"
    )
    manager: Optional[Manager] = Field(None, description="Менеджер ответственный за отгрузку")
    date: Optional[datetime] = Field(
        None, description="Дата отгрузки", serialization_alias="date"
    )
    time: Optional[TimeInterval] = Field(None, description="Время отгрузки")
    address: Optional[DeliveryAddress] = Field(None, description="Адрес отгрузки")
    store: Optional[str] = Field(None, description="Склад отгрузки")
    orders: Optional[list[ShipmentOrder]] = Field(
        None, description="Заказы в составе отгрузки"
    )
    comment: Optional[str] = Field(None, description="Комментарий")
    extraData: Optional[list] = Field(
        None, description="Дополнительные данные отгрузки (shipmentDataField.code => значение)"
    )

    date_serializer = field_serializer("date")(datetime_serializer("%Y-%m-%d"))


class ResponseShipmentSave(BaseRetailCrmScheme):
    shipmentId: str = Field(description="Идентификатор отгрузки в службе доставки")
    extraData: Optional[list] = Field(None, description="Дополнительные данные отгрузки")


class CallbackDeliveryShipmentSaveResponse(BaseRetailCrmScheme):
    success: Optional[bool] = Field(None, description="Результат запроса (успешный/неуспешный)")
    result: Optional[ResponseShipmentSave] = Field(None, description="Данные доставки")


class Tariff(BaseRetailCrmScheme):
    code: str = Field(description="Код тарифа")
    name: Optional[str] = Field(None, description="Название тарифа")
    description: Optional[str] = Field(None, description="Описание тарифа")
    type: Optional[str] = Field(
        None,
        description="Тип тарифа (Возможные значения: courier - курьерская доставка, selfDelivery - самовывоз)",
    )


class CallbackDeliveryTariffListResponse(BaseRetailCrmScheme):
    success: Optional[bool] = Field(None, description="Результат запроса (успешный/неуспешный)")
    result: Optional[list[Tariff]] = Field(None, description="Данные доставки")
