import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5


@pytest.mark.asyncio
async def test_reference_status_groups_success(
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
            "statuses": [
                "new"
            ]
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
                "prepayed"
            ]
        }}}
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/status-groups"
    ).mock(httpx.Response(json=mock_status_groups_response, status_code=200))

    status_groups_response = await mock_retailcrm_client_v5.references.status_groups()

    assert status_groups_response.success is True


@pytest.mark.asyncio
async def test_reference_statuses_success(
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
                "group": "new"
            },
            "complete": {
                "name": "Выполнен",
                "code": "complete",
                "active": True,
                "ordering": 10,
                "group": "complete"
            }
        }
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/reference/statuses"
    ).mock(httpx.Response(json=mock_statuses_response, status_code=200))

    statuses_response = await mock_retailcrm_client_v5.references.statuses()

    assert statuses_response.success is True
