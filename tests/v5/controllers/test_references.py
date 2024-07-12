import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5
from retailcrm.v5.schemas.references import (
    SerializedCostGroup,
    SerializedCostItem,
    SerializedCourier, SerializedOrderMethod, SerializedOrderType, SerializedPaymentStatus, SerializedPaymentType,
    SerializedPriceType, SerializedOrderProductStatus, SerializedSite,
)


@pytest.mark.asyncio
async def test_cost_groups_get_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_status_groups_response = {
        "success": True,
        "costGroups": [
            {
                "code": "product-cost",
                "name": "Стоимость товара",
                "ordering": 990,
                "active": True,
                "color": "#22C993",
            },
        ],
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/cost-groups"
    ).mock(httpx.Response(json=mock_status_groups_response, status_code=200))

    cost_groups_response = await mock_retailcrm_client_v5.references.cost_groups()

    assert cost_groups_response.success is True


@pytest.mark.asyncio
async def test_cost_groups_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_status_groups_response = {
        "success": True,
    }
    mock_code = "product-cost"
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/cost-groups/{mock_code}/edit"
    ).mock(httpx.Response(json=mock_status_groups_response, status_code=200))

    cost_groups_edit_response = (
        await mock_retailcrm_client_v5.references.cost_groups_edit(
            code=mock_code,
            cost_group=SerializedCostGroup(
                active=False,
            ),
        )
    )

    assert cost_groups_edit_response.success is True


@pytest.mark.asyncio
async def test_cost_items_get_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_cost_items_response = {
        "success": True,
        "costItems": [
            {
                "code": "products-purchase-price",
                "name": "Закупочная стоимость товаров",
                "group": "product-cost",
                "ordering": 990,
                "active": True,
                "appliesToOrders": False,
                "type": "var",
                "appliesToUsers": False,
            },
        ],
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/cost-items"
    ).mock(httpx.Response(json=mock_cost_items_response, status_code=200))

    cost_items_response = await mock_retailcrm_client_v5.references.cost_items()

    assert cost_items_response.success is True


@pytest.mark.asyncio
async def test_cost_items_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_cost_items_edit_response = {
        "success": True,
    }
    mock_code = "delivery-cost"
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/cost-items/{mock_code}/edit"
    ).mock(httpx.Response(json=mock_cost_items_edit_response, status_code=200))

    cost_items_edit_response = (
        await mock_retailcrm_client_v5.references.cost_items_edit(
            code=mock_code,
            cost_item=SerializedCostItem(
                active=False,
            ),
        )
    )

    assert cost_items_edit_response.success is True


@pytest.mark.asyncio
async def test_countries_get_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_countries_response = {
        "success": True,
        "countriesIso": ["RU", "UA", "BY", "KZ"],
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/countries"
    ).mock(httpx.Response(json=mock_countries_response, status_code=200))

    cost_items_response = await mock_retailcrm_client_v5.references.countries()

    assert cost_items_response.success is True


@pytest.mark.asyncio
async def test_couriers_get_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_couriers_response = {
        "success": True,
        "couriers": [
            {
                "id": 1,
                "firstName": "Иван",
                "lastName": "Иванов",
                "patronymic": "Иванович",
                "active": True,
                "phone": {},
                "description": "19",
            }
        ],
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/couriers"
    ).mock(httpx.Response(json=mock_couriers_response, status_code=200))

    cost_items_response = await mock_retailcrm_client_v5.references.couriers()

    assert cost_items_response.success is True


@pytest.mark.asyncio
async def test_couriers_create_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_couriers_create_response = {
        "success": True,
    }
    (
        respx_mock.post(
            f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/couriers/create"
        ).mock(httpx.Response(json=mock_couriers_create_response, status_code=200))
    )

    couriers_create_response = (
        await mock_retailcrm_client_v5.references.couriers_create(
            courier=SerializedCourier(
                firstName="Иван",
                lastName="Иванов",
                patronymic="Иванович",
                active=True,
                phone=None,
                description="19",
            )
        )
    )

    assert couriers_create_response.success is True


@pytest.mark.asyncio
async def test_couriers_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_couriers_edit_response = {
        "success": True,
    }
    mock_id = 10

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/couriers/{mock_id}/edit"
    ).mock(httpx.Response(json=mock_couriers_edit_response, status_code=200))

    couriers_edit_response = await mock_retailcrm_client_v5.references.couriers_edit(
        courier_id=10, courier=SerializedCourier(description="19")
    )

    assert couriers_edit_response.success is True


#####################################

@pytest.mark.asyncio
async def test_order_methods_get_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_order_methods_response = {
        "success": True,
        "orderMethods": {
            "phone": {
                "name": "По телефону",
                "code": "phone",
                "active": True,
                "defaultForCrm": True,
                "defaultForApi": True
            },
        }
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/order-methods"
    ).mock(httpx.Response(json=mock_order_methods_response, status_code=200))

    order_methods_response = await mock_retailcrm_client_v5.references.order_methods()

    assert order_methods_response.success is True


@pytest.mark.asyncio
async def test_order_methods_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_order_methods_edit_response = {
        "success": True,
    }
    mock_code = "phone"
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/order-methods/{mock_code}/edit"
    ).mock(httpx.Response(json=mock_order_methods_edit_response, status_code=200))

    order_methods_edit_response = await mock_retailcrm_client_v5.references.order_methods_edit(
        code=mock_code,
        order_method=SerializedOrderMethod(
            active=True
        )
    )

    assert order_methods_edit_response.success is True


@pytest.mark.asyncio
async def test_order_types_get_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_order_types_response = {
        "success": True,
        "orderTypes": {
            "main": {
                "name": "Основной",
                "code": "main",
                "active": True,
                "defaultForCrm": True,
                "defaultForApi": True,
                "ordering": 1
            }
        }
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/order-types"
    ).mock(httpx.Response(json=mock_order_types_response, status_code=200))

    order_types_response = await mock_retailcrm_client_v5.references.order_types()

    assert order_types_response.success is True


@pytest.mark.asyncio
async def test_order_types_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_order_types_edit_response = {
        "success": True,
    }
    mock_code = "main"
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/order-types/{mock_code}/edit"
    ).mock(httpx.Response(json=mock_order_types_edit_response, status_code=200))

    order_types_edit_response = (
        await mock_retailcrm_client_v5.references.order_types_edit(
            code=mock_code,
            order_type=SerializedOrderType(
                active=False,
            )
        )
    )

    assert order_types_edit_response.success is True


@pytest.mark.asyncio
async def test_payment_statuses_get_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_payment_statuses_response = {
        "success": True,
        "paymentStatuses": {
            "not-paid": {
                "name": "Не оплачен",
                "code": "not-paid",
                "active": True,
                "defaultForCrm": False,
                "defaultForApi": False,
                "paymentComplete": False,
                "ordering": 10,
                "paymentTypes": [
                    "bank-card",
                    "bank-transfer",
                    "beznal",
                    "kassa",
                    "credit",
                    "cash",
                    "e-money"
                ]
            },
        }
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/payment-statuses"
    ).mock(httpx.Response(json=mock_payment_statuses_response, status_code=200))

    payment_statuses_response = await mock_retailcrm_client_v5.references.payment_statuses()

    assert payment_statuses_response.success is True


@pytest.mark.asyncio
async def test_payment_statuses_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_payment_statuses_edit_response = {
        "success": True,
    }
    mock_code = "invoice"
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/payment-statuses/{mock_code}/edit"
    ).mock(httpx.Response(json=mock_payment_statuses_edit_response, status_code=200))

    payment_statuses_edit_response = (
        await mock_retailcrm_client_v5.references.payment_statuses_edit(
            code=mock_code,
            payment_status=SerializedPaymentStatus(
                active=False,
            ),
        )
    )

    assert payment_statuses_edit_response.success is True


@pytest.mark.asyncio
async def test_payment_types_get_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_payment_types_response = {
        "success": True,
        "paymentTypes": {
            "cash": {
                "name": "Наличные",
                "code": "cash",
                "active": True,
                "defaultForCrm": False,
                "defaultForApi": False,
                "deliveryTypes": [
                    "courier",
                    "self-delivery",
                    "evropochta",
                    "evropochta-3",
                    "evropochta-2"
                ],
                "paymentStatuses": [
                    "not-paid",
                    "invoice",
                    "wait-approved",
                    "payment-start",
                    "canceled",
                    "fail",
                    "paid",
                    "returned"
                ],
                "sites": []
            },
        }
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/payment-types"
    ).mock(httpx.Response(json=mock_payment_types_response, status_code=200))

    payment_types_response = await mock_retailcrm_client_v5.references.payment_types()

    assert payment_types_response.success is True


@pytest.mark.asyncio
async def test_payment_types_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    payment_types_edit_response = {
        "success": True,
    }
    mock_code = "cash"
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/payment-types/{mock_code}/edit"
    ).mock(httpx.Response(json=payment_types_edit_response, status_code=200))

    payment_types_edit_response = (
        await mock_retailcrm_client_v5.references.payment_types_edit(
            code=mock_code,
            payment_type=SerializedPaymentType(
                active=False,
            ),
        )
    )

    assert payment_types_edit_response.success is True


@pytest.mark.asyncio
async def test_price_types_get_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_price_types_response = {
        "success": True,
        "priceTypes": [
            {
                "id": 2,
                "code": "base",
                "name": "Базовая",
                "active": True,
                "default": True,
                "geo": [],
                "groups": [],
                "ordering": 991,
                "currency": "BYN"
            }
        ]
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/price-types"
    ).mock(httpx.Response(json=mock_price_types_response, status_code=200))

    price_types_response_response = await mock_retailcrm_client_v5.references.price_types()

    assert price_types_response_response.success is True


@pytest.mark.asyncio
async def test_price_types_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_cost_items_edit_response = {
        "success": True,
    }
    mock_code = "delivery-cost"
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/price-types/{mock_code}/edit"
    ).mock(httpx.Response(json=mock_cost_items_edit_response, status_code=200))

    cost_items_edit_response = (
        await mock_retailcrm_client_v5.references.price_types_edit(
            code=mock_code,
            price_type=SerializedPriceType(
                active=False,
            )
        )
    )

    assert cost_items_edit_response.success is True


@pytest.mark.asyncio
async def test_product_statuses_get_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_product_statuses_response = {
        "success": True,
        "productStatuses": {
            "new": {
                "code": "new",
                "ordering": 10,
                "active": True,
                "createdAt": "2024-05-29 00:00:20",
                "cancelStatus": False,
                "name": "Добавлен"
            },
        }
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/product-statuses"
    ).mock(httpx.Response(json=mock_product_statuses_response, status_code=200))

    product_statuses_response = await mock_retailcrm_client_v5.references.product_statuses()

    assert product_statuses_response.success is True


@pytest.mark.asyncio
async def test_product_statuses_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_product_statuses_edit_response = {
        "success": True,
    }
    mock_code = "new"
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/product-statuses/{mock_code}/edit"
    ).mock(httpx.Response(json=mock_product_statuses_edit_response, status_code=200))

    product_statuses_edit_response = (
        await mock_retailcrm_client_v5.references.product_statuses_edit(
            code=mock_code,
            product_status=SerializedOrderProductStatus(
                active=False,
            ),
        )
    )

    assert product_statuses_edit_response.success is True


@pytest.mark.asyncio
async def test_sites_get_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_sites_response = {
        "success": True,
        "sites": {
            "milfey": {
                "catalogId": "3",
                "isCatalogMainSite": True,
                "isDemo": False,
                "id": 3,
                "name": "milfey",
                "code": "milfey",
                "defaultForCrm": False,
                "ymlUrl": "https://milfey-shop.ru/retailcrm.xml",
                "loadFromYml": False,
                "catalogUpdatedAt": "2024-06-01 23:40:58",
                "catalogLoadingAt": "2024-06-01 23:40:58",
                "ordering": 990,
                "countryIso": "",
                "currency": "BYN"
            },
        }
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/sites"
    ).mock(httpx.Response(json=mock_sites_response, status_code=200))

    sites_response = await mock_retailcrm_client_v5.references.sites()

    assert sites_response.success is True


@pytest.mark.asyncio
async def test_sites_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_sites_edit_response = {
        "success": True,
        "id": 10
    }
    mock_code = "milfey"
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/sites/{mock_code}/edit"
    ).mock(httpx.Response(json=mock_sites_edit_response, status_code=200))

    sites_edit_response = (
        await mock_retailcrm_client_v5.references.sites_edit(
            code=mock_code,
            site= SerializedSite(
                defaultForCrm=False,
            ),
        )
    )

    assert sites_edit_response.success is True


#####################################


@pytest.mark.asyncio
async def test_status_groups_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_status_groups_response = {
        "success": True,
        "statusGroups": {
            "new": {
                "name": "Новый",
                "code": "new",
                "active": True,
                "ordering": 10,
                "process": False,
                "statuses": ["new"],
            },
            "approval": {
                "name": "Согласование",
                "code": "approval",
                "active": True,
                "ordering": 20,
                "process": True,
                "statuses": [
                    "availability-confirmed",
                    "offer-analog",
                    "ready-to-wait",
                    "waiting-for-arrival",
                    "client-confirmed",
                    "prepayed",
                ],
            },
        },
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/status-groups"
    ).mock(httpx.Response(json=mock_status_groups_response, status_code=200))

    status_groups_response = await mock_retailcrm_client_v5.references.status_groups()

    assert status_groups_response.success is True


@pytest.mark.asyncio
async def test_statuses_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_payment: dict,
):
    mock_statuses_response = {
        "success": True,
        "statuses": {
            "new": {
                "name": "Новый",
                "code": "new",
                "active": True,
                "ordering": 10,
                "group": "new",
            },
            "complete": {
                "name": "Выполнен",
                "code": "complete",
                "active": True,
                "ordering": 10,
                "group": "complete",
            },
        },
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/statuses"
    ).mock(httpx.Response(json=mock_statuses_response, status_code=200))

    statuses_response = await mock_retailcrm_client_v5.references.statuses()

    assert statuses_response.success is True
