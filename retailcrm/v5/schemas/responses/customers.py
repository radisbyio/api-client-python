from datetime import datetime
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import PaginatedResponse, SuccessResponse
from retailcrm.v5.schemas.entities.customers import (
    Customer,
    CustomerHistory,
    CustomerNote,
    EntityWithExternalId,
)
from retailcrm.v5.schemas.shared.fix_external_row import FixExternalRow


class CustomersResponse(PaginatedResponse):
    customers: list[Customer] = Field(default_factory=list)


class CustomersCombineResponse(SuccessResponse):
    pass


class CustomerCreateResponse(SuccessResponse):
    id: Optional[int] = Field(None, description="Внутренний ID созданного клиента")


class CustomersFixExternalIdsResponse(SuccessResponse):
    pass


class CustomersHistoryResponse(PaginatedResponse):
    generatedAt: Optional[datetime] = Field(
        None, description="Время формирования ответа"
    )
    history: list[CustomerHistory] = Field(default_factory=list)


class CustomersNotesResponse(PaginatedResponse):
    notes: list[CustomerNote] = Field(default_factory=list)


class CustomerNoteCreateResponse(SuccessResponse):
    id: Optional[int] = Field(None, description="Внутренний ID созданной заметки")


class CustomersUploadResponse(SuccessResponse):
    uploadedCustomers: list[FixExternalRow] = Field(default_factory=list)
    failedCustomers: list[EntityWithExternalId] = Field(default_factory=list)


class CustomerGetResponse(SuccessResponse):
    customer: Optional[Customer] = Field(None)
    combinedTo: Optional[Customer] = Field(
        None,
        description="Информация о клиенте, который получился после объединения с текущим клиентом",
    )


class CustomerEditResponse(SuccessResponse):
    id: Optional[int] = Field(None, description="Внутренний ID клиента")
    state: Optional[str] = Field(
        None, description="Состояние клиента (по умолчанию не возвращается)"
    )


class CustomerSubscriptionsResponse(SuccessResponse):
    pass
