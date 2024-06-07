from retailcrm.http_cilent import BaseHttpClient
from retailcrm.response import Response


class RetailCrmPaymentsApi:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def check(self, check_json: str) -> Response:
        """
        **Проверка инвойса**
        Метод позволяет проверить параметры инвойса перед списанием средств.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-payment-check
        :param check_json: JSON с данными для проверки
        :return: Response
        """
        return await self._client.post(
            endpoint="/payment/check",
            data={
                "check": check_json,
            },
        )

    async def create_invoice(self, create_invoice_json: str) -> Response:
        """
        **Создание инвойса**
        Метод позволяет создать ссылку на оплату для заданного платежа.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-payment-check
        :param create_invoice_json: JSON с данными инвойса
        :return: Response
        """
        return await self._client.post(
            endpoint="/payment/create-invoice",
            data={
                "createInvoice": create_invoice_json,
            },
        )

    async def update_invoice(self, update_invoice_json: str) -> Response:
        """
        **Изменение инвойса**
        Метод позволяет изменить данные инвойса в системе.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-payment-update-invoice
        :param update_invoice_json:	JSON с данными инвойса
        :return: Response
        """
        return await self._client.post(
            endpoint=f"/payment/update-invoice",
            data={"updateInvoice": update_invoice_json},
        )
