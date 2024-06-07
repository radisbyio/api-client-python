from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from retailcrm.v5.schemas.base import RetailCrmResponse
from retailcrm.v5.schemas.shared import (
    DeclaredValueItem,
    Order,
    OrderProduct,
    Package,
    Payment,
)


# todo: заполнить
class CreateOrder(BaseModel):
    id: int
    externalId: Optional[str] = None


# todo: заполнить
class ResponseCreateOrder(RetailCrmResponse):
    order: Optional[CreateOrder] = None


class GenericData(BaseModel):
    externalId: Optional[str] = Field(None)


class CourierData(BaseModel):
    externalId: Optional[str] = Field(None)
    trackNumber: Optional[str] = Field(None)
    status: Optional[str] = Field(None)
    locked: Optional[bool] = Field(None)
    pickuppointAddress: Optional[str] = Field(None)
    days: Optional[str] = Field(None)
    statusText: Optional[str] = Field(None)
    statusDate: Optional[datetime] = Field(None)
    tariff: Optional[str] = Field(None)
    tariffName: Optional[str] = Field(None)
    pickuppointId: Optional[str] = Field(None)
    pickuppointSchedule: Optional[str] = Field(None)
    pickuppointPhone: Optional[str] = Field(None)
    payerType: Optional[str] = Field(None)
    statusComment: Optional[str] = Field(None)
    cost: Optional[float] = Field(None)
    minTerm: Optional[int] = Field(None)
    maxTerm: Optional[int] = Field(None)
    shipmentpointId: Optional[str] = Field(None)
    shipmentpointName: Optional[str] = Field(None)
    shipmentpointAddress: Optional[str] = Field(None)
    shipmentpointSchedule: Optional[str] = Field(None)
    shipmentpointPhone: Optional[str] = Field(None)
    shipmentpointCoordinateLatitude: Optional[str] = Field(None)
    shipmentpointCoordinateLongitude: Optional[str] = Field(None)
    pickuppointName: Optional[str] = Field(None)
    pickuppointCoordinateLatitude: Optional[str] = Field(None)
    pickuppointCoordinateLongitude: Optional[str] = Field(None)
    extraData: Optional[dict] = Field(None)
    itemDeclaredValues: Optional[List["DeclaredValueItem"]] = Field(None)
    packages: Optional[List["Package"]] = Field(None)


class NewPostData(BaseModel):
    externalId: Optional[str] = Field(None)
    trackNumber: Optional[str] = Field(None)
    status: Optional[str] = Field(None)
    locked: Optional[bool] = Field(None)
    pickuppointAddress: Optional[str] = Field(None)
    days: Optional[str] = Field(None)
    statusText: Optional[str] = Field(None)
    statusDate: Optional[datetime] = Field(None)
    tariff: Optional[str] = Field(None)
    tariffName: Optional[str] = Field(None)
    pickuppointId: Optional[str] = Field(None)
    pickuppointSchedule: Optional[str] = Field(None)
    pickuppointPhone: Optional[str] = Field(None)
    payerType: Optional[str] = Field(None)
    statusComment: Optional[str] = Field(None)
    cost: Optional[float] = Field(None)
    minTerm: Optional[int] = Field(None)
    maxTerm: Optional[int] = Field(None)
    shipmentpointId: Optional[str] = Field(None)
    shipmentpointName: Optional[str] = Field(None)
    shipmentpointAddress: Optional[str] = Field(None)
    shipmentpointSchedule: Optional[str] = Field(None)
    shipmentpointPhone: Optional[str] = Field(None)
    shipmentpointCoordinateLatitude: Optional[str] = Field(None)
    shipmentpointCoordinateLongitude: Optional[str] = Field(None)
    pickuppointName: Optional[str] = Field(None)
    pickuppointCoordinateLatitude: Optional[str] = Field(None)
    pickuppointCoordinateLongitude: Optional[str] = Field(None)
    extraData: Optional[dict] = Field(None)
    itemDeclaredValues: Optional[List["DeclaredValueItem"]] = Field(None)
    packages: Optional[List["Package"]] = Field(None)


class DDeliveryData(BaseModel):
    externalId: Optional[str] = Field(None)
    trackNumber: Optional[str] = Field(None)
    status: Optional[str] = Field(None)
    locked: Optional[bool] = Field(None)
    pickuppointAddress: Optional[str] = Field(None)
    days: Optional[str] = Field(None)
    statusText: Optional[str] = Field(None)
    statusDate: Optional[datetime] = Field(None)
    tariff: Optional[str] = Field(None)
    tariffName: Optional[str] = Field(None)
    pickuppointId: Optional[str] = Field(None)
    pickuppointSchedule: Optional[str] = Field(None)
    pickuppointPhone: Optional[str] = Field(None)
    payerType: Optional[str] = Field(None)
    statusComment: Optional[str] = Field(None)
    cost: Optional[float] = Field(None)
    minTerm: Optional[int] = Field(None)
    maxTerm: Optional[int] = Field(None)
    shipmentpointId: Optional[str] = Field(None)
    shipmentpointName: Optional[str] = Field(None)
    shipmentpointAddress: Optional[str] = Field(None)
    shipmentpointSchedule: Optional[str] = Field(None)
    shipmentpointPhone: Optional[str] = Field(None)
    shipmentpointCoordinateLatitude: Optional[str] = Field(None)
    shipmentpointCoordinateLongitude: Optional[str] = Field(None)
    pickuppointName: Optional[str] = Field(None)
    pickuppointCoordinateLatitude: Optional[str] = Field(None)
    pickuppointCoordinateLongitude: Optional[str] = Field(None)
    extraData: Optional[dict] = Field(None)
    itemDeclaredValues: Optional[List["DeclaredValueItem"]] = Field(None)
    packages: Optional[List["Package"]] = Field(None)


class KazPostData(BaseModel):
    externalId: Optional[str] = Field(None)
    trackNumber: Optional[str] = Field(None)
    status: Optional[str] = Field(None)
    locked: Optional[bool] = Field(None)
    pickuppointAddress: Optional[str] = Field(None)
    days: Optional[str] = Field(None)
    statusText: Optional[str] = Field(None)
    statusDate: Optional[datetime] = Field(None)
    tariff: Optional[str] = Field(None)
    tariffName: Optional[str] = Field(None)
    pickuppointId: Optional[str] = Field(None)
    pickuppointSchedule: Optional[str] = Field(None)
    pickuppointPhone: Optional[str] = Field(None)
    payerType: Optional[str] = Field(None)
    statusComment: Optional[str] = Field(None)
    cost: Optional[float] = Field(None)
    minTerm: Optional[int] = Field(None)
    maxTerm: Optional[int] = Field(None)
    shipmentpointId: Optional[str] = Field(None)
    shipmentpointName: Optional[str] = Field(None)
    shipmentpointAddress: Optional[str] = Field(None)
    shipmentpointSchedule: Optional[str] = Field(None)
    shipmentpointPhone: Optional[str] = Field(None)
    shipmentpointCoordinateLatitude: Optional[str] = Field(None)
    shipmentpointCoordinateLongitude: Optional[str] = Field(None)
    pickuppointName: Optional[str] = Field(None)
    pickuppointCoordinateLatitude: Optional[str] = Field(None)
    pickuppointCoordinateLongitude: Optional[str] = Field(None)
    extraData: Optional[dict] = Field(None)
    itemDeclaredValues: Optional[List["DeclaredValueItem"]] = Field(None)
    packages: Optional[List["Package"]] = Field(None)


class User(BaseModel):
    id: int = Field(description="ID пользователя")


class ApiKey(BaseModel):
    current: Optional[bool] = Field(
        None,
        description="Изменение было сделано с помощью ключа, используемого в данный момент",
    )
    id: Optional[int] = Field(None, description="ID API-ключа")


class OrderHistory(BaseModel):
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
    old_value: Optional[str | int | datetime | dict] = Field(
        None, description="Старое значение свойства", validation_alias="oldValue"
    )
    new_value: Optional[str | int | datetime | dict] = Field(
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


class ResponseGetOrder(RetailCrmResponse):
    order: Optional[Order] = None


class ResponseOrders(RetailCrmResponse):
    orders: list[Order] = Field([], description="Список заказов")


class FixExternalRow(BaseModel):
    id: Optional[int] = Field(None, description="Внутренний ID")
    external_id: Optional[str] = Field(
        None, description="Внешний ID", validation_alias="externalId"
    )


class EntityWithExternalId(BaseModel):
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


class ResponseOrderHistory(RetailCrmResponse):
    generated_at: Optional[datetime] = Field(
        None, description="Время формирования ответа", validation_alias="generatedAt"
    )
    history: list[OrderHistory] = []


class ResponseDeleteOrderPayment(RetailCrmResponse):
    pass
