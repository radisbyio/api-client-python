from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessPaginatedResponse
from retailcrm.v5.schemas.entities.segments import Segment


class SegmentsFilterResponse(SuccessPaginatedResponse):
    segments: Optional[list[Segment]] = Field(None, description="Сегмент")