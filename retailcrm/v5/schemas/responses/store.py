from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse, SuccessPaginatedResponse
from retailcrm.v5.schemas.entities.store import Offer, ProductGroup, Product, PriceUploadNotFoundResponse, \
    ProductEditNotFoundResponse, ProductProperty, ProductPropertyValueResponse


class InventoriesFilterResponse(SuccessPaginatedResponse):
    offers: list[Offer] = Field(
        default_factory=list, description="Торговое предложение (SKU)"
    )


class InventoriesUploadResponse(SuccessResponse):
    notFoundOffers: list[Offer] = Field(
        default_factory=list, description="Торговое предложение (SKU)"
    )


class OfferFilterResponse(SuccessPaginatedResponse):
    offers: list[Offer] = Field(
        default_factory=list, description="Торговое предложение (SKU)"
    )

class PricesUploadResponse(SuccessResponse):
    processedOffersCount: Optional[int] = Field(
        None, description="Количество успешно обработанных торговых предложений"
    )
    notFoundOffers: list[PriceUploadNotFoundResponse] = Field(
        default_factory=list, description="Список не обработанных торговых предложений"
    )


class ProductGroupFilterResponse(SuccessPaginatedResponse):
    productGroup: list[ProductGroup] = Field(
        default_factory=list, description="Товарная группа"
    )


class ProductGroupCreateResponse(SuccessResponse):
    id: Optional[int] = Field(
        None, description="Внутренний ID созданной товарной группы"
    )


class ProductGroupEditResponse(SuccessResponse):
    id: Optional[int] = Field(
        None, description="Внутренний ID созданной товарной группы"
    )


class ProductFilterResponse(SuccessPaginatedResponse):
    products: list[Product] = Field(default_factory=list, description="Товар")


class ResponseProductBatchCreate(SuccessResponse):
    processedProductsCount: Optional[int] = Field(
        None, description="Количество успешно обработанных товаров"
    )
    addedProducts: list[int] = Field(
        default_factory=list, description="Список id добавленных товаров"
    )


class ProductBatchEditResponse(SuccessResponse):
    processedProductsCount: Optional[int] = Field(
        description="Количество успешно обработанных товаров"
    )
    notFoundProducts: list[ProductEditNotFoundResponse] = Field(
        default_factory=list, description="Список id добавленных товаров"
    )

class ProductPropertiesFilterResponse(SuccessPaginatedResponse):
    properties: list[ProductProperty] = Field(
        default_factory=list, description="Свойство товара"
    )


class ProductPropertyValuesFilterResponse(SuccessPaginatedResponse):
    productPropertyValues: list[ProductPropertyValueResponse] = Field(
        default_factory=list
    )