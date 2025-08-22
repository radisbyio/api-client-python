from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class CodeValueModel(BaseRetailCrmScheme):
    code: str | None = Field(None, description="Код")
    value: str | None = Field(None, description="Значение")
