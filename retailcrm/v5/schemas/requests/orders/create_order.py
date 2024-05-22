from typing import List, Optional, Union, Dict

from pydantic import BaseModel


class TimeInterval(BaseModel):
    from_time: Optional[str]
    to_time: Optional[str]
    custom: Optional[str]


class GenericData(BaseModel):
    externalId: str = ""
    trackNumber: str = ""
    locked: bool = False
    tariff: str = ""
    pickuppointId: str = ""
    payerType: str = ""
    shipmentpointId: str = ""
    extraData: Optional[List[Dict[str, str]]] = None
    itemDeclaredValues: Optional[List[Dict[str, Union[int, float]]]] = None
    packages: Optional[List[Dict[str, Union[str, float, int, List[Dict[str, Union[int, str]]]]]]] = None


class PackageItemOrderProduct(BaseModel):
    id: int
    externalId: Optional[str]
    externalIds: Optional[List[Dict[str, str]]]


class PackageItem(BaseModel):
    orderProduct: PackageItemOrderProduct
    quantity: float


class Package(BaseModel):
    packageId: str
    weight: float
    length: int
    width: int
    height: int
    items: List[PackageItem]


class DeliveryService(BaseModel):
    name: str
    code: str = ""
    active: bool = False
    deliveryType: str = ""


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
    paidAt: Optional[str] = ""
    comment: Optional[str] = ""
    type: str = ""
    status: str = ""


class Offer(BaseModel):
    id: int = 0
    externalId: str = ""
    xmlId: str = ""


class Item(BaseModel):
    markingCodes: Optional[List[str]] = None
    initialPrice: float
    discountManualAmount: float = 0
    discountManualPercent: float = 0
    vatRate: str = ""
    createdAt: str = ""
    quantity: float
    comment: str = ""
    properties: Optional[List[Dict[str, str]]] = None
    purchasePrice: float = 0
    ordering: int = 0
    offer: Optional[Offer] = None
    productName: str
    status: str = ""
    priceType: Dict[str, str] = None
    externalId: str = ""
    externalIds: Optional[List[Dict[str, str]]] = None


class SerializedOrderDelivery(BaseModel):
    code: str = ""
    data: Optional[GenericData] = None
    service: Optional[DeliveryService] = None
    cost: float = 0
    netCost: float = 0
    date: str = ""
    time: Optional[TimeInterval] = None
    address: Optional[OrderDeliveryAddress] = None
    vatRate: str = ""


class Customer(BaseModel):
    id: int
    externalId: str = ""
    browserId: str = ""
    site: str = ""
    type: str = ""
    nickName: str = ""


class Contact(BaseModel):
    id: int
    externalId: str = ""
    browserId: str = ""
    site: str = ""


class Source(BaseModel):
    source: str = ""
    medium: str = ""
    campaign: str = ""
    keyword: str = ""
    content: str = ""


class MGDialog(BaseModel):
    pass  # Define MGDialog model if needed


class OrderContragent(BaseModel):
    contragentType: str
    legalName: str
    legalAddress: str
    INN: str
    OKPO: str
    KPP: str
    OGRN: str
    OGRNIP: str
    certificateNumber: str
    certificateDate: str
    BIK: str
    bank: str
    bankAddress: str
    corrAccount: str
    bankAccount: str


class SerializedOrder(BaseModel):
    number: str = ""
    externalId: str = ""
    privilegeType: str = ""
    countryIso: str = ""
    createdAt: str = ""
    statusUpdatedAt: str = ""
    discountManualAmount: float = 0
    discountManualPercent: float = 0
    mark: int = 0
    markDatetime: str = ""
    lastName: str = ""
    firstName: str = ""
    patronymic: str = ""
    phone: str = ""
    additionalPhone: str = ""
    email: str = ""
    call: bool = False
    expired: bool = False
    customerComment: str = ""
    managerComment: str = ""
    # contragent: OrderContragent
    statusComment: str = ""
    weight: float = 0
    length: int = 0
    width: int = 0
    height: int = 0
    shipmentDate: str = ""
    shipped: bool = False
    dialogId: Optional[MGDialog] = None
    customFields: Dict[str, str] = None
    orderType: str = ""
    orderMethod: str = ""
    customer: Optional[Customer] = None
    contact: Optional[Contact] = None
    company: Optional[Dict[str, Union[int, str]]] = None
    managerId: int = 0
    status: str = ""
    items: List[Item] = None
    delivery: Optional[SerializedOrderDelivery] = None
    source: Optional[Source] = None
    shipmentStore: str = ""
    payments: List[Payment] = None
    loyaltyEventDiscountId: int = 0
    applyRound: bool = False
    isFromCart: bool = False
    clientId: str = ""

# todo: remove
class SchemaRequestCreateOrder(BaseModel):
    site: str
    order: SerializedOrder
