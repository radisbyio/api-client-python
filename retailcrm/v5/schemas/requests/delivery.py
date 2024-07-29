from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field, RootModel


class TimeInterval(BaseModel):
    from_: Optional[datetime] = None
    to: Optional[datetime] = None
    custom: str = ""


class SerializedEntityOrder(BaseModel):
    id: int
    externalId: str = ""
    number: str = ""


class StatusInfo(BaseModel):
    code: str = ""
    updated_at: datetime = Field(None, validation_alias="updatedAt")
    comment: str = ""


class RequestStatusUpdateItem(BaseModel):
    delivery_id: str = Field("", validation_alias="deliveryId")
    trackNumber: str = Field("", validation_alias="trackNumber")
    cost: float = Field("", validation_alias="cost")
    history: list[StatusInfo] = []
    extra_data: dict[str, str] = {}  # TODO: поле не точное


class OrderDeliveryAddress(BaseModel):
    index: str = ""
    countryIso: str = ""
    region: str = ""
    regionId: int = 0
    city: str = ""
    cityId: int = 0
    cityType: str = ""
    street: str = ""
    streetId: int = 0
    streetType: str = ""
    building: str = ""
    flat: str = ""
    floor: int = 0
    block: int = 0
    house: str = ""
    housing: str = ""
    metro: str = ""


# class SerializedOrder(BaseModel):
#     weight: float = 0
#     length: int = 0
#     width: int = 0
#     height: int = 0
#     items: list[SerializedOrderProduct] = []
#     delivery: Optional[SerializedOrderDelivery] = None


class DeliveryShipment(BaseModel):
    id: int
    integration_code: str = Field("", validation_alias="integrationCode")
    external_id: str = Field("", validation_alias="externalId")
    deliveryType: str = Field("", validation_alias="deliveryType")
    store: str = ""
    manager_id: int = Field(0, validation_alias="managerId")
    status: str = Field("", examples=["created", "processing", "shipped", "cancelled"])
    date: Optional[datetime] = None
    time: Optional[TimeInterval] = None
    comment: str = ""
    orders: list[SerializedEntityOrder] = []
    extra_data: dict[str, str] = Field(
        {}, validation_alias="extraData"
    )  # TODO: поле не точное


class DeliveryShipmentFilterData(BaseModel):
    ids: list[int] = []
    external_id: str = Field("", validation_alias="externalId")
    order_number: str = Field("", validation_alias="orderNumber")
    deliveryType: list[str] = Field([], validation_alias="deliveryType")
    managers: list[int] = Field([], validation_alias="managers")
    stores: list[str] = Field([], validation_alias="stores")
    statuses: list[str] = Field([], validation_alias="statuses")
    date_from: Optional[date] = Field(None, validation_alias="dateFrom")
    date_to: Optional[date] = Field(None, validation_alias="dateTo")


class StatusUpdates(RootModel[list[RequestStatusUpdateItem]]):
    root: list[RequestStatusUpdateItem] = []
