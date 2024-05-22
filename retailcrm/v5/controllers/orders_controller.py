from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.api.orders import RetailCrmOrdersApi
from retailcrm.v5.enums import IdTypes
from retailcrm.exceptions import RetailCrmApiError
from retailcrm.v5.schemas.requests.orders.create_order import SerializedOrder
from retailcrm.v5.schemas.responses.orders.create_order import ResponseCreateOrder
from retailcrm.v5.schemas.responses.orders.get_order import ResponseGetOrder


class OrdersController:
    def __init__(self, client: BaseHttpClient):
        self._api = RetailCrmOrdersApi(client)

    async def create_order(self, order_data: SerializedOrder, site: str) -> ResponseCreateOrder:
        response = await self._api.create_order(
            order_json=order_data.model_dump_json(exclude_unset=True, by_alias=True),
            site=site
        )
        response_obj = ResponseCreateOrder.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def get_order(
            self,
            order_id,
            site,
            id_type: IdTypes = IdTypes.EXTERNAL_ID
    ) -> ResponseGetOrder:
        response = await self._api.get_order(
            order_id=order_id,
            by=id_type.value,
            site=site
        )
        response_obj = ResponseGetOrder.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj
