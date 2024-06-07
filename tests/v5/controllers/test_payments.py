from datetime import datetime

import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5
from retailcrm.v5.schemas import ApiCheckRequest, ApiCreateInvoiceRequest, ApiUpdateInvoiceRequest

@pytest.mark.asyncio
async def test_payment_check_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    check_request = ApiCheckRequest(
        invoiceUuid="577",
        amount=1,
        currency="RU",
    )

    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/payment/check").mock(
        httpx.Response(json={'success': 'true', 'result': {'success': 'true'}}, status_code=201)
    )

    check_response = await mock_retailcrm_client_v5.payments.check_payment(check_request)

    assert check_response.success is True


@pytest.mark.asyncio
async def test_payment_create_invoice_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    create_invoice_request = ApiCreateInvoiceRequest(
        paymentId=577,
        returnUrl="https://test.ru",
    )

    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/payment/create-invoice").mock(
        httpx.Response(json={'success': 'true', 'result': {'link': 'https://test.ru'}}, status_code=201)
    )

    check_response = await mock_retailcrm_client_v5.payments.create_invoice(create_invoice_request)

    assert check_response.success is True


@pytest.mark.asyncio
async def test_payment_update_invoice_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    update_invoice_request = ApiUpdateInvoiceRequest(
        invoiceUuid="577",
        paymentId="5304",
        paidAt=datetime(2024, 2, 2, 10, 21, 21),
    )

    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/payment/update-invoice").mock(
        httpx.Response(json={'success': 'true'}, status_code=201)
    )

    update_response = await mock_retailcrm_client_v5.payments.update_invoice(update_invoice_request)

    assert update_response.success is True
