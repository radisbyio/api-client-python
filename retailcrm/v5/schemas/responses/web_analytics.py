from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.web_analytics import ClientId, Source, Visit


class ClientIdsUploadResponse(SuccessResponse):
    failedClientIds: list[ClientId] = Field(
        default_factory=list, description="Массив clientId для загрузки"
    )


class SourcesUploadResponse(SuccessResponse):
    failedSources: list[Source] = Field(
        default_factory=list, description="Массив источников для загрузки"
    )


class VisitsUploadResponse(SuccessResponse):
    failedVisits: list[Visit] = Field(
        default_factory=list, description="Массив визитов для загрузки"
    )
