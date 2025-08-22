import decimal
from typing import Optional

from pydantic import Field, field_serializer, model_serializer

from retailcrm.v5.enums.orders import CombineTechniqueTypes
from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme, IdTypesLiteral
from retailcrm.v5.schemas.entities.orders import (
    SerializedOrder,
    SerializedOrderLink,
    SerializedOrderReference,
    SerializedPayment,
)
from retailcrm.v5.schemas.filters.orders import OrderHistoryFilterV4Type, OrdersFilter
from retailcrm.v5.schemas.shared.fix_external_row import FixExternalRow
from retailcrm.v5.schemas.shared.order import SerializedEntityOrder
from retailcrm.v5.utils import pydantic_to_nested_dict


class OrdersFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(None, description="Количество элементов в ответе")
    page: Optional[int] = Field(None, description="Номер страницы с результатами")
    filter_obj: Optional[OrdersFilter] = Field(None, description="Объект фильтра")

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter"),
        }


class OrdersGetRequest(BaseRetailCrmScheme):
    site: str | None = None
    by: IdTypesLiteral | str = "externalId"


class OrdersCombineRequest(BaseRetailCrmScheme):
    order: SerializedOrderReference
    resultOrder: SerializedOrderReference
    technique: CombineTechniqueTypes

    order_serializer = field_serializer("order")(to_json_serializer())
    result_order_serializer = field_serializer("resultOrder")(to_json_serializer())


class OrdersCreateRequest(BaseRetailCrmScheme):
    order: SerializedOrder
    site: str | None = None

    order_serializer = field_serializer("order")(to_json_serializer())


class FixExternalIdsRequest(BaseRetailCrmScheme):
    orders: list[FixExternalRow]

    orders_serializer = field_serializer("orders")(to_json_serializer())


class OrdersHistoryRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(None, description="Количество элементов в ответе")
    page: Optional[int] = Field(None, description="Номер страницы с результатами")
    filter_obj: Optional[OrderHistoryFilterV4Type] = Field(
        None, description="Объект фильтра"
    )

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter"),
        }


class OrderLinkCreateRequest(BaseRetailCrmScheme):
    site: Optional[str] = Field(
        None,
        description="Символьный код магазина. Указывается в случае указания заказов через externalId или number",
    )
    link: SerializedOrderLink

    link_serializer = field_serializer("link")(to_json_serializer())


class LoyaltyApplyRequest(BaseRetailCrmScheme):
    order: SerializedEntityOrder
    site: Optional[str] = None
    bonuses: decimal.Decimal

    order_serializer = field_serializer("order")(to_json_serializer())


class LoyaltyCancelBonusOperationsRequest(BaseRetailCrmScheme):
    order: SerializedEntityOrder
    site: Optional[str] = None

    order_serializer = field_serializer("order")(to_json_serializer())


class OrdersPaymentCreateRequest(BaseRetailCrmScheme):
    payment: SerializedPayment
    site: Optional[str] = None

    payment_serializer = field_serializer("payment")(to_json_serializer())


class OrdersPaymentEditRequest(BaseRetailCrmScheme):
    payment: SerializedPayment
    by: IdTypesLiteral | str
    site: Optional[str]

    payment_serializer = field_serializer("payment")(to_json_serializer())


class OrdersUploadRequest(BaseRetailCrmScheme):
    site: Optional[str] = None
    orders: list[SerializedOrder]

    orders_serializer = field_serializer("orders")(to_json_serializer())


class OrdersEditRequest(BaseRetailCrmScheme):
    site: Optional[str] = None
    by: IdTypesLiteral | str
    order: SerializedOrder

    order_serializer = field_serializer("order")(to_json_serializer())


class OrdersDeliveryCancelRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral | str
    force: bool


class OrdersPlatesPrintRequest(BaseRetailCrmScheme):
    site: Optional[str] = None
    by: IdTypesLiteral | str
