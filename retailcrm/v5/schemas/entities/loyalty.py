import decimal
from datetime import datetime
from typing import Any, Optional

from pydantic import Field, field_serializer, field_validator

from retailcrm.v5.helpers import datetime_serializer, dict_validator
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.customers import Customer
from retailcrm.v5.schemas.shared.customer import SerializedEntityCustomer


# TODO: заполнить https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-loyalty-loyalties-id
class LoyaltyLevel(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID уровня")
    name: str | None = Field(None, description="Название уровня")
    sum: decimal.Decimal | None = Field(
        None,
        description="Сумма, необходимая для перехода на данный уровень (в валюте объекта)",
    )
    privilegeSize: int | None = Field(
        None,
        description="Размер скидки, процент или курс начисления бонусов для товаров по обычной цене (в валюте объекта)",
    )
    privilegeSizePromo: int | None = Field(
        None,
        description="Размер скидки, процент или курс начисления бонусов для акционных товаров (в валюте объекта)",
    )


class LoyaltyEventDiscount(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID")


class SmsVerification(BaseRetailCrmScheme):
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


class Loyalty(BaseRetailCrmScheme):
    levels: list[LoyaltyLevel] = Field(
        default_factory=list, description="Уровни программы лояльности"
    )
    active: Optional[bool] = Field(None, description="Активна")
    blocked: Optional[bool] = Field(None, description="Заблокирована")
    currency: Optional[str] = Field(None, description="Валюта")
    id: Optional[int] = Field(None, description="ID программы лояльности")
    name: Optional[str] = Field(None, description="Название программы лояльности")
    confirmSmsCharge: Optional[bool] = Field(
        None, description="Подтверждать списание по СМС"
    )
    confirmSmsRegistration: Optional[bool] = Field(
        None, description="Подтверждать участие по СМС"
    )
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    activatedAt: Optional[datetime] = Field(None, description="Дата запуска")
    deactivatedAt: Optional[datetime] = Field(None, description="Дата остановки")
    blockedAt: Optional[datetime] = Field(None, description="Дата блокировки")

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    activatedAt_serializer = field_serializer("activatedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    deactivatedAt_serializer = field_serializer("deactivatedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    blockedAt_serializer = field_serializer("blockedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class LoyaltyAccount(BaseRetailCrmScheme):
    active: Optional[bool] = Field(None, description="Признак активности участия")
    id: Optional[int] = Field(None, description="ID участия")
    loyalty: Optional[Loyalty] = Field(None, description="Программа лояльности")
    customer: Optional[Customer] = Field(None, description="Клиент")
    phoneNumber: Optional[str] = Field(None, description="Номер телефона")
    cardNumber: Optional[str] = Field(None, description="Номер карты")
    amount: Optional[decimal.Decimal] = Field(
        None, description="Количество активных бонусов"
    )
    ordersSum: Optional[decimal.Decimal] = Field(
        None, description="Сумма покупок (в валюте объекта)"
    )
    nextLevelSum: Optional[decimal.Decimal] = Field(
        None, description="Необходимая сумма покупок для перехода на след уровень"
    )
    level: Optional[LoyaltyLevel] = Field(None, description="Уровень участия")
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    activatedAt: Optional[datetime] = Field(None, description="Дата активации участия")
    confirmedPhoneAt: Optional[datetime] = Field(
        None, description="Дата верификации номера телефона"
    )
    lastCheckId: Optional[str] = Field(None, description="ID последней СМС-верификации")
    status: Optional[str] = Field(
        None,
        description="Статус участия. Возможные значения: not_confirmed, activated, deactivated",
    )
    customFields: Optional[dict] = Field(
        None, description="Ассоциативный массив пользовательских полей"
    )

    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    activatedAt_serializer = field_serializer("activatedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    confirmedPhoneAt_serializer = field_serializer("confirmedPhoneAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
    customFields_validator = field_validator("customFields", mode="before")(
        dict_validator()
    )


class LoyaltyBonus(BaseRetailCrmScheme):
    amount: Optional[decimal.Decimal] = Field(
        None, description="Количество начисленных бонусов"
    )
    activationDate: Optional[datetime] = Field(
        None, description="Дата активации бонусов"
    )
    expireDate: Optional[datetime] = Field(None, description="Дата сгорания бонусов")


class OperationOrder(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID заказа")
    externalId: Optional[str] = Field(None, description="Внешний ID заказа")


class OperationBonus(BaseRetailCrmScheme):
    activationDate: Optional[datetime] = Field(
        None, description="Дата активации бонусов"
    )
    expireDate: Optional[datetime] = Field(None, description="Дата сгорания бонусов")


class OperationEvent(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID события")
    type: Optional[str] = Field(
        None, description="Тип события. Возможные значения: birthday, welcome"
    )


class OperationLoyaltyAccount(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID участия")


class OperationLoyalty(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID программы лояльности")


class Operation(BaseRetailCrmScheme):
    type: Optional[str] = Field(None, description="Тип действия")
    createdAt: Optional[datetime] = Field(None, description="Дата действия")
    amount: Optional[decimal.Decimal] = Field(None, description="Количество бонусов")
    order: Optional[OperationOrder] = Field(None, description="Связанный заказ")
    bonus: Optional[OperationBonus] = Field(None, description="Начисленные бонусы")
    event: Optional[OperationEvent] = Field(
        None, description="Событие программы лояльности"
    )
    comment: Optional[str] = Field(None, description="Комментарий")
    loyaltyAccount: Optional[OperationLoyaltyAccount] = Field(
        None, alias="loyaltyAccount", description="Связанное участие"
    )
    loyalty: Optional[OperationLoyalty] = Field(
        None, description="Связанная программа лояльности"
    )


class LoyaltyCalculation(BaseRetailCrmScheme):
    privilegeType: Optional[str] = Field(None, description="Тип привилегии")
    discount: Optional[decimal.Decimal] = Field(
        None,
        description="Денежная скидка на заказ с учетом списанных бонусов по курсу, заданному в настройках",
    )
    creditBonuses: Optional[decimal.Decimal] = Field(
        None, description="Бонусы к начислению"
    )
    loyaltyEventDiscount: Optional[LoyaltyEventDiscount] = Field(
        None, description="Скидка по событию программы лояльности"
    )
    maxChargeBonuses: Optional[decimal.Decimal] = Field(
        None, description="Бонусы, доступные для списания"
    )
    maximum: Optional[bool] = Field(
        None, description="Привилегия с максимальной выгодой"
    )


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
    customFields: Optional[dict[str, Any]] = Field(
        None, description="Ассоциативный массив пользовательских полей"
    )
    loyaltyLevelId: Optional[int] = Field(
        None, description="Идентификатор уровня программы лояльности"
    )
