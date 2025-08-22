import decimal
from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.enums import ProductTypes
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class PriceUploadPricesInput(BaseRetailCrmScheme):
    code: Optional[str] = Field(description="Код типа цены")
    price: Optional[decimal.Decimal] = Field(description="Цена")
    remove: Optional[bool] = Field(None, description="Удалить цену")


class PriceUploadInput(BaseRetailCrmScheme):
    id: Optional[int] = None
    externalId: Optional[str] = None
    xmxlId: Optional[str] = None
    site: Optional[str] = None
    prices: Optional[list[PriceUploadPricesInput]] = None


class Inventory(BaseRetailCrmScheme):
    quantity: decimal.Decimal | None = Field(None, description="Количество")
    purchasePrice: decimal.Decimal | None = Field(None, description="Закупочная цена")
    store: str | None = Field(description="Склад")


class Offer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID торгового предложения")
    externalId: Optional[str] = Field(
        None, description="ID торгового предложения в магазине"
    )
    xmlId: Optional[str] = Field(
        None, description="ID торгового предложения в складской системе"
    )
    site: Optional[str] = Field(
        None, description="	deprecated Магазин. Используйте getCatalog()"
    )
    purchasePrice: decimal.Decimal | None = Field(
        None, description="Закупочная цена SKU (в базовой валюте)"
    )
    quantity: decimal.Decimal | None = Field(None, description="Доступное количество")
    stores: list[Inventory] = Field(
        default_factory=list, description="	Остатки по складам"
    )


class SerializedStore(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код")
    available: Optional[decimal.Decimal] = Field(
        None, description="Количество доступного товара или факт наличия"
    )
    purchasePrice: Optional[decimal.Decimal] = Field(
        None, description="Закупочная цена"
    )


class SerializedOffer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID торгового предложения")
    externalId: Optional[str] = Field(
        None, description="ID торгового предложения в магазине"
    )
    xmlId: Optional[str] = Field(
        None, description="ID торгового предложения в складской системе"
    )
    stores: Optional[list[SerializedStore]] = Field(None)


class ProductGroup(BaseRetailCrmScheme):
    id: int | None = Field(None, description="ID")
    externalId: Optional[str] = Field(None, description="Внешний ID товарной группы")
    parentId: Optional[int] = Field(None, description="ID родительской группы")
    site: Optional[str] = Field(None, description="Магазин")
    lvl: Optional[int] = Field(None, description="Уровень вложенности")
    active: bool = Field(False, description="Активность")


class Product(BaseRetailCrmScheme):
    type: str = Field(description="Тип (товар product или услуга service)")
    minPrice: Optional[decimal.Decimal] = Field(
        None, description="deprecated Минимальная цена на товар (в базовой валюте)"
    )
    maxPrice: Optional[decimal.Decimal] = Field(
        None, description="deprecated Максимальная цена на товар (в базовой валюте)"
    )
    catalogId: Optional[int] = Field(None, description="ID каталога")
    id: int = Field(description="ID товара")
    article: Optional[str] = Field(None, description="Артикул")
    name: str = Field(description="Название")
    url: Optional[str] = Field(None, description="Ссылка на страницу товара в магазине")
    imageUrl: Optional[str] = Field(None, description="Ссылка на изображение товара")
    description: Optional[str] = Field(None, description="Описание")
    popular: Optional[bool] = Field(None, description="Метка Лидер продаж")
    stock: Optional[bool] = Field(None, description="Метка Лучшая цена")
    novelty: Optional[bool] = Field(None, description="Метка Новинка")
    recommended: Optional[bool] = Field(None, description="Метка Рекомендуем")
    options: Optional[list[dict]] = Field(None, description="Массив опций товара")
    groups: Optional[list[ProductGroup]] = Field(
        None, description="Товарные группы, которым принадлежит товар"
    )
    externalId: Optional[str] = Field(None, description="Внешний ID товара")
    manufacturer: Optional[str] = Field(None, description="Производитель")
    offers: Optional[list[Offer]] = Field(None, description="Торговые предложения")
    updatedAt: Optional[datetime] = Field(
        None, description="Дата редактирования товара в системе"
    )
    active: Optional[bool] = Field(None, description="Активность")
    quantity: Optional[decimal.Decimal] = Field(None, description="Количество")
    markable: Optional[bool] = Field(None, description="Подлежит маркировке")

    updatedAt_serializer = field_serializer("updatedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class ProductEditNotFoundResponse(BaseRetailCrmScheme):
    id: str | None = Field(None, description="ID необработанного товара")
    externalId: str | None = Field(
        None, description="Внешний ID необработанного товара"
    )


class SerializedProductGroup(BaseRetailCrmScheme):
    parentId: Optional[int] = Field(None, description="ID родительской группы")
    name: Optional[str] = Field(None, description="Название")
    description: Optional[str] = Field(None, description="Описание")
    externalId: Optional[str] = Field(None, description="Внешний ID товарной группы")
    active: Optional[bool] = Field(None, description="Активность")
    parentExternalId: Optional[str] = Field(
        None, description="Внешний ID родительской товарной группы"
    )
    site: Optional[str] = Field(None, description="Код магазина")


class ProductEditGroupInput(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(None, description="Внешний ID товарной группы")
    id: Optional[int] = Field(None, description="ID товарной группы")


class ProductPropertyGroup(BaseRetailCrmScheme):
    id: int | None = Field(None, description="ID группы")
    name: str | None = Field(None, description="Наименование группы")


class ProductProperty(BaseRetailCrmScheme):
    sites: Optional[list[str]] = Field(
        None, description="Символьные коды сайтов к которым привязан каталог"
    )
    groups: Optional[list[ProductPropertyGroup]] = Field(
        None, description="Группы, содержащие товары с данным свойством"
    )
    code: str | None = Field(description="Символьный код свойства")
    name: str | None = Field(description="Наименование свойства")
    isNumeric: Optional[bool] = Field(None, description="Числовое свойство")
    visible: Optional[bool] = Field(None, description="Видимость свойства")
    variative: Optional[bool] = Field(None, description="Вариативность свойства")


class ProductPropertyResponse(BaseRetailCrmScheme):
    code: str | None = Field(description="Символьный код свойства")
    name: str | None = Field(description="Название свойства")


class ProductPropertyValueResponse(BaseRetailCrmScheme):
    property: ProductPropertyResponse | None = Field(None)
    value: str | None = Field(None, description="Значение свойства")
    offersCount: Optional[int] = Field(
        None, description="Количество использований в торговых предложениях"
    )


class PriceUploadNotFoundResponse(BaseRetailCrmScheme):
    id: int | None = Field(None)
    externalId: Optional[str] = Field(
        None, description="ID не обработанного торгового предложения в магазине"
    )
    xmlId: Optional[str] = Field(
        None,
        description="ID не обработанного торгового предложения в складской системе",
    )


class ProductCreateInput(BaseRetailCrmScheme):
    type: Optional[str | ProductTypes] = Field(
        None, description="Тип (товар product или услуга service)"
    )
    catalogId: Optional[int] = Field(None, description="ID каталога")
    article: Optional[str] = Field(None, description="Артикул")
    name: Optional[str] = Field(None, description="Название")
    url: Optional[str] = Field(None, description="Ссылка на страницу товара в магазине")
    description: Optional[str] = Field(None, description="Описание")
    popular: Optional[bool] = Field(None, description="Метка Лидер продаж")
    stock: Optional[bool] = Field(None, description="Метка Лучшая цена")
    novelty: Optional[bool] = Field(None, description="Метка Новинка")
    recommended: Optional[bool] = Field(None, description="Метка Рекомендуем")
    groups: Optional[list[ProductEditGroupInput]] = Field(
        None, description="Товарные группы, которым принадлежит товар"
    )
    externalId: Optional[str] = Field(None, description="Внешний ID товара")
    manufacturer: Optional[str] = Field(None, description="Производитель")
    active: Optional[bool] = Field(None, description="Активность")
    markable: Optional[bool] = Field(None, description="Подлежит маркировке")
