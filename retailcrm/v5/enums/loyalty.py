from enum import Enum


class BonusOperationType(str, Enum):
    CREDIT_FOR_ORDER = "credit_for_order"
    BURN = "burn"
    CREDIT_FOR_EVENT = "credit_for_event"
    CHARGE_FOR_ORDER = "charge_for_order"
    CHARGE_MANUAL = "charge_manual"
    CREDIT_MANUAL = "credit_manual"
    CANCEL_OF_CHARGE = "cancel_of_charge"
    CANCEL_OF_CREDIT = "cancel_of_credit"


class BonusOperationEventType(str, Enum):
    BIRTHDAY = "birthday"
    WELCOME = "welcome"
