from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse, PaginatedResponse
from retailcrm.v5.schemas.callbacks.entities.delivery import ResponseLoadDeliveryData, ResponseSave
from retailcrm.v5.schemas.entities.delivery import DeliveryShipment, DeliveryCalculation


class DeliveryCalculateResponse(SuccessResponse):
    calculations: list[DeliveryCalculation] = Field(default_factory=list)

class DeliveryGetResponse(SuccessResponse):
    result: list[ResponseLoadDeliveryData] = Field(default_factory=list)


class DeliverySaveResponse(SuccessResponse):
    result: ResponseSave = Field(None, description="Результат оформления доставки")


class DeliveryShipmentsResponse(PaginatedResponse):
    deliveryShipments: list[DeliveryShipment] = Field(default_factory=list)


class DeliveryShipmentCreateResponse(SuccessResponse):
    id: Optional[int] = Field(None, description="Идентификатор отгрузки")
    status: Optional[str] = Field(None, description="Статус отгрузки")


class DeliveryShipmentGetResponse(SuccessResponse):
    deliveryShipment: Optional[DeliveryShipment] = Field(None, description="Заявка на отгрузку в службу доставки")


class DeliveryShipmentEditResponse(SuccessResponse):
    id: Optional[int] = Field(None, description="Идентификатор отгрузки")
    status: Optional[str] = Field(None, description="Статус отгрузки")