from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.responses.settings import SettingsResponse


class SettingsApiResource(ApiResource):
    async def retrieve(self) -> SettingsResponse:
        """
        Получение настроек системы

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-settings
        """
        response = await self._client.get(
            endpoint="/settings",
        )

        return self._process_response(response, SettingsResponse)
