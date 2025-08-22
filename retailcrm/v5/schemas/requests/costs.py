from typing import Optional

from pydantic import Field, field_serializer, model_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.costs import SerializedCost
from retailcrm.v5.schemas.filters.costs import CostFilter
from retailcrm.v5.utils import pydantic_to_nested_dict


class CostsFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(20, description="Количество элементов в ответе")
    page: Optional[int] = Field(1, description="Номер страницы с результатами")
    filter_obj: Optional[CostFilter] = Field(None)

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter"),
        }


class CostCreateRequest(BaseRetailCrmScheme):
    site: Optional[str] = Field(
        None,
        description="Символьный код магазина. Указывается в случае привязки к заказу по externalId или number",
    )
    cost: SerializedCost

    cost_serializer = field_serializer("cost")(to_json_serializer())


class CostsDeleteRequest(BaseRetailCrmScheme):
    ids: list[int] = Field(
        default_factory=list, description="Идентификаторы удаляемых расходов"
    )


class CostsUploadRequest(BaseRetailCrmScheme):
    costs: list[SerializedCost]

    costs_serializer = field_serializer("costs")(to_json_serializer())


class CostEditRequest(BaseRetailCrmScheme):
    site: Optional[str] = Field(
        None,
        description="Символьный код магазина. Указывается в случае привязки к заказу по externalId или number",
    )
    cost: SerializedCost

    cost_serializer = field_serializer("cost")(to_json_serializer())
