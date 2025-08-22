from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme

__all__ = ["SerializedEntityOrder", "AbstractOrder"]


class SerializedEntityOrder(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID заказа")
    externalId: Optional[str] = Field(None, description="Внешний ID заказа")
    number: Optional[str] = Field(None, description="Номер заказа")


class AbstractOrder(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID заказа")
    externalId: Optional[str] = Field(None, description="Внешний ID заказа")
    number: Optional[str] = Field(None, description="Номер заказа")
    site: Optional[str] = Field(None, description="Магазин")
