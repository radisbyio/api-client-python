from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from retailcrm.v5.schemas.base import RetailCrmResponse
from retailcrm.v5.schemas.shared import Courier, CourierPhone, SerializedSource

__all__ = [
    "Status",
    "ResponseStatuses",
    "StatusGroup",
    "ResponseStatusGroups",
    "CostGroup",
    "ResponseCostGroups",
    "SerializedCostGroup",
    "CostItem",
    "ResponseCostItems",
    "SerializedCostItem",
    "ResponseCostItems",
    "ResponseCountries",
    "ResponseCouriers",
    "SerializedCourier",
]


class Status(BaseModel):
    name: str = Field(description="Название")
    code: str = Field(description="Символьный код")
    active: bool = Field(False, description="Статус активности")
    ordering: int = Field(description="Порядок")
    group: str = Field(description="Группа статусов, к которой относится статус")


class ResponseStatuses(RetailCrmResponse):
    statuses: dict[str, Status] = Field(
        default_factory=list, description="Статусы заказа"
    )


class StatusGroup(BaseModel):
    name: str = Field(description="Название")
    code: str = Field(description="Символьный код")
    active: bool = Field(False, description="Статус активности")
    ordering: int = Field(description="Порядок")
    process: bool = Field(
        False, description="Является или нет процессным состоянием заказа"
    )
    statuses: list[str] = Field(
        default_factory=list,
        description="Статусы заказов, которые входят в данную группу",
    )


class ResponseStatusGroups(RetailCrmResponse):
    statusGroups: dict[str, StatusGroup] = Field(
        default_factory=list, description="Группа статусов"
    )


class CostGroup(BaseModel):
    code: str = Field(description="Символьный код группы расходов")
    name: str = Field(description="Название группы расходов")
    ordering: int = Field(description="Порядок")
    active: bool = Field(False, description="Активность")
    color: str = Field(description="Цвет")


class ResponseCostGroups(RetailCrmResponse):
    costGroups: list[CostGroup] = Field(
        default_factory=list, description="Группа расходов"
    )


class SerializedCostGroup(BaseModel):
    code: Optional[str] = Field(None, description="Символьный код группы расходов")
    name: Optional[str] = Field(None, description="Название группы расходов")
    ordering: Optional[int] = Field(None, description="Порядок")
    active: Optional[bool] = Field(None, description="Активность")
    color: Optional[str] = Field(
        None,
        description="Цвет",
        examples=[
            "#19976e",
            "#4191ff",
            "#6ce0b9",
            "#8453df",
            "#8a96a6",
            "#bc6b01",
            "#c7cdd4",
            "#ef8e06",
            "#ff8e87",
            "#ffd298",
        ],
    )


class CostItem(BaseModel):
    source: Optional[SerializedSource] = Field(
        None, description="Данные по источнику клиента"
    )
    code: str = Field(description="Символьный код статьи расходов")
    name: str = Field(description="Название статьи расходов")
    group: str = Field(description="Символьный код группы расходов")
    ordering: int = Field(description="Порядок")
    active: bool = Field(False, description="Активность")
    appliesToOrders: bool = Field(False, description="Относится к расходам по заказам")
    type: str = Field(description="Тип расхода")
    appliesToUsers: bool = Field(
        False, description="Относится к расходам по пользователям"
    )


class ResponseCostItems(RetailCrmResponse):
    costItems: list[CostItem] = Field([], description="Статьи расходов")


class SerializedCostItem(BaseModel):
    code: Optional[str] = Field(None, description="Символьный код статьи расходов")
    name: Optional[str] = Field(None, description="Название статьи расходов")
    ordering: Optional[int] = Field(None, description="Порядок")
    active: bool = Field(False, description="Активность")
    appliesToOrders: bool = Field(False, description="Относится к расходам по заказам")
    appliesToUsers: bool = Field(
        False, description="Относится к расходам по пользователям"
    )
    group: Optional[str] = Field(None, description="Символьный код группы расходов")
    source: Optional[SerializedSource] = Field(
        None, description="Данные по источнику клиента"
    )
    type: Optional[str] = Field(None, description="Тип расхода")


class ResponseCountries(RetailCrmResponse):
    countriesIso: list[str] = Field(
        default_factory=list,
        description="Список ISO 3166-1 alpha-2 кодов активных стран",
    )


class ResponseCouriers(RetailCrmResponse):
    couriers: list[Courier] = Field(default_factory=list, description="Курьеры")


class SerializedCourier(BaseModel):
    firstName: Optional[str] = Field(None, description="Имя")
    lastName: Optional[str] = Field(None, description="Фамилия")
    patronymic: Optional[str] = Field(None, description="Отчество")
    active: Optional[bool] = Field(None, description="Признак активности")
    email: Optional[str] = Field(None, description="Электронная почта")
    description: Optional[str] = Field(None, description="Примечание")
    phone: Optional[CourierPhone] = Field(None, description="Контактный телефон")


class LegalEntity(BaseModel):
    contragentType: str = Field()
    legalName: str = Field()
    legalAddress: str = Field()
    inn: str = Field()
    okpo: str = Field()
    kpp: str = Field()
    ogrn: str = Field()
    ogrnip: str = Field()
    certificateNumber: str = Field()
    certificateDate: datetime = Field()
    bik: str = Field()
    bank: str = Field()
    bankAddress: str = Field()
    corrAccount: str = Field()
    bankAccount: str = Field()
    code: str = Field()
    countryIso: str = Field()
    vatRate: str = Field()


class Site(BaseModel):
    catalogId: str = Field()
    isCatalogMainSite: bool = Field(False)
    isDemo: bool = Field(False)
    id: int = Field()
    name: str = Field()
    url: str = Field("")
    code: str = Field()
    description: str = Field("")
    phones: str = Field("")
    address: str = Field("")
    zip: str = Field("")
    defaultForCrm: bool = Field(False)
    ymlUrl: str = Field("")
    loadFromCrm: bool = Field(False)
    catalogUpdatedAt: Optional[datetime] = Field(None)
    catalogLoadingAt: Optional[datetime] = Field(None)
    ordering: int = Field()
    contragent: Optional[LegalEntity] = Field(None)
    countryIso: str = Field("")
    currency: str = Field("")
    senderEmail: str = Field("")
    senderName: str = Field("")


class SerializedSite(BaseModel):
    name: Optional[str] = Field(None)
    url: Optional[str] = Field(None)
    code: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    phones: Optional[str] = Field(None)
    address: Optional[str] = Field(None)
    zip: Optional[str] = Field(None)
    ymlUrl: Optional[str] = Field(None)
    defaultForCrm: Optional[bool] = Field(None)
    loadFromCrm: Optional[bool] = Field(None)
    catalogUpdatedAt: Optional[datetime] = Field(None)
    catalogLoadingAt: Optional[datetime] = Field(None)
    countryIso: Optional[str] = Field(None)
    contragentCode: Optional[str] = Field(None)
    currency: Optional[str] = Field(None)


class ResponseSites(RetailCrmResponse):
    sites: dict[str, Site] = Field(default_factory=dict)


class ResponseSitesEdit(RetailCrmResponse):
    id: int = Field(description="Внутренний ID созданного объекта")


class OrderProductStatus(BaseModel):
    code: str = Field()
    ordering: int = Field()
    active: bool = Field(False)
    createdAt: datetime = Field()
    orderStatusByProductStatus: str = Field("")
    orderStatusForProductStatus: str = Field("")
    cancelStatus: bool = Field(False)
    name: str = Field()


class ResponseProductStatuses(RetailCrmResponse):
    productStatuses: dict[str, OrderProductStatus] = Field(default_factory=dict)


class SerializedOrderProductStatus(BaseModel):
    name: Optional[str] = Field(None)
    code: Optional[str] = Field(None)
    type: Optional[str] = Field(None)
    ordering: Optional[int] = Field(None)
    active: Optional[bool] = Field(None)
    cancelStatus: Optional[bool] = Field(None)
    orderStatusByProductStatus: Optional[str] = Field(None)
    orderStatusForProductStatus: Optional[str] = Field(None)


class GeoHierarchyRow(BaseModel):
    country: str = Field("")
    regionId: str = Field("")
    region: str = Field("")
    cityId: str = Field("")
    city: str = Field("")


class PriceType(BaseModel):
    id: int = Field()
    code: str = Field()
    name: str = Field()
    active: bool = Field(False)
    default: bool = Field(False)
    description: str = Field("")
    filterExpression: str = Field("")
    geo: list[GeoHierarchyRow] = Field(default_factory=list)
    groups: list[int] = Field(default_factory=list)  # TODO: проверить ответ на этот запрос
    ordering: int = Field()
    currency: str = Field("")


class SerializedPriceType(BaseModel):
    code: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    active: Optional[bool] = Field(None)
    default: Optional[bool] = Field(None)
    description: Optional[str] = Field(None)
    filterExpression: Optional[str] = Field(None)
    geo: list[GeoHierarchyRow] = Field(default_factory=list)
    groups: list[int] = Field(default_factory=list)
    ordering: Optional[int] = Field(None)
    currency: Optional[str] = Field(None)


class ResponsePriceTypes(RetailCrmResponse):
    priceTypes: list[PriceType] = Field(default_factory=list)


class IntegrationModule(BaseModel):
    active: bool = Field(False)
    name: str = Field("")
    logo: str = Field("")


class PaymentType(BaseModel):
    name: str = Field("")
    code: str = Field("")
    active: bool = Field(False)
    defaultForCrm: bool = Field(False)
    defaultForApi: bool = Field(False)
    description: str = Field("")
    deliveryTypes: list[str] = Field(default_factory=list)
    paymentStatuses: list[str] = Field(default_factory=list)
    integrationModule: Optional[IntegrationModule] = Field(None)
    sites: list[Site] = Field(default_factory=list)


class SerializedPaymentType(BaseModel):
    name: Optional[str] = Field(None)
    code: Optional[str] = Field(None)
    sites: list[str] = Field(default_factory=list)
    active: bool = Field(False)
    defaultForCrm: bool = Field(False)
    defaultForApi: bool = Field(False)
    description: str = Field("")
    deliveryTypes: list[str] = Field(default_factory=list)
    paymentStatuses: list[str] = Field(default_factory=list)


class ResponsePaymentTypes(RetailCrmResponse):
    paymentTypes: dict[str, PaymentType] = Field(default_factory=dict)


class PaymentStatus(BaseModel):
    name: str = Field("")
    code: str = Field("")
    active: bool = Field(False)
    defaultForCrm: Optional[bool] = Field(False)
    defaultForApi: Optional[bool] = Field(False)
    paymentComplete: bool = Field(False)
    ordering: int = Field()
    description: str = Field("")
    paymentTypes: list[str] = Field(default_factory=list)


class ResponsePaymentStatuses(RetailCrmResponse):
    paymentStatuses: dict[str, PaymentStatus] = Field(default_factory=dict)


class SerializedPaymentStatus(BaseModel):
    name: Optional[str] = Field(None)
    code: Optional[str] = Field(None)
    ordering: Optional[int] = Field(None)
    active: Optional[bool] = Field(None)
    defaultForCrm: Optional[bool] = Field(None)
    defaultForApi: Optional[bool] = Field(None)
    paymentComplete: Optional[bool] = Field(None)
    description: Optional[str] = Field(None)


class OrderType(BaseModel):
    name: str = Field("")
    code: str = Field("")
    active: bool = Field(False)
    defaultForCrm: Optional[bool] = Field(False)
    defaultForApi: Optional[bool] = Field(False)
    ordering: int = Field()


class ResponseOrderTypes(RetailCrmResponse):
    orderTypes: dict[str, OrderType] = Field(default_factory=dict)


class SerializedOrderType(BaseModel):
    name: Optional[str] = Field(None)
    code: Optional[str] = Field(None)
    active: Optional[bool] = Field(None)
    defaultForCrm: Optional[bool] = Field(None)
    defaultForApi: Optional[bool] = Field(None)
    ordering: Optional[int] = Field(None)


class OrderMethod(BaseModel):
    name: str = Field("")
    code: str = Field("")
    active: bool = Field(False)
    defaultForCrm: Optional[bool] = Field(False)
    defaultForApi: Optional[bool] = Field(False)


class ResponseOrderMethod(RetailCrmResponse):
    orderMethods: dict[str, OrderMethod] = Field(default_factory=dict)


class SerializedOrderMethod(BaseModel):
    name: Optional[str] = Field(None)
    code: Optional[str] = Field(None)
    active: Optional[bool] = Field(None)
    defaultForCrm: Optional[bool] = Field(None)
    defaultForApi: Optional[bool] = Field(None)
