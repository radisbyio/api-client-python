from pydantic import Field

from retailcrm.v5.schemas import BaseRetailCrmScheme


class CustomerPhone(BaseRetailCrmScheme):
    number: str | None = Field(None, description="Номер телефона")