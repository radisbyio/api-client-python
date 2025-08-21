import decimal
from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer, field_validator

from retailcrm.v5.helpers import datetime_serializer, dict_validator
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.customers import Customer


class LoyaltyLevel(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID уровня")
    name: str | None = Field(None, description="Название уровня")
    sum: decimal.Decimal | None = Field(None, description="Сумма, необходимая для перехода на данный уровень (в валюте объекта)")
    privilegeSize: int | None = Field(None, description="Размер скидки, процент или курс начисления бонусов для товаров по обычной цене (в валюте объекта)")
    privilegeSizePromo: int | None = Field(None, description="Размер скидки, процент или курс начисления бонусов для акционных товаров (в валюте объекта)")

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
    amount: Optional[float] = Field(None, description="Количество активных бонусов")
    ordersSum: Optional[float] = Field(
        None, description="Сумма покупок (в валюте объекта)"
    )
    nextLevelSum: Optional[float] = Field(
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
