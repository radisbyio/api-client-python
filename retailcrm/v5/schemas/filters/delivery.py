from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class DeliveryShipmentFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Идентификаторы отгрузок")
    externalId: Optional[str] = Field(
        None, description="Внешний идентификатор отгрузки"
    )
    orderNumber: Optional[str] = Field(
        None, description="Номер заказа в составе отгрузки"
    )
    deliveryTypes: Optional[list[str]] = Field(None, description="Типы доставки")
    managers: Optional[list[int]] = Field(None, description="Идентификаторы менеджеров")
    stores: Optional[list[str]] = Field(None, description="Склады")
    statuses: Optional[list[str]] = Field(None, description="Статусы")
    dateFrom: Optional[datetime] = Field(None, description="Дата отгрузки (с)")
    dateTo: Optional[datetime] = Field(None, description="Дата отгрузки (до)")

    dateFrom_serializer = field_serializer("dateFrom")(datetime_serializer("%Y-%m-%d"))
    dateTo_serializer = field_serializer("dateTo")(datetime_serializer("%Y-%m-%d"))
