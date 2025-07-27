from datetime import datetime

import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5
from retailcrm.v5.schemas.entities.tasks import TaskFilter, SerializedTask, TaskHistoryFilter


@pytest.mark.asyncio
async def test_task_get_all_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        'success': 'true',
        'pagination': {
            'limit': 20,
            'totalCount': 139,
            'currentPage': 1,
            'totalPageCount': 7
        },
        'tasks': [
            {
                'id': 433,
                'text': 'test task edited',
                'commentary': 'test commentary',
                'datetime': '2020-02-20 05:01',
                'createdAt': '2020-02-20 01:01:28',
                'complete': 'false',
                'performer': 15,
                'performerType': 'user'
            },
            {
                'id': 432,
                'text': 'test task edited',
                'commentary': 'test commentary',
                'datetime': '2020-02-20 05:00',
                'createdAt': '2020-02-20 01:00:07',
                'complete': 'false',
                'performer': 15,
                'performerType': 'user'
            }
        ]
    }

    respx_mock.get(f"{mock_retailcrm_client_v5.crm_url}/api/v5/tasks").mock(
        httpx.Response(
            json={"success": "true", "result": mock_response}, status_code=200
        )
    )

    tasks_response = await mock_retailcrm_client_v5.tasks.filter(TaskFilter())

    assert tasks_response.success is True


@pytest.mark.asyncio
async def test_tasks_create_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_task = {
        'id': 433,
        'text': 'test task edited',
        'commentary': 'test commentary',
        'complete': 'false',
        'phone': '+79185550000',
        'performerId': 15
    }
    mock_site = "mock_site"

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/tasks/create"
    ).mock(
        httpx.Response(
            json={'success': 'true', 'id': 434},
            status_code=201,
        )
    )

    create_response = await mock_retailcrm_client_v5.tasks.create(
        SerializedTask.model_validate(mock_task),
        mock_site
    )

    assert create_response.success is True


@pytest.mark.asyncio
async def test_tasks_history_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_history = {}

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/tasks/history"
    ).mock(httpx.Response(json={"success": "true"}, status_code=201))

    update_response = await mock_retailcrm_client_v5.tasks.history(
        TaskHistoryFilter()
    )

    assert update_response.success is True


@pytest.mark.asyncio
async def test_tasks_get_by_id_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_task = {
        'id': 433,
        'text': 'test task edited',
        'commentary': 'test commentary',
        'complete': 'false',
        'phone': '+79185550000',
        'performerId': 15
    }
    mock_id = 433

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/tasks/{mock_id}"
    ).mock(httpx.Response(json={"success": "true", "task": mock_task}, status_code=200))

    get_by_id_response = await mock_retailcrm_client_v5.tasks.get(mock_id)

    assert get_by_id_response.success is True


@pytest.mark.asyncio
async def test_tasks_history_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    # TODO: write test

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/payment/update-invoice"
    ).mock(httpx.Response(json={"success": "true"}, status_code=201))

    update_response = await mock_retailcrm_client_v5.tasks.history(
        TaskHistoryFilter()
    )

    assert update_response.success is True


# TODO: add task comments


@pytest.mark.asyncio
async def test_tasks_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_task = {
        'id': 433,
        'text': 'test task edited',
        'commentary': 'test commentary',
        'complete': 'false',
        'phone': '+79185550000',
        'performerId': 15
    }
    mock_id = 433

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/tasks/{mock_id}/edit"
    ).mock(httpx.Response(json={"success": "true", "task": mock_task}, status_code=200))

    update_response = await mock_retailcrm_client_v5.tasks.edit(
        mock_id, SerializedTask.model_validate(mock_task)
    )

    assert update_response.success is True
