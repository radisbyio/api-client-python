from pydantic import Field, field_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.integrations import IntegrationModule, Requires


class IntegrationModuleEditRequest(BaseRetailCrmScheme):
    integrationModule: IntegrationModule = Field(description="Интеграционный модуль")

    integrationModule_serializer = field_serializer("integrationModule")(to_json_serializer())

class IntegrationModuleUpdateScopesRequest(BaseRetailCrmScheme):
    requires: Requires

    requires_serializer = field_serializer("requires")(to_json_serializer())
