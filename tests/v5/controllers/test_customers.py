import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5, RetailCrmApiError
from retailcrm.v5.schemas.requests import CustomerFilterData


@pytest.mark.asyncio
async def test_customers_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_customer: dict,
):
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers",
        params={"limit": 20, "page": 1, "filter[online]": False, "filter[vip]": True},
    ).mock(
        httpx.Response(
            json={
                "success": "true",
                "pagination": {
                    "limit": 20,
                    "totalCount": 4347,
                    "currentPage": 1,
                    "totalPageCount": 87,
                },
                "customers": [mock_customer],
            },
            status_code=200,
        )
    )

    get_customers_result = await mock_retailcrm_client_v5.customers.customers(
        filter_data=CustomerFilterData(online=False, vip=True)
    )

    assert get_customers_result.success is True


@pytest.mark.asyncio
async def test_customers_error(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    filter_data = {"online": "No", "contragentType": "individual"}

    respx_mock.get(f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers").mock(
        httpx.Response(
            json={"success": "false", "errorMsg": "Bad request"}, status_code=400
        )
    )

    with pytest.raises(RetailCrmApiError) as exc_info:
        _ = await mock_retailcrm_client_v5.customers.customers(
            filter_data=CustomerFilterData.model_validate(filter_data)
        )

    assert exc_info.value.status_code == 400
    assert exc_info.value.error_msg == "Bad request"
