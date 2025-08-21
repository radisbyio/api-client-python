from pydantic import field_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.references import SerializedCostGroup, SerializedCostItem, SerializedCourier, \
    SerializedCurrency, SerializedDeliveryService, SerializedDeliveryType, SerializedLegalEntity, SerializedOrderMethod, \
    SerializedOrderType, SerializedPaymentStatus, SerializedPaymentType, SerializedSite, SerializedUnit, \
    SerializedPriceType, SerializedOrderProductStatus
from retailcrm.v5.schemas.entities.store import SerializedStore


class CostGroupsEditRequest(BaseRetailCrmScheme):
    costGroup: SerializedCostGroup

    costGroup_serializer = field_serializer("costGroup")(to_json_serializer())


class CostItemsEditRequest(BaseRetailCrmScheme):
    costItem: SerializedCostItem

    costItem_serializer = field_serializer("costItem")(to_json_serializer())


class CouriersCreateRequest(BaseRetailCrmScheme):
    courier: SerializedCourier

    courier_serializer = field_serializer("courier")(to_json_serializer())


class CouriersEditRequest(BaseRetailCrmScheme):
    courier: SerializedCourier

    courier_serializer = field_serializer("courier")(to_json_serializer())



class CurrenciesCreateRequest(BaseRetailCrmScheme):
    currency: SerializedCurrency

    currency_serializer = field_serializer("currency")(to_json_serializer())


class CurrenciesEditRequest(BaseRetailCrmScheme):
    currency: SerializedCurrency

    currency_serializer = field_serializer("currency")(to_json_serializer())


class DeliveryServicesEditRequest(BaseRetailCrmScheme):
    deliveryService: SerializedDeliveryService

    deliveryService_serializer = field_serializer("deliveryService")(to_json_serializer())


class DeliveryTypesEditRequest(BaseRetailCrmScheme):
    deliveryType: SerializedDeliveryType

    deliveryType_serializer = field_serializer("deliveryType")(to_json_serializer())


class LegalEntitiesEditRequest(BaseRetailCrmScheme):
    legalEntity: SerializedLegalEntity

    legalEntity_serializer = field_serializer("legalEntity")(to_json_serializer())


class OrderMethodEditRequest(BaseRetailCrmScheme):
    orderMethod: SerializedOrderMethod

    orderMethod_serializer = field_serializer("orderMethod")(to_json_serializer())


class OrderTypesEditRequest(BaseRetailCrmScheme):
    orderType: SerializedOrderType

    orderType_serializer = field_serializer("orderType")(to_json_serializer())


class PaymentStatusEditRequest(BaseRetailCrmScheme):
    paymentStatus: SerializedPaymentStatus

    paymentStatus_serializer = field_serializer("paymentStatus")(to_json_serializer())


class PaymentTypesEditRequest(BaseRetailCrmScheme):
    paymentType: SerializedPaymentType

    paymentType_serializer = field_serializer("paymentType")(to_json_serializer())


class PriceTypesEditRequest(BaseRetailCrmScheme):
    priceType: SerializedPriceType

    priceType_serializer = field_serializer("priceType")(to_json_serializer())

class ProductStatusesEditRequest(BaseRetailCrmScheme):
    productStatus: SerializedOrderProductStatus

    productStatus_serializer = field_serializer("productStatus")(to_json_serializer())


class SitesEditRequest(BaseRetailCrmScheme):
    site: SerializedSite

    site_serializer = field_serializer("site")(to_json_serializer())


class StoreEditRequest(BaseRetailCrmScheme):
    store: SerializedStore

    store_serializer = field_serializer("store")(to_json_serializer())


class UnitEditRequest(BaseRetailCrmScheme):
    unit: SerializedUnit

    unit_serializer = field_serializer("unit")(to_json_serializer())