__all__ = ["DeliveryActions"]

from retailcrm.v5.interfaces.integrations import IntegrationActionsInterface
from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.callbacks.entities.delivery import RequestCalculate, RequestDelete, RequestPrint, \
    RequestShipmentDelete, RequestSave, RequestShipmentSave
from retailcrm.v5.schemas.callbacks.responses.delivery import DeliveryGetCallbackResponse, DeliverySaveCallbackResponse, \
    DeliveryAutocompleteCallbackResponse, DeliveryCalculateCallbackResponse, DeliveryShipmentPointListCallbackResponse, \
    DeliveryShipmentTariffCallbackResponse, DeliveryShipmentSaveCallbackResponse


class DeliveryActions(IntegrationActionsInterface):
    async def autocomplete(self, client_id: str, term: str) -> DeliveryAutocompleteCallbackResponse:
        pass

    async def calculate(self, client_id: str, calculate: RequestCalculate) -> None:
        pass

    async def delete(self, client_id: str, delete: RequestDelete) -> DeliveryCalculateCallbackResponse:
        pass

    async def get(self, client_id: str, delivery_id: str) -> DeliveryGetCallbackResponse:
        pass

    async def print(self, client_id: str, print_: RequestPrint) -> bytes:
        pass

    async def save(self, client_id: str, save: RequestSave) -> DeliverySaveCallbackResponse:
        pass

    async def shipment_delete(self, client_id: str, shipment_delete: RequestShipmentDelete) -> SuccessResponse:
        pass

    async def shipment_point_list(self, client_id: str, country: str, region: str, region_id: str, city: str, city_id: str, code: str) -> DeliveryShipmentPointListCallbackResponse:
        pass


    async def shipment_save(self, client_id: str, shipment_save: RequestShipmentSave) -> DeliveryShipmentSaveCallbackResponse:
        pass
    async def tariff_list(self, client_id: str) -> DeliveryShipmentTariffCallbackResponse:
        pass


