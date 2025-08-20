from datetime import date, datetime, time
from typing import Optional, Union

from pydantic import Field, RootModel, field_serializer, ConfigDict

from retailcrm.v5.enums import DeliveryStatusTypes, PrivilegeType, VatRateTypes
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas import BaseRetailCrmScheme, RetailCrmResponse
from retailcrm.v5.schemas.shared import (
    ApiKey,
    CodeValueModel,
    Contact,
    Customer,
    MGDialog,
    Order,
    OrderProduct,
    OrderProductProperties,
    Payment,
    PriceType,
    SerializedOrderDelivery,
    Source,
    User,
    FixExternalRow,
    SerializedEntityOrder,
    OrderContragent,
    EntityWithExternalIdInput,
    SerializedLoyaltyOrder
)


class DeliveryService(BaseRetailCrmScheme):
    name: str
    code: str = ""
    active: bool = False
    deliveryType: str = ""
















class SerializedOrderList(RootModel):
    root: list[SerializedOrder] = Field(default_factory=list)





class EntityWithExternalId(BaseRetailCrmScheme):
    external_id: Optional[str] = Field(
        None, description="Внешний ID (при наличии)", validation_alias="externalId"
    )


class ResponseOrdersUpload(RetailCrmResponse):
    uploaded_orders: list[FixExternalRow] = Field(
        [],
        description="Идентификаторы загруженных объектов",
        validation_alias="uploadedOrders",
    )
    failed_orders: list[FixExternalRow] = Field(
        [],
        description="Идентификаторы незагруженных объектов",
        validation_alias="failedOrders",
    )
    orders: list[Order] = Field([], description="Список заказов")


class ResponseEditOrder(RetailCrmResponse):
    id: Optional[int] = None
    order: Optional[Order] = None


class ResponseCreateOrderPayment(RetailCrmResponse):
    id: Optional[int] = 0


class ResponseEditOrderPayment(RetailCrmResponse):
    id: Optional[int] = 0


class ResponseDeleteOrderPayment(RetailCrmResponse):
    pass


# TODO: Вырезать
class ResponseGetOrder(RetailCrmResponse):
    order: Optional[Order] = None


class ResponseOrders(RetailCrmResponse):
    orders: list[Order] = Field([], description="Список заказов")


# todo: заполнить
class CreateOrder(BaseRetailCrmScheme):
    model_config = ConfigDict(extra="allow")
    id: int
    externalId: Optional[str] = None


# todo: заполнить
class ResponseCreateOrder(RetailCrmResponse):
    order: Optional[CreateOrder] = None





class OrderRetrieveResponse(RetailCrmResponse):
    order: Order | None = None


class SmsVerification(BaseRetailCrmScheme):
    createdAt: datetime | None = Field(None, description="Дата создания (Y-m-d H:i:s)")
    expiredAt: datetime | None = Field(None, description="Дата окончания срока жизни (Y-m-d H:i:s)")
    verifiedAt: datetime | None = Field(None, description="Дата успешной верификации (Y-m-d H:i:s)")
    checkId: str | None = Field(None, description="Идентификатор проверки кода")
    actionType: str | None = Field(None, description="Тип действия")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    expiredAt_serializer = field_serializer("expiredAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    verifiedAt_serializer = field_serializer("verifiedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class LoyaltyApplyResponse(RetailCrmResponse):
    order: SerializedLoyaltyOrder | None = Field(None)
    verification: SmsVerification | None = Field(None, description="SMS-верификация")


class LoyaltyCancelBonusOperationsResponse(RetailCrmResponse):
    order: Order | None = Field(None, description="Заказ")
