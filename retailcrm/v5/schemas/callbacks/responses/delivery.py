from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.callbacks.entities.delivery import (
    ResponseAutocompleteItem,
    ResponseCalculate,
    ResponseLoadDeliveryData,
    ResponseSave,
    ResponseShipmentSave,
    Tariff,
    Terminal,
)


class DeliveryAutocompleteCallbackResponse(SuccessResponse):
    result: Optional[list[ResponseAutocompleteItem]] = Field(None)


class DeliveryCalculateCallbackResponse(SuccessResponse):
    result: Optional[list[ResponseCalculate]] = Field(None)


class DeliveryGetCallbackResponse(SuccessResponse):
    result: Optional[ResponseLoadDeliveryData] = Field(None)


class DeliverySaveCallbackResponse(SuccessResponse):
    result: Optional[ResponseSave] = Field(None)


class DeliveryShipmentPointListCallbackResponse(SuccessResponse):
    result: Optional[list[Terminal]] = Field(None)


class DeliveryShipmentSaveCallbackResponse(SuccessResponse):
    result: Optional[list[ResponseShipmentSave]] = Field(None)


class DeliveryShipmentTariffCallbackResponse(SuccessResponse):
    result: Optional[list[Tariff]] = Field(None)
