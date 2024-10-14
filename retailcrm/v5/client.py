from dataclasses import dataclass
from typing import Optional

from retailcrm.http_cilent import BaseHttpClient, HttpClient
from retailcrm.v5.controllers import (
    CustomersController,
    CustomFieldsController,
    LoyaltyController,
    OrdersController,
    PaymentController,
    ReferencesController,
    StoreController,
    TasksController,
    UsersController, DeliveryController,
)

__all__ = ["RetailCrmApiClientV5"]


@dataclass(slots=True)
class RetailCrmApiClientV5:
    _crm_url: str
    _api_key: str
    _client: BaseHttpClient
    _payment_controller: Optional[PaymentController]
    _orders_controller: Optional[OrdersController]
    _customers_controller: Optional[CustomersController]
    _references_controller: Optional[ReferencesController]
    _custom_fields_controller: Optional[CustomFieldsController]
    _users_controller: Optional[UsersController]
    _tasks_controller: Optional[TasksController]
    _loyalty_controller: Optional[LoyaltyController]
    _store_controller: Optional[StoreController]
    _delivery_controller: Optional[DeliveryController]

    def __init__(
        self,
        crm_url: str,
        api_key: str,
        client: BaseHttpClient = None,
        use_retries: bool = False,
    ):
        self._crm_url = crm_url
        self._api_key = api_key

        if not client:
            self._client = HttpClient(crm_url, api_key, "v5", use_retries)
        else:
            self._client = client

        self._payment_controller = None
        self._orders_controller = None
        self._customers_controller = None
        self._references_controller = None
        self._custom_fields_controller = None
        self._users_controller = None
        self._tasks_controller = None
        self._loyalty_controller = None
        self._store_controller = None

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

    @property
    def tasks(self) -> TasksController:
        if not self._tasks_controller:
            self._tasks_controller = TasksController(self._client)
        return self._tasks_controller

    @property
    def loyalty(self) -> LoyaltyController:
        if not self._loyalty_controller:
            self._loyalty_controller = LoyaltyController(self._client)
        return self._loyalty_controller

    @property
    def store(self) -> StoreController:
        if not self._store_controller:
            self._store_controller = StoreController(self._client)
        return self._store_controller

    @property
    def delivery(self) -> DeliveryController:
        if not self._delivery_controller:
            self._delivery_controller = DeliveryController(self._client)
        return self._delivery_controller