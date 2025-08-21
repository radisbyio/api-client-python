from typing import Optional, Any

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme

__all__ = ["SerializedEntityCustomer", "AbstractCustomer"]


class SerializedEntityCustomer(BaseRetailCrmScheme):
    site: Optional[str] = Field(None) # TODO: ???
    id: Optional[int] = Field(None, description="Внутренний ID клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    type: Optional[str] = Field(None) # TODO: ??
    firstName: Optional[str] = Field(None) # TODO: ??
    lastName: Optional[str] = Field(None) # TODO: ??
    patronymic: Optional[str] = Field(None) # TODO: ??
    customFields: Optional[Any] = Field(None) # TODO: ??


class AbstractCustomer(BaseRetailCrmScheme):
    site: Optional[str] = Field(None, description="Магазин, с которого пришел клиент")
    id: Optional[int] = Field(None, description="Внутренний ID клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    type: Optional[str] = Field(None, description="Тип клиента")