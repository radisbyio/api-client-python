from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.entities.integrations import IntegrationModule
from retailcrm.v5.schemas.requests.integrations import IntegrationModuleEditRequest
from retailcrm.v5.schemas.responses.integrations import (
    IntegrationModuleEditResponse,
    IntegrationModuleGetResponse,
)

__all__ = ["IntegrationsApiResource"]


class IntegrationsApiResource(ApiResource):
    async def get(self, code: str) -> IntegrationModuleGetResponse:
        """
        **Получение интеграционного модуля**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-integration-modules-code
        :param code: Символьный код экземпляра модуля.
        :return: IntegrationModuleGetResponse
        """
        response = await self._client.get(
            endpoint=f"/integration-modules/{code}",
        )
        return self._process_response(response, IntegrationModuleGetResponse)

    async def edit(
        self, code: str, integration_module: IntegrationModule
    ) -> IntegrationModuleEditResponse:
        """
        **Создание/редактирование интеграционного модуля**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-integration-modules-code-edit
        :param code: Символьный код экземпляра модуля.
        :param integration_module: Объект интеграционного модуля.
        :return: IntegrationModuleEditResponse
        """
        request = IntegrationModuleEditRequest(integrationModule=integration_module)
        response = await self._client.post(
            endpoint=f"/integration-modules/{code}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, IntegrationModuleEditResponse)
