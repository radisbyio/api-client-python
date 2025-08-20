from typing import Optional

from pydantic import model_serializer, Field

from retailcrm.v5.schemas import BaseRetailCrmScheme
from retailcrm.v5.schemas.filters.segments import SegmentsFilter
from retailcrm.v5.utils import pydantic_to_nested_dict


class SegmentFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(None, description="Количество элементов в ответе")
    page: Optional[int] = Field(None, description="Номер страницы с результатами")
    filter_obj: Optional[SegmentsFilter] = Field(None, description="Объект фильтра")

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }
