from typing import Protocol

from retailcrm.v5.schemas.requests.transports import (
    MgTransportOnlineRequest,
    MgTransportVisitsRequest,
)
from retailcrm.v5.schemas.responses.transports import (
    MgTransportOnlineResponse,
    MgTransportVisitsResponse,
)

__all__ = ["MGTransportActions"]


class MGTransportActions(Protocol):
    async def online(
        self, request: MgTransportOnlineRequest
    ) -> MgTransportOnlineResponse:
        pass

    async def visits(
        self, request: MgTransportVisitsRequest
    ) -> MgTransportVisitsResponse:
        pass
