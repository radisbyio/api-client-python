from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.schemas.store import (
    InventoryAlternativeFilterData,
    OfferFilterData,
    PriceUploadInput,
    ProductCreateInput,
    ProductFilterData,
    ProductGroupFilterData,
    ProductPropertiesFilterData,
    ProductPropertyValuesFilterData,
    ResponseInventoriesFilter,
    ResponseInventoriesUpload,
    ResponseOfferFilter,
    ResponsePricesUpload,
    ResponseProductBatchCreate,
    ResponseProductBatchEdit,
    ResponseProductFilter,
    ResponseProductGroupCreate,
    ResponseProductGroupEdit,
    ResponseProductGroupFilter,
    ResponseProductPropertiesFilter,
    ResponseProductPropertyValuesFilter,
    SerializedOffer,
    SerializedProductGroup,
)
from retailcrm.v5.utils import pydantic_list_dumps_to_json, pydantic_to_nested_dict


class StoreController:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def inventories_filter(
        self,
        filter_data: InventoryAlternativeFilterData,
        limit: int = 20,
        page: int = 1,
    ) -> ResponseInventoriesFilter:
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

        response_obj = ResponseInventoriesFilter.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def inventories_upload(
        self, offers: list[SerializedOffer], site: str = None
    ) -> ResponseInventoriesUpload:
        """
        Обновление остатков и закупочных цен

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-store-inventories-upload
        :param offers: Список торговых предложений
        :param site: Код магазина
        :return: RetailCrmResponse
        """
        data = {
            "offers": [
                offer.model_dump_json(exclude_unset=True, by_alias=True) for offer in offers
            ]
        }
        if site:
            data["site"] = site

        response = await self._client.post(
            endpoint="/store/inventories/upload", data=data
        )

        response_obj = ResponseInventoriesUpload.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def offers_filter(
        self, filter_data: OfferFilterData, limit: int = 20, page: int = 1
    ) -> ResponseOfferFilter:
        """
        Получение списка торговых предложений, удовлетворяющих заданному фильтру

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-store-offers
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_data: Фильтр
        :return: ResponseOfferFilter
        """
        response = await self._client.get(
            endpoint="/store/offers",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = ResponseOfferFilter.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def prices_upload(
        self, prices: list[PriceUploadInput]
    ) -> ResponsePricesUpload:
        """
        Обновление цен торговых предложений

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-store-prices-upload
        :param prices: Список цен
        :return: Response
        """
        response = await self._client.post(
            endpoint="/store/prices/upload",
            data={
                "prices": [
                    price.model_dump(exclude_none=True, by_alias=True)
                    for price in prices
                ]
            },
        )

        response_obj = ResponsePricesUpload.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def product_groups_filter(
        self, filter_data: ProductGroupFilterData, limit: int = 20, page: int = 1
    ) -> ResponseProductGroupFilter:
        """
        Получение списка групп товаров, удовлетворяющих заданному фильтру

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-store-product-groups
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_data: Фильтр
        :return: ResponseProductGroupFilter
        """
        response = await self._client.get(
            endpoint="/store/product-groups",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = ResponseProductGroupFilter.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def product_group_create(
        self, product_group: SerializedProductGroup
    ) -> ResponseProductGroupCreate:
        """
        Добавление товарной группы

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-store-product-groups-create
        :param product_group: Данные товарной группы
        :return: ResponseProductGroupCreate
        """
        response = await self._client.post(
            endpoint="/store/product-groups/create",
            data={"productGroup": product_group.model_dump(exclude_unset=True)},
        )

        response_obj = ResponseProductGroupCreate.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def product_group_edit(
        self,
        external_id: str,
        product_group: SerializedProductGroup,
        site: str,
        by: str = "externalId",
    ) -> ResponseProductGroupEdit:
        """
        Редактирование товарной группы

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-store-product-groups-externalId-edit
        :param external_id: Внешний ID товарной группы
        :param product_group: Данные товарной группы
        :param site: Код магазина
        :param by: Тип идентификатора
        :return: ResponseProductGroupEdit
        """
        response = await self._client.post(
            endpoint=f"/store/product-groups/{external_id}/edit",
            params={"by": by, "site": site},
            data={"productGroup": product_group.model_dump(exclude_unset=True)},
        )

        response_obj = ResponseProductGroupEdit.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def products_filter(
        self, filter_data: ProductFilterData, limit: int = 20, page: int = 1
    ) -> ResponseProductFilter:
        """
        Получение списка товаров с торговыми предложениями, удовлетворяющих заданному фильтру

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-store-products
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_data: Фильтр
        :return: ResponseProductFilter
        """
        response = await self._client.get(
            endpoint="/store/products",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = ResponseProductFilter.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj


    async def products_batch_create(
        self, products: list[ProductCreateInput]
    ) -> ResponseProductBatchCreate:
        """
        Пакетное добавление товаров и услуг

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-store-products-batch-create
        :param products: Товары или услуги
        :return: ResponseProductFilter
        """

        data = {"products": pydantic_list_dumps_to_json(products, ProductCreateInput)}

        response = await self._client.post(
            endpoint="/store/products/batch/create", data=data
        )

        response_obj = ResponseProductBatchCreate.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(
                response.status_code,
                response_obj.errorMsg,
                response_obj.errors,
                response_obj.model_dump(),
            )
        return response_obj

    async def products_batch_edit(
        self, products: list[ProductCreateInput]
    ) -> ResponseProductBatchEdit:
        """
        Пакетное добавление товаров и услуг

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-store-products-batch-create
        :param products: Товары или услуги
        :return: ResponseProductBatchEdit
        """
        response = await self._client.post(
            endpoint="/store/products/batch/edit", data={"products": products}
        )

        response_obj = ResponseProductBatchEdit.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def product_properties_filter(
        self, filter_data: ProductPropertiesFilterData, limit: int = 20, page: int = 1
    ) -> ResponseProductPropertiesFilter:
        """
        Получение списка свойств товаров, удовлетворяющих заданному фильтру

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-store-products-properties
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_data: Фильтр
        :return: ResponseProductPropertiesFilter
        """
        response = await self._client.get(
            endpoint="/store/products/properties",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = ResponseProductPropertiesFilter.model_validate_json(
            response.body
        )
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def product_property_values_filter(
        self,
        filter_data: ProductPropertyValuesFilterData,
        limit: int = 20,
        page: int = 1,
    ) -> ResponseProductPropertyValuesFilter:
        """
        method_hint.GET /api/v5/store/products/properties/values

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-store-products-properties-values
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_data: Фильтр
        :return: ResponseProductPropertyValuesFilter
        """
        response = await self._client.get(
            endpoint="/store/products/properties/values",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = ResponseProductPropertyValuesFilter.model_validate_json(
            response.body
        )
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj
