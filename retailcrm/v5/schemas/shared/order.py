from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas import BaseRetailCrmScheme


__all__ = ["SerializedEntityOrder"]


class SerializedEntityOrder(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID заказа")
    externalId: Optional[str] = Field(None, description="Внешний ID заказа")
    number: Optional[str] = Field(None, description="Номер заказа")