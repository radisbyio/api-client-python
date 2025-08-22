from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme, IdTypesLiteral
from retailcrm.v5.schemas.entities.corporate_customers import (
    SerializedCompany,
    SerializedCustomerAddress,
    SerializedCustomerContact,
    SerializedCustomerCorporate,
)
from retailcrm.v5.schemas.entities.customers import (
    SerializedCustomerNote,
    SerializedCustomerReference,
)
from retailcrm.v5.schemas.filters.customers_corporate import (
    CompanyFilter,
    CustomerAddressFilter,
    CustomerContactFilter,
    CustomerCorporateApiFilterData,
    CustomerHistoryFilterV4Type,
    CustomerNoteFilter,
)
from retailcrm.v5.schemas.shared.fix_external_row import FixExternalRow


class CustomerCorporateFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int]
    page: Optional[int]
    filter_obj: Optional[CustomerCorporateApiFilterData] = Field(
        None, alias="filter_obj"
    )


class CustomerCorporateCombineRequest(BaseRetailCrmScheme):
    resultCustomer: SerializedCustomerReference = Field(alias="resultCustomer")
    customers: list[SerializedCustomerReference] = Field(default_factory=list)

    resultCustomer_serializer = field_serializer("resultCustomer")(to_json_serializer())
    customers_serializer = field_serializer("customers")(to_json_serializer())


class CustomerCorporateCreateRequest(BaseRetailCrmScheme):
    customerCorporate: SerializedCustomerCorporate = Field(alias="customerCorporate")

    customerCorporate_serializer = field_serializer("customerCorporate")(
        to_json_serializer()
    )


class CustomerCorporateFixExternalIdsRequest(BaseRetailCrmScheme):
    customersCorporate: list[FixExternalRow] = Field(
        default_factory=list, alias="customersCorporate"
    )

    customersCorporate_serializer = field_serializer("customersCorporate")(
        to_json_serializer()
    )


class CustomerCorporateHistoryRequest(BaseRetailCrmScheme):
    limit: Optional[int]
    page: Optional[int]
    filter_obj: Optional[CustomerHistoryFilterV4Type] = Field(None, alias="filter_obj")


class CustomerCorporateNotesFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int]
    page: Optional[int]
    filter_obj: Optional[CustomerNoteFilter] = Field(None, alias="filter_obj")


class CustomerCorporateNoteCreateRequest(BaseRetailCrmScheme):
    site: Optional[str] = Field(None, description="Символьный код магазина")
    note: SerializedCustomerNote

    note_serializer = field_serializer("note")(to_json_serializer())


class CustomerCorporateUploadRequest(BaseRetailCrmScheme):
    site: str = Field(
        description="Символьный код магазина, к которому относятся загружаемые клиенты"
    )
    customersCorporate: list[SerializedCustomerCorporate] = Field(
        default_factory=list, alias="customersCorporate"
    )

    customersCorporate_serializer = field_serializer("customersCorporate")(
        to_json_serializer()
    )


class CustomerCorporateGetRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral
    site: Optional[str] = Field(None)


class CustomerCorporateAddressesRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral
    site: Optional[str] = Field(None)
    limit: Optional[int] = Field(20)
    page: Optional[int] = Field(1)
    filter_obj: Optional[CustomerAddressFilter]


class CustomerCorporateAddressCreateRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral
    site: Optional[str] = Field(None)
    address: SerializedCustomerAddress = Field(alias="address")

    address_serializer = field_serializer("address")(to_json_serializer())


class CustomerCorporateAddressEditRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral
    site: Optional[str] = Field(None)
    entityBy: IdTypesLiteral
    address: SerializedCustomerAddress

    address_serializer = field_serializer("address")(to_json_serializer())


class CustomerCorporateCompaniesRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral
    site: Optional[str] = Field(None)
    limit: Optional[int]
    page: Optional[int]
    filter_obj: Optional[CompanyFilter]


class CustomerCorporateCompanyCreateRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral
    site: Optional[str] = Field(None)
    company: SerializedCompany

    company_serializer = field_serializer("company")(to_json_serializer())


class CustomerCorporateCompanyEditRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral
    site: Optional[str] = Field(None)
    entityBy: IdTypesLiteral
    company: SerializedCompany

    company_serializer = field_serializer("company")(to_json_serializer())


class CustomerCorporateContactsRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral
    site: Optional[str] = Field(None)
    limit: Optional[int]
    page: Optional[int]
    filter_obj: Optional[CustomerContactFilter] = Field(None)


class CustomerCorporateContactCreateRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral
    site: Optional[str] = Field(None)
    contact: SerializedCustomerContact

    contact_serializer = field_serializer("contact")(to_json_serializer())


class CustomerCorporateContactEditRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral
    site: Optional[str] = Field(None)
    entityBy: IdTypesLiteral
    contact: SerializedCustomerContact

    contact_serializer = field_serializer("contact")(to_json_serializer())


class CustomerCorporateEditRequest(BaseRetailCrmScheme):
    by: IdTypesLiteral
    site: Optional[str] = Field(None)
    customerCorporate: SerializedCustomerCorporate

    customerCorporate_serializer = field_serializer("customerCorporate")(
        to_json_serializer()
    )
