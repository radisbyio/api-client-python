from typing import Optional

from pydantic import BaseModel, Field

__all__ = ["RetailCrmResponse", "PaginationResponse"]


class PaginationResponse(BaseModel):
    limit: int = 0
    totalCount: int = 0
    currentPage: int = 0
    totalPageCount: int = 0


class RetailCrmResponse(BaseModel):
    success: bool = Field(False, description="Результат запроса (успешный/неуспешный)")
    pagination: Optional[PaginationResponse] = None
    errorMsg: str = Field("", description="Текст ошибки")
    errors: list[str] = Field([], description="Массив с детализациями ошибок")
