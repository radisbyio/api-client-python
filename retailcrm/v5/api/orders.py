from retailcrm.http_cilent import BaseHttpClient
from retailcrm.response import Response


class RetailCrmOrdersApi:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def create(self, order_json: str, site: str) -> Response:
        """
        **Создание заказа**
        Метод создает заказ и возвращает внутренний ID созданного заказа.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-create
        :param order_json: string
        :param site: string
        :return: Response
        """
        return await self._client.post(
            endpoint="/orders/create",
            data={
                "site": site,
                "order": order_json,
            },
        )

    async def upload(self, orders_json: str, site: str) -> Response:
        """
        **Пакетная загрузка заказов**
        Метод позволяет загружать пакетно до 50 заказов.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-upload
        :param orders_json: string
        :param site: string
        :return: Response
        """
        return await self._client.post(
            endpoint="/orders/upload",
            data={
                "site": site,
                "orders": orders_json,
            },
        )

    async def edit(
            self, order_id: str, by: str, order_json: str, site: str
    ) -> Response:
        """
        **Редактирование заказа**
        Метод позволяет вносить изменения в заказ.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-create
        :param order_id: Внутренний или внешний ИД заказа
        :param by: Указывается, что передается в параметре externalId: внутренний (by=id) или внешний (by=externalId) ID заказа. По умолчанию externalId.
        :param order_json: Данные заказа
        :param site: Символьный код магазина
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/orders/{order_id}/edit",
            data={
                "by": by,
                "site": site,
                "order": order_json,
            },
        )

    async def get_by_id(self, order_id: str, by: str, site: str) -> Response:
        """
        **Получение информации о заказе.**
        Для доступа к методу необходимо разрешение order_read.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-orders-externalId
        :param order_id: Внутренний или внешний ИД заказа
        :param by: Указывается, что передается в параметре id: внутренний (by=id) или внешний (by=externalId) ID платежа. По умолчанию id.
        :param site: string
        :return: Response
        """
        params = {
            "by": by,
        }
        if site:
            params["site"] = site

        return await self._client.get(endpoint=f"/orders/{order_id}", params=params)

    async def get_all(
            self, filter_dict: dict, limit: int = 20, page: int = 1
    ) -> Response:
        """
        **Получение списка заказов, удовлетворяющих заданному фильтру.**
        Результат возвращается постранично. В поле pagination содержится информация о постраничной разбивке.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-orders
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_dict: Фильтр
        :return: Response
        """
        return await self._client.get(
            endpoint=f"/orders",
            params={
                "limit": limit,
                "page": page,
                **filter_dict,
            },
        )

    async def history(
            self, filter_dict: dict, limit: int = 20, page: int = 1
    ) -> Response:
        """
        **Получение списка заказов, удовлетворяющих заданному фильтру.**
        Результат возвращается постранично. В поле pagination содержится информация о постраничной разбивке.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-orders
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_dict: Фильтр
        :return: Response
        """
        return await self._client.get(
            endpoint=f"/orders/history",
            params={
                "limit": limit,
                "page": page,
                **filter_dict,
            },
        )

    async def payment_create(self, payment_json: str, site: str) -> Response:
        """
        **Добавление платежа**
        Для доступа к методу необходимо разрешение order_write.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-payments-create
        :param payment_json: Информация о платеже
        :param site: string
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/orders/payments/create",
            data={
                "site": site,
                "payment": payment_json,
            },
        )

    async def payment_edit(
            self, payment_id: str, payment_json: str, by: str, site: str = None
    ) -> Response:
        """
        **Редактирование платежа**
        Метод позволяет вносить изменения в платёж.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-payments-id-edit
        :param payment_id: Информация о платеже
        :param payment_json: Информация о платеже
        :param by: Указывается, что передается в параметре id: внутренний (by=id) или внешний (by=externalId) ID платежа. По умолчанию id.
        :param site: string
        :return: Response
        """
        data = {
            "by": by,
            "payment": payment_json,
        }
        if site:
            data["site"] = site

        return await self._client.post(
            endpoint=f"/orders/payments/{payment_id}/edit", data=data
        )

    async def payment_delete(self, payment_id: str) -> Response:
        """
        **Удаление платежа**
        Метод позволяет удалить платёж.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-payments-id-delete
        :param payment_id: 	Внутренний ID удаляемого платежа
        :return: Response
        """

        return await self._client.post(
            endpoint=f"/orders/payments/{payment_id}/delete",
        )

    async def combine(self, order_json: str, result_order_json: str, technique: str) -> Response:
        """
        **Объединение заказов**
        Метод позволяет удалить платёж.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-orders-combine
        :param order_json: 	Заказ будет удален в результате объединения
        :param resul_order_json: Заказ, в который произойдет объединение
        :param technique: Способ объединения в случае одинаковых товаров в составах заказов
        :return: Response
        """
        data = {
            "order": order_json,
            "resultOrder": result_order_json,
            "technique": technique
        }

        return await self._client.post(
            endpoint=f"/orders/combine",
            data=data,
        )
