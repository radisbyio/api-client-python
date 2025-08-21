import decimal
from datetime import datetime
from typing import Optional

from pydantic import field_serializer, Field, model_serializer

from retailcrm.v5.helpers import datetime_serializer, to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.loyalty import SerializedCreateLoyaltyAccount, SerializedEditLoyaltyAccount
from retailcrm.v5.schemas.entities.orders import SerializedOrder
from retailcrm.v5.schemas.filters.loyalty import LoyaltyAccountFilterData, LoyaltyAccountBonusOperationsApiFilterType, \
    LoyaltyAccountBonusApiFilterType, LoyaltyApiFilterData, LoyaltyBonusOperationsApiFilterType
from retailcrm.v5.utils import pydantic_to_nested_dict


class LoyaltyAccountsFilterRequest(BaseRetailCrmScheme):
    limit: int = Field(description="Количество элементов в ответе")
    page: int = Field(description="Номер страницы с результатами")
    filter_obj: Optional[LoyaltyAccountFilterData] = None

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }


class LoyaltyAccountCreateRequest(BaseRetailCrmScheme):
    site: Optional[str] = Field(None, description="Символьный код магазина")
    loyaltyAccount: SerializedCreateLoyaltyAccount = Field(None)

    loyaltyAccount_serializer = field_serializer("loyaltyAccount")(to_json_serializer())


class LoyaltyAccountEditRequest(BaseRetailCrmScheme):
    loyaltyAccount: SerializedEditLoyaltyAccount = Field(None)

    loyaltyAccount_serializer = field_serializer("loyaltyAccount")(to_json_serializer())


class LoyaltyAccountBonusChargeRequest(BaseRetailCrmScheme):
    amount: decimal.Decimal = Field(None, description="Количество бонусов к списанию")
    comment: str = Field(None, description="Комментарий")


class LoyaltyAccountBonusCreditRequest(BaseRetailCrmScheme):
    amount: decimal.Decimal = Field(None, description="Количество бонусов к начислению")
    activationDate: Optional[datetime] = Field(None, alias="activationDate", description="Дата активации бонусов")
    expireDate: Optional[datetime] = Field(None, alias="expireDate", description="Дата сгорания бонусов")
    comment: Optional[str] = Field(None, description="Комментарий")

    activationDate_serializer = field_serializer("activationDate")(datetime_serializer("%Y-%m-%d"))
    expireDate_serializer = field_serializer("expireDate")(datetime_serializer("%Y-%m-%d"))


class LoyaltyAccountBonusOperationsRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(20, description="Количество элементов в ответе")
    page: Optional[int] = Field(1, description="Номер страницы с результатами")
    filter_obj: Optional[LoyaltyAccountBonusOperationsApiFilterType] = Field(None)

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }


class LoyaltyBonusDetailsRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(20, description="Количество элементов в ответе")
    page: Optional[int] = Field(1, description="Номер страницы с результатами")
    filter_obj: Optional[LoyaltyAccountBonusApiFilterType] = Field(None)

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }


class LoyaltyBonusOperationsAllRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(20, description="Количество элементов в ответе")
    cursor: Optional[str] = Field(None, description="Курсор элемента с которого начинается поиск")
    filter_obj: Optional[LoyaltyBonusOperationsApiFilterType] = Field(None)

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "cursor": self.cursor,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }


class LoyaltyCalculateRequest(BaseRetailCrmScheme):
    site: str = Field(None, description="Символьный код магазина")
    order: SerializedOrder = Field(None, description="Заказ")
    bonuses: decimal.Decimal = Field(0, description="Количество бонусов для списания")

    order_serializer = field_serializer("order")(to_json_serializer())


class LoyaltiesFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(20, description="Количество элементов в ответе")
    page: Optional[int] = Field(1, description="Номер страницы с результатами")
    filter_obj: Optional[LoyaltyApiFilterData] = Field(None)

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }
