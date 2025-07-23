from dataclasses import dataclass
from typing import TypeVar

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
    UsersController, DeliveryController, WebAnalyticsApiResource, StatisticApiResource, VerificationController, CorporateCustomersController
)
from retailcrm.v5.utils import validate_crm_url
from retailcrm.v5.resources.base import ApiResource

__all__ = ["RetailCrmApiClientV5"]


T = TypeVar("T", bound=ApiResource)


class RetailCrmApiClientV5:
    __slots__ = (
        "_crm_url",
        "_api_key",
        "_client",
        "_resource_cache",
    )

    def __init__(
        self,
        crm_url: str,
        api_key: str,
        client: BaseHttpClient = None,
        use_retries: bool = False,
    ):
        validate_crm_url(crm_url)

        self._crm_url = crm_url
        self._api_key = api_key
        self._client = client or HttpClient(crm_url, api_key, "v5", use_retries)
        self._resource_cache: dict[str, ApiResource] = {}

    @property
    def crm_url(self) -> str:
        return self._crm_url

    @property
    def api_key(self) -> str:
        return self._api_key

    def _get_resource(self, name: str, controller_class: type[T]) -> T:
        if name not in self._resource_cache:
            self._resource_cache[name] = controller_class(self._client)
        return self._resource_cache[name]

    @property
    def payments(self) -> PaymentController:
        return self._get_resource("payments", PaymentController)

    @property
    def orders(self) -> OrdersController:
        return self._get_resource("orders", OrdersController)

    @property
    def corporate_customers(self) -> CorporateCustomersController:
        return self._get_resource("corporate_customers", CorporateCustomersController)

    @property
    def customers(self) -> CustomersController:
        return self._get_resource("customers", CustomersController)

    @property
    def references(self) -> ReferencesController:
        return self._get_resource("references", ReferencesController)

    @property
    def custom_fields(self) -> CustomFieldsController:
        return self._get_resource("custom_fields", CustomFieldsController)

    @property
    def users(self) -> UsersController:
        return self._get_resource("users", UsersController)

    @property
    def tasks(self) -> TasksController:
        return self._get_resource("tasks", TasksController)

    @property
    def loyalty(self) -> LoyaltyController:
        return self._get_resource("loyalty", LoyaltyController)

    @property
    def store(self) -> StoreController:
        return self._get_resource("store", StoreController)

    @property
    def delivery(self) -> DeliveryController:
        return self._get_resource("delivery", DeliveryController)

    @property
    def verification(self) -> VerificationController:
        return self._get_resource("verification", VerificationController)

    @property
    def web_analytics(self) -> WebAnalyticsApiResource:
        return self._get_resource("web_analytics", WebAnalyticsApiResource)

    @property
    def statistic(self) -> StatisticApiResource:
        return self._get_resource("statistic", StatisticApiResource)
