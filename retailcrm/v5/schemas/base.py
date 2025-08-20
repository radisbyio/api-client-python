from typing import Optional, Any

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_serializer

from retailcrm.v5.helpers import errors_dict_validator

__all__ = ["BaseRetailCrmScheme", "RetailCrmResponse", "Pagination", "SuccessResponse", "ErrorResponse"]


class BaseRetailCrmScheme(BaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        serialize_by_alias=True,
    )


class BaseRetailCrmResponse(BaseModel):
    pass


class Pagination(BaseModel):
    limit: int | None = None
    totalCount: int | None = None
    currentPage: int | None = None
    totalPageCount: int | None = None
    nextCursor: str | None = None


class SuccessResponse(BaseRetailCrmResponse):
    success: bool = Field(description="Результат запроса (успешный/неуспешный)")


class ErrorResponse(BaseRetailCrmResponse):
    success: bool = Field(description="Результат запроса (успешный/неуспешный)")
    errorMsg: str = Field(description="Текст ошибки")
    errors: dict[str, Any] = Field(
        default_factory=dict, description="Массив с детализациями ошибок"
    )

    errors_validator = field_validator("errors", mode="before")(errors_dict_validator())


class PaginatedResponse(SuccessResponse):
    pagination: Pagination


class IdResponse(SuccessResponse):
    id: int = Field(description="Внутренний ID созданного объекта")


class RetailCrmResponse(BaseModel):
    success: bool = Field(False, description="Результат запроса (успешный/неуспешный)")
    pagination: Optional[Pagination] = None
    errorMsg: str | None = Field(None, description="Текст ошибки")
    errors: dict[str, Any] = Field(
        default_factory=dict, description="Массив с детализациями ошибок"
    )

    errors_validator = field_validator("errors", mode="before")(errors_dict_validator())
