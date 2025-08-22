import decimal
from typing import Literal, Optional

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class IntegrationModule(BaseRetailCrmScheme):
    active: Optional[bool] = Field(None, description="Статус активности")
    freeze: Optional[bool] = Field(None, description="Работа модуля заморожена")


class IntegrationModuleBillingInfoCurrency(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="	Название валюты")
    shortName: Optional[str] = Field(
        None, description="Название валюты в сокращённом виде"
    )
    code: Optional[str] = Field(None, description="	Код валюты")


class IntegrationModuleBillingInfo(BaseRetailCrmScheme):
    price: Optional[decimal.Decimal] = Field(None, description="Стоимость модуля")
    priceWithDiscount: Optional[decimal.Decimal] = Field(
        None, description="Стоимость модуля со скидкой при её наличии"
    )
    currency: Optional[str] = Field(None, description="Код валюты")
    billingType: Optional[Literal["fixed", "byChannel"] | str] = Field(
        None, description="Тип оплаты (fixed - за модуль, byChannel - за канал)"
    )


class Register(BaseRetailCrmScheme):
    token: Optional[str] = Field(
        None,
        description="API-ключ в виде хэш-кода, сгенерированного на основе секретного токена с помощью алгоритма sha256 методом hmac для проверки подлинности запроса",
    )
    systemUrl: Optional[str] = Field(
        None,
        description="Технический домен системы, на который необходимо отправлять запросы",
    )
    apiKey: Optional[str] = Field(
        None, description="API-ключ для обращения к API системы"
    )
