from typing import Optional

from pydantic import Field, field_serializer, model_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.delivery import (
    DeliveryShipment,
    RequestStatusUpdateItem,
)
from retailcrm.v5.schemas.entities.orders import SerializedOrder
from retailcrm.v5.schemas.filters.delivery import DeliveryShipmentFilter
from retailcrm.v5.utils import pydantic_to_nested_dict


class DeliveryCalculateRequest(BaseRetailCrmScheme):
    deliveryTypeCodes: list[str] = Field(description="Коды типов доставок")
    order: SerializedOrder = Field(description="Заказ")

    order_serializer = field_serializer("order")(to_json_serializer())


class DeliveryGenericTrackingRequest(BaseRetailCrmScheme):
    statusUpdate: list[RequestStatusUpdateItem] = Field(alias="statusUpdate")

    statusUpdate_serializer = field_serializer("statusUpdate")(to_json_serializer())


class DeliveryShipmentsFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(20, description="Количество элементов в ответе")
    page: Optional[int] = Field(1, description="Номер страницы с результатами")
    filter_obj: Optional[DeliveryShipmentFilter] = Field(None)

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter"),
        }


class DeliveryShipmentCreateRequest(BaseRetailCrmScheme):
    deliveryType: str = Field(description="Тип доставки")
    site: Optional[str] = Field(
        None,
        description="Символьный код магазина (указывается в случае добавления заказов в отгрузку по externalId или number)",
    )
    deliveryShipment: DeliveryShipment = Field(alias="deliveryShipment")

    deliveryShipment_serializer = field_serializer("deliveryShipment")(
        to_json_serializer()
    )


class DeliveryShipmentEditRequest(BaseRetailCrmScheme):
    site: Optional[str] = Field(
        None,
        description="Символьный код магазина (указывается в случае добавления заказов в отгрузку по externalId или number)",
    )
    deliveryShipment: DeliveryShipment = Field(alias="deliveryShipment")

    deliveryShipment_serializer = field_serializer("deliveryShipment")(
        to_json_serializer()
    )
