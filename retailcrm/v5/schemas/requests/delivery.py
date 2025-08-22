from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.delivery import RequestStatusUpdateItem, DeliveryShipment
from retailcrm.v5.schemas.entities.orders import SerializedOrder
from retailcrm.v5.schemas.filters.delivery import DeliveryShipmentFilter


class DeliveryCalculateRequest(BaseRetailCrmScheme):
    deliveryTypeCodes: list[str] = Field( description="Коды типов доставок")
    order: SerializedOrder = Field( description="Заказ")

    order_serializer = field_serializer("order")(to_json_serializer())


class DeliveryGenericTrackingRequest(BaseRetailCrmScheme):
    statusUpdate: list[RequestStatusUpdateItem] = Field( alias="statusUpdate")

    statusUpdate_serializer = field_serializer("statusUpdate")(to_json_serializer())


class DeliveryShipmentsFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(20, description="Количество элементов в ответе")
    page: Optional[int] = Field(1, description="Номер страницы с результатами")
    filter: Optional[DeliveryShipmentFilter] = Field(None)


class DeliveryShipmentCreateRequest(BaseRetailCrmScheme):
    deliveryType: str = Field( description="Тип доставки")
    site: Optional[str] = Field(None, description="Символьный код магазина (указывается в случае добавления заказов в отгрузку по externalId или number)")
    deliveryShipment: DeliveryShipment = Field( alias="deliveryShipment")

    deliveryShipment_serializer = field_serializer("deliveryShipment")(to_json_serializer())


class DeliveryShipmentEditRequest(BaseRetailCrmScheme):
    site: Optional[str] = Field(None, description="Символьный код магазина (указывается в случае добавления заказов в отгрузку по externalId или number)")
    deliveryShipment: DeliveryShipment = Field( alias="deliveryShipment")

    deliveryShipment_serializer = field_serializer("deliveryShipment")(to_json_serializer())