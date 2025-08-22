from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.responses.api import ApiVersionsResponse, ApiCredentialsResponse


__all__ = ["ApiInfoApiResource"]

class ApiInfoApiResource(ApiResource):
    async def api_version(self) -> ApiVersionsResponse:
        """
        **Получение списка доступных версий API**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-api-versions

        :return: ApiVersionsResponse
        """
        response = await self._client.get(
            endpoint="/api-versions",
            use_version=False,
        )
        return self._process_response(response, ApiVersionsResponse)

    async def credentials(self) -> ApiCredentialsResponse:
        """
        **Загрузка файла на сервер**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-credentials
        :return: ApiCredentialsResponse
        """
        response = await self._client.post(
            endpoint="/credentials",
            use_version=False
        )
        return self._process_response(response, ApiCredentialsResponse)
