from typing import Protocol

from retailcrm.v5.schemas.requests.telephony import MgTelephonyPersonalAccountUrlRequest, MgTelephonyMakeCallUrlRequest, \
    MgTelephonyChangeUserStatusUrlRequest

__all__ = ["MGTelephonyActions"]

class MGTelephonyActions(Protocol):
    async def change_user_status_url(self, request: MgTelephonyChangeUserStatusUrlRequest) -> None:
        pass

    async def make_call_url(self, request: MgTelephonyMakeCallUrlRequest) -> None:
        pass

    async def personal_account_url(self, request: MgTelephonyPersonalAccountUrlRequest) -> None:
        pass
