from enum import Enum

__all__ = [
    "IdTypes",
    "VatRateTypes",
    "PaymentObjects",
    "PaymentMethods",
    "RefundStatuses",
    "DiscountTypes",
    "PrivilegeType",
    "ContragentTypes",
    "SexTypes",
    "TasksStatuses",
    "NotificationTypes",
    "ViewModeTypes",
    "CustomFieldEntityTypes",
    "DisplayAreaTypes",
    "CustomFieldTypes",
    "CombineTechniqueTypes",
    "DeliveryStatusTypes",
    "DeliveryShipmentStatusTypes",
    "ProductTypes",
]


class RetailCrmEnum(Enum):
    def __str__(self):
        return str(self.value)


class IdTypes(str, RetailCrmEnum):
    ID = "id"
    EXTERNAL_ID = "externalId"


class VatRateTypes(str, RetailCrmEnum):
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





class CombineTechniqueTypes(str, Enum):
    OURS = "ours"
    SUMM = "summ"
    THEIRS = "theirs"


class CustomFieldEntityTypes(str, RetailCrmEnum):
    ORDER = "order"
    CUSTOMER = "customer"
    CUSTOMER_CORPORATE = "customer_corporate"
    COMPANY = "company"
    LOYALTY_ACCOUNT = "loyalty_account"


class DisplayAreaTypes(str, Enum):
    ADDRESS = "address"
    CUSTOMER = "customer"
    DELIVERY = "delivery"
    DIMENSIONS = "dimensions"
    LEGAL_DETAILS = "legal_details"
    MAIN_DATA = "main_data"
    PAYMENT = "payment"
    SHIPMENT = "shipment"


class CustomFieldTypes(str, Enum):
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
    DICTIONARY = "dictionary"
    EMAIL = "email"
    INTEGER = "integer"
    MULTISELECT_DICTIONARY = "multiselect_dictionary"
    NUMERIC = "numeric"
    STRING = "string"
    TEXT = "text"


class ViewModeTypes(str, Enum):
    EDITABLE = "editable"
    MISS = "miss"
    NOT_EDITABLE = "not_editable"


class NotificationTypes(str, Enum):
    API_INFO = "api.info"
    API_ERROR = "api.error"


class DeliveryStatusTypes(str, Enum):
    CANCEL = "cancel"
    CANCEL_FORCE = "cancel_force"
    ERROR = "error"
    NONE = "none"
    PROCESSING = "processing"
    SUCCESS = "success"


class DeliveryShipmentStatusTypes(str, Enum):
    CREATED = "created"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


class ProductTypes(str, Enum):
    PRODUCT = "product"
    SERVICE = "service"
