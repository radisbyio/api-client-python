from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.notifications import SerializedApiNotification
from retailcrm.v5.schemas.requests.notifications import SendNotificationRequest


class NotificationsApiResource(ApiResource):
    async def send(self, notification: SerializedApiNotification) -> SuccessResponse:
        """
        Отправка оповещения

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-custom-fields
        :param notification:
        :return: SendNotificationResponse
        """

        request = SendNotificationRequest(
            notification=notification,
        )
        response = await self._client.post(
            endpoint="/notifications/send",
            content=request.model_dump_json(exclude_unset=True, by_alias=True),
        )
        return self._process_response(response, SuccessResponse)
