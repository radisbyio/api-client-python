from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas import CostItem
from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.customers import MGChannel
from retailcrm.v5.schemas.entities.references import CostGroup, Courier, Currency, DeliveryService, DeliveryType, \
    OrderMethod, OrderType, PaymentStatus, PaymentType, Site, Store, StatusGroup, Status, SerializedUnit, LegalEntity, \
    PriceType, OrderProductStatus


class CostGroupsResponse(SuccessResponse):
    costGroups: list[CostGroup] = Field(
        default_factory=list, description="Группа расходов"
    )


class CostItemsResponse(SuccessResponse):
    costItems: list[CostItem] = Field(
        default_factory=list, description="Статьи расходов"
    )


class CountriesResponse(SuccessResponse):
    countriesIso: list[str] = Field(
        default_factory=list,
        description="Список ISO 3166-1 alpha-2 кодов активных стран",
    )


class CouriersResponse(SuccessResponse):
    couriers: list[Courier] = Field(default_factory=list, description="Курьеры")


class CurrenciesResponse(SuccessResponse):
    currencies: list[Currency] = Field(default_factory=list, description="Курьеры")


class CurrenciesCreateResponse(SuccessResponse):
    id: int | None = Field(None, description="Внутренний ID созданного объекта")

class DeliveryServicesResponse(SuccessResponse):
    deliveryServices: list[DeliveryService] = Field(default_factory=list, description="Служба доставки")

class DeliveryTypesResponse(SuccessResponse):
    deliveryServices: list[DeliveryType] = Field(default_factory=list, description="Тип доставки")

class LegalEntitiesResponse(SuccessResponse):
    legalEntities: list[LegalEntity] = Field(default_factory=list, description="Список юридических лиц")


class MGChannelsResponse(SuccessResponse):
    mgChannels: list[MGChannel] = Field(default_factory=list, description="Список юридических лиц")


class OrderMethodResponse(SuccessResponse):
    orderMethods: dict[str, OrderMethod] = Field(default_factory=dict, description="Способ оформления заказа")

class OrderTypesResponse(SuccessResponse):
    orderTypes: dict[str, OrderType] = Field(default_factory=dict, description="Тип заказа")



class PaymentStatusesResponse(SuccessResponse):
    paymentStatuses: dict[str, PaymentStatus] = Field(default_factory=dict, description="	Статус оплаты")


class PaymentTypesResponse(SuccessResponse):
    paymentTypes: list[PaymentType] = Field(default_factory=list, description="Тип оплаты")


class PriceTypesResponse(SuccessResponse):
    priceTypes: list[PriceType] = Field(default_factory=list, description="Тип цены")

class ProductStatusesResponse(SuccessResponse):
    productStatuses: Optional[list[OrderProductStatus]] = Field(None, description="Статус товара в заказе")


class SitesResponse(SuccessResponse):
    sites: list[Site] = Field(default_factory=list, description="Магазин")


class StatusGroupsResponse(SuccessResponse):
    statusGroups: dict[str, StatusGroup] = Field(
        default_factory=list, description="Группа статусов"
    )

class StatusesResponse(SuccessResponse):
    statuses: dict[str, Status] = Field(default_factory=dict, description="Статус заказа")


class StoresResponse(SuccessResponse):
    stores: list[Store] =  Field(default_factory=list, description="Склад")


class UnitsResponse(SuccessResponse):
    units: list[SerializedUnit] = Field(default_factory=list)