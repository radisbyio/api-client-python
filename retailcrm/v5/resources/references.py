from retailcrm.v5.api.references import RetailCrmReferencesApi
from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas import SuccessResponse
from retailcrm.v5.schemas.entities.references import SerializedCurrency, SerializedDeliveryService, \
    SerializedDeliveryType, SerializedLegalEntity, SerializedOrderMethod, SerializedOrderType, SerializedPaymentStatus, \
    SerializedPaymentType, SerializedUnit, SerializedCostGroup, SerializedCostItem, SerializedCourier, \
    SerializedPriceType, SerializedSite
from retailcrm.v5.schemas.entities.store import SerializedStore
from retailcrm.v5.schemas.references import SerializedOrderProductStatus
from retailcrm.v5.schemas.requests.references import CostGroupsEditRequest, CostItemsEditRequest, CouriersCreateRequest, \
    CouriersEditRequest, CurrenciesCreateRequest, CurrenciesEditRequest, DeliveryServicesEditRequest, \
    DeliveryTypesEditRequest, LegalEntitiesEditRequest, OrderMethodEditRequest, OrderTypesEditRequest, \
    PaymentStatusEditRequest, PaymentTypesEditRequest, PriceTypesEditRequest, ProductStatusesEditRequest, \
    SitesEditRequest, StoreEditRequest, UnitEditRequest
from retailcrm.v5.schemas.responses.references import CostGroupsResponse, CostItemsResponse, CountriesResponse, \
    CouriersResponse, CurrenciesResponse, CurrenciesCreateResponse, DeliveryServicesResponse, DeliveryTypesResponse, \
    LegalEntitiesResponse, MGChannelsResponse, OrderMethodResponse, OrderTypesResponse, PaymentStatusesResponse, \
    PaymentTypesResponse, PriceTypesResponse, ProductStatusesResponse, SitesResponse, StatusGroupsResponse, \
    StatusesResponse, StoresResponse


class ReferencesController(ApiResource):
    _api: RetailCrmReferencesApi

    async def cost_groups(self) -> CostGroupsResponse:
        """
        **Получение списка групп расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-cost-groups
        :return: CostGroupsResponse
        """
        response = await self._client.get(
            endpoint="/reference/cost-groups",
        )

        return self._process_response(response, CostGroupsResponse)

    async def cost_groups_edit(
        self, code: str, cost_group: SerializedCostGroup
    ) -> SuccessResponse:
        """
        **Редактирование группы расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-cost-groups-code-edit
        :return: SuccessResponse
        """
        request = CostGroupsEditRequest(costGroup=cost_group)
        response = await self._client.post(
            endpoint=f"/reference/cost-groups/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, SuccessResponse)

    async def cost_items(self) -> CostItemsResponse:
        """
        **Получение списка статей расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-cost-items
        :return: CostItemsResponse
        """
        response = await self._client.get(
            endpoint="/reference/cost-items",
        )
        return self._process_response(response, CostItemsResponse)

    async def cost_items_edit(
        self, code: str, cost_item: SerializedCostItem
    ) -> SuccessResponse:
        """
        **Редактирование статьи расходов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-cost-items-code-edit
        :return: SuccessResponse
        """
        request = CostItemsEditRequest(costItem=cost_item)
        response =  await self._client.post(
            endpoint=f"/reference/cost-items/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, SuccessResponse)

    async def countries(self) -> CountriesResponse:
        """
        **Получение списка кодов доступных стран**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-countries
        :return: Response
        """
        response = await self._client.get(
            endpoint="/reference/countries",
        )
        return self._process_response(response, CountriesResponse)

    async def couriers(self) -> CouriersResponse:
        """
        **Получение списка курьеров**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-couriers
        :return: CouriersResponse
        """
        response = await self._client.get(
            endpoint="/reference/couriers",
        )
        return self._process_response(response, CouriersResponse)

    async def couriers_create(self, courier: SerializedCourier) -> SuccessResponse:
        """
        **Создание курьера**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-couriers
        :return: Response
        """
        request = CouriersCreateRequest(courier=courier)
        response = await self._client.post(
            endpoint="/reference/couriers/create",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, SuccessResponse)

    async def couriers_edit(
        self, courier_id: int, courier: SerializedCourier
    ) -> SuccessResponse:
        """
        **Редактирование курьера**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-couriers-id-edit
        :return: Response
        """
        request = CouriersEditRequest(courier=courier)
        response = await self._client.post(
            endpoint=f"/reference/couriers/{courier_id}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, SuccessResponse)

    async def currencies(self) -> CurrenciesResponse:
        """
        **Получение списка валют**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-currencies
        :return: CurrenciesResponse
        """
        response = await self._client.get(
            endpoint="/reference/currencies",
        )
        return self._process_response(response, CurrenciesResponse)

    async def currencies_create(self, currency: SerializedCurrency) -> CurrenciesCreateResponse:
        """
        **Создание валюты**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-currencies-create
        :return: CurrenciesCreateResponse
        """
        request = CurrenciesCreateRequest(currency=currency)
        response = await self._client.post(
            endpoint="/reference/currencies/create",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, CurrenciesCreateResponse)

    async def currencies_edit(self, currency_id: int, currency: SerializedCurrency) -> SuccessResponse:
        """
        **Редактирование валюты**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-currencies-id-edit
        :return: SuccessResponse
        """
        request = CurrenciesEditRequest(currency=currency)
        response = await self._client.post(
            endpoint=f"reference/currencies/{currency_id}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, SuccessResponse)

    async def delivery_services(self) -> DeliveryServicesResponse:
        """
        **Получение списка служб доставки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-delivery-services
        :return: DeliveryServicesResponse
        """
        response = await self._client.get(
            endpoint="/reference/delivery-services",
        )
        return self._process_response(response, DeliveryServicesResponse)

    async def delivery_services_edit(self, code: str, delivery_service: SerializedDeliveryService) -> SuccessResponse:
        """
        **Редактирование валюты**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-currencies-id-edit
        :return: SuccessResponse
        """
        request = DeliveryServicesEditRequest(deliveryService=delivery_service)
        response = await self._client.post(
            endpoint=f"reference/delivery-services/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, SuccessResponse)



    async def delivery_types(self) -> DeliveryTypesResponse:
        """
        **Получение списка типов доставки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-delivery-types
        :return: DeliveryTypesResponse
        """
        response = await self._client.get(
            endpoint="/reference/delivery-types",
        )
        return self._process_response(response, DeliveryTypesResponse)

    async def delivery_types_edit(self, code: str, delivery_type: SerializedDeliveryType) -> SuccessResponse:
        """
        **Создание/редактирование типа доставки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-delivery-types-code-edit
        :return: SuccessResponse
        """
        request = DeliveryTypesEditRequest(deliveryType=delivery_type)
        response = await self._client.post(
            endpoint=f"reference/delivery-services/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, SuccessResponse)

    async def legal_entities(self) -> LegalEntitiesResponse:
        """
        **Получение списка юридических лиц**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-legal-entities
        :return: LegalEntitiesResponse
        """
        response = await self._client.get(
            endpoint="/reference/legal-entities",
        )
        return self._process_response(response, LegalEntitiesResponse)

    async def legal_entities_edit(self, code: str, legal_entity: SerializedLegalEntity) -> SuccessResponse:
        """
        **Создание/редактирование юридического лица**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-legal-entities-code-edit
        :return: SuccessResponse
        """
        request = LegalEntitiesEditRequest(legalEntity=legal_entity)
        response = await self._client.post(
            endpoint=f"/reference/legal-entities/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, SuccessResponse)

    async def mg_channels(self) -> MGChannelsResponse:
        """
        **Получение списка MessageGateway каналов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-mg-channels
        :return: MGChannelsResponse
        """
        response = await self._client.get(
            endpoint="/reference/mg-channels",
        )
        return self._process_response(response, MGChannelsResponse)


    async def order_methods(self) -> OrderMethodResponse:
        """
        **Получение списка способов оформления заказов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-order-methods
        :return: OrderMethodResponse
        """

        response =await self._client.get(
            endpoint="/reference/order-methods",
        )

        return self._process_response(response, OrderMethodResponse)

    async def order_methods_edit(
        self, code: str, order_method: SerializedOrderMethod
    ) -> SuccessResponse:
        """
        **Создание/редактирование способа оформления заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-order-methods-code-edit
        :return: SerializedOrderMethod
        """

        request = OrderMethodEditRequest(orderMethod=order_method)

        response = await self._client.post(
            endpoint=f"/reference/order-methods/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )

        return self._process_response(response, SuccessResponse)

    async def order_types(self) -> OrderTypesResponse:
        """
        **Получение списка типов заказов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-order-types
        :return: OrderTypesResponse
        """

        response = await self._client.get(
            endpoint="/reference/order-types",
        )

        return self._process_response(response, OrderTypesResponse)

    async def order_types_edit(
        self, code: str, order_type: SerializedOrderType
    ) -> SuccessResponse:
        """
        **Создание/редактирование типа заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-order-types-code-edit
        :return: SuccessResponse
        """

        request = OrderTypesEditRequest(orderType=order_type)

        response = await self._client.post(
            endpoint=f"/reference/order-types/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )

        return self._process_response(response, SuccessResponse)

    async def payment_statuses(self) -> PaymentStatusesResponse:
        """
        **Получение списка статусов оплаты**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-payment-statuses
        :return: PaymentStatusesResponse
        """

        response =  await self._client.get(
            endpoint="/reference/payment-statuses",
        )
        return self._process_response(response, PaymentStatusesResponse)

    async def payment_statuses_edit(
        self, code: str, payment_status: SerializedPaymentStatus
    ) -> SuccessResponse:
        """
        **Создание/редактирование статусов оплаты**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-couriers-id-edit
        :return: SuccessResponse
        """

        request = PaymentStatusEditRequest(paymentStatus=payment_status)

        response = await self._client.post(
            endpoint=f"/reference/payment-statuses/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )

        return self._process_response(response, SuccessResponse)

    async def payment_types(self) -> PaymentTypesResponse:
        """
        **Получение списка типов оплаты**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-payment-types
        :return: PaymentTypesResponse
        """
        response = await self._client.get(
            endpoint="/reference/payment-types",
        )
        return self._process_response(response, PaymentTypesResponse)

    async def payment_types_edit(
        self, code: str, payment_type: SerializedPaymentType
    ) -> SuccessResponse:
        """
        **Создание/редактирование типа оплаты**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-payment-types-code-edit
        :return: SuccessResponse
        """
        request = PaymentTypesEditRequest(paymentType=payment_type)
        response = await self._client.post(
            endpoint=f"/reference/payment-types/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, SuccessResponse)

    async def price_types(self) -> PriceTypesResponse:
        """
        **Получение списка типов цен**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-price-types
        :return: PriceTypesResponse
        """
        response = await self._client.get(
            endpoint="/reference/price-types",
        )
        return self._process_response(response, PriceTypesResponse)

    async def price_types_edit(
        self, code: str, price_type: SerializedPriceType
    ) -> SuccessResponse:
        """
        **Создание/редактирование типа цены**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-price-types-code-edit
        :return: SuccessResponse
        """
        request = PriceTypesEditRequest(priceType=price_type)
        response = await self._client.post(
            endpoint=f"/reference/price-types/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, SuccessResponse)

    async def product_statuses(self) -> ProductStatusesResponse:
        """
        **Получение списка статусов товаров в заказе**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-product-statuses
        :return: ProductStatusesResponse
        """
        response = await self._client.get(
            endpoint="/reference/product-statuses",
        )
        return self._process_response(response, ProductStatusesResponse)

    async def product_statuses_edit(
        self, code: str, product_status: SerializedOrderProductStatus
    ) -> SuccessResponse:
        """
        **Создание/редактирование статуса товара в заказе**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-product-statuses-code-edit
        :return: SuccessResponse
        """
        request = ProductStatusesEditRequest(productStatus=product_status)
        response = await self._client.post(
            endpoint=f"/reference/product-statuses/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, SuccessResponse)

    async def sites(self) -> SitesResponse:
        """
        **Получение списка магазинов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-sites
        :return: SitesResponse
        """
        response = await self._client.get(
            endpoint="/reference/sites",
        )
        return self._process_response(response, SitesResponse)

    async def sites_edit(self, code: str, site: SerializedSite) -> SuccessResponse:
        """
        **Создание/редактирование магазина**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-sites-code-edit
        :return: SuccessResponse
        """
        request = SitesEditRequest(site=site)
        response = await self._client.post(
            endpoint=f"/reference/sites/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, SuccessResponse)

    async def status_groups(self) -> StatusGroupsResponse:
        """
        **Получение списка групп статусов заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-status-groups
        :return: StatusGroupsResponse
        """
        response = await self._client.get(
            endpoint="/reference/status-groups",
        )
        return self._process_response(response, StatusGroupsResponse)

    async def statuses(self) -> StatusesResponse:
        """
        **Получение списка статусов заказа**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-statuses
        :return: StatusesResponse
        """
        response = await self._client.get(
            endpoint="/reference/statuses",
        )
        return self._process_response(response, StatusesResponse)

    async def stores(self) -> StoresResponse:
        """
        **Получение списка складов**
        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-stores
        :return: StoresResponse
        """
        response = await self._client.get(
            endpoint="/reference/stores",
        )
        return self._process_response(response, StoresResponse)

    async def stores_edit(self, code: str, store: SerializedStore) -> SuccessResponse:
        """
        **Создание/редактирование сведений о складе**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-stores-code-edit
        :return: SuccessResponse
        """
        request = StoreEditRequest(store=store)
        response = await self._client.post(
            endpoint=f"/reference/stores/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )
        return self._process_response(response, SuccessResponse)

    async def units(self) -> StatusGroupsResponse:
        """
        **Получение списка единиц измерений**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-reference-units
        :return: StatusGroupsResponse
        """
        response = await self._client.get(
            endpoint="/reference/units",
        )
        return self._process_response(response, StatusGroupsResponse)

    async def units_edit(self, code: str, unit: SerializedUnit) -> SuccessResponse:
        """
        **Создание/редактирование единицы измерения**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-reference-units-code-edit
        :return: SuccessResponse
        """
        request = UnitEditRequest(unit=unit)

        response = await self._client.post(
            endpoint=f"/reference/units/{code}/edit",
            json_str=request.model_dump_json(exclude_none=True, exclude_unset=True),
        )

        return self._process_response(response, SuccessResponse)