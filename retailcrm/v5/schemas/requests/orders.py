from datetime import datetime, date
from typing import Dict, List, Optional, Union

from pydantic import BaseModel, Field, RootModel


class TimeInterval(BaseModel):
    from_time: str = ""
    to_time: str = ""
    custom: str = ""


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
    packages: List[
        Dict[str, Union[str, float, int, List[Dict[str, Union[int, str]]]]]
    ] = []


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
    paid_at: Optional[datetime] = Field(None, serialization_alias="paid_at")
    comment: Optional[str] = ""
    type: str = ""
    status: str = ""


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


class SerializedOrder(BaseModel):
    number: str = ""
    externalId: str = ""
    privilegeType: str = ""
    countryIso: str = ""
    created_at: Optional[datetime] = Field(None, serialization_alias="createdAt")
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
    payments: List[Payment] = []
    loyaltyEventDiscountId: int = 0
    applyRound: bool = False
    isFromCart: bool = False
    clientId: str = ""


class SerializedOrderList(RootModel):
    root: list[SerializedOrder] = []


class SerializedEntityOrder(BaseModel):
    id: int = Field(0, description="Внутренний ID заказа")
    external_id: str = Field("", alias="externalId", description="Внешний ID заказа")
    number: str = Field("", description="Номер заказа")


class SerializedPayment(BaseModel):
    externalId: Optional[str] = ""
    amount: float = 0
    paidAt: Optional[str] = ""
    comment: Optional[str] = ""
    order: Optional[SerializedEntityOrder] = None
    type: str = ""
    status: str = ""


class OrderHistoryFilterV4Type(BaseModel):
    order_id: Optional[int] = Field(
        None, serialization_alias="orderId", description="ID заказа"
    )
    since_id: Optional[int] = Field(
        None, serialization_alias="sinceId", description="Начиная с ID истории заказов"
    )
    external_id: Optional[str] = Field(
        None, serialization_alias="externalId", description="Внешний ID заказа"
    )
    start_date: Optional[date] = Field(
        None, serialization_alias="startDate", description="Дата/время изменения (от)"
    )
    end_date: Optional[date] = Field(
        None, serialization_alias="endDate", description="Дата/время изменения (до)"
    )
