from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class OrderProductPackFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID комплектаций заказов")
    stores: Optional[list[str]] = Field(None, description="Склад")
    itemId: Optional[int] = Field(None, description="ID товара")
    offerXmlId: Optional[str] = Field(None, description="Xml ID торгового предложения")
    offerExternalId: Optional[str] = Field(None, description="Внешний ID торгового предложения")
    orderId: Optional[int] = Field(None, description="ID заказа")
    orderExternalId: Optional[str] = Field(None, description="Внешний ID заказа")
    shipmentDateFrom: Optional[datetime] = Field(None, description="Дата отгрузки от")
    shipmentDateTo: Optional[datetime] = Field(None, description="Дата отгрузки до")
    invoiceNumber: Optional[str] = Field(None, description="Номер счета-фактуры")
    deliveryNoteNumber: Optional[str] = Field(None, description="Номер накладной")

    shipment_date_from_serializer = field_serializer("shipmentDateFrom")(datetime_serializer("%Y-%m-%d %H:%M:%S"))
    shipment_date_to_serializer = field_serializer("shipmentDateTo")(datetime_serializer("%Y-%m-%d %H:%M:%S"))


class OrderProductPackHistoryFilterType(BaseRetailCrmScheme):
    order_id: Optional[int] = Field(None, alias="orderId", description="Внутренний идентификатор заказа", ge=0)
    since_id: Optional[int] = Field(None, alias="sinceId", description="Нижнее ограничение по идентификатору записи в истории (исключая границу)", ge=0)
    order_external_id: Optional[str] = Field(None, alias="orderExternalId", description="Идентификатор заказа из магазина", max_length=255)
    start_date: Optional[datetime] = Field(None, alias="startDate", description="Время изменения (с)")
    end_date: Optional[datetime] = Field(None, alias="endDate", description="Время изменения (до)")

    start_date_serializer = field_serializer("start_date")(datetime_serializer("%Y-%m-%d %H:%M:%S"))
    end_date_serializer = field_serializer("end_date")(datetime_serializer("%Y-%m-%d %H:%M:%S"))
