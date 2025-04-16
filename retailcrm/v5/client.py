from dataclasses import dataclass

from retailcrm.http_cilent import BaseHttpClient, HttpClient
from retailcrm.v5.resources import (
    CustomersController,
    CustomFieldsController,
    LoyaltyController,
    OrdersController,
    PaymentController,
    ReferencesController,
    StoreController,
    TasksController,
    UsersController, DeliveryController, WebAnalyticsController, StatisticController, VerificationController, CorporateCustomersController
)

__all__ = ["RetailCrmApiClientV5"]


@dataclass(slots=True)
class RetailCrmApiClientV5:
    _crm_url: str
    _api_key: str
    _client: BaseHttpClient

    def __init__(
            self,
            crm_url: str,
            api_key: str,
            client: BaseHttpClient = None,
            use_retries: bool = False,
    ):
        self._crm_url = crm_url
        self._api_key = api_key
        self._client = client or HttpClient(crm_url, api_key, "v5", use_retries)

    @property
    def crm_url(self):
        return self._crm_url

    @property
    def api_key(self):
        return self._api_key

    @property
    def payments(self) -> PaymentController:
        return PaymentController(self._client)

    @property
    def orders(self) -> OrdersController:
        return OrdersController(self._client)

    @property
    def corporate_customers(self) -> CorporateCustomersController:
        return CorporateCustomersController(self._client)

    @property
    def customers(self) -> CustomersController:
        return CustomersController(self._client)

    @property
    def references(self) -> ReferencesController:
        return ReferencesController(self._client)

    @property
    def custom_fields(self) -> CustomFieldsController:
        return CustomFieldsController(self._client)

    @property
    def users(self) -> UsersController:
        return UsersController(self._client)

    @property
    def tasks(self) -> TasksController:
        return TasksController(self._client)

    @property
    def loyalty(self) -> LoyaltyController:
        return LoyaltyController(self._client)

    @property
    def store(self) -> StoreController:
        return StoreController(self._client)

    @property
    def delivery(self) -> DeliveryController:
        return DeliveryController(self._client)

    @property
    def verification(self) -> VerificationController:
        return VerificationController(self._client)

    @property
    def web_analytics(self) -> WebAnalyticsController:
        return WebAnalyticsController(self._client)

    @property
    def statistic(self) -> StatisticController:
        return StatisticController(self._client)
