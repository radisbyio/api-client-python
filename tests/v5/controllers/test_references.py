import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5
from retailcrm.v5.schemas.references import (
    SerializedCostGroup,
    SerializedCostItem,
    SerializedCourier,
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
