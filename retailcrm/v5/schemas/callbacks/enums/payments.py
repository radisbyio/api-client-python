from enum import StrEnum

__all__ = ["ContragentType", "PaymentObject", "PaymentMethod", "Vat"]


class ContragentType(StrEnum):
    INDIVIDUAL = "individual"
    LEGAL_ENTITY = "legal-entity"
    ENTERPRENEUR = "enterpreneur"


class PaymentObject(StrEnum):
    COMMODITY = "commodity"
    SERVICE = "service"
    PAYMENT = "payment"


class PaymentMethod(StrEnum):
    FULL_PREPAYMENT = "full_prepayment"
    ADVANCE = "advance"


class Vat(StrEnum):
    NONE = "none"
    VAT0 = "vat0"
    VAT10 = "vat10"
    VAT110 = "vat110"
    VAT20 = "vat20"
    VAT120 = "vat120"
