from retailcrm.http_cilent import BaseHttpClient, HttpClient
from retailcrm.v5.controllers.customers import CustomersController
from retailcrm.v5.controllers.orders import OrdersController
from retailcrm.v5.controllers.payments import PaymentController


class RetailCrmApiClientV5:
    _payment_controller: PaymentController = None
    _orders_controller: OrdersController = None
    _customers_controller: CustomersController = None

    def __init__(self, crm_url: str, api_key: str, client: BaseHttpClient = None):
        self._crm_url = crm_url
        self._api_key = api_key

        if not client:
            self._client = HttpClient(crm_url, api_key, version="v5")
        else:
            self._client = client

    @property
    def crm_url(self):
        return self._crm_url

    @property
    def api_key(self):
        return self._api_key

    @property
    def payments(self) -> PaymentController:
        if not self._payment_controller:
            self._payment_controller = PaymentController(self._client)
        return self._payment_controller

    @property
    def orders(self) -> OrdersController:
        if not self._orders_controller:
            self._orders_controller = OrdersController(self._client)
        return self._orders_controller

    @property
    def customers(self) -> CustomersController:
        if not self._customers_controller:
            self._customers_controller = CustomersController(self._client)
        return self._customers_controller
