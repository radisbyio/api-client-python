from datetime import datetime, date

import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5, RetailCrmApiError
from retailcrm.v5.enums import SexTypes
from retailcrm.v5.schemas import CustomerFilterData, SerializedCustomer, CustomerPhone, CustomerAddress, \
    SerializedSource


@pytest.mark.asyncio
async def test_customers_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_customer: dict,
):
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers",
        params={"limit": 20, "page": 1, "filter[online]": False, "filter[vip]": True, "filter[sex]": "male"},
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
        filter_data=CustomerFilterData(online=False, vip=True, sex=SexTypes.MALE)
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


@pytest.mark.asyncio
async def test_create_customer_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    customer_request = SerializedCustomer(
        externalId="ext_customer_123",
        firstName="John",
        lastName="Doe",
        email="john.doe@example.com",
        phones=[CustomerPhone(number="+15551234567")],
        birthday=date(1980, 1, 1),
        createdAt=datetime(2023, 11, 9, 10, 00, 00),
        address=CustomerAddress(city="New York"),
        source=SerializedSource(source="website", medium="referral"),
    )

    mock_response = {"success": True, "id": 12345}
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers/create"
    ).mock(httpx.Response(json=mock_response, status_code=201))

    response = await mock_retailcrm_client_v5.customers.create(customer_request, "site")

    assert response.success is True
    assert response.id == 12345
