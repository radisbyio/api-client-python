from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas import SuccessResponse
from retailcrm.v5.schemas.entities.payments import ApiCheckRequest, ApiCreateInvoiceRequest, ApiUpdateInvoiceRequest, \
    ApiImportInvoiceRequest
from retailcrm.v5.schemas.requests.payments import CreateInvoiceRequest, UpdateInvoiceRequest, InvoiceImportRequest
from retailcrm.v5.schemas.responses.payments import CheckResponsePayment, CreateInvoiceResponsePayment, \
    InvoiceImportResponse


class PaymentController(ApiResource):
    async def check_payment(self, check: ApiCheckRequest) -> CheckResponsePayment:
        """
        **Проверка инвойса**
        Метод позволяет проверить параметры инвойса перед списанием средств.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-payment-check
        :param check: JSON с данными для проверки
        :return: PaymentCheckResponse
        """
        response = await self._client.post(
            endpoint="/payment/check",
            json_str=check.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, CheckResponsePayment)

    async def create_invoice(
        self, create_invoice: ApiCreateInvoiceRequest
    ) -> CreateInvoiceResponsePayment:
        """
        **Создание инвойса**
        Метод позволяет создать ссылку на оплату для заданного платежа.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-payment-check
        :param create_invoice: JSON с данными инвойса
        :return: PaymentCreateInvoiceResponse
        """
        request = CreateInvoiceRequest(createInvoice=create_invoice)
        response = await self._client.post(
            endpoint="/payment/create-invoice",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, CreateInvoiceResponsePayment)

    async def update_invoice(
        self, update_invoice: ApiUpdateInvoiceRequest
    ) -> SuccessResponse:
        """
        **Изменение инвойса**
        Метод позволяет изменить данные инвойса в системе.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-payment-update-invoice
        :param update_invoice: JSON с данными инвойса
        :return: SuccessResponse
        """
        request = UpdateInvoiceRequest(updateInvoice=update_invoice)

        response = await self._client.post(
            endpoint=f"/payment/update-invoice",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )

        return self._process_response(response, SuccessResponse)

    async def invoice_import(
        self, invoice: ApiImportInvoiceRequest
    ) -> InvoiceImportResponse:
        """
        **Импорт инвойса**
        Метод позволяет импортировать инвойс.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-payment-invoice-import
        :param invoice: JSON с данными инвойса
        :return: SuccessResponse
        """
        request = InvoiceImportRequest(invoice=invoice)

        response = await self._client.post(
            endpoint=f"/payment/invoice/import",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )

        return self._process_response(response, InvoiceImportResponse)

    async def invoice(
        self, invoice_uuid: str
    ) -> SuccessResponse:
        """
        **Получение инвойса**
        Метод позволяет изменить данные инвойса в системе.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-payment-invoice-invoiceUuid
        :param invoice_uuid: UUID инвойса
        :return: SuccessResponse
        """

        response = await self._client.get(
            endpoint=f"/payment/invoice/{invoice_uuid}",
        )

        return self._process_response(response, SuccessResponse)