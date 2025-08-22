from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.delivery import (
    DeliveryShipment,
    RequestStatusUpdateItem,
)
from retailcrm.v5.schemas.entities.orders import SerializedOrder
from retailcrm.v5.schemas.filters.delivery import DeliveryShipmentFilter
from retailcrm.v5.schemas.requests.delivery import (
    DeliveryCalculateRequest,
    DeliveryGenericTrackingRequest,
    DeliveryShipmentCreateRequest,
    DeliveryShipmentEditRequest,
    DeliveryShipmentsFilterRequest,
)
from retailcrm.v5.schemas.responses.delivery import (
    DeliveryCalculateResponse,
    DeliveryShipmentCreateResponse,
    DeliveryShipmentEditResponse,
    DeliveryShipmentGetResponse,
    DeliveryShipmentsResponse,
)


class DeliveryApiResource(ApiResource):
    async def calculate(
        self, delivery_type_codes: list[str], order: SerializedOrder
    ) -> DeliveryCalculateResponse:
        """
        **Расчёт стоимости доставки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-delivery-calculate
        :param delivery_type_codes: Коды типов доставок.
        :param order: Объект заказа.
        :return: DeliveryCalculateResponse
        """
        request = DeliveryCalculateRequest(
            deliveryTypeCodes=delivery_type_codes, order=order
        )
        response = await self._client.post(
            endpoint="/delivery/calculate",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, DeliveryCalculateResponse)

    async def generic_tracking(
        self, subcode: str, status_update: list[RequestStatusUpdateItem]
    ) -> SuccessResponse:
        """
        **Обновление статусов доставки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-delivery-generic-subcode-tracking
        :param subcode: Код интеграции.
        :param status_update: JSON с данными по статусам заказов.
        :return: DeliveryGenericTrackingResponse
        """
        if len(status_update) > 100:
            raise ValueError(
                "Too many status updates, only 100 are allowed per request."
            )
        request = DeliveryGenericTrackingRequest(statusUpdate=status_update)
        response = await self._client.post(
            endpoint=f"/delivery/generic/{subcode}/tracking",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, SuccessResponse)

    async def shipments_filter(
        self,
        filter_obj: DeliveryShipmentFilter | None = None,
        limit: int = 20,
        page: int = 1,
    ) -> DeliveryShipmentsResponse:
        """
        **Получение списка отгрузок в службы доставки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-delivery-shipments
        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: DeliveryShipmentsResponse
        """
        request = DeliveryShipmentsFilterRequest(
            filter_obj=filter_obj, limit=limit, page=page
        )
        response = await self._client.get(
            endpoint="/delivery/shipments",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, DeliveryShipmentsResponse)

    async def shipments_create(
        self,
        delivery_type: str,
        delivery_shipment: DeliveryShipment,
        site: str | None = None,
    ) -> DeliveryShipmentCreateResponse:
        """
        **Создание отгрузки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-delivery-shipments-create
        :param delivery_type: Тип доставки.
        :param delivery_shipment: Заявка на отгрузку в службу доставки.
        :param site: Символьный код магазина.
        :return: DeliveryShipmentCreateResponse
        """
        request = DeliveryShipmentCreateRequest(
            deliveryType=delivery_type, deliveryShipment=delivery_shipment, site=site
        )
        response = await self._client.post(
            endpoint="/delivery/shipments/create",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, DeliveryShipmentCreateResponse)

    async def shipments_get(self, shipment_id: str) -> DeliveryShipmentGetResponse:
        """
        **Получение информации об отгрузке**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-delivery-shipments-id
        :param shipment_id: Идентификатор отгрузки.
        :return: DeliveryShipmentGetResponse
        """
        response = await self._client.get(
            endpoint=f"/delivery/shipments/{shipment_id}",
        )
        return self._process_response(response, DeliveryShipmentGetResponse)

    async def shipments_edit(
        self,
        shipment_id: str,
        delivery_shipment: DeliveryShipment,
        site: str | None = None,
    ) -> DeliveryShipmentEditResponse:
        """
        **Редактирование отгрузки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-delivery-shipments-id-edit
        :param shipment_id: Идентификатор отгрузки.
        :param delivery_shipment: Заявка на отгрузку в службу доставки.
        :param site: Символьный код магазина.
        :return: DeliveryShipmentEditResponse
        """
        request = DeliveryShipmentEditRequest(
            deliveryShipment=delivery_shipment, site=site
        )
        response = await self._client.post(
            endpoint=f"/delivery/shipments/{shipment_id}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, DeliveryShipmentEditResponse)
