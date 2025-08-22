import decimal
from datetime import datetime
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import (
    BaseRetailCrmResponse,
    CursorPaginatedResponse,
    PaginatedResponse,
    SuccessResponse,
)
from retailcrm.v5.schemas.entities.loyalty import (
    Loyalty,
    LoyaltyAccount,
    LoyaltyBonus,
    LoyaltyCalculation,
    Operation,
    SmsVerification,
)
from retailcrm.v5.schemas.entities.orders import SerializedLoyaltyOrder


class LoyaltyAccountCreateResponse(SuccessResponse):
    loyaltyAccount: Optional[LoyaltyAccount] = Field(
        None, description="Участие в программе лояльности"
    )
    warnings: Optional[list[str]] = Field(None)


class LoyaltyAccountGetResponse(SuccessResponse):
    loyaltyAccount: Optional[LoyaltyAccount] = Field(
        None, description="Участие в программе лояльности"
    )


class LoyaltyAccountEditResponse(SuccessResponse):
    loyaltyAccount: Optional[LoyaltyAccount] = Field(
        None, description="Участие в программе лояльности"
    )


class LoyaltyAccountActivateResponse(SuccessResponse):
    loyaltyAccount: Optional[LoyaltyAccount] = Field(
        None, description="Участие в программе лояльности"
    )
    verification: Optional[SmsVerification] = Field(None, description="SMS-верификация")


class LoyaltyAccountBonusChargeResponse(SuccessResponse):
    pass


class LoyaltyAccountBonusCreditResponse(SuccessResponse):
    loyaltyBonus: Optional[LoyaltyBonus] = Field(None)


class LoyaltyAccountBonusOperationsResponse(PaginatedResponse):
    bonusOperations: list[Operation] = Field(
        default_factory=list, description="Запись в истории бонусного счета"
    )


class LoyaltyBonusStatisticResponse(BaseRetailCrmResponse):
    totalAmount: Optional[decimal.Decimal] = Field(
        None, description="Общее количество бонусов"
    )


class BonusDetail(BaseRetailCrmResponse):
    date: Optional[datetime] = Field(
        None, description="Дата сгорания или активации бонусов"
    )
    amount: Optional[decimal.Decimal] = Field(None, description="Количество бонусов")


class LoyaltyBonusDetailsResponse(PaginatedResponse):
    statistic: Optional[LoyaltyBonusStatisticResponse] = Field(
        None, description="Статистика по бонусам"
    )
    bonuses: list[BonusDetail] = Field(default_factory=list)


class LoyaltyBonusOperationsResponse(CursorPaginatedResponse):
    bonusOperations: list[Operation] = Field(
        default_factory=list, description="Запись в истории бонусного счета"
    )


class LoyaltyCalculateResponse(SuccessResponse):
    order: Optional[SerializedLoyaltyOrder] = Field(None)
    calculations: list[LoyaltyCalculation] = Field(default_factory=list)
    loyalty: Optional[Loyalty] = Field(None)


class LoyaltiesFilterResponse(PaginatedResponse):
    loyalties: list[Loyalty] = Field(
        default_factory=list, description="Программа лояльности"
    )


class LoyaltyRetrieveResponse(SuccessResponse):
    loyalty: Optional[Loyalty] = Field(None, description="Программа лояльности")


class LoyaltyAccountsResponse(PaginatedResponse):
    loyaltyAccounts: list[LoyaltyAccount] = Field(
        default_factory=list, description="Участие в программе лояльности"
    )
