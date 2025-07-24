from typing import Protocol

from retailcrm.v5.schemas.requests.transports import MGTransportOnlineRequest, MGTransportVisitsRequest
from retailcrm.v5.schemas.responses.transports import MGTransportOnlineResponse, MGTransportVisitsResponse

__all__ = ["MGTransportActions"]

class MGTransportActions(Protocol):
    async def online(self, request: MGTransportOnlineRequest) -> MGTransportOnlineResponse:
        pass

    async def visits(self, request: MGTransportVisitsRequest) -> MGTransportVisitsResponse:
        pass
