from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import PaginatedResponse, SuccessResponse
from retailcrm.v5.schemas.entities.costs import Cost


class CostsFilterResponse(PaginatedResponse):
    costs: list[Cost] = Field(default_factory=list, description="Расход")


class CostCreateResponse(SuccessResponse):
    id: Optional[int] = Field(None, description="Внутренний ID созданного расхода")


class CostsDeleteResponse(SuccessResponse):
    count: Optional[int] = Field(None, description="Количество удаленных расходов")
    notRemovedIds: list[int] = Field(
        default_factory=list, description="Идентификаторы неудаленных расходов"
    )


class CostsUploadResponse(SuccessResponse):
    uploadedCosts: list[int] = Field(
        default_factory=list, description="Идентификаторы загруженных расходов"
    )


class CostGetResponse(SuccessResponse):
    cost: Optional[Cost] = Field(None, description="Расход")


class CostEditResponse(SuccessResponse):
    id: Optional[int] = Field(None, description="Внутренний ID расхода")
