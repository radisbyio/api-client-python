from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.entities.web_analytics import ClientId, Source, Visit
from retailcrm.v5.schemas.requests.web_analytics import ClientIdsUploadRequest, SourceUploadRequest, VisitsUploadRequest
from retailcrm.v5.schemas.responses.web_analytics import ClientIdsUploadResponse, SourcesUploadResponse, \
    VisitsUploadResponse


class WebAnalyticsApiResource(ApiResource):
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

        request = ClientIdsUploadRequest(
            clientIds=client_ids,
            site=site,
        )

        response = await self._client.post(
            endpoint="/web-analytics/client-ids/upload",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, ClientIdsUploadResponse)

    async def sources_upload(self, sources: list[Source], site: str) -> SourcesUploadResponse:
        """
        Пакетная загрузка источников.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-web-analytics-sources-upload
        :param sources: Массив источников для загрузки.
        :param site: Символьный код магазина.
        :return: SourcesUploadResponse
        """

        request = SourceUploadRequest(
            sources=sources,
            site=site,
        )

        response = await self._client.post(
            endpoint="/web-analytics/sources/upload",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )

        return self._process_response(response, SourcesUploadResponse)

    async def visits_upload(self, visits: list[Visit], site: str) -> VisitsUploadResponse:
        """
        Пакетная загрузка визитов.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-web-analytics-visits-upload

        :param visits: Массив визитов для загрузки.
        :param site: Символьный код магазина.
        :return: VisitsUploadResponse
        """

        request = VisitsUploadRequest(
            visits=visits,
            site=site,
        )

        response = await self._client.post(
            endpoint="/web-analytics/visits/upload",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )

        return self._process_response(response, VisitsUploadResponse)
