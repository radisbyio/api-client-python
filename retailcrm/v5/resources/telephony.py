from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.entities.telephony import CallEvent, CallUpload
from retailcrm.v5.schemas.requests.telephony import (
    CallEventRequest,
    CallsUploadRequest,
    ManagerRequest,
)
from retailcrm.v5.schemas.responses.telephony import (
    CallEventResponse,
    CallsUploadResponse,
    ManagerResponse,
)


class TelephonyApiResource(ApiResource):
    async def call_event(self, event: CallEvent) -> CallEventResponse:
        """
        **События звонка**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-telephony-call-event
        :param event:
        :return: CallEventResponse
        """

        request = CallEventRequest(event=event)

        response = await self._client.post(
            endpoint="/telephony/call/event",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CallEventResponse)

    async def calls_upload(self, calls: list[CallUpload]) -> CallsUploadResponse:
        """
        **Загрузка телефонных звонков**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-telephony-calls-upload
        :param calls: Звонок
        :return: CallsUploadResponse
        """

        request = CallsUploadRequest(calls=calls)

        response = await self._client.post(
            endpoint="/telephony/calls/upload",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CallsUploadResponse)

    async def manager(
        self, phone: str, details: str = None, ignore_status: str | None = None
    ) -> ManagerResponse:
        """
        **Получение ответственного менеджера**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-telephony-manager
        :param phone: Телефон
        :param details: Детальная информация
        :param ignore_status:Игнорировать статус менеджера
        :return: ManagerResponse
        """

        request = ManagerRequest(
            phone=phone, details=details, ignoreStatus=ignore_status
        )
        response = await self._client.post(
            endpoint="/telephony/manager",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, ManagerResponse)
