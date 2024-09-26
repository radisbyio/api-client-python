from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.schemas.notifications import (
    SendNotificationResponse,
    SerializedApiNotification,
)


class NotificationsController:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def send(
        self, notification: SerializedApiNotification
    ) -> SendNotificationResponse:
        """
        Отправка оповещения

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-custom-fields
        :param notification:
        :return: SendNotificationResponse
        """
        response = await self._client.post(
            endpoint="/notifications/send",
            params={
                "notification": notification.model_dump_json(
                    exclude_none=True, by_alias=True
                )
            },
        )

        response_obj = SendNotificationResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj
