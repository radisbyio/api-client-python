from datetime import datetime

import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5, RetailCrmApiError
from retailcrm.v5.enums.user_statuses import UserStatuses
from retailcrm.v5.schemas import responses, entities


@pytest.mark.asyncio
async def test_users_filter_groups_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": True,
        "pagination": {"totalCount": 2, "limit": 20, "page": 1, "pages": 1},
        "groups": [
            {"code": "group1", "name": "Group One"},
            {"code": "group2", "name": "Group Two"},
        ],
    }

    respx_mock.get(f"{mock_retailcrm_client_v5.crm_url}/api/v5/user-groups").mock(
        httpx.Response(json=mock_response, status_code=200)
    )

    response = await mock_retailcrm_client_v5.users.filter_groups(limit=20, page=1)


    assert isinstance(response, responses.users.UserGroupsResponse)
    assert response.success is True
    assert response.pagination.totalCount == 2
    assert len(response.groups) == 2
    assert response.groups[0].code == "group1"


@pytest.mark.asyncio
async def test_users_filter_groups_failure(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": False,
        "errorMsg": "Invalid limit or page.",
    }
    respx_mock.get(f"{mock_retailcrm_client_v5.crm_url}/api/v5/user-groups").mock(
        httpx.Response(json=mock_response, status_code=400)
    )

    with pytest.raises(RetailCrmApiError) as exc_info:
        await mock_retailcrm_client_v5.users.filter_groups(limit=0)

    assert exc_info.value.status_code == 400
    assert exc_info.value.error_msg == "Invalid limit or page."


@pytest.mark.asyncio
async def test_users_filter_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    filter_obj = entities.users.ApiUserFilter(
        online=True,
        email="test@example.com",
        groups=["managers"],
        createdAtFrom=datetime(2023, 1, 1, 10, 0, 0),
    )
    mock_response = {
        "success": True,
        "pagination": {"totalCount": 1, "limit": 20, "page": 1, "pages": 1},
        "users": [
            {
                "id": 123,
                "email": "test@example.com",
                "online": True,
                "active": True,
                "status": "active",
                "createdAt": "2023-01-01 10:00:00",
                "groups": [
                    {
                        "id": 1,
                        "name": "test_group",
                        "code": "test_group"
                    }
                ],
            }
        ],
    }

    expected_params = {
        "limit": 20,
        "page": 1,
        "filter[online]": 1,
        "filter[email]": "test@example.com",
        "filter[groups][0]": "managers",
        "filter[createdAtFrom]": "2023-01-01 10:00:00",
    }

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/users",
        params=expected_params,
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.users.filter(filter_obj=filter_obj)

    assert isinstance(response, responses.users.UserListResponse)
    assert response.success is True
    assert response.pagination.totalCount == 1
    assert len(response.users) == 1
    assert response.users[0].id == 123
    assert response.users[0].email == "test@example.com"
    assert response.users[0].online is True


@pytest.mark.asyncio
async def test_users_filter_failure_no_results(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    filter_obj = entities.users.ApiUserFilter(email="nonexistent@example.com")
    mock_response = {
        "success": True,  # API might return success even if no users match
        "pagination": {"totalCount": 0, "limit": 20, "page": 1, "pages": 0},
        "users": [],
    }

    expected_params = {
        "limit": 20,
        "page": 1,
        "filter[email]": "nonexistent@example.com",
    }

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/users",
        params=expected_params,
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.users.filter(filter_obj=filter_obj)

    assert isinstance(response, responses.users.UserListResponse)
    assert response.success is True
    assert response.pagination.totalCount == 0
    assert len(response.users) == 0


@pytest.mark.asyncio
async def test_users_user_by_id_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    user_id = 456
    mock_response = {
        "success": True,
        "user": {
            "id": user_id,
            "email": "single_user@example.com",
            "online": False,
            "active": True,
            "createdAt": "2022-05-15 10:00:00",
        },
    }
    respx_mock.get(f"{mock_retailcrm_client_v5.crm_url}/api/v5/users/{user_id}").mock(
        httpx.Response(json=mock_response, status_code=200)
    )

    response = await mock_retailcrm_client_v5.users.user(user_id)

    assert isinstance(response, responses.users.UserResponse)
    assert response.success is True
    assert response.user.id == user_id
    assert response.user.email == "single_user@example.com"
    assert response.user.online is False


@pytest.mark.asyncio
async def test_users_user_by_id_failure_not_found(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    user_id = 999
    mock_response = {"success": False, "errorMsg": "User not found."}
    respx_mock.get(f"{mock_retailcrm_client_v5.crm_url}/api/v5/users/{user_id}").mock(
        httpx.Response(json=mock_response, status_code=404)
    )

    with pytest.raises(RetailCrmApiError) as exc_info:
        await mock_retailcrm_client_v5.users.user(user_id)

    assert exc_info.value.status_code == 404
    assert exc_info.value.error_msg == "User not found."


@pytest.mark.asyncio
async def test_users_set_status_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    user_id = 789
    new_status = UserStatuses.BUSY
    mock_response = {
        "success": True,
    }

    expected_params = {"status": UserStatuses.BUSY.value}
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/users/{user_id}/status",
        params=expected_params,
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.users.user_set_status(user_id, new_status)

    assert response.success is True


@pytest.mark.asyncio
async def test_users_set_status_failure_user_not_found(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    user_id = 9999
    new_status = UserStatuses.BUSY
    mock_response = {"success": False, "errorMsg": f"User with ID {user_id} not found."}
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/users/{user_id}/status",
        params={"status": new_status.value},
    ).mock(httpx.Response(json=mock_response, status_code=404))

    with pytest.raises(RetailCrmApiError) as exc_info:
        await mock_retailcrm_client_v5.users.user_set_status(user_id, new_status)

    assert exc_info.value.status_code == 404
    assert exc_info.value.error_msg == f"User with ID {user_id} not found."
