from typing import Optional

from pydantic import BaseModel, Field, field_validator, ConfigDict

from retailcrm.v5.helpers import errors_dict_validator

__all__ = ["RetailCrmResponse", "PaginationResponse"]


class BaseRetailCrmScheme(BaseModel):
    model_config = ConfigDict(use_enum_values=True)


class PaginationResponse(BaseModel):
    limit: int = 0
    totalCount: int = 0
    currentPage: int = 0
    totalPageCount: int = 0


class RetailCrmResponse(BaseModel):
    success: bool = Field(False, description="Результат запроса (успешный/неуспешный)")
    pagination: Optional[PaginationResponse] = None
    errorMsg: str = Field("", description="Текст ошибки")
    errors: dict[str, str] = Field(
        default_factory=dict, description="Массив с детализациями ошибок"
    )

    errors_validator = field_validator("errors", mode="before")(errors_dict_validator())
