import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5, RetailCrmApiError
from retailcrm.v5.schemas.requests import SerializedOrder, SerializedPayment


@pytest.mark.asyncio
async def test_order_create_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_order: dict
):
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/create").mock(
        httpx.Response(json={'success': 'true', 'id': 8888, 'order': mock_order}, status_code=201)
    )

    create_result = await mock_retailcrm_client_v5.orders.create_order(
        SerializedOrder.model_validate(mock_order),
        "test_site"
    )

    assert create_result.success is True


@pytest.mark.asyncio
async def test_order_create_error(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_order: dict
):
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/create").mock(
        httpx.Response(json={'success': 'false', 'errorMsg': "Invalid body"}, status_code=400)
    )

    with pytest.raises(RetailCrmApiError) as exc_info:
        _ = await mock_retailcrm_client_v5.orders.create_order(
            SerializedOrder.model_validate(mock_order),
            "test_site"
        )

    assert exc_info.value.status_code == 400
    assert exc_info.value.error_msg == "Invalid body"


@pytest.mark.asyncio
async def test_get_order_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_order: dict
):
    respx_mock.get(f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/8888?by=externalId&site=test_site").mock(
        httpx.Response(json={'success': 'true', 'order': mock_order}, status_code=200)
    )

    get_order_result = await mock_retailcrm_client_v5.orders.get_order(
        order_id="8888",
        site="test_site",
    )

    assert get_order_result.success is True
    assert get_order_result.order.id == mock_order["id"]


@pytest.mark.asyncio
async def test_get_order_error(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    respx_mock.get(f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/8888?by=externalId&site=test_site").mock(
        httpx.Response(json={'success': 'false', 'errorMsg': "Not found"}, status_code=404)
    )

    with pytest.raises(RetailCrmApiError) as exc_info:
        _ = await mock_retailcrm_client_v5.orders.get_order(
            order_id="8888",
            site="test_site",
        )

    assert exc_info.value.status_code == 404
    assert exc_info.value.error_msg == "Not found"


@pytest.mark.asyncio
async def test_payment_create_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict
):
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/payments/create").mock(
        httpx.Response(json={'success': 'true', 'id': 123}, status_code=201)
    )

    get_order_result = await mock_retailcrm_client_v5.orders.payment_create(
        payment=SerializedPayment.model_validate(mock_payment),
        site="test_site",
    )

    assert get_order_result.success is True


@pytest.mark.asyncio
async def test_payment_create_error(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict
):
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/payments/create").mock(
        httpx.Response(json={'success': 'false', 'errorMsg': "Bad request"}, status_code=400)
    )

    with pytest.raises(RetailCrmApiError) as exc_info:
        _ = await mock_retailcrm_client_v5.orders.payment_create(
            payment=SerializedPayment.model_validate(mock_payment),
            site="test_site",
        )

    assert exc_info.value.status_code == 400
    assert exc_info.value.error_msg == "Bad request"


@pytest.mark.asyncio
async def test_payment_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict
):
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/payments/123/edit").mock(
        httpx.Response(json={'success': 'true', 'id': 123}, status_code=200)
    )

    get_order_result = await mock_retailcrm_client_v5.orders.payment_edit(
        payment_id="123",
        payment=SerializedPayment.model_validate(mock_payment),
        site="test_site",
    )

    assert get_order_result.success is True


@pytest.mark.asyncio
async def test_payment_edit_error(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict
):
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/payments/123/edit").mock(
        httpx.Response(json={'success': 'false', 'errorMsg': "Bad request"}, status_code=400)
    )

    with pytest.raises(RetailCrmApiError) as exc_info:
        _ = await mock_retailcrm_client_v5.orders.payment_edit(
            payment_id="123",
            payment=SerializedPayment.model_validate(mock_payment),
            site="test_site",
        )

    assert exc_info.value.status_code == 400
    assert exc_info.value.error_msg == "Bad request"


@pytest.mark.asyncio
async def test_payment_delete_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict
):
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/payments/123/delete").mock(
        httpx.Response(json={'success': 'true', 'id': 123}, status_code=200)
    )

    get_order_result = await mock_retailcrm_client_v5.orders.payment_delete(
        payment_id="123"
    )

    assert get_order_result.success is True


@pytest.mark.asyncio
async def test_payment_delete_error(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/payments/123/delete").mock(
        httpx.Response(json={'success': 'false', 'errorMsg': "Not found"}, status_code=404)
    )

    with pytest.raises(RetailCrmApiError) as exc_info:
        _ = await mock_retailcrm_client_v5.orders.payment_delete(
            payment_id="123"
        )

    assert exc_info.value.status_code == 404
    assert exc_info.value.error_msg == "Not found"
