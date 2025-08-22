from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class OfferFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID торговых предложений")
    externalIds: Optional[list[str]] = Field(None, description="Массив externalId")
    xmlIds: Optional[list[str]] = Field(None, description="Массив xmlId")
    name: Optional[str] = Field(
        None,
        description="Название/артикул товара либо артикул/штрихкод торгового предложения",
        max_length=255,
    )
    sites: Optional[list[str]] = Field(None, description="Массив кодов магазинов")
    catalogs: Optional[list[int]] = Field(None, description="Массив ID каталогов")
    groups: Optional[list[int]] = Field(
        None, description="Массив ID групп товаров или услуг"
    )
    priceType: Optional[str] = Field(None, description="Тип цены")
    active: Optional[bool] = Field(None, description="Активность")
    properties: Optional[list[str]] = Field(
        None, description="Свойства торговых предложений"
    )
    sinceId: Optional[int] = Field(
        None,
        description="Начиная с ID торгового предложения",
    )
    minPrice: Optional[int] = Field(None, description="Цена торгового предложения (от)")
    maxPrice: Optional[int] = Field(None, description="Цена торгового предложения (до)")
    minQuantity: Optional[int] = Field(
        None, description="Количество торгового предложения (от)"
    )
    maxQuantity: Optional[int] = Field(
        None, description="Количество торгового предложения (до)"
    )


class InventoryAlternativeFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID торговых предложений")
    sites: Optional[list[str]] = Field(None, description="Магазины")
    catalogs: Optional[list[int]] = Field(None, description="Массив ID каталогов")
    productExternalId: Optional[str] = Field(
        None, description="Внешний ID товара", max_length=255
    )
    productArticle: Optional[list[str]] = Field(
        None, description="Массив артикулов товаров"
    )
    productActive: Optional[bool] = Field(
        None, description="Возвращать остатки только по активным товарам"
    )
    offerExternalId: Optional[list[str]] = Field(
        None, description="Массив внешних ID торговых предложений"
    )
    offerXmlId: Optional[list[str]] = Field(
        None, description="Массив XmlId торговых предложений"
    )
    offerArticle: Optional[list[str]] = Field(
        None, description="Массив артикулов торговых предложений"
    )
    offerActive: Optional[bool] = Field(
        None, description="Возвращать остатки только по активным торговым предложениям"
    )
    details: Optional[bool] = Field(
        None, description="Возвращать детализацию остатков по складам"
    )


class ProductGroupFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID групп товаров")
    sites: Optional[list[str]] = Field(None, description="Магазины")
    catalogs: Optional[list[int]] = Field(None, description="Массив ID каталогов")
    active: Optional[bool] = Field(None, description="Активность")
    parentGroupId: Optional[int] = Field(
        None, description="ID родительской группы товаров"
    )
    loadFromYml: Optional[bool] = Field(
        None, description="Каталог загружен из ICML файла"
    )
    minLevel: Optional[int] = Field(None, description="Минимальный уровень вложенности")
    maxLevel: Optional[int] = Field(
        None, description="Максимальный уровень вложенности"
    )


class ProductFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID товаров")
    name: Optional[str] = Field(
        None,
        description="Название/артикул товара либо артикул/штрихкод торгового предложения",
    )
    groups: Optional[list[int]] = Field(None, description="Группа товара")
    sites: Optional[list[str]] = Field(None, description="Магазины")
    catalogs: Optional[list[int]] = Field(None, description="Массив ID каталогов")
    priceType: Optional[str] = Field(None, description="Тип цены")
    manufacturer: Optional[str] = Field(None, description="Производитель")
    externalId: Optional[str] = Field(None, description="Внешний ID")
    xmlId: Optional[str] = Field(None, description="Xml ID")
    url: Optional[str] = Field(None, description="URL")
    classSegment: Optional[str] = Field(None, description="ABC/XYZ-сегмент")
    active: Optional[bool] = Field(None, description="Активность")
    popular: Optional[bool] = Field(None, description="Метка Лидер продаж")
    stock: Optional[bool] = Field(None, description="Метка Лучшая цена")
    novelty: Optional[bool] = Field(None, description="Метка Новинка")
    recommended: Optional[bool] = Field(None, description="Метка Рекомендуем")
    properties: Optional[list[str]] = Field(None, description="Свойства товаров")
    markable: Optional[bool] = Field(None, description="")
    offerIds: Optional[list[int]] = Field(
        None, description="Массив ID торговых предложений"
    )
    offerExternalId: Optional[str] = Field(
        None,
        description="Внешний ID торгового предложения",
    )
    offerXmlId: Optional[str] = Field(
        None,
        description="XmlId торгового предложения",
    )
    groupExternalId: Optional[str] = Field(
        None,
        description="Внешний ID товарной группы",
    )
    sinceUpdatedAt: Optional[datetime] = Field(
        None,
        description="Нижнее ограничение по дате изменения товара (исключая границу)",
    )
    sinceId: Optional[int] = Field(
        None,
        description="Начиная с ID товара",
    )
    minPrice: Optional[int] = Field(None, description="Цена товара (от)")
    maxPrice: Optional[int] = Field(None, description="Цена товара (до)")
    minPurchasePrice: Optional[int] = Field(
        None, description="Закупочная цена товара (от)"
    )
    maxPurchasePrice: Optional[int] = Field(
        None, description="Закупочная цена товара (до)"
    )
    minQuantity: Optional[int] = Field(None, description="Количество товара (от)")
    maxQuantity: Optional[int] = Field(None, description="Количество товара (до)")

    sinceUpdatedAt_serializer = field_serializer("sinceUpdatedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class ProductPropertiesFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID товаров или услуг")
    name: Optional[str] = Field(None, description="Название товара или услуги")
    code: Optional[str] = Field(None, description="Символьный код товара или услуги")
    sites: Optional[list[str]] = Field(None, description="Массив кодов магазинов")
    visible: Optional[bool] = Field(None, description="Видимость свойства")
    variative: Optional[bool] = Field(None, description="Вариативность свойства")
    catalogs: Optional[list[int]] = Field(None, description="Массив ID каталогов")
    groups: Optional[list[int]] = Field(
        None, description="Массив ID групп товаров или услуг"
    )


class ProductPropertyValuesFilter(BaseRetailCrmScheme):
    propertyName: Optional[str] = Field(None, description="Название свойства")
    propertyCode: Optional[str] = Field(None, description="Код свойства")
    groups: Optional[list[int]] = Field(
        None, description="Массив ID групп товаров или услуг"
    )
