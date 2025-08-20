import decimal
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas import BaseRetailCrmScheme
from retailcrm.v5.schemas.callbacks.enums.payments import ContragentType, Sex, PaymentObject, PaymentMethod, Vat

__all__ = ["Item", "Customer", "Create", "Result", "ModuleApiRequest"]

class Item(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Наименование")
    price: Optional[decimal.Decimal] = Field(None, description="Цена")
    quantity: Optional[decimal.Decimal] = Field(None, description="Количество")
    measurementUnit: Optional[str] = Field(None, description="Единица измерения")
    vat: Optional[Vat] = Field(
        None, description="Ставка НДС. Возможные значения: none, vat0, vat10, vat110, vat20, vat120",
    )
    paymentMethod: Optional[PaymentMethod] = Field(
        None, description="Признак способа расчета. Возможные значения: full_prepayment, advance",
    )
    paymentObject: Optional[PaymentObject] = Field(
        None, description="Признак предмета расчета. Возможные значения: commodity, service, payment",
    )
    productCode: Optional[str] = Field(None, description="Код маркировки в шестнадцатеричном представлении")
    markingCode: Optional[str] = Field(None, description="Код маркировки")
    offerId: Optional[int] = Field(None, description="ID торгового предложения")
    offerExternalId: Optional[str] = Field(None, description="Внешний ID торгового предложения")
    offerXmlId: Optional[str] = Field(None, description="ID торгового предложения в складской системе")


class Customer(BaseRetailCrmScheme):
    email: Optional[str] = Field(None, description="Адрес электронной почты")
    phone: Optional[str] = Field(None, description="Номер телефона")
    first_name: Optional[str] = Field(None, alias="firstName", description="Имя")
    last_name: Optional[str] = Field(None, alias="lastName", description="Фамилия")
    patronymic: Optional[str] = Field(None, description="Отчество")
    sex: Optional[Sex] = Field(None, description="Пол, возможные значения: male, female")
    contragentType: Optional[ContragentType] = Field(
        None, description="Тип контрагента: физ. лицо individual, юр. лицо legal-entity, ИП enterpreneur",
    )
    legalName: Optional[str] = Field(None, description="Полное наименование юр.лица или ИП, передается в случае фискализации на стороне модуля для юр. лиц и ИП")
    INN: Optional[str] = Field(None, description="ИНН клиента, передается в случае фискализации на стороне модуля для юр. лиц и ИП")


class Create(BaseRetailCrmScheme):
    shopId: Optional[str] = Field(None, description="ID магазина")
    invoiceUuid: Optional[str] = Field(None, description="Идентификатор инвойса в системе(UUID). Все обращения к API системы совершаются через этот ID.")
    invoiceType: Optional[str] = Field(None, description="Тип инвойса. Возможные значения: link")
    amount: Optional[float] = Field(None, description="Сумма в выбранной валюте")
    currency: Optional[str] = Field(None, description="Код валюты в формате ISO-4217")
    orderNumber: Optional[str] = Field(None, description="Номер заказа")
    orderId: Optional[int] = Field(None, description="Внутренний ID заказа")
    siteUrl: Optional[str] = Field(None, description="URL магазина")
    returnUrl: Optional[str] = Field(None, description="URL, на который вернется пользователь после подтверждения или отмены платежа")
    items: Optional[list[Item]] = Field(None, description="Список товаров")
    customer: Optional[Customer] = Field(None, description="Данные покупателя")


class Result(BaseRetailCrmScheme):
    paymentId: Optional[str] = Field(None, description="Внутренний идентификатор оплаты в модуле")
    invoiceUrl: Optional[str] = Field(None, description="Ссылка на страницу оплаты для покупателя")
    cancellable: Optional[bool] = Field(None, description="Признак возможности отмены платежа")

class ModuleApiRequest(BaseRetailCrmScheme):
    paymentId: Optional[str] = Field(
        None, description="Внутренний идентификатор оплаты в модуле"
    )
    amount: Optional[decimal.Decimal] = Field(
        None, description="Итоговая сумма, которая спишется с клиента"
    )
