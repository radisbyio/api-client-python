from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.entities.store import SerializedOffer, PriceUploadInput, ProductCreateInput, \
    SerializedProductGroup
from retailcrm.v5.schemas.filters.store import OfferFilter, ProductGroupFilter, ProductFilter, \
    InventoryAlternativeFilter, ProductPropertiesFilter, ProductPropertyValuesFilter
from retailcrm.v5.schemas.requests.store import InventoriesUploadRequest, OffersFilterRequest, PricesUploadRequest, \
    ProductGroupsFilterRequest, ProductGroupCreateRequest, ProductGroupEditRequest, ProductsFilterRequest, \
    ProductsBatchCreateRequest, ProductsBatchEditRequest, ProductPropertiesFilter, ProductsPropertyValuesFilterRequest, \
    ProductPropertiesFilterRequest
from retailcrm.v5.schemas.responses.store import InventoriesFilterResponse, InventoriesUploadResponse, \
    OfferFilterResponse, PricesUploadResponse, ProductGroupFilterResponse, ProductGroupCreateResponse, \
    ProductGroupEditResponse, ProductFilterResponse, ResponseProductBatchCreate, ProductBatchEditResponse, \
    ProductPropertiesFilterResponse, ProductPropertyValuesFilterResponse
from retailcrm.v5.utils import pydantic_to_nested_dict


class StoreApiResource(ApiResource):
    async def inventories_filter(
            self, filter_data: InventoryAlternativeFilter | None = None, limit: int = 20, page: int = 1,
    ) -> InventoriesFilterResponse:
        """
        Получение остатков и закупочных цен

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-store-inventories
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_data: Фильтр
        :return: Response
        """
        response = await self._client.get(
            endpoint="/store/inventories",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )
        return self._process_response(response, InventoriesFilterResponse)

    async def inventories_upload(
            self, offers: list[SerializedOffer], site: str = None
    ) -> InventoriesUploadResponse:
        """
        Обновление остатков и закупочных цен

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-store-inventories-upload
        :param offers: Список торговых предложений
        :param site: Код магазина
        :return: RetailCrmResponse
        """

        request = InventoriesUploadRequest(
            offers=offers,
            site=site,
        )

        response = await self._client.post(
            endpoint="/store/inventories/upload",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True)
        )

        return self._process_response(response, InventoriesUploadResponse)

    async def offers_filter(
            self, filter_obj: OfferFilter | None = None, limit: int = 20, page: int = 1
    ) -> OfferFilterResponse:
        """
        Получение списка торговых предложений, удовлетворяющих заданному фильтру

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-store-offers
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_obj: Фильтр
        :return: ResponseOfferFilter
        """
        request = OffersFilterRequest(
            filter_obj=filter_obj,
            limit=limit,
            page=page,
        )
        response = await self._client.get(
            endpoint="/store/offers",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )

        return self._process_response(response, OfferFilterResponse)

    async def prices_upload(
            self, prices: list[PriceUploadInput]
    ) -> PricesUploadResponse:
        """
        Обновление цен торговых предложений

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-store-prices-upload
        :param prices: Список цен
        :return: Response
        """
        request = PricesUploadRequest(
            prices=prices,
        )
        response = await self._client.post(
            endpoint="/store/prices/upload",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, PricesUploadResponse)

    async def product_groups_filter(
            self, filter_obj: ProductGroupFilter | None = None, limit: int = 20, page: int = 1
    ) -> ProductGroupFilterResponse:
        """
        Получение списка групп товаров, удовлетворяющих заданному фильтру

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-store-product-groups
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_obj: Фильтр
        :return: ResponseProductGroupFilter
        """
        request = ProductGroupsFilterRequest(
            filter_obj=filter_obj,
            limit=limit,
            page=page,
        )

        response = await self._client.get(
            endpoint="/store/product-groups",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, ProductGroupFilterResponse)

    async def product_group_create(
            self, product_group: SerializedProductGroup
    ) -> ProductGroupCreateResponse:
        """
        Добавление товарной группы

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-store-product-groups-create
        :param product_group: Данные товарной группы
        :return: ProductGroupCreateResponse
        """
        request = ProductGroupCreateRequest(
            productGroup=product_group,
        )

        response = await self._client.post(
            endpoint="/store/product-groups/create",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )

        return self._process_response(response, ProductGroupCreateResponse)

    async def product_group_edit(
            self,
            external_id: str,
            product_group: SerializedProductGroup,
            site: str,
            by: str = "externalId",
    ) -> ProductGroupEditResponse:
        """
        Редактирование товарной группы

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-store-product-groups-externalId-edit
        :param external_id: Внешний ID товарной группы
        :param product_group: Данные товарной группы
        :param site: Код магазина
        :param by: Тип идентификатора
        :return: ResponseProductGroupEdit
        """
        requests = ProductGroupEditRequest(
            by=by,
            site=site,
            productGroup=product_group,
        )
        response = await self._client.post(
            endpoint=f"/store/product-groups/{external_id}/edit",
            json_str=requests.model_dump_json(exclude_none=True, by_alias=True),
        )

        return self._process_response(response, ProductGroupEditResponse)

    async def products_filter(
            self, filter_obj: ProductFilter | None = None, limit: int = 20, page: int = 1
    ) -> ProductFilterResponse:
        """
        Получение списка товаров с торговыми предложениями, удовлетворяющих заданному фильтру

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-store-products
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_obj: Фильтр
        :return: ProductFilterResponse
        """
        request = ProductsFilterRequest(
            limit=limit,
            page=page,
            filter_obj=filter_obj,
        )
        response = await self._client.get(
            endpoint="/store/products",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )

        return self._process_response(response, ProductFilterResponse)

    async def products_batch_create(
            self, products: list[ProductCreateInput]
    ) -> ResponseProductBatchCreate:
        """
        Пакетное добавление товаров и услуг

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-store-products-batch-create
        :param products: Товары или услуги
        :return: ResponseProductBatchCreate
        """

        request = ProductsBatchCreateRequest(
            products=products
        )

        response = await self._client.post(
            endpoint="/store/products/batch/create",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )

        return self._process_response(response, ResponseProductBatchCreate)

    async def products_batch_edit(
            self, products: list[ProductCreateInput]
    ) -> ProductBatchEditResponse:
        """
        Пакетное добавление товаров и услуг

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-store-products-batch-create
        :param products: Товары или услуги
        :return: ResponseProductBatchEdit
        """
        request = ProductsBatchEditRequest(
            products=products
        )

        response = await self._client.post(
            endpoint="/store/products/batch/edit",
            json_str=request.model_dump_json(exclude_none=True, by_alias=True),
        )

        return self._process_response(response, ProductBatchEditResponse)

    async def product_properties_filter(
            self, filter_obj: ProductPropertiesFilter | None = None, limit: int = 20, page: int = 1
    ) -> ProductPropertiesFilterResponse:
        """
        Получение списка свойств товаров, удовлетворяющих заданному фильтру

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-store-products-properties
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_obj: Фильтр
        :return: ProductPropertiesFilterResponse
        """
        request = ProductPropertiesFilterRequest(
            limit=limit,
            page=page,
            filter_obj=filter_obj,
        )
        response = await self._client.get(
            endpoint="/store/products/properties",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )

        return self._process_response(response, ProductPropertiesFilterResponse)


    async def product_property_values_filter(
            self,
            filter_obj: ProductPropertyValuesFilter | None = None,
            limit: int = 20,
            page: int = 1,
    ) -> ProductPropertyValuesFilterResponse:
        """
        method_hint.GET /api/v5/store/products/properties/values

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-store-products-properties-values
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_obj: Фильтр
        :return: ProductPropertyValuesFilterResponse
        """
        request = ProductsPropertyValuesFilterRequest(
            limit=limit,
            page=page,
            filter_obj=filter_obj,
        )
        response = await self._client.get(
            endpoint="/store/products/properties/values",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )

        return self._process_response(response, ProductPropertyValuesFilterResponse)
