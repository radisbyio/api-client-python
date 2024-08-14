from dataclasses import dataclass
from typing import Optional

from retailcrm.http_cilent import BaseHttpClient, HttpClient
from retailcrm.v5.controllers.custom_fields import CustomFieldsController
from retailcrm.v5.controllers.customers import CustomersController
from retailcrm.v5.controllers.delivery import DeliveryController
from retailcrm.v5.controllers.orders import OrdersController
from retailcrm.v5.controllers.payments import PaymentController
from retailcrm.v5.controllers.references import ReferencesController
from retailcrm.v5.controllers.users import UsersController


@dataclass(slots=True)
class RetailCrmApiClientV5:
    _crm_url: str
    _api_key: str
    _client: BaseHttpClient
    _payment_controller: Optional[PaymentController]
    _orders_controller: Optional[OrdersController]
    _customers_controller: Optional[CustomersController]
    _delivery_controller: Optional[DeliveryController]
    _references_controller: Optional[ReferencesController]
    _custom_fields_controller: Optional[CustomFieldsController]
    _users_controller: Optional[UsersController]

    def __init__(self, crm_url: str, api_key: str, client: BaseHttpClient = None):
        self._crm_url = crm_url
        self._api_key = api_key

        if not client:
            self._client = HttpClient(crm_url, api_key, version="v5")
        else:
            self._client = client

        self._payment_controller = None
        self._orders_controller = None
        self._customers_controller = None
        self._delivery_controller = None
        self._references_controller = None
        self._custom_fields_controller = None
        self._users_controller = None

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

    @property
    def delivery(self) -> DeliveryController:
        if not self._delivery_controller:
            self._delivery_controller = DeliveryController(self._client)
        return self._delivery_controller

    @property
    def references(self) -> ReferencesController:
        if not self._references_controller:
            self._references_controller = ReferencesController(self._client)
        return self._references_controller

    @property
    def custom_fields(self) -> CustomFieldsController:
        if not self._custom_fields_controller:
            self._custom_fields_controller = CustomFieldsController(self._client)
        return self._custom_fields_controller

    @property
    def users(self) -> UsersController:
        if not self._users_controller:
            self._users_controller = UsersController(self._client)
        return self._users_controller
