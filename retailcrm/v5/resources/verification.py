from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.entities.verification import SmsVerificationConfirm
from retailcrm.v5.schemas.responses.verification import VerificationConfirmResponse


class VerificationController(ApiResource):
    async def sms_confirm(
        self, verification: SmsVerificationConfirm
    ) -> VerificationConfirmResponse:
        """
        Подтверждение верификации.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-verification-sms-confirm

        :param verification: Данные для подтверждения верификации.
        :return: VerificationConfirmResponse
        """
        response = await self._client.post(
            endpoint="/verification/sms/confirm",
            content=verification.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, VerificationConfirmResponse)

    async def sms_status(self, check_id: str) -> VerificationConfirmResponse:
        """
        Проверка статуса верификации.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-verification-sms-checkId-status

        :param check_id: Идентификатор проверки кода.
        :return: VerificationConfirmResponse
        """

        response = await self._client.get(
            endpoint=f"/verification/sms/{check_id}/status",
        )
        return self._process_response(response, VerificationConfirmResponse)
