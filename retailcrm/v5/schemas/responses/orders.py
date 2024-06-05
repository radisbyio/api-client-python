from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from retailcrm.v5.schemas.base import RetailCrmResponse


class CreateOrder(BaseModel):
    id: int
    externalId: Optional[str] = None


class ResponseCreateOrder(RetailCrmResponse):
    order: Optional[CreateOrder] = None


class Order(BaseModel):
    id: Optional[int] = Field(None, description="ID заказа")
    external_id: Optional[str] = Field(None, description="Внешний ID заказа", validation_alias="externalId")
    created_at: Optional[str] = Field(None, description="", validation_alias="createdAt")
    number: Optional[str] = Field(None, description="")
    site: Optional[str] = Field(None, description="Магазин")
    status: Optional[str] = Field(None, description="Статус заказа")
    status_comment: Optional[str] = Field(None, description="", validation_alias="statusComment")
    manager_id: Optional[int] = Field(None, description="Менеджер, прикрепленный к заказу",
                                      validation_alias="managerId")


class CodeValueModel(BaseModel):
    code: Optional[str] = Field(None, description="Код")
    value: Optional[str] = Field(None, description="Значение")


class AbstractDiscount(BaseModel):
    type: Optional[str] = Field(None,
                                description="Тип скидки. Возможные значения:  <br>`manual_order` - Разовая скидка на заказ;  <br>`manual_product` - Дополнительная скидка на товар;  <br>`loyalty_level` - Скидка по уровню программы лояльности;  <br>`loyalty_event` - Скидка по событию программы лояльности;  <br>`personal` - Персональная скидка;  <br>`bonus_charge` - Списание бонусов ПЛ;  <br>`round` - Скидка от округления")
    amount: Optional[float] = Field(None, description="Сумма скидки")


class Offer(BaseModel):
    id: Optional[int] = Field(None, description="ID торгового предложения")
    externalId: Optional[str] = Field(None, description="ID торгового предложения в магазине")
    xmlId: Optional[str] = Field(None, description="ID торгового предложения в складской системе")
    properties: Optional[list[str]] = Field(None, description="Свойства SKU")


class User(BaseModel):
    id: int = Field(description="ID пользователя")


class ApiKey(BaseModel):
    current: Optional[bool] = Field(None,
                                    description="Изменение было сделано с помощью ключа, используемого в данный момент")
    id: Optional[int] = Field(None, description="ID API-ключа")


class Payment(BaseModel):
    id: Optional[int] = Field(None, description="Внутренний ID")
    type: Optional[str] = Field(None, description="Тип оплаты")
    external_id: Optional[str] = Field(None, description="Внешний ID платежа", validation_alias="externalId")


class OrderProduct(BaseModel):
    id: Optional[int] = Field(None, description="ID позиции в заказе")
    external_ids: list[CodeValueModel] = Field([], description="Внешние идентификаторы позиции в заказе",
                                               validation_alias="externalIds")
    discounts: list[AbstractDiscount] = Field([], description="Массив скидок")
    offer: Optional[Offer] = Field(None, description="Торговое предложение")
    ordering: Optional[int] = Field(None, description="Порядок")
    properties: list[dict] = Field([], description="Дополнительные свойства позиции в заказе")


class OrderHistory(BaseModel):
    id: Optional[int] = Field(None, alias="id", description="Внутренний идентификатор записи в истории")
    created_at: Optional[datetime] = Field(None, description="Дата внесения изменения", validation_alias="createdAt")
    created: Optional[bool] = Field(None, description="Признак создания сущности")
    deleted: Optional[bool] = Field(None, description="Признак удаления сущности")
    source: Optional[str] = Field(None, description="Источник изменения")
    user: Optional[User] = Field(None, description="Пользователь")
    field: Optional[str] = Field(None, description="Имя изменившегося поля")
    old_value: Optional[str | int | datetime | dict] = Field(None, description="Старое значение свойства", validation_alias="oldValue")
    new_value: Optional[str | int | datetime | dict] = Field(None, description="Новое значение свойства", validation_alias="newValue")
    api_key: Optional[ApiKey] = Field(None, description="Информация о ключе api, использовавшемся для этого изменения",
                                      validation_alias="apiKey")
    order: Optional[Order] = Field(None, description="Заказ")
    item: Optional[OrderProduct] = Field(None, description="Позиция в заказе")
    payment: Optional[Payment] = Field(None, description="Платёж")
    combined_to: Optional[Order] = Field(None,
                                         description="Информация о заказе который получился после объединения с текущим заказом",
                                         validation_alias="combinedTo")
    ancestor: Optional[Order] = Field(None, description="Информация о заказе из которого был создан текущий заказ")


class ResponseGetOrder(RetailCrmResponse):
    order: Optional[Order] = None


class ResponseEditOrder(RetailCrmResponse):
    id: Optional[int] = None
    order: Optional[Order] = None


class ResponseCreateOrderPayment(RetailCrmResponse):
    id: Optional[int] = 0


class ResponseEditOrderPayment(RetailCrmResponse):
    id: Optional[int] = 0


class ResponseOrderHistory(RetailCrmResponse):
    generated_at: Optional[datetime] = Field(None, description="Время формирования ответа",
                                             validation_alias="generatedAt")
    history: list[OrderHistory] = []


class ResponseDeleteOrderPayment(RetailCrmResponse):
    pass


class ResponseOrdersHistory(RetailCrmResponse):
    generated_at: Optional[datetime] = Field(None, )
