from pydantic import field_serializer, Field

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme, IdTypesLiteral
from retailcrm.v5.schemas.entities.customer_interaction import SerializedCart, SerializedFavorite


class CartClearRequest(BaseRetailCrmScheme):
    cart: SerializedCart

    cart_serializer = field_serializer("cart")(to_json_serializer())


class CartSetRequest(BaseRetailCrmScheme):
    cart: SerializedCart

    cart_serializer = field_serializer("cart")(to_json_serializer())


class CartGetRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral
    siteBy: str


class FavoritesGetRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral = Field(IdTypesLiteral.EXTERNAL_ID)
    siteBy: str


class FavoritesAddRequest(BaseRetailCrmScheme):
    favorite: SerializedFavorite

    favorite_serializer = field_serializer("favorite")(to_json_serializer())


class FavoritesRemoveRequest(BaseRetailCrmScheme):
    favorite: SerializedFavorite

    favorite_serializer = field_serializer("favorite")(to_json_serializer())