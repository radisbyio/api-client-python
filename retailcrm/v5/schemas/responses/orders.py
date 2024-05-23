from typing import Optional

from pydantic import BaseModel

from retailcrm.v5.schemas.base import RetailCrmResponse


class CreateOrder(BaseModel):
    id: int
    externalId: Optional[str] = None


class ResponseCreateOrder(RetailCrmResponse):
    order: Optional[CreateOrder] = None


class Order(BaseModel):
    id: int
    externalId: str = ""
    createdAt: str = ""
    number: str = ""

    site: str = ""
    status: str = ""
    statusComment: str = ""


class ResponseGetOrder(RetailCrmResponse):
    order: Optional[Order] = None


class ResponseEditOrder(RetailCrmResponse):
    id: Optional[int] = None
    order: Optional[Order] = None


class ResponseCreateOrderPayment(RetailCrmResponse):
    id: Optional[int] = 0


class ResponseEditOrderPayment(RetailCrmResponse):
    id: Optional[int] = 0


class ResponseDeleteOrderPayment(RetailCrmResponse):
    pass
