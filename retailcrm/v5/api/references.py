from retailcrm.http_cilent import BaseHttpClient
from retailcrm.response import Response


class RetailCrmReferencesApi:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def cost_groups(self) -> Response:
        """
        **Получение списка групп расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-cost-groups
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/cost-groups",
        )

    async def cost_groups_edit(self, code: str, cost_group_json: str) -> Response:
        """
        **Редактирование группы расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-cost-groups-code-edit
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/reference/cost-groups/{code}/edit",
            data={"costGroup": cost_group_json},
        )

    async def cost_items(self) -> Response:
        """
        **Получение списка статей расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-cost-items
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/cost-items",
        )

    async def cost_items_edit(self, code: str, cost_item_json: str) -> Response:
        """
        **Редактирование статьи расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-cost-items-code-edit
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/reference/cost-items/{code}/edit",
            data={"costItem": cost_item_json},
        )

    async def countries(self) -> Response:
        """
        **Получение списка кодов доступных стран**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-countries
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/countries",
        )

    async def couriers(self) -> Response:
        """
        **Получение списка курьеров**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-couriers
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/couriers",
        )

    async def couriers_create(self, courier_json: str) -> Response:
        """
        **Создание курьера**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-couriers
        :return: Response
        """
        return await self._client.post(
            endpoint="/reference/couriers/create", data={"courier": courier_json}
        )

    async def couriers_edit(self, courier_id: id, courier_json: str) -> Response:
        """
        **Редактирование курьера**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-couriers-id-edit
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/reference/couriers/{courier_id}/edit",
            data={"courier": courier_json},
        )

    async def order_methods(self) -> Response:
        """
        **Получение списка способов оформления заказов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-order-methods
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/order-methods",
        )

    async def order_methods_edit(self, code: str, order_method_json: str) -> Response:
        """
        **Создание/редактирование способа оформления заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-order-methods-code-edit
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/reference/order-methods/{code}/edit",
            data={"orderMethod": order_method_json},
        )

    async def order_types(self) -> Response:
        """
        **Получение списка типов заказов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-order-types
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/order-types",
        )

    async def order_types_edit(self, code: str, order_type_json: str) -> Response:
        """
        **Создание/редактирование типа заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-order-types-code-edit
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/reference/order-types/{code}/edit",
            data={"orderType": order_type_json},
        )

    async def payment_statuses(self) -> Response:
        """
        **Получение списка статусов оплаты**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-payment-statuses
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/payment-statuses",
        )

    async def payment_statuses_edit(self, code: str, payment_status_json: str) -> Response:
        """
        **Создание/редактирование статусов оплаты**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-couriers-id-edit
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/reference/payment-statuses/{code}/edit",
            data={"paymentStatus": payment_status_json},
        )

    async def payment_types(self) -> Response:
        """
        **Получение списка типов оплаты**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-payment-types
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/payment-types",
        )

    async def payment_types_edit(self, code: str, payment_type_json: str) -> Response:
        """
        **Создание/редактирование типа оплаты**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-payment-types-code-edit
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/reference/payment-types/{code}/edit",
            data={"paymentType": payment_type_json},
        )

    async def price_types(self) -> Response:
        """
        **Получение списка типов цен**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-price-types
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/price-types",
        )

    async def price_types_edit(self, code: str, price_type_json: str) -> Response:
        """
        **Создание/редактирование типа цены**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-price-types-code-edit
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/reference/price-types/{code}/edit",
            data={"priceType": price_type_json},
        )

    async def product_statuses(self) -> Response:
        """
        **Получение списка статусов товаров в заказе**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-product-statuses
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/product-statuses",
        )

    async def product_statuses_edit(self, code: str, product_status_json: str) -> Response:
        """
        **Создание/редактирование статуса товара в заказе**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-product-statuses-code-edit
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/reference/product-statuses/{code}/edit",
            data={"productStatus": product_status_json},
        )

    async def sites(self) -> Response:
        """
        **Получение списка магазинов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-sites
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/sites",
        )

    async def sites_edit(self, code: str, sites_json: str) -> Response:
        """
        **Создание/редактирование магазина**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-sites-code-edit
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/reference/sites/{code}/edit",
            data={"site": sites_json},
        )

    async def status_groups(self) -> Response:
        """
        **Получение списка групп статусов заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-status-groups
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/status-groups",
        )

    async def statuses(self) -> Response:
        """
        **Получение списка статусов заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-statuses
        :return: Response
        """
        return await self._client.get(
            endpoint="/reference/statuses",
        )
