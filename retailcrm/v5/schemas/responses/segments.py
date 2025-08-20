from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import PaginatedResponse
from retailcrm.v5.schemas.entities.segments import Segment


class SegmentsFilterResponse(PaginatedResponse):
    segments: Optional[list[Segment]] = Field(None, description="Сегмент")