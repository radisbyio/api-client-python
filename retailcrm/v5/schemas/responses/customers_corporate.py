from datetime import datetime
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import PaginatedResponse, SuccessResponse
from retailcrm.v5.schemas.entities.corporate_customers import (
    Company,
    CustomerContact,
    CustomerCorporate,
    CustomerCorporateHistory,
)
from retailcrm.v5.schemas.entities.customers import (
    CustomerAddress,
    CustomerNote,
    EntityWithExternalId,
)
from retailcrm.v5.schemas.shared.fix_external_row import FixExternalRow


class CustomerCorporateResponse(PaginatedResponse):
    customersCorporate: list[CustomerCorporate] = Field(default_factory=list)


class CustomerCorporateCombineResponse(SuccessResponse):
    pass


class CustomerCorporateCreateResponse(SuccessResponse):
    id: Optional[int] = Field(None, description="Внутренний ID созданного клиента")


class CustomerCorporateFixExternalIdsResponse(SuccessResponse):
    pass


class CustomerCorporateHistoryResponse(PaginatedResponse):
    generatedAt: Optional[datetime] = Field(
        None, description="Время формирования ответа"
    )
    history: list[CustomerCorporateHistory] = Field(default_factory=list)


class CustomerCorporateNotesResponse(PaginatedResponse):
    notes: list[CustomerNote] = Field(default_factory=list)


class CustomerCorporateNoteCreateResponse(SuccessResponse):
    id: Optional[int] = Field(None, description="Внутренний ID созданной заметки")


class CustomerCorporateUploadResponse(SuccessResponse):
    uploadedCustomers: list[FixExternalRow] = Field(default_factory=list)
    failedCustomers: list[EntityWithExternalId] = Field(default_factory=list)


class CustomerCorporateGetResponse(SuccessResponse):
    customerCorporate: Optional[CustomerCorporate] = Field(None)


class CustomerCorporateAddressesResponse(PaginatedResponse):
    addresses: list[CustomerAddress] = Field(default_factory=list)


class CustomerCorporateAddressCreateResponse(SuccessResponse):
    id: Optional[int] = Field(None)


class CustomerCorporateAddressEditResponse(SuccessResponse):
    id: Optional[int] = Field(None)


class CustomerCorporateCompaniesResponse(PaginatedResponse):
    companies: list[Company] = Field(default_factory=list)


class CustomerCorporateCompanyCreateResponse(SuccessResponse):
    id: Optional[int] = Field(None)


class CustomerCorporateCompanyEditResponse(SuccessResponse):
    id: Optional[int] = Field(None)


class CustomerCorporateContactsResponse(PaginatedResponse):
    contacts: list[CustomerContact] = Field(default_factory=list)


class CustomerCorporateContactCreateResponse(SuccessResponse):
    id: Optional[int] = Field(None)


class CustomerCorporateContactEditResponse(SuccessResponse):
    id: Optional[int] = Field(None)


class CustomerCorporateEditResponse(SuccessResponse):
    id: Optional[int] = Field(None, description="Внутренний ID клиента")
    state: Optional[str] = Field(
        None, description="Состояние клиента (по умолчанию не возвращается)"
    )
