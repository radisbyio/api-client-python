from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.schemas.verification import (
    SmsVerificationConfirm,
    VerificationConfirmResponse,
)


class VerificationController:
    def __init__(self, client: BaseHttpClient):
        self._client = client

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
            data=verification.model_dump(exclude_none=True, by_alias=True),
        )
        response_obj = VerificationConfirmResponse.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

        return response_obj

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
        response_obj = VerificationConfirmResponse.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)
        return response_obj
