from pydantic import BaseModel, Field

__all__ = ["MGTransportVisitsRequest", "MGTransportOnlineRequest"]


class MGTransportOnlineRequest(BaseModel):
    externalUserId: str = Field(None, description="GET-параметр с внешним идентификатором клиента чата")

class MGTransportVisitsRequest(BaseModel):
    externalUserId: str = Field(None, description="GET-параметр с внешним идентификатором клиента чата")
