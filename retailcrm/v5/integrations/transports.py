import abc

from retailcrm.v5.schemas.transports import MGTransportOnlineResponse, ChatLastVisit


class IMgTransportActions(abc.ABC):
    async def online(self, externalUserId: str) -> MGTransportOnlineResponse:
        pass

    async def visits(self, externalChatId: str) -> ChatLastVisit:
        pass