from typing import TypeVar

from retailcrm.http_cilent import BaseHttpClient, HttpClient
from retailcrm.v5.resources import (
    PaymentApiResource,
    ReferencesController,
    StoreApiResource,
    TasksApiResource,
    SettingsApiResource,
    UsersApiResource, WebAnalyticsApiResource, StatisticApiResource, VerificationController, TelephonyApiResource,
    SegmentsApiResource, OrdersPacksApiResource,
    NotificationsApiResource, OrdersApiResource, FilesApiResource, LoyaltyApiResource
)
from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.utils import validate_crm_url

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


    # @property
    # def corporate_customers(self) -> CorporateCustomersController:
    #     return self._get_resource("corporate_customers", CorporateCustomersController)
    #
    # @property
    # def customers(self) -> CustomersController:
    #     return self._get_resource("customers", CustomersController)
    #
    # @property
    # def custom_fields(self) -> CustomFieldsController:
    #     return self._get_resource("custom_fields", CustomFieldsController)

    @property
    def files(self) -> FilesApiResource:
        return self._get_resource("files", FilesApiResource)

    @property
    def loyalty(self) -> LoyaltyApiResource:
        return self._get_resource("loyalty", LoyaltyApiResource)

    @property
    def notifications(self) -> NotificationsApiResource:
        return self._get_resource("notifications", NotificationsApiResource)

    @property
    def orders(self) -> OrdersApiResource:
        return self._get_resource("orders", OrdersApiResource)

    @property
    def orders_packs(self) -> OrdersPacksApiResource:
        return self._get_resource("orders_packs", OrdersPacksApiResource)

    @property
    def payments(self) -> PaymentApiResource:
        return self._get_resource("payments", PaymentApiResource)

    @property
    def references(self) -> ReferencesController:
        return self._get_resource("references", ReferencesController)

    @property
    def segments(self) -> SegmentsApiResource:
        return self._get_resource("segments", SegmentsApiResource)

    @property
    def settings(self) -> SettingsApiResource:
        return self._get_resource("settings", SettingsApiResource)

    @property
    def store(self) -> StoreApiResource:
        return self._get_resource("store", StoreApiResource)

    @property
    def tasks(self) -> TasksApiResource:
        return self._get_resource("tasks", TasksApiResource)

    @property
    def telephony(self) -> TelephonyApiResource:
        return self._get_resource("telephony", TelephonyApiResource)

    @property
    def users(self) -> UsersApiResource:
        return self._get_resource("users", UsersApiResource)

    @property
    def verification(self) -> VerificationController:
        return self._get_resource("verification", VerificationController)

    @property
    def web_analytics(self) -> WebAnalyticsApiResource:
        return self._get_resource("web_analytics", WebAnalyticsApiResource)

    @property
    def statistic(self) -> StatisticApiResource:
        return self._get_resource("statistic", StatisticApiResource)
