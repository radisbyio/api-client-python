from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas import BaseRetailCrmScheme

__all__ = ["SerializedEntityCustomer"]


class SerializedEntityCustomer(BaseRetailCrmScheme):
    site: Optional[str] = Field(None) # TODO: ???
    id: Optional[int] = Field(None, description="Внутренний ID клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    type: Optional[str] = Field(None) # TODO: ??
