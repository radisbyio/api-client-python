from enum import Enum

__all__ = [
    "IdTypes",
    "VatRateTypes",
    "PaymentObjects",
    "PaymentMethods",
    "RefundStatuses",
    "DiscountTypes",
    "PrivilegeType",
    "ContragentTypes"
    "SexTypes",
]


class IdTypes(str, Enum):
    ID = "id"
    EXTERNAL_ID = "externalId"


class VatRateTypes(str, Enum):
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


class PrivilegeType(str, Enum):
    NONE = "none"
    PERSONAL_DISCOUNT = "personal_discount"
    LOYALTY_LEVEL = "loyalty_level"
    LOYALTY_EVENT = "loyalty_event"


class DiscountTypes(str, Enum):
    MANUAL_ORDER = "manual_order"
    MANUAL_PRODUCT = "manual_product"
    LOYALTY_LEVEL = "loyalty_level"
    LOYALTY_EVENT = "loyalty_event"
    PERSONAL = "personal"
    BONUS_CHARGE = "bonus_charge"
    ROUND = "round"


class ContragentTypes(str, Enum):
    ENTERPRENEUR = "enterpreneur"
    INDIVIDUAL = "individual"
    LEGAL_ENTITY = "legal-entity"


class SexTypes(str, Enum):
    FEMALE = "female"
    MALE = "male"
