from pydantic import BaseModel, Field

__all__ = ["MgTransportVisitsRequest", "MgTransportOnlineRequest"]


class MgTransportOnlineRequest(BaseModel):
    externalUserId: str = Field(None, description="GET-параметр с внешним идентификатором клиента чата")

class MgTransportVisitsRequest(BaseModel):
    externalUserId: str = Field(None, description="GET-параметр с внешним идентификатором клиента чата")
