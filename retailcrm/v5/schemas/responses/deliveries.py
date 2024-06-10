from datetime import date, datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from retailcrm.v5.schemas.base import RetailCrmResponse


class TimeInterval(BaseModel):
    from_: Optional[datetime] = None
    to: Optional[datetime] = None
    custom: str = ""


class SerializedEntityOrder(BaseModel):
    id: int
    externalId: str = ""
    number: str = ""


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


class DeliveryCalculation(BaseModel):
    code: str = ""
    available: bool = False
    vat_rate: str = Field("", validation_alias="vatRate")
    cost: float = 0


class ResponseCalculation(RetailCrmResponse):
    calculations: list[DeliveryCalculation] = []
