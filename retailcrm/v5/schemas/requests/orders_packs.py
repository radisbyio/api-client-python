from typing import Optional

from pydantic import Field, model_serializer, field_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.orders_packs import SerializedOrderProductPack
from retailcrm.v5.schemas.filters.orders_packs import OrderProductPackFilter
from retailcrm.v5.utils import pydantic_to_nested_dict


class OrdersProductsPacksFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(None, description="Количество элементов в ответе")
    page: Optional[int] = Field(None, description="Номер страницы с результатами")
    filter_obj: Optional[OrderProductPackFilter] = Field(None, description="Объект фильтра")

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }


class OrdersPacksCreateRequest(BaseRetailCrmScheme):
    pack: SerializedOrderProductPack

    pack_serializer = field_serializer("pack")(to_json_serializer())


class OrdersPacksEditRequest(BaseRetailCrmScheme):
    pack: SerializedOrderProductPack

    pack_serializer = field_serializer("pack")(to_json_serializer())


class OrdersProductsPacksHistoryFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(None, description="Количество элементов в ответе")
    page: Optional[int] = Field(None, description="Номер страницы с результатами")
    filter_obj: Optional[OrderProductPackFilter] = Field(None, description="Объект фильтра")

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }