from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme


# TODO: Поправить доку
class EntityWithExternalIdInput(BaseRetailCrmScheme):
    id: int | None = Field(None, description="ID")
    externalId: str | None = Field(None, description="Внешний ID")