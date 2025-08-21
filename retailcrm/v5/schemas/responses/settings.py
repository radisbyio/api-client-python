from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.settings import Settings


class SettingsResponse(SuccessResponse):
    settings: Optional[Settings] = Field(None, description="Настройки системы")