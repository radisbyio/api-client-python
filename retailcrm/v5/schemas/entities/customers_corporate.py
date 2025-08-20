import decimal
from datetime import datetime
from typing import Optional, Any

from pydantic import Field, field_serializer, field_validator

from retailcrm.v5.helpers import datetime_serializer, dict_validator
from retailcrm.v5.schemas import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.customers import CustomerAddress
from retailcrm.v5.schemas.shared.customer import SerializedEntityCustomer
from retailcrm.v5.schemas.shared.customer_phone import CustomerPhone
from retailcrm.v5.schemas.shared.source import SerializedSource



class CompanyContragent(BaseRetailCrmScheme):
    contragentType: Optional[str] = Field(None, description="Тип контрагента")
    legalName: Optional[str] = Field(None, description="Полное наименование")
    legalAddress: Optional[str] = Field(None, description="Адрес регистрации")
    INN: Optional[str] = Field(None, description="ИНН")
    OKPO: Optional[str] = Field(None, description="ОКПО")
    KPP: Optional[str] = Field(None, description="КПП")
    OGRN: Optional[str] = Field(None, description="ОГРН")
    OGRNIP: Optional[str] = Field(None, description="ОГРНИП")
    certificateNumber: Optional[str] = Field(None, description="Номер свидетельства")
    certificateDate: Optional[datetime] = Field(None, description="Дата свидетельства")
    BIK: Optional[str] = Field(None, description="БИК")
    bank: Optional[str] = Field(None, description="Банк")
    bankAddress: Optional[str] = Field(None, description="Адрес банка")
    corrAccount: Optional[str] = Field(None, description="Корр. счёт")
    bankAccount: Optional[str] = Field(None, description="Расчётный счёт")

    certificateDate_serializer = field_serializer("certificateDate")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )

class Company(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID компании")
    externalId: Optional[str] = Field(None, description="Внешний ID компании")
    customer: Optional[SerializedEntityCustomer] = Field(None, description="Клиент")
    active: Optional[bool] = Field(None, description="Активность")
    name: Optional[str] = Field(None, description="Наименование")
    brand: Optional[str] = Field(None, description="Бренд")
    site: Optional[str] = Field(None, description="Сайт компании")
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    contragent: Optional[CompanyContragent] = Field(None, description="Реквизиты")
    address: Optional[CustomerAddress] = Field(None, description="Адрес")
    avgMarginSumm: Optional[float] = Field(None, description="Средняя валовая прибыль по заказам клиента (в базовой валюте)")
    marginSumm: Optional[float] = Field(None, description="LTV (в базовой валюте)")
    totalSumm: Optional[float] = Field(None, description="Общая сумма заказов (в базовой валюте)")
    averageSumm: Optional[float] = Field(None, description="Средняя сумма заказа (в базовой валюте)")
    costSumm: Optional[float] = Field(None, description="Сумма расходов (в базовой валюте)")
    ordersCount: Optional[int] = Field(None, description="Количество заказов")
    customFields: Optional[dict[str, Any]] = Field(None, description="Ассоциативный массив пользовательских полей")

    customFields_validator = field_validator("customFields", mode="before")(
        dict_validator()
    )
    createdAt_serializer = field_serializer("createdAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
