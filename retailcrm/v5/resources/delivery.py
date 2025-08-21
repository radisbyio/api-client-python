from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.schemas.delivery import (
    DeliveryTrackingResponse,
    DeliveryShipmentFilterData,
    FilterDeliveryShipmentsResponse,
    CreateDeliveryShipmentsResponse,
    GetDeliveryShipmentResponse,
    EditDeliveryShipmentsResponse,
    DeliveryShipment,
    RequestStatusUpdateItem,
    CalculationResponse,
)
from retailcrm.v5.utils import pydantic_to_nested_dict


class DeliveryController:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def calculate(self, order: SerializedOrder, delivery_type_codes: list[str]) -> CalculationResponse:
        """
        Расчёт стоимости доставки

        Метод рассчитывает стоимость доставки для выбранных типов доставок (deliveryTypeCodes).
        :param order:
        :param delivery_type_codes:
        :return:
        """
        response = await self._client.post(
            endpoint=f"/delivery/calculate",
            data={
                "deliveryTypeCodes": delivery_type_codes,
                "order": order.model_dump_json(exclude_unset=True, by_alias=True),
            },
        )
        response_obj = CalculationResponse.model_validate_json(response.content)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def tracking(
            self, status_update: RequestStatusUpdateItem, sub_code: str
    ) -> DeliveryTrackingResponse:
        """
        Обновление статусов доставки
        Метод позволяет передавать статусы отдельно для каждого заказа в момент смены
        статуса или передавать историю изменений по группе заказов через определенные
        промежутки на усмотрение службы доставки.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-delivery-generic-subcode-tracking
        :param sub_code: Идентификатор модуля интеграции
        :param status_update:
        :return: Response
        """
        response = await self._client.post(
            endpoint=f"/delivery/generic/{sub_code}/tracking",
            data={
                "statusUpdate": [
                    status_update.model_dump_json(exclude_unset=True, by_alias=True)
                ],
            },
        )
        response_obj = DeliveryTrackingResponse.model_validate_json(response.content)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def shipments_filter(
            self, filter_data: DeliveryShipmentFilterData | None = None, limit: int = 20, page: int = 1
    ) -> FilterDeliveryShipmentsResponse:
        """
        Получение списка отгрузок в службы доставки

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-delivery-shipments
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_data: Фильтр
        :return: Response
        """
        response = await self._client.get(
            endpoint=f"/delivery/shipments",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )
        response_obj = FilterDeliveryShipmentsResponse.model_validate_json(response.content)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def shipments_create(
            self, delivery_shipment: DeliveryShipment, delivery_type: str, site: str
    ) -> CreateDeliveryShipmentsResponse:
        """
        Создание отгрузки

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-delivery-shipments-create
        :param delivery_type: Тип доставки
        :param site: Символьный код магазина
        :param delivery_shipment: Заявка на отгрузку в службу доставки
        :return: Response
        """
        response = await self._client.post(
            endpoint="/delivery/shipments/create",
            data={
                "deliveryType": delivery_type,
                "site": site,
                "deliveryShipment": delivery_shipment.model_dump_json(
                    exclude_unset=True, by_alias=True
                ),
            },
        )

        response_obj = CreateDeliveryShipmentsResponse.model_validate_json(
            response.content
        )
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def shipments_get(self, shipment_id: int) -> GetDeliveryShipmentResponse:
        """
        Получение информации об отгрузке

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-delivery-shipments-id
        :param shipment_id: Идентификатор отгрузки
        :return: Response
        """
        response = await self._client.get(
            endpoint=f"/delivery/shipments/{shipment_id}"
        )

        response_obj = GetDeliveryShipmentResponse.model_validate_json(
            response.content
        )
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def shipments_edit(
            self, shipment_id: int, delivery_shipment: DeliveryShipment, site: str = None
    ) -> EditDeliveryShipmentsResponse:
        """
        Редактирование платежа
        Метод позволяет вносить изменения в платёж.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-payments-id-edit
        :param shipment_id: Идентификатор отгрузки
        :param delivery_shipment: Заявка на отгрузку в службу доставки
        :param site: string
        :return: Response
        """
        data = {
            "deliveryShipment": delivery_shipment.model_dump_json(
                exclude_unset=True, by_alias=True
            ),
        }
        if site:
            data["site"] = site

        response = await self._client.post(
            endpoint=f"/delivery/shipments/{shipment_id}/edit", data=data
        )
        response_obj = EditDeliveryShipmentsResponse.model_validate_json(
            response.content
        )
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj
