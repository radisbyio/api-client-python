from pydantic import Field, model_serializer, field_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.store import SerializedOffer, PriceUploadInput, SerializedProductGroup, \
    ProductCreateInput
from retailcrm.v5.schemas.filters.store import OfferFilter, ProductGroupFilter, ProductFilter, \
    ProductPropertiesFilter, ProductPropertyValuesFilter
from retailcrm.v5.utils import pydantic_to_nested_dict


class InventoriesUploadRequest(BaseRetailCrmScheme):
    offers: list[SerializedOffer]
    site: str | None = Field(description="Символьный код магазина. Указывается в случае идентификации торговых предложений по externalId")


class OffersFilterRequest(BaseRetailCrmScheme):
    filter_obj: OfferFilter | None
    limit: int
    page: int

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
    filter_obj: ProductGroupFilter
    limit: int
    page: int

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
    filter_obj: ProductFilter
    limit: int
    page: int

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
    filter_obj: ProductPropertiesFilter
    limit: int
    page: int

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }



class ProductsPropertyValuesFilterRequest(BaseRetailCrmScheme):
    filter_obj: ProductPropertyValuesFilter
    limit: int
    page: int

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }