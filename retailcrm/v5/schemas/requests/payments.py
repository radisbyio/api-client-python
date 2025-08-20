from pydantic import field_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.payments import ApiCheckRequest, ApiCreateInvoiceRequest, ApiUpdateInvoiceRequest, \
    ApiImportInvoiceRequest


class CheckRequest(BaseRetailCrmScheme):
    check: ApiCheckRequest

    check_serializer = field_serializer("check")(to_json_serializer())


class CreateInvoiceRequest(BaseRetailCrmScheme):
    createInvoice: ApiCreateInvoiceRequest

    createInvoice_serializer = field_serializer("createInvoice")(to_json_serializer())


class UpdateInvoiceRequest(BaseRetailCrmScheme):
    updateInvoice: ApiUpdateInvoiceRequest

    updateInvoice_serializer = field_serializer("updateInvoice")(to_json_serializer())


class InvoiceImportRequest(BaseRetailCrmScheme):
    invoice: ApiImportInvoiceRequest

    invoice_serializer = field_serializer("invoice")(to_json_serializer())