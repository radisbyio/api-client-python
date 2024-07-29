from datetime import datetime
from typing import Dict, List, Optional

from pydantic import BaseModel, Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer


class PackageItemOrderProduct(BaseModel):
    id: int
    externalId: str = ""
    externalIds: List[Dict[str, str]] = []


class PackageItem(BaseModel):
    orderProduct: PackageItemOrderProduct
    quantity: float


class Package(BaseModel):
    packageId: str = ""
    weight: float = 0
    length: int = 0
    width: int = 0
    height: int = 0
    items: List[PackageItem] = []


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
    notes: str = ""
    text: str = ""


class Payment(BaseModel):
    externalId: Optional[str] = ""
    amount: float
    paid_at: Optional[datetime] = Field(None, serialization_alias="paidAt")
    comment: Optional[str] = ""
    type: str = ""
    status: str = ""

    paid_at_serializer = field_serializer("paid_at")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class Offer(BaseModel):
    id: int = 0
    externalId: str = ""
    xmlId: str = ""


class Item(BaseModel):
    markingCodes: List[str] = []
    initialPrice: float
    discountManualAmount: float = 0
    discountManualPercent: float = 0
    vatRate: str = ""
    createdAt: str = ""
    quantity: float
    comment: str = ""
    properties: List[Dict[str, str]] = []
    purchasePrice: float = 0
    ordering: int = 0
    offer: Optional[Offer] = None
    productName: str
    status: str = ""
    priceType: Dict[str, str] = {}
    externalId: str = ""
    externalIds: List[Dict[str, str]] = []


class Customer(BaseModel):
    id: int
    externalId: str = ""
    browserId: str = ""
    site: str = ""
    type: str = ""
    nickName: str = ""


class OrderContragent(BaseModel):
    contragentType: str = ""
    legalName: str = ""
    legalAddress: str = ""
    INN: str = ""
    OKPO: str = ""
    KPP: str = ""
    OGRN: str = ""
    OGRNIP: str = ""
    certificateNumber: str = ""
    certificateDate: str = ""
    BIK: str = ""
    bank: str = ""
    bankAddress: str = ""
    corrAccount: str = ""
    bankAccount: str = ""


class OrderFilterData(BaseModel):
    pass


class MGDialog(BaseModel):
    pass  # Define MGDialog model if needed
