from pydantic import Field
from retailcrm.v5.schemas import BaseRetailCrmScheme

__all__ = ["MgTransportVisitsRequest", "MgTransportOnlineRequest"]


class MgTransportOnlineRequest(BaseRetailCrmScheme):
    externalUserId: str = Field(None, description="GET-параметр с внешним идентификатором клиента чата")

class MgTransportVisitsRequest(BaseRetailCrmScheme):
    externalUserId: str = Field(None, description="GET-параметр с внешним идентификатором клиента чата")
