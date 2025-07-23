from datetime import datetime
from typing import List, Optional, Union, Any

from pydantic import BaseModel, Field, field_serializer, field_validator

from retailcrm.v5.enums.loyalty import BonusOperationType, BonusOperationEventType
from retailcrm.v5.helpers import datetime_serializer, list_to_dict_validator
from retailcrm.v5.schemas.base import BaseRetailCrmScheme, RetailCrmResponse
from retailcrm.v5.schemas.shared import (
    SerializedEntityCustomer,
    SerializedLoyaltyOrder,
    LoyaltyAccount,
    Loyalty,
)

__all__ = [
    "ResponseLoyaltyAccounts",
    "ResponseLoyaltyCalculate",
    "ResponseEditLoyaltyAccount",
    "ResponseLoyaltyAccountBonusOperations",
    "ResponseLoyaltyBonusDetails",
    "Loyalty",
    "LoyaltyLevel",
    "LoyaltyAccount",
    "LoyaltyCalculation",
    "LoyaltyEventDiscount",
    "LoyaltyBonusStatisticResponse",
    "LoyaltyApiFilterData",
    "LoyaltyAccountFilterData",
    "LoyaltyAccountBonusApiFilterType",
    "LoyaltyBonusOperationsApiFilterType",
    "LoyaltyAccountBonusOperationsApiFilterType",
    "ResponseLoyaltiesFilter",
    "SerializedCreateLoyaltyAccount",
    "ResponseLoyaltyRetrieve",
    "SerializedEditLoyaltyAccount",
    "ResponseActivateLoyaltyAccount",
    "ResponseCreateLoyaltyAccount",
    "ResponseChargeLoyaltyAccountBonus",
    "ResponseLoyaltyBonusOperations",
    "ResponseCreditLoyaltyAccountBonus",
]


class LoyaltyLevel(BaseModel):
    type: Optional[str] = Field(
        None,
        description="Тип уровня. Возможные значения: bonus_converting, bonus_percent, discount",
    )
    id: Optional[int] = Field(None, description="ID уровня")
    name: str | None = Field(None, description="Название уровня")
    sum: Optional[Union[float, int]] = Field(
        None, description="Сумма, необходимая для перехода на данный уровень"
    )
    privilegeSize: Optional[float] = Field(
        None, description="Размер скидки, процент или курс начисления бонусов"
    )
    privilegeSizePromo: Optional[float] = Field(
        None,
        description="Размер скидки, процент или курс начисления бонусов для акционных товаров",
    )


class SerializedLoyalty(BaseRetailCrmScheme):
    currency: Optional[str] = Field(None, description="Валюта")
    name: Optional[str] = Field(None, description="Название программы лояльности")
    chargeRate: Optional[float] = Field(None, description="Курс при списании бонусов")


class SmsVerification(BaseModel):
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    expiredAt: Optional[datetime] = Field(
        None, description="Дата окончания срока жизни"
    )
    verifiedAt: Optional[datetime] = Field(
        None, description="Дата успешной верификации"
    )
    checkId: Optional[str] = Field(None, description="Идентификатор проверки кода")
    actionType: Optional[str] = Field(None, description="Тип действия")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    expiredAt_serializer = field_serializer("expiredAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    verifiedAt_serializer = field_serializer("verifiedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class LoyaltyEventDiscount(BaseModel):
    id: int = Field(None, description="ID")


class OrderProductPriceItem(BaseRetailCrmScheme):
    price: float = Field(
        0,
        description="Итоговая цена c учетом всех скидок на товар и заказ (в валюте объекта)",
    )
    quantity: float = Field(0, description="Количество товара по заданной цене")


class AbstractDiscount(BaseRetailCrmScheme):
    type: str = Field(description="Тип скидки")
    amount: float = Field(0, description="Сумма скидки")


class PriceType(BaseRetailCrmScheme):
    code: str = Field(description="Код типа цены")


class OrderProduct(BaseRetailCrmScheme):
    id: Optional[int] = Field(description="ID позиции в заказе")
    externalIds: List[str] = Field(
        [], description="Внешние идентификаторы позиции в заказе"
    )
    discounts: List[AbstractDiscount] = Field([], description="Массив скидок")
    offer: Optional["Offer"] = Field(None, description="Торговое предложение")

    bonusesChargeTotal: Optional[float] = Field(
        0, description="Количество списанных бонусов"
    )
    bonusesCreditTotal: Optional[float] = Field(
        0, description="Количество начисленных бонусов"
    )
    priceType: Optional[PriceType] = Field(None, description="Тип цены")
    initialPrice: Optional[float] = Field(
        0, description="Цена товара/SKU (в валюте объекта)"
    )
    discountTotal: Optional[float] = Field(
        0,
        description="Итоговая денежная скидка на единицу товара c учетом всех скидок на товар и заказ (в валюте объекта)",
    )
    prices: List[OrderProductPriceItem] = Field(
        [], description="Набор итоговых цен реализации с указанием количества"
    )
    vatRate: Optional[str] = Field(None, description="Ставка НДС")
    quantity: Optional[float] = Field(0, description="Количество")


class Offer(BaseRetailCrmScheme):
    id: Optional[int] = Field(description="ID торгового предложения")
    externalId: Optional[str] = Field(
        "", description="ID торгового предложения в магазине"
    )
    xmlId: Optional[str] = Field(
        "", description="ID торгового предложения в складской системе"
    )


class LoyaltyCalculation(BaseModel):
    privilegeType: Optional[str] = Field(None, description="Тип привилегии")
    discount: Optional[float] = Field(
        None,
        description="Денежная скидка на заказ с учетом списанных бонусов по курсу, заданному в настройках",
    )
    creditBonuses: Optional[float] = Field(None, description="Бонусы к начислению")
    loyaltyEventDiscount: Optional[LoyaltyEventDiscount] = Field(
        None, description="Скидка по событию программы лояльности"
    )
    maxChargeBonuses: Optional[float] = Field(
        None, description="Бонусы, доступные для списания"
    )
    maximum: Optional[bool] = Field(
        None, description="Привилегия с максимальной выгодой"
    )


class ResponseLoyaltyCalculate(RetailCrmResponse):
    order: Optional[SerializedLoyaltyOrder] = Field(None, description="")
    calculations: Optional[List[LoyaltyCalculation]] = None
    loyalty: Optional[SerializedLoyalty] = Field(None, description="")


class LoyaltyAccountFilterData(BaseRetailCrmScheme):
    ids: Optional[List[int]] = Field(
        None, description="Массив ID участий в программе лояльности"
    )
    id: Optional[int] = Field(None, description="ID участия")
    customer: Optional[str] = Field(None, description="Клиент", max_length=255)
    loyalties: Optional[List[int]] = Field(
        None, description="Массив ID Программ лояльности"
    )
    sites: Optional[List[str]] = Field(None, description="Магазины")
    status: Optional[str] = Field(
        None, description="Статус", max_length=255, min_length=1
    )
    phoneNumber: Optional[str] = Field(
        None, description="Номер телефона", max_length=255
    )
    cardNumber: Optional[str] = Field(None, description="Номер карты", max_length=255)
    level: Optional[int] = Field(None, description="Внутренний ID уровня")
    customerId: Optional[int] = Field(
        None, description="Внутренний ID клиента", ge=0, le=100000000000
    )
    customerExternalId: Optional[str] = Field(
        None, description="Внешний ID клиента", max_length=255
    )
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
    customFields: Optional[dict[str, Any]] = Field(None, description="Пользовательские поля")


class ResponseLoyaltyAccounts(RetailCrmResponse):
    loyaltyAccounts: Optional[List[LoyaltyAccount]] = Field(
        None, description="Участие в программе лояльности"
    )


class OperationOrder(BaseModel):
    id: Optional[int] = Field(None, description="ID заказа")
    externalId: Optional[str] = Field(None, description="Внешний ID заказа")


class OperationBonus(BaseModel):
    activationDate: Optional[datetime] = Field(
        None, description="Дата активации бонусов"
    )


class OperationEvent(BaseModel):
    id: Optional[int] = Field(None, description="ID события")
    type: Optional[BonusOperationEventType] = Field(
        None, description="Тип события. Возможные значения: birthday, welcome"
    )


class OperationLoyaltyAccount(BaseModel):
    id: Optional[int] = Field(None, description="ID участия")


class OperationLoyalty(BaseModel):
    id: Optional[int] = Field(None, description="ID программы лояльности")


class Operation(BaseModel):
    type: Optional[BonusOperationType] = Field(None, description="Тип действия")
    createdAt: Optional[datetime] = Field(None, description="Дата действия")
    amount: Optional[float] = Field(None, description="Количество бонусов")
    order: Optional[OperationOrder] = Field(None, description="Связанный заказ")
    bonus: Optional[OperationBonus] = Field(None, description="Начисленные бонусы")
    event: Optional[OperationEvent] = Field(
        None, description="Событие программы лояльности"
    )
    loyaltyAccount: Optional[OperationLoyaltyAccount] = Field(
        None, description="Связанное участие"
    )
    loyalty: Optional[OperationLoyalty] = Field(
        None, description="Связанная программа лояльности"
    )
    comment: Optional[str] = Field(None, description="Комментарий")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class LoyaltyAccountBonusOperationsApiFilterType(BaseRetailCrmScheme):
    createdAtFrom: Optional[str] = Field(None, description="Дата создания (от)")
    createdAtTo: Optional[str] = Field(None, description="Дата создания (до)")


class LoyaltyBonusOperationsApiFilterType(BaseRetailCrmScheme):
    loyalties: Optional[List[int]] = Field(
        None, description="Массив ID Программ лояльности"
    )


class BonusDetail(BaseModel):
    date: Optional[datetime] = Field(
        None, description="Дата сгорания или активации бонусов"
    )
    amount: Optional[float] = Field(None, description="Количество бонусов")

    date_serializer = field_serializer("date")(datetime_serializer("%Y-%m-%d %H:%M:%S"))


class LoyaltyAccountBonusApiFilterType(BaseRetailCrmScheme):
    date: Optional[datetime] = Field(None, description="")


class LoyaltyBonusStatisticResponse(BaseModel):
    totalAmount: Optional[float] = Field(None, description="Общее количество бонусов")


class ResponseLoyaltyBonusDetails(RetailCrmResponse):
    statistic: Optional[LoyaltyBonusStatisticResponse] = Field(
        None, description="Статистика по бонусам"
    )
    bonuses: Optional[List[BonusDetail]] = Field(None, description="")


class LoyaltyApiFilterData(BaseRetailCrmScheme):
    ids: Optional[List[int]] = Field(None, description="Массив ID программ лояльности")
    sites: Optional[List[str]] = Field(None, description="Магазины")
    active: Optional[bool] = Field(None, description="Активна")
    blocked: Optional[bool] = Field(None, description="Заблокирована")


class ResponseLoyaltiesFilter(RetailCrmResponse):
    loyalties: list[Loyalty] = Field(
        default_factory=list, description="Программа лояльности"
    )


class ResponseLoyaltyRetrieve(RetailCrmResponse):
    loyalty: Loyalty | None = Field(None, description="Программа лояльности")


class SerializedCreateLoyaltyAccount(BaseRetailCrmScheme):
    phoneNumber: Optional[str] = Field(None, description="Номер телефона")
    cardNumber: Optional[str] = Field(None, description="Номер карты")
    customFields: Optional[dict] = Field(
        None, description="Ассоциативный массив пользовательских полей"
    )
    customer: Optional[SerializedEntityCustomer] = Field(None, description="Клиент")


class SerializedEditLoyaltyAccount(BaseRetailCrmScheme):
    phoneNumber: Optional[str] = Field(None, description="Номер телефона")
    cardNumber: Optional[str] = Field(None, description="Номер карты")
    customFields: Optional[dict] = Field(
        None, description="Ассоциативный массив пользовательских полей"
    )
    loyaltyLevelId: Optional[int] = Field(
        None, description="Идентификатор уровня программы лояльности"
    )


class ResponseCreateLoyaltyAccount(RetailCrmResponse):
    loyaltyAccount: Optional[LoyaltyAccount] = Field(
        None, description="Участие в программе лояльности"
    )
    warnings: dict[str, str] = Field(default_factory=dict)

    warnings_validator = field_validator("warnings", mode="before")(list_to_dict_validator())


class ResponseActivateLoyaltyAccount(RetailCrmResponse):
    loyaltyAccount: Optional[LoyaltyAccount] = Field(
        None, description="Участие в программе лояльности"
    )
    verification: Optional[SmsVerification] = Field(None, description="SMS-верификация")


class ResponseChargeLoyaltyAccountBonus(RetailCrmResponse):
    pass


class ResponseCreditLoyaltyAccountBonus(RetailCrmResponse):
    loyaltyBonus: Optional[dict] = Field(None)


class ResponseLoyaltyAccountBonusOperations(RetailCrmResponse):
    bonusOperations: Optional[List[Operation]] = Field(
        None, description="Запись в истории бонусного счета"
    )


class ResponseLoyaltyBonusOperations(RetailCrmResponse):
    bonusOperations: Optional[List[Operation]] = Field(
        None, description="Запись в истории бонусного счета"
    )


class ResponseEditLoyaltyAccount(RetailCrmResponse):
    loyaltyAccount: Optional[LoyaltyAccount] = Field(
        None, description="Участие в программе лояльности"
    )
