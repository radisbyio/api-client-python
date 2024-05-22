from pydantic import BaseModel
from typing import Optional

from retailcrm.v5.schemas.base import BaseRetailCrmResponse


class CreateOrder(BaseModel):
    id: int
    externalId: Optional[str] = None


class ResponseCreateOrder(BaseRetailCrmResponse):
    order: Optional[CreateOrder] = None
