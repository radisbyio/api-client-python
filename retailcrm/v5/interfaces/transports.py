from typing import Protocol

from retailcrm.v5.schemas.requests.transports import MGTransportOnlineRequest, MGTransportVisitsRequest
from retailcrm.v5.schemas.responses.transports import MGTransportOnlineResponse, MGTransportVisitsResponse


class MGTransportActions(Protocol):
    async def online(self, client_id: str, request: MGTransportOnlineRequest) -> MGTransportOnlineResponse:
        pass

    async def visits(self, client_id: str, request: MGTransportVisitsRequest) -> MGTransportVisitsResponse:
        pass
