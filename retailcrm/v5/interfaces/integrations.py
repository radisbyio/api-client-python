from typing import Protocol

from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.callbacks.entities.integrations import (
    IntegrationModuleBillingInfo,
    Register,
)
from retailcrm.v5.schemas.callbacks.responses.integrations import (
    IntegrationsConfigResponse,
    IntegrationsRegisterUrlResponse,
)
from retailcrm.v5.schemas.entities.integrations import IntegrationModule
from retailcrm.v5.schemas.entities.settings import Settings


class IntegrationActionsInterface(Protocol):
    async def activity(
        self,
        client_id: str,
        activity: IntegrationModule,
        system_url: str,
        billing_info: IntegrationModuleBillingInfo,
    ) -> SuccessResponse:
        pass

    async def settings(self, client_id: str, settings: Settings) -> SuccessResponse:
        pass


class IntegrationInterface(Protocol):
    async def config_url(self) -> IntegrationsConfigResponse:
        pass

    async def register_url(self, register: Register) -> IntegrationsRegisterUrlResponse:
        pass
