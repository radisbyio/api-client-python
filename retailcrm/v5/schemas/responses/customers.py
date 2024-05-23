from datetime import date, datetime
from typing import Annotated, List, Optional

from pydantic import BaseModel, BeforeValidator

from retailcrm.v5.schemas.base import RetailCrmResponse


def check_custom_field(v: list | dict) -> dict:
    if isinstance(v, list):
        return {}
    return v


class CustomerContragent(BaseModel):
    contragentType: str = ""
    legalName: str = ""
    legalAddress: str = ""
    INN: str = ""
    OKPO: str = ""
    KPP: str = ""
    OGRN: str = ""
    OGRNIP: str = ""
    certificateNumber: str = ""
    certificateDate: Optional[datetime] = None
    BIK: str = ""
    bank: str = ""
    bankAddress: str = ""
    corrAccount: str = ""
    bankAccount: str = ""


class CustomerTagLink(BaseModel):
    name: str = ""
    colorCode: str = ""
    attached: bool = False


class SerializedSource(BaseModel):
    source: str = ""
    medium: str = ""
    campaign: str = ""
    keyword: str = ""
    content: str = ""


class MGChannel(BaseModel):
    id: int = 0
    externalId: int = 0
    type: str = ""
    active: bool = False
    name: str = ""


class MGCustomer(BaseModel):
    id: int = 0
    externalId: int = 0
    mgChannel: MGChannel = None


class CustomerAddress(BaseModel):
    id: int = 0
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
    notes: str = ""
    text: str = ""
    externalId: str = ""
    name: str = ""


class Segment(BaseModel):
    id: int = 0
    code: str = ""
    name: str = ""
    createdAt: Optional[datetime] = None
    isDynamic: bool = False
    customersCount: int = 0
    active: bool = False


class CustomerPhone(BaseModel):
    number: str = ""


class Customer(BaseModel):
    type: str = ""
    id: int = 0
    externalId: str = ""
    isContact: bool = False
    createdAt: Optional[datetime] = None
    managerId: int = 0
    vip: bool = False
    bad: bool = False
    site: str = ""
    contragent: Optional[CustomerContragent] = None
    tags: List[CustomerTagLink] = []
    firstClientId: str = ""
    lastClientId: str = ""
    customFields: Annotated[dict, BeforeValidator(check_custom_field)] = {}
    avgMarginSumm: float = 0
    marginSumm: float = 0
    totalSumm: float = 0
    averageSumm: float = 0
    ordersCount: int = 0
    costSumm: float = 0
    personalDiscount: float = 0
    cumulativeDiscount: float = 0
    discountCardNumber: str = ""
    address: Optional[CustomerAddress] = None
    segments: List[Segment] = []
    maturationTime: int = 0
    firstName: str = ""
    lastName: str = ""
    patronymic: str = ""
    sex: str = ""
    presumableSex: str = ""
    email: str = ""
    emailMarketingUnsubscribedAt: Optional[datetime] = None
    phones: List[CustomerPhone] = []
    birthday: Optional[date] = None
    source: Optional[SerializedSource] = None
    mgCustomers: List[MGCustomer] = []
    photoUrl: str = ""


class ResponseCustomers(RetailCrmResponse):
    customers: List[Customer] = []
