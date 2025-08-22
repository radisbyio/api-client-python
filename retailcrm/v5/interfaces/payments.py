from typing import Protocol

from retailcrm.v5.interfaces.integrations import IntegrationActionsInterface
from retailcrm.v5.schemas.callbacks.entities.payments import Create, ModuleApiRequest, Result
from retailcrm.v5.schemas.entities.payments import ModuleRefund

__all__ = ["PaymentsActions"]

class PaymentsActions(IntegrationActionsInterface):
    async def approve(self, client_id: str, approve: ModuleApiRequest) -> None:
        pass

    async def cancel(self, client_id: str, cancel: ModuleApiRequest) -> None:
        pass

    async def create(self, client_id: str, create: Create) -> Result:
        pass

    async def refund(self, client_id: str, refund: ModuleApiRequest) -> ModuleRefund:
        pass