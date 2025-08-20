import decimal
from datetime import datetime
from typing import Optional, Any

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas import BaseRetailCrmScheme
from retailcrm.v5.schemas.shared.code_value_model import CodeValueModel


class Unit(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код")
    name: Optional[str] = Field(None, description="Название")
    sym: Optional[str] = Field(None, description="Краткое обозначение")


class Order(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID заказа")


class Offer(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(None , description="ID торгового предложения в магазине")
    xmlId: Optional[str] = Field(None, description="ID торгового предложения в складской системе")


class OrderProduct(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(None, description="deprecated Внешний ID позиции в заказе")
    id: Optional[int] = Field(None, description="ID позиции в заказе")
    externalIds: Optional[list[CodeValueModel]] = Field(None, description="Внешние идентификаторы позиции в заказе")
    order: Optional[Order] = Field(None, description="Заказ")
    offer: Optional[Offer] = Field(None, description="Торговое предложение")


class OrderProductPack(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID")
    purchasePrice: Optional[decimal.Decimal] = Field(None, description="Закупочная цена (в базовой валюте)")
    quantity: Optional[float] = Field(None, description="Количество товара в упаковке")
    unit: Optional[Unit] = Field(None, description="Единица измерения")
    store: Optional[str] = Field(None, description="Склад")
    item: Optional[OrderProduct] = Field(None, description="Позиция в заказе")
    shipmentDate: Optional[datetime] = Field(None, description="Дата забора пака")
    invoiceNumber: Optional[str] = Field(None, description="Номер счет-фактуры")
    deliveryNoteNumber: Optional[str] = Field(None, description="Номер товарной накладной")

    shipment_date_serializer = field_serializer("shipment_date")(datetime_serializer("%Y-%m-%d %H:%M:%S"))


class SerializedOrderProductPack(BaseRetailCrmScheme):
    purchase_price: Optional[float] = Field(None, alias="purchasePrice", description="Закупочная цена (в базовой валюте)")
    quantity: Optional[float] = Field(None, description="Количество товара в упаковке")
    store: Optional[str] = Field(None, description="Склад")
    shipment_date: Optional[datetime] = Field(None, alias="shipmentDate", description="Дата забора пака")
    invoice_number: Optional[str] = Field(None, alias="invoiceNumber", description="Номер счет-фактуры")
    delivery_note_number: Optional[str] = Field(None, alias="deliveryNoteNumber", description="Номер товарной накладной")
    item_id: Optional[int] = Field(None, alias="itemId", description="ID позиции в заказе")

    shipment_date_serializer = field_serializer("shipment_date")(datetime_serializer("%Y-%m-%d %H:%M:%S"))


class User(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID пользователя")


class Store(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код")


class OrderProductPackHistory(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний идентификатор записи в истории")
    createdAt: Optional[datetime] = Field(None, description="Дата внесения изменения")
    created: Optional[bool] = Field(None, description="Флаг выводится для создания нового пакета товаров")
    deleted: Optional[bool] = Field(None, description="Флаг выводится при удалении пакета товаров")
    field: Optional[str] = Field(None, description="Имя изменившегося поля")
    oldValue: Optional[Any] = Field(None, description="Старое значение")
    newValue: Optional[Any] = Field(None, description="Новое значение")
    pack: Optional[OrderProductPack] = Field(None, description="Пак - упаковка товаров, в рамках одной товарной позиции, с одного склада")
    source: Optional[str] = Field(None, description="Источник изменения")
    user: Optional[User] = Field(None)

    createdAt_serializer = field_serializer("createdAt")(datetime_serializer("%Y-%m-%d %H:%M:%S"))


