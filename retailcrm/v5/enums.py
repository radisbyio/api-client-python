from enum import Enum

__all__ = [
    "IdTypes",
    "VatRateTypes",
    "PaymentObjects",
    "PaymentMethods",
    "RefundStatuses",
    "DiscountTypes",
    "PrivilegeType",
]


class RetailEnum(Enum):
    def __str__(self):
        return self.value


class IdTypes(str, RetailEnum):
    ID = "id"
    EXTERNAL_ID = "externalId"


class VatRateTypes(str, RetailEnum):
    NONE = "none"
    VAT0 = "vat0"
    VAT10 = "vat10"
    VAT110 = "vat110"
    VAT20 = "vat20"
    VAT120 = "vat120"


class PaymentObjects(str, RetailEnum):
    COMMODITY = "commodity"
    SERVICE = "service"
    PAYMENT = "payment"


class PaymentMethods(str, RetailEnum):
    FULL_PREPAYMENT = "full_prepayment"
    ADVANCE = "advance"


class RefundStatuses(str, RetailEnum):
    PENDING = "pending"
    SUCCEEDED = "succeeded"
    CANCELED = "canceled"


class PrivilegeType(str, RetailEnum):
    NONE = "none"
    PERSONAL_DISCOUNT = "personal_discount"
    LOYALTY_LEVEL = "loyalty_level"
    LOYALTY_EVENT = "loyalty_event"


class DiscountTypes(str, RetailEnum):
    MANUAL_ORDER = "manual_order"
    MANUAL_PRODUCT = "manual_product"
    LOYALTY_LEVEL = "loyalty_level"
    LOYALTY_EVENT = "loyalty_event"
    PERSONAL = "personal"
    BONUS_CHARGE = "bonus_charge"
    ROUND = "round"
