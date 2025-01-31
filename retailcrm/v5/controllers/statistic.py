from retailcrm import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.schemas import RetailCrmResponse


class StatisticController:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def update(self) -> RetailCrmResponse:
        """
        Для доступа к методу необходимо разрешение analytics_write.

        Ставит в очередь задание на обновление ключевых статистических показателей в системе.
        Таймаут повторного вызова 60 сек. При более частых вызовах будет возвращаться 400 ошибка.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-statistic-update

        :param client_ids: Массив clientId для загрузки.
        :param site: Символьный код магазина.
        :return: RetailCrmResponse
        """

        response = await self._client.get(
            endpoint="/statistic/update",
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)
        return response_obj
