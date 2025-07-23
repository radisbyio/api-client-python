from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.base import SuccessResponse


class StatisticApiResource(ApiResource):
    async def update(self) -> SuccessResponse:
        """
        Ставит в очередь задание на обновление ключевых статистических показателей в системе.
        Таймаут повторного вызова 60 сек. При более частых вызовах будет возвращаться 400 ошибка.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-statistic-update

        :return: RetailCrmResponse
        """

        response = await self._client.get(
            endpoint="/statistic/update",
        )
        return self._process_response(response, SuccessResponse)
