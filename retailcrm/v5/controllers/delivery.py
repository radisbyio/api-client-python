from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.api.deliveries import RetailCrmDeliveryApi
from retailcrm.v5.enums import IdTypes
from retailcrm.v5.schemas.base import RetailCrmResponse
from retailcrm.v5.schemas.requests.delivery import (  # SerializedOrder,
    DeliveryShipmentFilterData,
    RequestStatusUpdateItem,
    StatusUpdates,
)
from retailcrm.v5.schemas.responses.deliveries import ResponseCalculation


class DeliveryController:
    def __init__(self, client: BaseHttpClient):
        self._api = RetailCrmDeliveryApi(client)

    # async def calculate(
    #     self, order: SerializedOrder, deliveryTypeCodes: list[str]
    # ) -> ResponseCalculation:
    #     response = await self._api.calculate(
    #         order_json=order.model_dump_json(exclude_unset=True, by_alias=True),
    #         delivery_type_codes=deliveryTypeCodes,
    #     )
    #     response_obj = ResponseCalculation.model_validate_json(response.body)
    #     if response.status_code >= 400:
    #         raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
    #     return response_obj

    async def tracking(
        self, status_updates: list[RequestStatusUpdateItem], sub_code: str
    ) -> RetailCrmResponse:
        response = await self._api.tracking(
            status_update_json=StatusUpdates(status_updates).model_dump_json(
                exclude_unset=True, by_alias=True
            ),
            sub_code=sub_code,
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    #
    # async def shipments(
    #     self, filter_data: DeliveryShipmentFilterData, limit: int = 20, page: int = 1
    # ) -> ResponseGetOrder:
    #     response = await self._api.shipments(
    #         filter_json=filter_data.model_dump_json(exclude_unset=True, by_alias=True),
    #         limit=limit,
    #         page=page,
    #     )
    #     response_obj = ResponseGetOrder.model_validate_json(response.body)
    #     if response.status_code >= 400:
    #         raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
    #     return response_obj
