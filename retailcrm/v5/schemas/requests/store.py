from typing import Optional

from pydantic import Field, model_serializer, field_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.store import SerializedOffer, PriceUploadInput, SerializedProductGroup, \
    ProductCreateInput
from retailcrm.v5.schemas.filters.store import OfferFilter, ProductGroupFilter, ProductFilter, \
    ProductPropertiesFilter, ProductPropertyValuesFilter
from retailcrm.v5.utils import pydantic_to_nested_dict


class InventoriesUploadRequest(BaseRetailCrmScheme):
    offers: list[SerializedOffer]
    site: str | None = Field(description="Символьный код магазина. Указывается в случае идентификации торговых предложений по externalId")


class OffersFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(None, description="Количество элементов в ответе")
    page: Optional[int] = Field(None, description="Номер страницы с результатами")
    filter_obj: Optional[OfferFilter] = Field(None, description="Объект фильтра")

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }


class PricesUploadRequest(BaseRetailCrmScheme):
    prices: list[PriceUploadInput] | None


class ProductGroupsFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(None, description="Количество элементов в ответе")
    page: Optional[int] = Field(None, description="Номер страницы с результатами")
    filter_obj: Optional[ProductGroupFilter] = Field(None, description="Объект фильтра")

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }


class ProductGroupCreateRequest(BaseRetailCrmScheme):
    productGroup: SerializedProductGroup | None = None


class ProductGroupEditRequest(BaseRetailCrmScheme):
    by: str
    site: str
    productGroup: SerializedProductGroup


class ProductsFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(None, description="Количество элементов в ответе")
    page: Optional[int] = Field(None, description="Номер страницы с результатами")
    filter_obj: Optional[ProductFilter] = Field(None, description="Объект фильтра")

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }


class ProductsBatchCreateRequest(BaseRetailCrmScheme):
    products: list[ProductCreateInput]

    products_serializer = field_serializer("products")(to_json_serializer())


class ProductsBatchEditRequest(BaseRetailCrmScheme):
    products: list[ProductCreateInput]

    products_serializer = field_serializer("products")(to_json_serializer())


class ProductPropertiesFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(None, description="Количество элементов в ответе")
    page: Optional[int] = Field(None, description="Номер страницы с результатами")
    filter_obj: Optional[ProductPropertiesFilter] = Field(None, description="Объект фильтра")

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }



class ProductsPropertyValuesFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(None, description="Количество элементов в ответе")
    page: Optional[int] = Field(None, description="Номер страницы с результатами")
    filter_obj: Optional[ProductPropertyValuesFilter] = Field(None, description="Объект фильтра")


    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }