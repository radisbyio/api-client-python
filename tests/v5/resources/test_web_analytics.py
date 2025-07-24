from datetime import datetime

import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5, RetailCrmApiError
from retailcrm.v5.schemas.entities.web_analytics import (
    ClientId, Source, Visit,
)
from retailcrm.v5.schemas.responses.web_analytics import (
    ClientIdsUploadResponse,
    VisitsUploadResponse,
    SourcesUploadResponse
)


@pytest.mark.asyncio
async def test_client_ids_upload_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    client_ids_data = [
        {"value": "client_id_1", "site": "test_site"},
        {"value": "client_id_2", "createdAt": "2024-07-24 10:00:00", "site": "test_site"},
    ]
    client_ids = [ClientId.model_validate(data) for data in client_ids_data]

    mock_response = {
        "success": True,
        "failedClientIds": [],
    }

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/web-analytics/client-ids/upload"
    ).mock(httpx.Response(json=mock_response, status_code=201))

    response = await mock_retailcrm_client_v5.web_analytics.client_ids_upload(client_ids, site="site")

    assert isinstance(response, ClientIdsUploadResponse)
    assert response.success is True
    assert response.failedClientIds == []


@pytest.mark.asyncio
async def test_client_ids_upload_failure(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    client_ids_data = [{"value": "client_id_1"}]
    client_ids = [ClientId.model_validate(data) for data in client_ids_data]

    mock_response = {
        "success": False,
        "errorMsg": "Invalid request parameters",
        "errors": {
            "site": "This field is required"
        },
    }

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/web-analytics/client-ids/upload"
    ).mock(httpx.Response(json=mock_response, status_code=400))

    with pytest.raises(RetailCrmApiError) as exc_info:
        await mock_retailcrm_client_v5.web_analytics.client_ids_upload(client_ids, site="site")

    assert exc_info.value.status_code == 400
    assert exc_info.value.error_msg == "Invalid request parameters"
    assert exc_info.value.errors == {"site": "This field is required"}


@pytest.mark.asyncio
async def test_sources_upload_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    sources_data = [
        {
            "source": "google",
            "medium": "organic",
            "clientId": "client_id_1",
            "site": "test_site"
        },
        {
            "source": "facebook",
            "medium": "cpc",
            "order": {"id": 123},
            "site": "test_site"
        }
    ]
    sources = [Source.model_validate(data) for data in sources_data]

    mock_response = {
        "success": True,
        "failedSources": []
    }
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/web-analytics/sources/upload"
    ).mock(httpx.Response(json=mock_response, status_code=201))

    response = await mock_retailcrm_client_v5.web_analytics.sources_upload(sources, site="test_site")

    assert isinstance(response, SourcesUploadResponse)
    assert response.success is True
    assert response.failedSources == []


@pytest.mark.asyncio
async def test_sources_upload_failure(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    sources_data = [
        {"source": "google", "medium": "organic"}  # Missing clientId and site
    ]
    sources = [Source.model_validate(data) for data in sources_data]
    mock_response = {
        "success": False,
        "errorMsg": "Missing required fields",
    }

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/web-analytics/sources/upload"
    ).mock(httpx.Response(json=mock_response, status_code=400))

    with pytest.raises(RetailCrmApiError):
        await mock_retailcrm_client_v5.web_analytics.sources_upload(sources, site="site")


@pytest.mark.asyncio
async def test_visits_upload_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    visits_data = [
        {
            "createdAt": "2024-07-25 12:00:00",
            "clientId": "client_id_3",
            "site": "test_site",
            "pages": [
                {"url": "/"},
                {"url": "/products", "title": "Products"},
            ],
            "source": {
                "source": "google",
                "medium": "organic",
            },
        }
    ]
    visits = [Visit.model_validate(data) for data in visits_data]

    mock_response = {
        "success": True,
        "failedVisits": [],
    }
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/web-analytics/visits/upload"
    ).mock(httpx.Response(json=mock_response, status_code=201))

    response = await mock_retailcrm_client_v5.web_analytics.visits_upload(visits, site="site")

    assert isinstance(response, VisitsUploadResponse)
    assert response.success is True


@pytest.mark.asyncio
async def test_visits_upload_failure(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    visits = [Visit(createdAt=datetime.now())]  # Missing pages, clientId and site
    mock_response = {"success": False, "errorMsg": "Missing required data in visit"}

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/web-analytics/visits/upload"
    ).mock(httpx.Response(json=mock_response, status_code=400))

    with pytest.raises(RetailCrmApiError):
        await mock_retailcrm_client_v5.web_analytics.visits_upload(visits, site="site")
