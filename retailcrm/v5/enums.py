from enum import Enum


class IdTypes(str, Enum):
    ID = "id"
    EXTERNAL_ID = "externalId"


class VatTypes(str, Enum):
    NONE = "none"
    VAT0 = "vat0"
    VAT10 = "vat10"
    VAT110 = "vat110"
    VAT20 = "vat20"
    VAT120 = "vat120"


class PaymentObjects(str, Enum):
    COMMODITY = "commodity"
    SERVICE = "service"
    PAYMENT = "payment"


class PaymentMethods(str, Enum):
    FULL_PREPAYMENT = "full_prepayment"
    ADVANCE = "advance"


class RefundStatuses(str, Enum):
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    CANCELED = "canceled"
