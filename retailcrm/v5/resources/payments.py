from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.api.payments import RetailCrmPaymentsApi
from retailcrm.v5.schemas import ApiCheckRequest, ApiCreateInvoiceRequest
from retailcrm.v5.schemas.payments import (
    ApiUpdateInvoiceRequest,
    PaymentCheckResponse,
    PaymentCreateInvoiceResponse,
    PaymentUpdateInvoiceResponse,
)


class PaymentController:
    def __init__(self, client: BaseHttpClient):
        self._api = RetailCrmPaymentsApi(client)

    async def check_payment(self, check: ApiCheckRequest) -> PaymentCheckResponse:
        response = await self._api.check(
            check_json=check.model_dump_json(exclude_unset=True)
        )
        response_obj = PaymentCheckResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def create_invoice(
        self, create_invoice: ApiCreateInvoiceRequest
    ) -> PaymentCreateInvoiceResponse:
        response = await self._api.create_invoice(
            create_invoice_json=create_invoice.model_dump_json(exclude_unset=True)
        )
        response_obj = PaymentCreateInvoiceResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def update_invoice(
        self, update_invoice: ApiUpdateInvoiceRequest
    ) -> PaymentUpdateInvoiceResponse:
        response = await self._api.update_invoice(
            update_invoice_json=update_invoice.model_dump_json(exclude_unset=True)
        )
        response_obj = PaymentUpdateInvoiceResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(
                response.status_code, response_obj.errorMsg, response_obj.errors
            )
        return response_obj
