from datetime import datetime
from typing import Optional, Union

from pydantic import Field, field_serializer, RootModel

from retailcrm.v5.enums import ProductTypes
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas import Offer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme, RetailCrmResponse


class Inventory(BaseRetailCrmScheme):
    quantity: float = Field(description="Количество")
    purchasePrice: Optional[float] = Field(None, description="Закупочная цена")
    store: str = Field(description="Склад")


class SerializedStore(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код")
    available: Optional[float] = Field(
        None, description="Количество доступного товара или факт наличия"
    )
    purchasePrice: Optional[float] = Field(None, description="Закупочная цена")


class SerializedOffer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID торгового предложения")
    externalId: Optional[str] = Field(
        None, description="ID торгового предложения в магазине"
    )
    xmlId: Optional[str] = Field(
        None, description="ID торгового предложения в складской системе"
    )
    stores: Optional[list[SerializedStore]] = Field(None)


class SerializedOfferList(RootModel):
    root: list[SerializedOffer] = Field(default_factory=list)


class ProductGroup(BaseRetailCrmScheme):
    id: int = Field(description="ID")
    externalId: Optional[str] = Field(None, description="Внешний ID товарной группы")
    parentId: Optional[int] = Field(None, description="ID родительской группы")
    site: Optional[str] = Field(None, description="Магазин")
    lvl: Optional[int] = Field(None, description="Уровень вложенности")
    active: bool = Field(False, description="Активность")


class Product(BaseRetailCrmScheme):
    type: str = Field(description="Тип (товар product или услуга service)")
    minPrice: Optional[float] = Field(
        None, description="deprecated Минимальная цена на товар (в базовой валюте)"
    )
    maxPrice: Optional[float] = Field(
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
    quantity: Optional[float] = Field(None, description="Количество")
    markable: Optional[bool] = Field(None, description="Подлежит маркировке")

    updatedAt_serializer = field_serializer("updatedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class InventoryAlternativeFilterData(BaseRetailCrmScheme):
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


class ResponseInventoriesFilter(RetailCrmResponse):
    offers: list[Offer] = Field(
        default_factory=list, description="Торговое предложение (SKU)"
    )


class ResponseInventoriesUpload(RetailCrmResponse):
    notFoundOffers: list[Offer] = Field(
        default_factory=list, description="Торговое предложение (SKU)"
    )


class OfferFilterData(BaseRetailCrmScheme):
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
        None, description="Начиная с ID торгового предложения", ge=0, le=2147483647
    )
    minPrice: Optional[int] = Field(None, description="Цена торгового предложения (от)")
    maxPrice: Optional[int] = Field(None, description="Цена торгового предложения (до)")
    minQuantity: Optional[int] = Field(
        None, description="Количество торгового предложения (от)"
    )
    maxQuantity: Optional[int] = Field(
        None, description="Количество торгового предложения (до)"
    )


class ResponseOfferFilter(RetailCrmResponse):
    offers: list[Offer] = Field(
        default_factory=list, description="Торговое предложение (SKU)"
    )


class PriceUploadPricesInput(BaseRetailCrmScheme):
    code: str = Field(description="Код типа цены")
    price: float = Field(description="Цена")
    remove: Optional[bool] = Field(None, description="Удалить цену")


class PriceUploadInput(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(
        None, description="ID торгового предложения в магазине"
    )
    xmlId: Optional[str] = Field(
        None, description="ID торгового предложения в складской системе"
    )
    id: Optional[int] = Field(None, description="ID торгового предложения")
    site: Optional[str] = Field(None, description="Код магазина")
    prices: list[PriceUploadPricesInput] = Field(
        description="Цена торгового предложения"
    )


class PriceUploadNotFoundResponse(BaseRetailCrmScheme):
    id: int = Field()
    externalId: Optional[str] = Field(
        None, description="ID не обработанного торгового предложения в магазине"
    )
    xmlId: Optional[str] = Field(
        None,
        description="ID не обработанного торгового предложения в складской системе",
    )


class ResponsePricesUpload(RetailCrmResponse):
    processedOffersCount: Optional[int] = Field(
        None, description="Количество успешно обработанных торговых предложений"
    )
    notFoundOffers: list[PriceUploadNotFoundResponse]


class ProductGroupFilterData(BaseRetailCrmScheme):
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


class ResponseProductGroupFilter(RetailCrmResponse):
    productGroup: list[ProductGroup] = Field(
        default_factory=list, description="Товарная группа"
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


class ResponseProductGroupCreate(RetailCrmResponse):
    id: Optional[int] = Field(
        None, description="Внутренний ID созданной товарной группы"
    )


class ResponseProductGroupEdit(RetailCrmResponse):
    id: Optional[int] = Field(
        None, description="Внутренний ID созданной товарной группы"
    )


class ProductFilterData(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID товаров")
    name: Optional[str] = Field(
        None,
        description="Название/артикул товара либо артикул/штрихкод торгового предложения",
        max_length=255,
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
        None, description="Внешний ID торгового предложения", max_length=255
    )
    offerXmlId: Optional[str] = Field(
        None, description="XmlId торгового предложения", max_length=255
    )
    groupExternalId: Optional[str] = Field(
        None, description="Внешний ID товарной группы", max_length=255
    )
    sinceUpdatedAt: Optional[datetime] = Field(
        None,
        description="Нижнее ограничение по дате изменения товара (исключая границу)",
    )
    sinceId: Optional[int] = Field(
        None, description="Начиная с ID товара", ge=0, le=2147483647
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


class ResponseProductFilter(RetailCrmResponse):
    products: list[Product] = Field(default_factory=list, description="Товар")


class ProductEditGroupInput(BaseRetailCrmScheme):
    externalId: Optional[str] = Field(None, description="Внешний ID товарной группы")
    id: Optional[int] = Field(None, description="ID товарной группы")


class ProductCreateInput(BaseRetailCrmScheme):
    type: Optional[Union[str, ProductTypes]] = Field(
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


class ResponseProductBatchCreate(RetailCrmResponse):
    processedProductsCount: Optional[int] = Field(
        None, description="Количество успешно обработанных товаров"
    )
    addedProducts: list[int] = Field(
        default_factory=list, description="Список id добавленных товаров"
    )


class ProductEditInput(BaseRetailCrmScheme):
    catalogId: Optional[int] = Field(None, description="ID каталога")
    id: Optional[int] = Field(None, description="ID товара")
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
    site: Optional[str] = Field(
        None, description="Код магазина, необходим при передаче externalId товара"
    )


class ProductEditNotFoundResponse(BaseRetailCrmScheme):
    id: str = Field(None, description="ID необработанного товара")
    externalId: str = Field(None, description="Внешний ID необработанного товара")


class ResponseProductBatchEdit(RetailCrmResponse):
    processedProductsCount: Optional[int] = Field(
        description="Количество успешно обработанных товаров"
    )
    notFoundProducts: list[ProductEditNotFoundResponse] = Field(
        default_factory=list, description="Список id добавленных товаров"
    )


class ProductPropertiesFilterData(BaseRetailCrmScheme):
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


class ProductPropertyGroup(BaseRetailCrmScheme):
    id: int = Field(description="ID группы")
    name: str = Field(description="Наименование группы")


class ProductProperty(BaseRetailCrmScheme):
    sites: Optional[list[str]] = Field(
        None, description="Символьные коды сайтов к которым привязан каталог"
    )
    groups: Optional[list[ProductPropertyGroup]] = Field(
        None, description="Группы, содержащие товары с данным свойством"
    )
    code: str = Field(description="Символьный код свойства")
    name: str = Field(description="Наименование свойства")
    isNumeric: Optional[bool] = Field(None, description="Числовое свойство")
    visible: Optional[bool] = Field(None, description="Видимость свойства")
    variative: Optional[bool] = Field(None, description="Вариативность свойства")


class ResponseProductPropertiesFilter(RetailCrmResponse):
    properties: list[ProductProperty] = Field(
        default_factory=list, description="Свойство товара"
    )


class ProductPropertyValuesFilterData(BaseRetailCrmScheme):
    propertyName: Optional[str] = Field(None, description="Название свойства")
    propertyCode: Optional[str] = Field(None, description="Код свойства")
    groups: Optional[list[int]] = Field(
        None, description="Массив ID групп товаров или услуг"
    )


class ProductPropertyResponse(BaseRetailCrmScheme):
    code: str = Field(description="Символьный код свойства")
    name: str = Field(description="Название свойства")


class ProductPropertyValueResponse(BaseRetailCrmScheme):
    property: ProductPropertyResponse = Field(description="")
    value: str = Field(description="Значение свойства")
    offersCount: Optional[int] = Field(
        None, description="Количество использований в торговых предложениях"
    )


class ResponseProductPropertyValuesFilter(RetailCrmResponse):
    productPropertyValues: list[ProductPropertyValueResponse] = Field(
        default_factory=list
    )


# TODO: Добавить схемы для интеграций
