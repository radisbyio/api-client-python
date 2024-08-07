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



