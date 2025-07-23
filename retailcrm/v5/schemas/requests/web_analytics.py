from pydantic import BaseModel, field_serializer

from retailcrm.v5.helpers import list_to_json_serializer
from retailcrm.v5.schemas.entities.web_analytics import ClientId, Source, Visit


class ClientIdsUploadRequest(BaseModel):
    clientIds: list[ClientId]
    site: str

    clientIds_serializer = field_serializer("clientIds")(list_to_json_serializer())


class SourceUploadRequest(BaseModel):
    sources: list[Source]
    site: str

    sources_serializer = field_serializer("sources")(list_to_json_serializer())


class VisitsUploadRequest(BaseModel):
    visits: list[Visit]
    site: str

    visits_serializer = field_serializer("visits")(list_to_json_serializer())