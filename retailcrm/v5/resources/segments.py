from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.filters.segments import SegmentsFilter
from retailcrm.v5.schemas.requests.segments import SegmentFilterRequest
from retailcrm.v5.schemas.responses.segments import SegmentsFilterResponse
from retailcrm.v5.schemas.responses.settings import SettingsResponse


class SegmentsApiResource(ApiResource):
    async def filter(
        self, filter_obj: SegmentsFilter | None = None, limit: int = 20, page: int = 1
    ) -> SegmentsFilterResponse:
        """
        Получение списка пользовательских сегментов

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-segments
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_obj: Фильтр
        :return: SegmentsFilterResponse
        """
        request = SegmentFilterRequest(limit=limit, page=page, filter_obj=filter_obj)
        response = await self._client.get(
            endpoint="/segments",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )

        return self._process_response(response, SegmentsFilterResponse)
