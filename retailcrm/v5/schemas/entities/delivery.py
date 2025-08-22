from datetime import datetime
from typing import Optional, Any

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.shared.order import SerializedEntityOrder


class TimeInterval(BaseRetailCrmScheme):
    from_: Optional[datetime] = Field(None, alias="from", description='Время "с"')
    to: Optional[datetime] = Field(None, description='Время "до"')
    custom: Optional[str] = Field(None, description="Временной диапазон в свободной форме")


class DeliveryCalculation(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код типа доставки")
    available: Optional[bool] = Field(None, description="Тип доставки подходит по заданным условиям")
    vatRate: Optional[str] = Field(None, description="Ставка НДС")
    cost: Optional[float] = Field(None, description="Стоимость доставки")


class StatusInfo(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код статуса доставки")
    updatedAt: Optional[datetime] = Field(None, description="Дата обновления статуса доставки")
    comment: Optional[str] = Field(None, description="Комментарий к статусу")


class RequestStatusUpdateItem(BaseRetailCrmScheme):
    deliveryId: Optional[str] = Field(None, description="Идентификатор доставки в СД")
    trackNumber: Optional[str] = Field(None, description="Трек номер (если установлена опция configuration[allowTrackNumber])")
    cost: Optional[float] = Field(None, description="Стоимость доставки")
    history: list[StatusInfo] = Field(default_factory=list, description="История смены статусов доставки")
    extraData: Optional[dict[str, str]] = Field(None, description="Массив дополнительных данных доставки (deliveryDataField.code => значение)")


class DeliveryShipment(BaseRetailCrmScheme):
    integrationCode: Optional[str] = Field(None, description="Код интеграции")
    id: Optional[int] = Field(None, description="Идентификатор отгрузки")
    externalId: Optional[str] = Field(None, description="Идентификатор отгрузки в службе доставки")
    deliveryType: Optional[str] = Field(None, description="Тип доставки")
    store: Optional[str] = Field(None, description="Склад отгрузки")
    managerId: Optional[int] = Field(None, description="Менеджер, ответственный за отгрузку")
    status: Optional[str] = Field(None, description="Статус отгрузки (Возможные значения created, processing, shipped, cancelled)")
    date: Optional[datetime] = Field(None, description="Дата отгрузки")
    time: Optional[TimeInterval] = Field(None, description="Время отгрузки")
    comment: Optional[str] = Field(None, description="Комментарий")
    orders: list[SerializedEntityOrder] = Field(default_factory=list, description="Заказы в составке отгрузки")
    extraData: Optional[dict[str, Any]] = Field(None, description="Дополнительные данные отгрузки (shipmentDataField.code => значение) (указывается только для отгрузок для типов доставок, интегрированных со службами доставки, подключенными через API)")