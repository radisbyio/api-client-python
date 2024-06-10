from retailcrm.http_cilent import BaseHttpClient
from retailcrm.response import Response


class RetailCrmDeliveryApi:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def calculate(
        self, order_json: str, delivery_type_codes: list[str]
    ) -> Response:
        """
        **Расчёт стоимости доставки**
        Метод рассчитывает стоимость доставки для выбранных типов доставок (deliveryTypeCodes).

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-delivery-calculate
        :param order_json: Данные заказа
        :param delivery_type_codes: Коды типов доставок
        :return: Response
        """
        return await self._client.post(
            endpoint="/delivery/calculate",
            data={
                "order": order_json,
                "deliveryTypeCodes": delivery_type_codes,
            },
        )

    async def tracking(self, status_update_json: str, sub_code: str) -> Response:
        """
        **Обновление статусов доставки**
        Метод позволяет передавать статусы отдельно для каждого заказа в момент смены
        статуса или передавать историю изменений по группе заказов через определенные
        промежутки на усмотрение службы доставки.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-delivery-generic-subcode-tracking
        :param sub_code: Идентификатор модуля интеграции
        :param tracking_data_json:
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/delivery/generic/{sub_code}/tracking",
            data={
                "statusUpdate": status_update_json,
            },
        )

    async def shipments(
        self, filter_json: str, limit: int = 20, page: int = 1
    ) -> Response:
        """
        **Получение списка отгрузок в службы доставки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-delivery-shipments
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_json: Фильтр
        :return: Response
        """

        return await self._client.get(
            endpoint=f"/delivery/shipments",
            params={
                "limit": limit,
                "page": page,
                "filter": filter_json,
            },
        )

    async def shipments_create(
        self, delivery_type: str, site: str, delivery_shipment_json: str
    ) -> Response:
        """
        **Создание отгрузки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-delivery-shipments-create
        :param delivery_type: Тип доставки
        :param site: Символьный код магазина
        :param delivery_shipment_json: Заявка на отгрузку в службу доставки
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/shipments/create",
            data={
                "deliveryType": delivery_type,
                "site": site,
                "deliveryShipment": delivery_shipment_json,
            },
        )

    async def shipments_get(self, shipment_id: str) -> Response:
        """
        **Получение информации об отгрузке**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-delivery-shipments-id
        :param shipment_id: Идентификатор отгрузки
        :return: Response
        """
        return await self._client.get(endpoint=f"/delivery/shipments/{shipment_id}")

    async def shipments_edit(
        self, shipment_id: str, delivery_shipment_json: str, site: str = None
    ) -> Response:
        """
        **Редактирование платежа**
        Метод позволяет вносить изменения в платёж.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-payments-id-edit
        :param shipment_id: Идентификатор отгрузки
        :param delivery_shipment_json: Заявка на отгрузку в службу доставки
        :param site: string
        :return: Response
        """
        data = {
            "deliveryShipment": delivery_shipment_json,
        }
        if site:
            data["site"] = site

        return await self._client.post(
            endpoint=f"/delivery/shipments/{shipment_id}/edit", data=data
        )
