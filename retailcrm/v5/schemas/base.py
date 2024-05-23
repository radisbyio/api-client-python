from typing import Optional

from pydantic import BaseModel


class PaginationResponse(BaseModel):
    limit: int = 0
    totalCount: int = 0
    currentPage: int = 0
    totalPageCount: int = 0


class RetailCrmResponse(BaseModel):
    success: bool = False
    pagination: Optional[PaginationResponse] = None
    errorMsg: str = ""
