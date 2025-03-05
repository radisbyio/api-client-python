from unittest.mock import AsyncMock

import pytest

from retailcrm import RetailCrmApiClientV5
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.api.orders import RetailCrmOrdersApi


@pytest.fixture
def test_client() -> RetailCrmOrdersApi:
    return AsyncMock()


@pytest.fixture
def mock_http_client() -> BaseHttpClient:
    return AsyncMock()


@pytest.fixture(scope="module")
def mock_retailcrm_client_v5() -> RetailCrmApiClientV5:
    return RetailCrmApiClientV5("http://testcrm.retailcrm.ru", "test_api_key")


@pytest.fixture
def mock_order() -> dict:
    return {
        "slug": 5604,
        "summ": 0,
        "id": 5604,
        "number": "5604A",
        "externalId": "5603",
        "orderMethod": "shopping-cart",
        "countryIso": "RU",
        "createdAt": "2020-04-07 15:44:24",
        "statusUpdatedAt": "2020-04-07 15:44:24",
        "totalSumm": 0,
        "prepaySum": 0,
        "purchaseSumm": 0,
        "markDatetime": "2020-04-07 15:44:24",
        "call": "false",
        "expired": "false",
        "customer": {
            "id": 3627,
            "createdAt": "2020-04-07 15:44:24",
            "vip": "false",
            "bad": "false",
            "marginSumm": 0,
            "totalSumm": 0,
            "averageSumm": 0,
            "ordersCount": 1,
            "customFields": [],
            "personalDiscount": 0,
            "email": "",
            "phones": [],
            "firstName": "John",
        },
        "contragentType": "individual",
        "delivery": {"cost": 0, "netCost": 0, "address": {}},
        "site": "127-0-0-1-8080",
        "status": "new",
        "items": [],
        "fromApi": "true",
    }


@pytest.fixture
def mock_payment() -> dict:
    return {"order": {"externalId": "5603"}, "type": "bank-card"}


@pytest.fixture()
def mock_customer() -> dict:
    return {
        "id": 9717,
        "externalId": "c-111111111",
        "createdAt": "2020-04-09 16:55:59",
        "vip": "false",
        "bad": "false",
        "site": "test-org",
        "marginSumm": 28180,
        "totalSumm": 28180,
        "averageSumm": 28180,
        "ordersCount": 1,
        "customFields": [],
        "personalDiscount": 0,
        "address": {"id": 5667, "text": "MAY"},
        "firstName": "Аа",
        "lastName": "Аа",
        "phones": [],
        "contragentType": "individual",
    }


@pytest.fixture()
def mock_corporate_customer() -> dict:
    return {
        'type': 'customer_corporate',
        'id': 9084,
        'externalId': 'cc_9',
        'nickName': 'Test',
        'mainAddress': {
            'id': 3995,
            'name': 'Test'
        },
        'createdAt': '2020-02-14 13:49:21',
        'vip': 'false',
        'bad': 'false',
        'site': 'opencart',
        'tags': [],
        'marginSumm': 0,
        'totalSumm': 0,
        'averageSumm': 0,
        'ordersCount': 0,
        'costSumm': 0,
        'customFields': [],
        'personalDiscount': 0,
        'ainCustomerContact': {
            'id': 33,
            'customer': {
                'id': 9083,
                'externalId': '9'
            },
            'companies': []
        },
        'mainCompany': {
            'id': 31,
            'name': 'Test'
        }
    }
