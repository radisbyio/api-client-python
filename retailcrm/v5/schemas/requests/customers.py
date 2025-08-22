from typing import Optional

from pydantic import Field, field_serializer, model_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme, IdTypesLiteral
from retailcrm.v5.schemas.entities.customers import SerializedCustomerReference, SerializedCustomerNote, \
    SerializedCustomer, SerializedSubscription
from retailcrm.v5.schemas.filters.customers import CustomerFilter, CustomerNoteFilter, CustomerHistoryFilterV4Type
from retailcrm.v5.schemas.shared.fix_external_row import FixExternalRow
from retailcrm.v5.utils import pydantic_to_nested_dict


class CustomersFilterRequest(BaseRetailCrmScheme):
    limit: int = Field(description="Количество элементов в ответе")
    page: int = Field(description="Номер страницы с результатами")
    filter_obj: Optional[CustomerFilter] = Field(None, description="Объект фильтра")

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }


class CustomersCombineRequest(BaseRetailCrmScheme):
    resultCustomer: SerializedCustomerReference
    customers: list[SerializedCustomerReference]

    resultCustomer_serializer = field_serializer("resultCustomer")(to_json_serializer())
    customers_serializer = field_serializer("customers")(to_json_serializer())


class CustomersCreateRequest(BaseRetailCrmScheme):
    site: Optional[str] = Field(None, description="Символьный код магазина")
    customer: SerializedCustomer

    customer_serializer = field_serializer("customer")(to_json_serializer())


class CustomersFixExternalIdsRequest(BaseRetailCrmScheme):
    customers: list[FixExternalRow] = Field(default_factory=list)

    customers_serializer = field_serializer("customers")(to_json_serializer())


class CustomersHistoryRequest(BaseRetailCrmScheme):
    limit: int = Field(description="Количество элементов в ответе")
    page: int = Field(description="Номер страницы с результатами")
    filter_obj: Optional[CustomerHistoryFilterV4Type] = Field(None, description="Объект фильтра")

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }


class CustomersNotesFilterRequest(BaseRetailCrmScheme):
    limit: int = Field(description="Количество элементов в ответе")
    page: int = Field(description="Номер страницы с результатами")
    filter_obj: Optional[CustomerNoteFilter] = Field(None, description="Объект фильтра")

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }


class CustomerNoteCreateRequest(BaseRetailCrmScheme):
    site: Optional[str] = Field(None, description="Символьный код магазина")
    note: SerializedCustomerNote

    note_serializer = field_serializer("note")(to_json_serializer())


class CustomersUploadRequest(BaseRetailCrmScheme):
    site: str = Field(description="Символьный код магазина, к которому относятся загружаемые клиенты")
    customers: list[SerializedCustomer] = Field(default_factory=list)

    customers_serializer = field_serializer("customers")(to_json_serializer())


class CustomerGetRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral = Field(description="Указывается, что передается в параметре externalId: внутренний (by=id) или внешний (by=externalId) ID клиента. По умолчанию externalId.")
    site: Optional[str] = Field(None, description="Символьный код магазина")


class CustomerEditRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral = Field(description="Указывается, что передается в параметре externalId: внутренний (by=id) или внешний (by=externalId) ID клиента. По умолчанию externalId.")
    site: Optional[str] = Field(None, description="Символьный код магазина")
    customer: SerializedCustomer

    customer_serializer = field_serializer("customer")(to_json_serializer())


class CustomerSubscriptionsRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral = Field(description="Указывается, что передается в параметре externalId: внутренний (by=id) или внешний (by=externalId) ID клиента. По умолчанию externalId.")
    site: Optional[str] = Field(None, description="Символьный код магазина")
    subscriptions: list[SerializedSubscription] = Field(default_factory=list)

    subscriptions_serializer = field_serializer("subscriptions")(to_json_serializer())