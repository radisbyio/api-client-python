import json

import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5
from retailcrm.v5.schemas import (
    InventoryAlternativeFilterData, SerializedOffer, SerializedStore, OfferFilterData,
    ProductGroupFilterData, SerializedProductGroup, ProductFilterData, ProductPropertiesFilterData,
    ProductPropertyValuesFilterData, PriceUploadInput, PriceUploadPricesInput, ProductCreateInput
)


@pytest.mark.asyncio
async def test_store_inventories_filter_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": True,
        "pagination": {
            "limit": 20,
            "totalCount": 6,
            "currentPage": 1,
            "totalPageCount": 1
        },
        "offers": [
            {
                "id": 1,
                "externalId": "1",
                "xmlId": "1",
                "site": "test-org",
                "purchasePrice": 700,
                "quantity": 1,
                "stores": [
                    {
                        "quantity": 1,
                        "purchasePrice": 700,
                        "store": "main"
                    }
                ]
            },
        ]
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/store/inventories",
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )

    get_inventories_result = await mock_retailcrm_client_v5.store.inventories_filter(
        InventoryAlternativeFilterData(sites=["main"])
    )

    assert get_inventories_result.success is True


@pytest.mark.asyncio
async def test_store_inventories_upload_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": True,
        "processedOffersCount": 1,
        "notFoundOffers": []
    }
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/store/inventories/upload"
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )
    create_result = await mock_retailcrm_client_v5.store.inventories_upload(
        [SerializedOffer(id=1, stores=[SerializedStore(code="main", available=10)])], "test-site"
    )
    assert create_result.success is True


@pytest.mark.asyncio
async def test_store_offers_filter_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": True,
        "pagination": {
            "limit": 20,
            "totalCount": 1,
            "currentPage": 1,
            "totalPageCount": 1
        },
        "offers": [
            {
                "id": 1,
                "externalId": "1",
                "xmlId": "1",
                "site": "test-org",
                "name": "Some offer",
                "article": "A123",
                "purchasePrice": 700,
                "vatRate": "none",
                "quantity": 1,
                "weight": 12.5,
                "active": True,
            },
        ]
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/store/offers"
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )

    get_offers_result = await mock_retailcrm_client_v5.store.offers_filter(
        OfferFilterData(active=True)
    )

    assert get_offers_result.success is True


@pytest.mark.asyncio
async def test_store_prices_upload_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": True,
        "processedOffersCount": 1,
        "notFoundOffers": []
    }

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/store/prices/upload",
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )

    price_upload_input = PriceUploadInput(
        externalId="test-ext-id",
        prices=[PriceUploadPricesInput(code="base", price=1000)]
    )

    create_result = await mock_retailcrm_client_v5.store.prices_upload(
        [price_upload_input]
    )
    assert create_result.success is True


@pytest.mark.asyncio
async def test_store_product_groups_filter_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": True,
        "pagination": {
            "limit": 20,
            "totalCount": 6,
            "currentPage": 1,
            "totalPageCount": 1
        },
        "productGroup": [
            {
                "parentId": 0,
                "site": "test-org",
                "id": 1,
                "name": "Test Group",
                "lvl": 1,
                "externalId": "test-group",
                "active": True
            },
        ]
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/store/product-groups",
        params={"limit": 20, "page": 1, "filter[active]": True},
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )

    get_product_groups_result = await mock_retailcrm_client_v5.store.product_groups_filter(
        ProductGroupFilterData(active=True)
    )

    assert get_product_groups_result.success is True


@pytest.mark.asyncio
async def test_store_product_group_create_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": True,
        "id": 1111
    }

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/store/product-groups/create",
        data={
            "productGroup": {"parentId": 0, "name": "Test Group", "externalId": "test-group", "active": True, "site": "test-org"}
        },
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=201,
        )
    )

    product_group = SerializedProductGroup(
        parentId=0,
        name="Test Group",
        externalId="test-group",
        active=True,
        site="test-org"
    )

    create_result = await mock_retailcrm_client_v5.store.product_group_create(
        product_group
    )

    assert create_result.success is True


@pytest.mark.asyncio
async def test_store_product_group_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": True,
        "id": 1111
    }
    mock_external_id = "test-group"
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/store/product-groups/{mock_external_id}/edit",
        params={"by": "externalId", "site": "test-org"},
        data={
            "productGroup": {"name": "Test Group Edited", "active": False}
        },
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )

    product_group = SerializedProductGroup(
        name="Test Group Edited",
        active=False
    )

    create_result = await mock_retailcrm_client_v5.store.product_group_edit(
        mock_external_id, product_group, site="test-org"
    )

    assert create_result.success is True


@pytest.mark.asyncio
async def test_store_products_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": True,
        "pagination": {
            "limit": 20,
            "totalCount": 6,
            "currentPage": 1,
            "totalPageCount": 1
        },
        "products": [
            {
                "type": "product",
                "minPrice": 700,
                "maxPrice": 700,
                "catalogId": 1,
                "id": 1,
                "article": "A123",
                "name": "Some product",
                "url": "https://some.site/product.html",
                "active": True,
                "quantity": 1,
            },
        ]
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/store/products",
        params={"limit": 20, "page": 1, "filter[active]": True},
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )

    get_products_result = await mock_retailcrm_client_v5.store.products_filter(
        filter_data=ProductFilterData(active=True)
    )

    assert get_products_result.success is True


@pytest.mark.asyncio
async def test_store_products_batch_create_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": True,
        "processedProductsCount": 1,
        "addedProducts": [1111]
    }

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/store/products/batch/create",
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )

    products = [
        ProductCreateInput(
            type="product",
            catalogId=1,
            article="A123",
            name="Some product",
            active=True,
        )
    ]

    create_result = await mock_retailcrm_client_v5.store.products_batch_create(
        products
    )

    assert create_result.success is True


@pytest.mark.asyncio
async def test_store_products_batch_edit_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": True,
        "processedProductsCount": 1,
        "notFoundProducts": []
    }

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/store/products/batch/edit",
        data={
            "products": [{"id": 1, "name": "Some product Edited", "active": False, "site": "test-org"}]
        },
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )

    create_result = await mock_retailcrm_client_v5.store.products_batch_edit(
        [{"id": 1, "name": "Some product Edited", "active": False, "site": "test-org"}]
    )

    assert create_result.success is True


@pytest.mark.asyncio
async def test_store_products_properties_filter_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": True,
        "pagination": {
            "limit": 20,
            "totalCount": 6,
            "currentPage": 1,
            "totalPageCount": 1
        },
        "properties": [
            {
                "sites": [
                    "test-org"
                ],
                "groups": [],
                "code": "weight",
                "name": "Вес",
                "isNumeric": True,
                "visible": True,
                "variative": False
            }
        ]
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/store/products/properties",
        params={"limit": 20, "page": 1, "filter[visible]": True},
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )

    get_properties_result = await mock_retailcrm_client_v5.store.product_properties_filter(
        ProductPropertiesFilterData(visible=True)
    )

    assert get_properties_result.success is True


@pytest.mark.asyncio
async def test_store_products_properties_values_filter_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": True,
        "pagination": {
            "limit": 20,
            "totalCount": 6,
            "currentPage": 1,
            "totalPageCount": 1
        },
        "productPropertyValues": [
            {
                "property": {
                    "code": "weight",
                    "name": "Вес"
                },
                "value": "50",
                "offersCount": 3
            }
        ]
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/store/products/properties/values",
        params={"limit": 20, "page": 1, "filter[propertyCode]": "weight"},
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )

    get_properties_values_result = await mock_retailcrm_client_v5.store.product_property_values_filter(
        ProductPropertyValuesFilterData(propertyCode="weight")
    )

    assert get_properties_values_result.success is True