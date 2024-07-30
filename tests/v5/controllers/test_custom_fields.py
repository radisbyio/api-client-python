import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5
from retailcrm.v5.schemas import CustomFieldFilter, CustomDictionaryFilter


@pytest.mark.asyncio
async def test_custom_fields_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_customer: dict,
):
    mock_response = {
        "success": True,
        "pagination": {
            "limit": 20,
            "totalCount": 6,
            "currentPage": 1,
            "totalPageCount": 1
        },
        "customFields": [
            {
                "name": "Менеджер",
                "code": "menedzher",
                "required": False,
                "inFilter": True,
                "inList": True,
                "inGroupActions": False,
                "type": "string",
                "entity": "order",
                "ordering": 50,
                "viewMode": "editable",
                "viewModeMobile": "editable"
            },
        ]
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/custom-fields",
        params={"limit": 20, "page": 1, "filter[code]": "menedzher"},
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )

    get_customers_result = await mock_retailcrm_client_v5.custom_fields.custom_fields(
        filter_data=CustomFieldFilter(code="menedzher")
    )

    assert get_customers_result.success is True


@pytest.mark.asyncio
async def test_dictionaries_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_customer: dict,
):
    mock_response = {
        "success": True,
        "pagination": {
            "limit": 20,
            "totalCount": 1,
            "currentPage": 1,
            "totalPageCount": 1
        },
        "customDictionaries": [
            {
                "name": "Тест",
                "code": "test",
                "elements": [
                    {
                        "name": "т1",
                        "code": "t1",
                        "ordering": 10
                    },
                    {
                        "name": "т2",
                        "code": "t2",
                        "ordering": 20
                    },
                    {
                        "name": "т3",
                        "code": "t3",
                        "ordering": 30
                    }
                ]
            }
        ]
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/custom-fields/dictionaries",
        params={"limit": 20, "page": 1, "filter[code]": "test"},
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )

    get_customers_result = await mock_retailcrm_client_v5.custom_fields.dictionaries(
        filter_data=CustomDictionaryFilter(code="test")
    )

    assert get_customers_result.success is True
