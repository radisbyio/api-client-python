from retailcrm import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.schemas.web_analytics import ClientId, ClientIdsUploadResponse, Source, \
    SourcesUploadResponse, Visit, VisitsUploadResponse
from retailcrm.v5.utils import pydantic_list_dumps_to_json


class WebAnalyticsController:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def client_ids_upload(
            self, client_ids: list[ClientId], site: str
    ) -> ClientIdsUploadResponse:
        """
        Пакетная загрузка clientId веб-аналитики.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-web-analytics-client-ids-upload

        :param client_ids: Массив clientId для загрузки.
        :param site: Символьный код магазина.
        :return: ClientIdsUploadResponse
        """

        response = await self._client.post(
            endpoint="/web-analytics/client-ids/upload",
            data={"clientIds": pydantic_list_dumps_to_json(client_ids, ClientId),
                  "site": site},
        )
        response_obj = ClientIdsUploadResponse.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)
        return response_obj

    async def sources_upload(self, sources: list[Source], site: str) -> SourcesUploadResponse:
        """
        Пакетная загрузка источников.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-web-analytics-sources-upload
        :param sources: Массив источников для загрузки.
        :param site: Символьный код магазина.
        :return: SourcesUploadResponse
        """

        response = await self._client.post(
            endpoint="/web-analytics/sources/upload",
            data={"sources": pydantic_list_dumps_to_json(sources, Source),
                  "site": site},
        )

        response_obj = SourcesUploadResponse.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

        return response_obj

    async def visits_upload(self, visits: list[Visit], site: str) -> VisitsUploadResponse:
        """
        Пакетная загрузка визитов.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-web-analytics-visits-upload

        :param visits: Массив визитов для загрузки.
        :param site: Символьный код магазина.
        :return: VisitsUploadResponse
        """
        response = await self._client.post(
            endpoint="/web-analytics/visits/upload",
            data={"visits": pydantic_list_dumps_to_json(visits, Visit),
                  "site": site},
        )

        response_obj = VisitsUploadResponse.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)
        return response_obj
