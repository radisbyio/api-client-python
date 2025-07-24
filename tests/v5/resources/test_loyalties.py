from datetime import datetime

import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5, RetailCrmApiError
from retailcrm.v5.schemas import SerializedOrder, SerializedOrderProductOffer, SerializedOrderProduct, SerializedOrderDelivery
from retailcrm.v5.schemas.loyalty import (
    LoyaltyAccountFilterData,
    LoyaltyAccountBonusOperationsApiFilterType,
    LoyaltyBonusOperationsApiFilterType,
    LoyaltyAccountBonusApiFilterType,
    LoyaltyApiFilterData,
    SerializedCreateLoyaltyAccount,
    SerializedEditLoyaltyAccount,
    SerializedEntityCustomer,
)


@pytest.mark.asyncio
async def test_loyalties_accounts_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    filter_data = LoyaltyAccountFilterData(ids=[123])
    mock_response = {"success": True, "loyaltyAccounts": []}

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/accounts",
        params={"limit": 20, "page": 1, "filter[ids][0]": "123"},
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.loyalty.accounts_filter(filter_data)

    assert response.success is True
    assert response.loyaltyAccounts == []


@pytest.mark.asyncio
async def test_loyalties_accounts_error(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    filter_data = LoyaltyAccountFilterData(ids=[123])
    mock_response = {"success": False, "errorMsg": "Invalid filter parameters"}

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/accounts",
        params={"limit": 20, "page": 1, "filter[ids][0]": "123"},
    ).mock(httpx.Response(json=mock_response, status_code=400))

    with pytest.raises(RetailCrmApiError) as exc_info:
        await mock_retailcrm_client_v5.loyalty.accounts_filter(filter_data)

    assert exc_info.value.status_code == 400
    assert exc_info.value.error_msg == "Invalid filter parameters"


@pytest.mark.asyncio
async def test_loyalties_account_create_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    loyalty_account = SerializedCreateLoyaltyAccount(
        phoneNumber="+79999999999",
        customer=SerializedEntityCustomer(id=123),
    )
    site = "test-site"
    mock_response = {
        "success": True,
        "loyaltyAccount": {
            "id": 456
        }
    }

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/account/create",
        params={"site": site},
    ).mock(httpx.Response(json=mock_response, status_code=201))

    response = await mock_retailcrm_client_v5.loyalty.account_create(
        loyalty_account, site
    )

    assert response.success is True
    assert response.loyaltyAccount.id == 456


@pytest.mark.asyncio
async def test_loyalties_account_get_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    account_id = 123
    mock_response = {"success": True, "loyaltyAccount": {"id": account_id}}

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/account/{account_id}"
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.loyalty.account_get(account_id)

    assert response.success is True
    assert response.loyaltyAccount.id == account_id


@pytest.mark.asyncio
async def test_loyalties_account_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    account_id = 123
    loyalty_account = SerializedEditLoyaltyAccount(phoneNumber="+79999999999")
    mock_response = {
        "success": True,
        "loyaltyAccount": {
            "id": account_id
        }
    }

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/account/{account_id}/edit"
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.loyalty.account_edit(
        account_id, loyalty_account
    )

    assert response.success is True
    assert response.loyaltyAccount.id == account_id


@pytest.mark.asyncio
async def test_loyalties_account_activate_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    account_id = 123
    mock_response = {"success": True, "loyaltyAccount": {"id": account_id}}

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/account/{account_id}/activate"
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.loyalty.account_activate(account_id)

    assert response.success is True
    assert response.loyaltyAccount.id == account_id


@pytest.mark.asyncio
async def test_loyalties_account_bonus_charge_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    account_id = 123
    amount = 100.0
    comment = "Test charge"
    mock_response = {"success": True}

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/account/{account_id}/bonus/charge"
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.loyalty.account_bonus_charge(
        account_id, amount, comment
    )

    assert response.success is True


@pytest.mark.asyncio
async def test_loyalties_account_bonus_credit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    account_id = 123
    amount = 100.0
    activation_date = datetime.now()
    expire_date = datetime(2024, 12, 31)
    comment = "Test credit"
    mock_response = {"success": True}

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/account/{account_id}/bonus/credit"
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.loyalty.account_bonus_credit(
        account_id, amount, activation_date, expire_date, comment
    )

    assert response.success is True


@pytest.mark.asyncio
async def test_loyalties_account_bonus_operations_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    account_id = 123
    filter_data = LoyaltyAccountBonusOperationsApiFilterType()
    mock_response = {"success": True, "bonusOperations": []}

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/account/{account_id}/bonus/operations",
        params={"limit": 20, "page": 1},
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.loyalty.account_bonus_operations(
        account_id, filter_data
    )

    assert response.success is True
    assert response.bonusOperations == []


@pytest.mark.asyncio
async def test_loyalties_account_bonus_details_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    account_id = 123
    status = "active"
    filter_data = LoyaltyAccountBonusApiFilterType()
    mock_response = {"success": True, "bonuses": []}

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/account/{account_id}/bonus/{status}/details",
        params={"limit": 20, "page": 1},
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.loyalty.account_bonus_details(
        account_id, status, filter_data
    )

    assert response.success is True
    assert response.bonuses == []


@pytest.mark.asyncio
async def test_loyalties_bonus_operations_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    filter_data = LoyaltyBonusOperationsApiFilterType()
    mock_response = {"success": True, "bonusOperations": []}

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/bonus/operations",
        params={"limit": 20},
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.loyalty.bonus_operations(filter_data)

    assert response.success is True
    assert response.bonusOperations == []


@pytest.mark.asyncio
async def test_loyalties_calculate_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    site = "test-site"
    order = SerializedOrder(
        items=[
            SerializedOrderProduct(
                initialPrice=100,
                quantity=2,
                offer=SerializedOrderProductOffer(id=123)
            )
        ],
        delivery=SerializedOrderDelivery(cost=50)
    )
    mock_response = {"success": True}

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/calculate",
        params={"site": site},
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.loyalty.calculate(site, order)

    assert response.success is True


@pytest.mark.asyncio
async def test_loyalties_loyalties_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    filter_data = LoyaltyApiFilterData()
    mock_response = {"success": True, "loyalties": []}

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/loyalties",
        params={"limit": 20, "page": 1},
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.loyalty.loyalties_filter(filter_data)

    assert response.success is True
    assert response.loyalties == []


@pytest.mark.asyncio
async def test_loyalties_loyalties_get_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    loyalty_id = 123
    mock_response = {"success": True, "loyalty": {"id": loyalty_id}}

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/loyalty/loyalties/{loyalty_id}"
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.loyalty.loyalty_get(loyalty_id)

    assert response.success is True
    assert response.loyalty.id == loyalty_id
