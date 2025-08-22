from datetime import datetime
from typing import List, Optional

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class LoyaltyAccountFilterData(BaseRetailCrmScheme):
    ids: Optional[List[int]] = Field(
        None, description="Массив ID участий в программе лояльности"
    )
    id: Optional[int] = Field(None, description="ID участия")
    customer: Optional[str] = Field(None, description="Клиент")
    loyalties: Optional[List[int]] = Field(
        None, description="Массив ID Программ лояльности"
    )
    sites: Optional[List[str]] = Field(
        None, description="Магазины программы лояльности"
    )
    status: Optional[str] = Field(None, description="Статус")
    phoneNumber: Optional[str] = Field(None, description="Номер телефона")
    cardNumber: Optional[str] = Field(None, description="Номер карты")
    level: Optional[int] = Field(None, description="Внутренний ID уровня")
    customerId: Optional[int] = Field(None, description="Внутренний ID клиента")
    customerExternalId: Optional[str] = Field(None, description="Внешний ID клиента")
    customerSites: Optional[List[str]] = Field(None, description="Магазины клиента")
    createdAtFrom: Optional[datetime] = Field(None, description="Дата регистрации (от)")
    createdAtTo: Optional[datetime] = Field(None, description="Дата регистрации (до)")
    burnDateFrom: Optional[datetime] = Field(
        None, description="Дата сгорания бонусов (от)"
    )
    burnDateTo: Optional[datetime] = Field(
        None, description="Дата сгорания бонусов (до)"
    )
    minOrdersSum: Optional[int] = Field(None, description="Сумма покупок (от)")
    maxOrdersSum: Optional[int] = Field(None, description="Сумма покупок (до)")
    minAmount: Optional[int] = Field(None, description="Баланс бонусов (от)")
    maxAmount: Optional[int] = Field(None, description="Баланс бонусов (до)")
    customFields: Optional[dict] = Field(None, description="Пользовательские поля")

    createdAtFrom_serializer = field_serializer("createdAtFrom")(
        datetime_serializer("%Y-%m-%d")
    )
    createdAtTo_serializer = field_serializer("createdAtTo")(
        datetime_serializer("%Y-%m-%d")
    )
    burnDateFrom_serializer = field_serializer("burnDateFrom")(
        datetime_serializer("%Y-%m-%d")
    )
    burnDateTo_serializer = field_serializer("burnDateTo")(
        datetime_serializer("%Y-%m-%d")
    )


class LoyaltyAccountBonusOperationsApiFilterType(BaseRetailCrmScheme):
    createdAtFrom: Optional[str] = Field(None, description="Дата создания (от)")
    createdAtTo: Optional[str] = Field(None, description="Дата создания (до)")


class LoyaltyAccountBonusApiFilterType(BaseRetailCrmScheme):
    date: Optional[datetime] = Field(None, description="Дата")

    date_serializer = field_serializer("date")(datetime_serializer("%Y-%m-%d"))


class LoyaltyBonusOperationsApiFilterType(BaseRetailCrmScheme):
    loyalties: Optional[List[int]] = Field(
        None, description="Массив ID Программ лояльности"
    )


class LoyaltyApiFilterData(BaseRetailCrmScheme):
    ids: Optional[List[int]] = Field(None, description="Массив ID программ лояльности")
    sites: Optional[List[str]] = Field(None, description="Магазины")
    active: Optional[bool] = Field(None, description="Активна")
    blocked: Optional[bool] = Field(None, description="Заблокирована")
