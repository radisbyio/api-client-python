from typing import Optional

from pydantic import BaseModel

from retailcrm.v5.schemas.base import BaseRetailCrmResponse


class Order(BaseModel):
    id: int
    externalId: Optional[str] = None
    createdAt: str
    number: Optional[str] = None

    site: Optional[str] = None
    status: str
    statusComment: Optional[str] = None


class ResponseGetOrder(BaseRetailCrmResponse):
    success: bool = False
    order: Optional[Order] = None
