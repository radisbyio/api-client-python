from datetime import date

import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5, RetailCrmApiError
from retailcrm.v5.schemas.requests import (
    OrderHistoryFilterV4Type,
    SerializedOrder,
    SerializedOrderList,
    SerializedPayment,
)


@pytest.mark.asyncio
async def test_order_create_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_order: dict,
):
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/create").mock(
        httpx.Response(
            json={"success": "true", "id": 8888, "order": mock_order}, status_code=201
        )
    )

    create_result = await mock_retailcrm_client_v5.orders.create_order(
        SerializedOrder.model_validate(mock_order), "test_site"
    )

    assert create_result.success is True


@pytest.mark.asyncio
async def test_orders_upload_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_order: dict,
):
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/upload").mock(
        httpx.Response(json={"success": "true"}, status_code=201)
    )

    create_result = await mock_retailcrm_client_v5.orders.upload(
        SerializedOrderList([mock_order]), "test_site"
    )

    assert create_result.success is True


@pytest.mark.asyncio
async def test_orders_upload_too_many_error(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_order: dict,
):
    orders = SerializedOrderList([mock_order] * 51)

    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/upload").mock(
        httpx.Response(json={"success": "true"}, status_code=201)
    )

    with pytest.raises(ValueError) as exc_info:
        create_result = await mock_retailcrm_client_v5.orders.upload(
            orders, "test_site"
        )

    assert str(exc_info.value) == "Too many orders, only 50 are allowed"


@pytest.mark.asyncio
async def test_get_order_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_order: dict,
):
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/8888?by=externalId&site=test_site"
    ).mock(
        httpx.Response(json={"success": "true", "order": mock_order}, status_code=200)
    )

    get_order_result = await mock_retailcrm_client_v5.orders.get_order_by_id(
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
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/8888?by=externalId&site=test_site"
    ).mock(
        httpx.Response(
            json={"success": "false", "errorMsg": "Not found"}, status_code=404
        )
    )

    with pytest.raises(RetailCrmApiError) as exc_info:
        _ = await mock_retailcrm_client_v5.orders.get_order_by_id(
            order_id="8888",
            site="test_site",
        )

    assert exc_info.value.status_code == 404
    assert exc_info.value.error_msg == "Not found"


@pytest.mark.asyncio
async def test_payment_create_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_payment: dict,
):
    payment = SerializedPayment.model_validate(mock_payment)

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/payments/create"
    ).mock(httpx.Response(json={"success": "true", "id": 123}, status_code=201))

    get_order_result = await mock_retailcrm_client_v5.orders.payment_create(
        payment=payment,
        site="test_site",
    )

    assert get_order_result.success is True


@pytest.mark.asyncio
async def test_payment_edit_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_payment: dict,
):
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/payments/123/edit"
    ).mock(httpx.Response(json={"success": "true", "id": 123}, status_code=200))

    get_order_result = await mock_retailcrm_client_v5.orders.payment_edit(
        payment_id="123",
        payment=SerializedPayment.model_validate(mock_payment),
        site="test_site",
    )

    assert get_order_result.success is True


@pytest.mark.asyncio
async def test_payment_delete_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/payments/123/delete"
    ).mock(httpx.Response(json={"success": "true", "id": 123}, status_code=200))

    get_order_result = await mock_retailcrm_client_v5.orders.payment_delete(
        payment_id="123"
    )

    assert get_order_result.success is True


@pytest.mark.asyncio
async def test_orders_history_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    filter_params = {
        "limit": 20,
        "page": 1,
        "filter[sinceId]": "1111",
        "filter[startDate]": "2016-01-07",
        "filter[endDate]": "2020-04-12",
    }
    history_response = {
        "success": "true",
        "generatedAt": "2020-04-16 11:03:00",
        "history": [
            {
                "id": 7887,
                "createdAt": "2018-04-11 09:01:29",
                "created": "true",
                "source": "api",
                "field": "status",
                "apiKey": {"current": "false"},
                "oldValue": "null",
                "newValue": {"code": "new"},
                "order": {
                    "slug": 9090,
                    "summ": 0,
                    "id": 9090,
                    "number": "9090A",
                    "externalId": "v4321",
                    "orderType": "eshop-individual",
                    "orderMethod": "shopping-cart",
                    "createdAt": "2018-04-11 09:01:29",
                    "statusUpdatedAt": "2018-04-11 09:01:29",
                    "totalSumm": 0,
                    "prepaySum": 0,
                    "purchaseSumm": 0,
                    "markDatetime": "2018-04-11 09:01:29",
                    "lastName": "xxxx",
                    "firstName": "xxxx",
                    "patronymic": "xxxx",
                    "email": "maymayslt@example.com",
                    "call": "false",
                    "expired": "false",
                    "customer": {
                        "id": 5544,
                        "isContact": "false",
                        "createdAt": "2018-04-11 09:01:29",
                        "vip": "false",
                        "bad": "false",
                        "site": "retailcrm-ru",
                        "contragent": {"contragentType": "individual"},
                        "marginSumm": 0,
                        "totalSumm": 0,
                        "averageSumm": 0,
                        "ordersCount": 1,
                        "customFields": [],
                        "personalDiscount": 0,
                        "cumulativeDiscount": 0,
                        "address": {"id": 3322},
                        "lastName": "xxxx",
                        "firstName": "xxxx",
                        "patronymic": "xxxx",
                        "email": "maymays@example.com",
                        "phones": [],
                    },
                    "contragent": {"contragentType": "individual"},
                    "delivery": {
                        "cost": 0,
                        "netCost": 0,
                        "address": {"id": 2477, "countryIso": ""},
                    },
                    "site": "retailcrm-ru",
                    "status": "new",
                    "items": [
                        {
                            "bonusesChargeTotal": 0,
                            "bonusesCreditTotal": 0,
                            "id": 168,
                            "initialPrice": 4000,
                            "discounts": [],
                            "discountTotal": 400,
                            "prices": [{"price": 3600, "quantity": 1}],
                            "createdAt": "2021-08-24 00:57:34",
                            "quantity": 1,
                            "status": "new",
                            "offer": {
                                "displayName": "Сыворотка для век Коррекция морщин",
                                "id": 76,
                                "externalId": "6464",
                                "name": "Сыворотка для век Коррекция морщин",
                                "article": "EL00243",
                                "vatRate": "none",
                                "properties": {
                                    "ean": "Absolute Eye Serum",
                                    "volume": "15ml",
                                },
                                "unit": {"code": "pc", "name": "Штука", "sym": "шт."},
                            },
                            "properties": {
                                "ean": "Absolute Eye Serum",
                                "volume": "15ml",
                            },
                            "purchasePrice": 0,
                        }
                    ],
                    "fromApi": "true",
                    "shipped": "false",
                    "customFields": [],
                },
            },
            {
                "id": 386,
                "createdAt": "2021-08-24 11:54:06",
                "source": "api",
                "field": "order_product",
                "apiKey": {"current": False, "id": 1},
                "oldValue": None,
                "newValue": {"id": 207, "discounts": []},
                "order": {
                    "id": 64,
                    "externalId": "41633",
                    "site": "milfey-shop-ru",
                    "status": "new",
                },
                "item": {
                    "bonusesChargeTotal": 0,
                    "bonusesCreditTotal": 0,
                    "id": 207,
                    "initialPrice": 2640,
                    "discounts": [],
                    "discountTotal": 330,
                    "prices": [{"price": 2310, "quantity": 1}],
                    "createdAt": "2021-08-24 11:54:06",
                    "quantity": 1,
                    "status": "new",
                    "properties": [],
                    "purchasePrice": 0,
                },
            },
        ],
    }
    mock_request = respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/orders/history",
        params=filter_params,
    ).mock(httpx.Response(json=history_response, status_code=200))

    request = OrderHistoryFilterV4Type(
        since_id=1111, start_date=date(2016, 1, 7), end_date=date(2020, 4, 12)
    )

    get_order_result = await mock_retailcrm_client_v5.orders.get_orders_history(request)

    query_params = mock_request.calls.last.request.url.params

    assert get_order_result.success is True
    assert all(
        [query_params.get(key) == str(value) for key, value in filter_params.items()]
    )
