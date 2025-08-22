from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse


class ApiVersionsResponse(SuccessResponse):
    version: Optional[list[str]] = Field(default_factory=list, description="Доступные версии API")


class ApiCredentialsResponse(SuccessResponse):
    credentials: Optional[list[str]] = Field(default_factory=list, description="(deprecated) Доступные методы для ключа")
    scopes: Optional[list[str]] = Field(default_factory=list, description="Разрешенные доступы для ключа")
    siteAccess: Optional[str] = Field(None, description="Режим доступа к магазинам.")
    sitesAvailable: Optional[list[str]] = Field(default_factory=list, description="Доступные магазины")
