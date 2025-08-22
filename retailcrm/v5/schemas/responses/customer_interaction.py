from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.customer_interaction import Cart, CustomerOffer


class CartClearResponse(SuccessResponse):
    pass


class CartSetResponse(SuccessResponse):
    pass


class CartGetResponse(SuccessResponse):
    cart: Optional[Cart] = Field(None)


class FavoritesGetResponse(SuccessResponse):
    favorites: list[CustomerOffer] = Field(default_factory=list)


class FavoritesAddResponse(SuccessResponse):
    pass


class FavoritesRemoveResponse(SuccessResponse):
    pass