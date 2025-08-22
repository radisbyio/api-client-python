from datetime import datetime
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.orders import Offer


class SerializedRelationAbstractCustomerWithGa(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    browserId: Optional[str] = Field(
        None, description="Идентификатор устройства в Collector"
    )
    gaClientId: Optional[str] = Field(
        None, description="Метка клиента Google Analytics"
    )
    site: Optional[str] = Field(
        None, description="Код магазина, необходим при передаче externalId"
    )


class SerializedRelationOrder(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="Внутренний ID заказа")
    externalId: Optional[str] = Field(None, description="Внешний ID заказа")
    number: Optional[str] = Field(None, description="Номер заказа")


class SerializedRelationOffer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID торгового предложения")
    externalId: Optional[str] = Field(
        None, description="Внешний ID торгового предложения"
    )
    xmlId: Optional[str] = Field(
        None, description="ID торгового предложения в складской системе"
    )


class SerializedCartItem(BaseRetailCrmScheme):
    quantity: Optional[float] = Field(None, description="Количество")
    price: Optional[float] = Field(None, description="Цена (в валюте объекта)")
    offer: Optional[SerializedRelationOffer] = Field(
        None, description="Торговое предложение"
    )


class SerializedCart(BaseRetailCrmScheme):
    clearedAt: Optional[datetime] = Field(
        None, description="Дата/время очистки корзины"
    )
    customer: Optional[SerializedRelationAbstractCustomerWithGa] = Field(None)
    order: Optional[SerializedRelationOrder] = Field(
        None, description="Заказ, созданный из корзины"
    )
    externalId: Optional[str] = Field(None, description="Внешний ID корзины")
    droppedAt: Optional[datetime] = Field(
        None, description="Дата/время, когда корзина стала брошенной"
    )
    link: Optional[str] = Field(None, description="Ссылка")
    items: list[SerializedCartItem] = Field(
        default_factory=list, description="Товары в корзине"
    )


class CartItem(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID элемента корзины")
    offer: Optional[Offer] = Field(None, description="Торговое предложение")
    quantity: Optional[float] = Field(None, description="Количество")
    price: Optional[float] = Field(None, description="Цена (в валюте объекта)")


class Cart(BaseRetailCrmScheme):
    currency: Optional[str] = Field(None, description="Валюта")
    externalId: Optional[str] = Field(None, description="Внешний ID корзины")
    droppedAt: Optional[datetime] = Field(
        None, description="Дата/время, когда корзина стала брошенной"
    )
    clearedAt: Optional[datetime] = Field(
        None, description="Дата/время очистки корзины"
    )
    link: Optional[str] = Field(None, description="Ссылка на корзину")
    items: list[CartItem] = Field(default_factory=list, description="Товары в корзине")


class CustomerOffer(BaseRetailCrmScheme):
    offer: Optional[Offer] = Field(None, description="Торговое предложение (SKU)")
    createdAt: Optional[datetime] = Field(
        None, description="Дата добавления в список избранного"
    )


class SerializedFavorite(BaseRetailCrmScheme):
    offer: Optional[SerializedRelationOffer] = Field(
        None, description="Торговое предложение"
    )
