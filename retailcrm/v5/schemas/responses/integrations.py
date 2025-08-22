from typing import Optional, Any

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.integrations import IntegrationModule


class IntegrationModuleGetResponse(SuccessResponse):
    integrationModule: Optional[IntegrationModule] = Field(None, description="Интеграционный модуль")


class IntegrationModuleEditResponse(SuccessResponse):
    info: Optional[Any] = Field(None, description="	Дополнительная информация о результатах редактирования модуля")


class IntegrationModuleUpdateScopesResponse(SuccessResponse):
    apiKey: Optional[str] = Field(None, description="Новый API ключ для интеграционного модуля")