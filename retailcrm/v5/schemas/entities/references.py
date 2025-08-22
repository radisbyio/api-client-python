import decimal
from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.shared.source import SerializedSource


# TODO: Заполнить
class SerializedOrderProductStatus(BaseRetailCrmScheme):
    name: Optional[str] = Field(None)
    code: Optional[str] = Field(None)
    type: Optional[str] = Field(None)
    ordering: Optional[int] = Field(None)
    active: Optional[bool] = Field(None)
    cancelStatus: Optional[bool] = Field(None)
    orderStatusByProductStatus: Optional[str] = Field(None)
    orderStatusForProductStatus: Optional[str] = Field(None)


class CostItem(BaseRetailCrmScheme):
    source: Optional[SerializedSource] = Field(
        None, description="Данные по источнику клиента"
    )
    code: str = Field(description="Символьный код статьи расходов")
    name: str = Field(description="Название статьи расходов")
    group: str = Field(description="Символьный код группы расходов")
    ordering: int = Field(description="Порядок")
    active: bool = Field(False, description="Активность")
    appliesToOrders: bool = Field(False, description="Относится к расходам по заказам")
    type: str = Field(description="Тип расхода")
    appliesToUsers: bool = Field(
        False, description="Относится к расходам по пользователям"
    )


class CostGroup(BaseRetailCrmScheme):
    code: str | None = Field(None, description="Символьный код группы расходов")
    name: str | None = Field(None, description="Название группы расходов")
    ordering: int | None = Field(None, description="Порядок")
    active: bool | None = Field(None, description="Активность")
    color: str | None = Field(None, description="Цвет")


class SerializedCostGroup(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код группы расходов")
    name: Optional[str] = Field(None, description="Название группы расходов")
    ordering: Optional[int] = Field(None, description="Порядок")
    active: Optional[bool] = Field(None, description="Активность")
    color: Optional[str] = Field(None, description="Цвет", examples=["#19976e"])


class SerializedCostItem(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код статьи расходов")
    name: Optional[str] = Field(None, description="Название статьи расходов")
    ordering: Optional[int] = Field(None, description="Порядок")
    active: bool = Field(False, description="Активность")
    appliesToOrders: bool = Field(None, description="Относится к расходам по заказам")
    appliesToUsers: bool = Field(
        None, description="Относится к расходам по пользователям"
    )
    group: Optional[str] = Field(None, description="Символьный код группы расходов")
    source: Optional[SerializedSource] = Field(
        None, description="Данные по источнику клиента"
    )
    type: Optional[str] = Field(None, description="Тип расхода")


class CourierPhone(BaseRetailCrmScheme):
    number: str | None = Field(None, description="Номер телефона")


class Courier(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID курьера")
    firstName: Optional[str] = Field(None, description="Имя")
    lastName: Optional[str] = Field(None, description="Фамилия")
    patronymic: Optional[str] = Field(None, description="Отчество")
    active: Optional[bool] = Field(None, description="Признак активности")
    email: Optional[str] = Field(None, description="Электронная почта")
    phone: Optional[CourierPhone] = Field(None, description="Контактный телефон")
    description: Optional[str] = Field(None, description="Примечание")


class SerializedCourier(BaseRetailCrmScheme):
    firstName: Optional[str] = Field(None, description="Имя")
    lastName: Optional[str] = Field(None, description="Фамилия")
    patronymic: Optional[str] = Field(None, description="Отчество")
    active: Optional[bool] = Field(None, description="Признак активности")
    email: Optional[str] = Field(None, description="Электронная почта")
    description: Optional[str] = Field(None, description="Примечание")
    phone: Optional[CourierPhone] = Field(None, description="Контактный телефон")


class Currency(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID")
    code: Optional[str] = Field(None, description="Код валюты")
    isBase: Optional[bool] = Field(None, description="Является базовой валютой")
    isAutoConvert: Optional[bool] = Field(
        None, description="Автоматическая конвертация валюты"
    )
    autoConvertExtraPercent: Optional[int] = Field(
        None, description="Наценка в % при автоматической конвертации"
    )
    manualConvertNominal: Optional[int] = Field(
        None, description="Номинал валюты при ручной конвертации"
    )
    manualConvertValue: Optional[decimal.Decimal] = Field(
        None, description="Курс валюты при ручной конвертации"
    )


class SerializedCurrency(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код валюты")
    autoConvertExtraPercent: Optional[int] = Field(
        None, description="Наценка в % при автоматической конвертации"
    )
    manualConvertNominal: Optional[int] = Field(
        None, description="Номинал валюты при ручной конвертации"
    )
    manualConvertValue: Optional[decimal.Decimal] = Field(
        None, description="Курс валюты при ручной конвертации"
    )
    isAutoConvert: Optional[bool] = Field(
        None, description="Автоматическая конвертация валюты"
    )


class DeliveryService(BaseRetailCrmScheme):
    name: str | None = Field(None, description="Название")
    code: str | None = Field(None, description="Символьный код")
    active: bool | None = Field(None, description="Статус активности")


class SerializedDeliveryService(BaseRetailCrmScheme):
    name: str = Field(None, description="Название")
    code: str = Field(None, description="Символьный код")
    deliveryType: str = Field(None, description="Тип доставки")
    active: bool = Field(None, description="Статус активности")


class DeliveryTypePaymentType(BaseRetailCrmScheme):
    code: str | None = Field(None, description="Символьный код")
    cod: bool | None = Field(None, description="Оплата наложенным платежом")


class DeliveryType(BaseRetailCrmScheme):
    paymentTypes: list[str] | None = Field(
        default_factory=list,
        description="(deprecated) Разрешенные типы оплат. Используйте deliveryPaymentTypes",
    )
    isDynamicCostCalculation: bool | None = Field(
        None, description="Динамический тип расчета стоимости доставки"
    )
    isAutoCostCalculation: bool | None = Field(
        None,
        description="Стоимости доставки расчитывается автоматически службой доставки",
    )
    isAutoNetCostCalculation: bool | None = Field(
        None,
        description="Себестоимости доставки расчитывается автоматически службой доставки",
    )
    isCostDependsOnRegionAndWeightAndSum: bool | None = Field(
        None, description="Стоимость доставки зависит от региона, веса и суммы заказа"
    )
    isCostDependsOnDateTime: bool | None = Field(
        None, description="Стоимость доставки зависит от времени и дня недели"
    )
    currency: str | None = Field(None, description="Валюта")
    name: str | None = Field(None, description="Название")
    code: str | None = Field(None, description="Символьный код")
    active: bool | None = Field(None, description="Статус активности")
    defaultCost: decimal.Decimal | None = Field(
        None, description="Стоимость по умолчанию (в валюте объекта)"
    )
    defaultNetCost: decimal.Decimal | None = Field(
        None, description="Себестоимость по умолчанию (в валюте объекта)"
    )
    description: str | None = Field(None, description="Комментарий")
    deliveryPaymentTypes: list[DeliveryTypePaymentType] | None = Field(
        default_factory=list, description="Разрешенные типы оплат"
    )
    integrationCode: str | None = Field(None, description="Код интеграционного модуля")
    deliveryServices: list[str] | None = Field(
        default_factory=list,
        description="Службы доставок, которые входят в данный тип доставки",
    )
    defaultForCrm: bool | None = Field(
        None,
        description="Устанавливается по умолчанию для заказов, создаваемых в системе",
    )
    vatRate: str | None = Field(None, description="Ставка НДС")
    defaultTariffCode: str | None = Field(None, description="Код тарифа по умолчанию")
    defaultTariffType: str | None = Field(None, description="Тип тарифа по умолчанию")
    defaultTariffName: str | None = Field(
        None, description="Название тарифа по умолчанию"
    )
    sites: list[str] | None = Field(
        default_factory=list,
        description="Магазины, в которых доступен данный тип доставки. Если пустой массив, то доступен во всех",
    )


class SerializedDeliveryType(BaseRetailCrmScheme):
    name: str | None = Field(None, description="Название")
    code: str | None = Field(None, description="Символьный код")
    defaultCost: decimal.Decimal | None = Field(
        None, description="Стоимость по умолчанию (в валюте объекта)"
    )
    defaultNetCost: decimal.Decimal | None = Field(
        None, description="Себестоимость по умолчанию (в валюте объекта)"
    )
    sites: list[str] | None = Field(
        None,
        description="Магазины, в которых доступен данный тип доставки. Если пустой массив, то доступен во всех",
    )
    integrationCode: str | None = Field(None, description="Код интеграционного модуля")
    regionWeightCostConditions: str | None = Field(None)
    vatRate: str | None = Field(None, description="Ставка НДС")
    defaultTariffCode: str | None = Field(None, description="Код тарифа по умолчанию")
    defaultTariffType: str | None = Field(None, description="Тип тарифа по умолчанию")
    defaultTariffName: str | None = Field(
        None, description="Название тарифа по умолчанию"
    )
    paymentTypes: list[str] | None = Field(
        None,
        description="(deprecated) Разрешенные типы оплат. Используйте deliveryPaymentTypes",
    )
    active: bool | None = Field(None, description="Статус активности")
    description: str | None = Field(None, description="Комментарий")
    defaultForCrm: bool | None = Field(
        None,
        description="Устанавливается по умолчанию для заказов, создаваемых в системе",
    )
    deliveryServices: list[str] | None = Field(
        default_factory=list,
        description="Службы доставок, которые входят в данный тип доставки",
    )


class LegalEntity(BaseRetailCrmScheme):
    contragentType: Optional[str] = Field(None, description="Тип юридического лица")
    legalName: Optional[str] = Field(None, description="Полное наименование")
    legalAddress: Optional[str] = Field(None, description="Адрес регистрации")
    inn: Optional[str] = Field(None, description="ИНН")
    okpo: Optional[str] = Field(None, description="ОКПО")
    kpp: Optional[str] = Field(None, description="КПП")
    ogrn: Optional[str] = Field(None, description="ОГРН")
    ogrnip: Optional[str] = Field(None, description="ОГРНИП")
    certificateNumber: Optional[str] = Field(None, description="Номер свидетельства")
    certificateDate: Optional[datetime] = Field(None, description="Дата свидетельства")
    bik: Optional[str] = Field(None, description="БИК")
    bank: Optional[str] = Field(None, description="Банк")
    bankAddress: Optional[str] = Field(None, description="Адрес банка")
    corrAccount: Optional[str] = Field(None, description="Корр. счёт")
    bankAccount: Optional[str] = Field(None, description="Расчётный счёт")
    code: Optional[str] = Field(None, description="Символьный код")
    countryIso: Optional[str] = Field(None, description="Страна")
    vatRate: Optional[str] = Field(None, description="Ставка НДС")


class SerializedLegalEntity(BaseRetailCrmScheme):
    contragentType: Optional[str] = Field(None, description="Тип юридического лица")
    legalName: Optional[str] = Field(None, description="Полное наименование")
    legalAddress: Optional[str] = Field(None, description="Адрес регистрации")
    inn: Optional[str] = Field(None, description="ИНН")
    okpo: Optional[str] = Field(None, description="ОКПО")
    kpp: Optional[str] = Field(None, description="КПП")
    ogrn: Optional[str] = Field(None, description="ОГРН")
    ogrnip: Optional[str] = Field(None, description="ОГРНИП")
    certificateNumber: Optional[str] = Field(None, description="Номер свидетельства")
    certificateDate: Optional[datetime] = Field(None, description="Дата свидетельства")
    bik: Optional[str] = Field(None, description="БИК")
    bank: Optional[str] = Field(None, description="Банк")
    bankAddress: Optional[str] = Field(None, description="Адрес банка")
    corrAccount: Optional[str] = Field(None, description="Корр. счёт")
    bankAccount: Optional[str] = Field(None, description="Расчётный счёт")
    code: Optional[str] = Field(None, description="Символьный код")
    countryIso: Optional[str] = Field(None, description="Страна")
    vatRate: Optional[str] = Field(None, description="Ставка НДС")

    certificateDate_serializer = field_serializer("certificateDate")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )


class OrderMethod(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    active: Optional[bool] = Field(None, description="Статус активности")
    defaultForCrm: Optional[bool] = Field(
        None,
        description="Устанавливается по умолчанию для заказов, создаваемых в системе",
    )
    defaultForApi: Optional[bool] = Field(
        None,
        description="Устанавливается по умолчанию для заказов, создаваемых через API",
    )


class SerializedOrderMethod(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    active: Optional[bool] = Field(None, description="Статус активности")
    defaultForCrm: Optional[bool] = Field(
        None,
        description="Устанавливается по умолчанию для заказов, создаваемых в системе",
    )
    defaultForApi: Optional[bool] = Field(
        None,
        description="Устанавливается по умолчанию для заказов, создаваемых через API",
    )


class OrderType(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    active: Optional[bool] = Field(None, description="Статус активности")
    defaultForCrm: Optional[bool] = Field(
        None,
        description="Устанавливается по умолчанию для заказов, создаваемых в системе",
    )
    defaultForApi: Optional[bool] = Field(
        None,
        description="Устанавливается по умолчанию для заказов, создаваемых через API",
    )
    ordering: Optional[int] = Field(None, description="Порядок")


class SerializedOrderType(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    active: Optional[bool] = Field(None, description="Статус активности")
    defaultForCrm: Optional[bool] = Field(
        None,
        description="Устанавливается по умолчанию для заказов, создаваемых в системе",
    )
    defaultForApi: Optional[bool] = Field(
        None,
        description="Устанавливается по умолчанию для заказов, создаваемых через API",
    )
    ordering: Optional[int] = Field(None, description="Порядок")


class PaymentStatus(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="	Название")
    code: Optional[str] = Field(None, description="	Символьный код")
    active: Optional[bool] = Field(None, description="	Статус активности")
    defaultForCrm: Optional[bool] = Field(
        None,
        description="	Устанавливается по умолчанию для заказов, создаваемых в системе",
    )
    defaultForApi: Optional[bool] = Field(
        None,
        description="	Устанавливается по умолчанию для заказов, создаваемых через API",
    )
    paymentComplete: Optional[bool] = Field(
        None, description="	Признак того, что заказ оплачен"
    )
    ordering: Optional[int] = Field(None, description="	Порядок")
    description: Optional[str] = Field(None, description="	Комментарий")
    paymentTypes: list[str] = Field(
        default_factory=list,
        description="Типы оплаты, где используется данный статус оплаты",
    )


class SerializedPaymentStatus(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="	Название")
    code: Optional[str] = Field(None, description="	Символьный код")
    active: Optional[bool] = Field(None, description="	Статус активности")
    defaultForCrm: Optional[bool] = Field(
        None,
        description="	Устанавливается по умолчанию для заказов, создаваемых в системе",
    )
    defaultForApi: Optional[bool] = Field(
        None,
        description="	Устанавливается по умолчанию для заказов, создаваемых через API",
    )
    paymentComplete: Optional[bool] = Field(
        None, description="	Признак того, что заказ оплачен"
    )
    ordering: Optional[int] = Field(None, description="	Порядок")
    description: Optional[str] = Field(None, description="	Комментарий")


class IntegrationModule(BaseRetailCrmScheme):
    active: Optional[bool] = Field(None, description="Статус активности")
    name: Optional[str] = Field(
        None,
        description="Название (требуется, если модуль не опубликован в маркетплейсе)",
    )
    logo: Optional[str] = Field(
        None,
        description="Ссылка на svg логотип (требуется, если модуль не опубликован в маркетплейсе)",
    )


class PaymentType(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    active: Optional[bool] = Field(None, description="Статус активности")
    default_for_crm: Optional[bool] = Field(
        None,
        alias="defaultForCrm",
        description="Устанавливается по умолчанию для заказов, создаваемых в системе",
    )
    default_for_api: Optional[bool] = Field(
        None,
        alias="defaultForApi",
        description="Устанавливается по умолчанию для заказов, создаваемых через API",
    )
    description: Optional[str] = Field(None, description="Комментарий")
    deliveryTypes: Optional[list[str]] = Field(
        default_factory=list, description="Совместимые типы доставки"
    )
    paymentStatuses: Optional[list[str]] = Field(
        None, description="Массив идентификаторов совместимых статусов оплаты"
    )
    integration_module: Optional[IntegrationModule] = Field(
        None, alias="integrationModule", description="Интеграционный модуль"
    )
    sites: Optional[list[str]] = Field(
        None,
        description="Магазины, в которых доступен данный тип оплаты. Если пустой массив, то доступен во всех",
    )


class SerializedPaymentType(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    sites: Optional[list[str]] = Field(
        None,
        description="Магазины, в которых доступен данный тип оплаты. Если пустой массив, то доступен во всех",
    )
    active: Optional[bool] = Field(None, description="Статус активности")
    default_for_crm: Optional[bool] = Field(
        None,
        alias="defaultForCrm",
        description="Устанавливается по умолчанию для заказов, создаваемых в системе",
    )
    default_for_api: Optional[bool] = Field(
        None,
        alias="defaultForApi",
        description="Устанавливается по умолчанию для заказов, создаваемых через API",
    )
    description: Optional[str] = Field(None, description="Комментарий")
    deliveryTypes: Optional[list[str]] = Field(
        default_factory=list, description="Совместимые типы доставки"
    )
    paymentStatuses: Optional[list[str]] = Field(
        None, description="Массив идентификаторов совместимых статусов оплаты"
    )


class GeoHierarchyRow(BaseRetailCrmScheme):
    country: Optional[str] = Field(None, description="Код страны ISO")
    region_id: Optional[str] = Field(
        None, alias="regionId", description="Идентификатор региона в Geohelper"
    )
    region: Optional[str] = Field(None, description="Наименование региона")
    city_id: Optional[str] = Field(
        None, alias="cityId", description="Идентификатор города в Geohelper"
    )
    city: Optional[str] = Field(None, description="Наименование города")


class PriceType(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID типа цены")
    code: Optional[str] = Field(None, description="Символьный код")
    name: Optional[str] = Field(None, description="Название")
    active: Optional[bool] = Field(None, description="Активность")
    promo: Optional[bool] = Field(None, description="Акционная цена")
    default: Optional[bool] = Field(None, description="Флаг базового типа цен")
    description: Optional[str] = Field(None, description="Описание")
    filter_expression: Optional[str] = Field(
        None, alias="filterExpression", description="Фильтр"
    )
    geo: Optional[list[GeoHierarchyRow]] = Field(
        default_factory=list, description="Региональные ограничения"
    )
    groups: Optional[list[str]] = Field(
        default_factory=list, description="Группы пользователей"
    )
    ordering: Optional[int] = Field(None, description="Порядок")
    currency: Optional[str] = Field(None, description="Валюта")


class SerializedPriceType(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код")
    name: Optional[str] = Field(None, description="Название")
    active: Optional[bool] = Field(None, description="Активность")
    promo: Optional[bool] = Field(None, description="Акционная цена")
    description: Optional[str] = Field(None, description="Описание")
    filter_expression: Optional[str] = Field(
        None, alias="filterExpression", description="Фильтр"
    )
    ordering: Optional[int] = Field(None, description="Порядок")
    geo: Optional[list[GeoHierarchyRow]] = Field(
        None, description="Региональные ограничения"
    )
    groups: Optional[list[str]] = Field(
        None, description="Группы пользователей"
    )  # Предполагается, что это список идентификаторов групп
    currency: Optional[str] = Field(None, description="Валюта")


class OrderProductStatus(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код")
    ordering: Optional[int] = Field(None, description="Порядок")
    active: Optional[bool] = Field(None, description="Статус активности")
    created_at: Optional[datetime] = Field(
        None, alias="createdAt", description="Дата создания"
    )
    order_status_by_product_status: Optional[str] = Field(
        None,
        alias="orderStatusByProductStatus",
        description="Статус заказа, который выставляется, если у всех товаров данный статус товара",
    )
    order_status_for_product_status: Optional[str] = Field(
        None,
        alias="orderStatusForProductStatus",
        description="Статус заказа, при котором статус товаров меняется на данный статус товара",
    )
    cancel_status: Optional[bool] = Field(
        None, alias="cancelStatus", description="Является статусом отмены"
    )
    name: Optional[str] = Field(None, description="Название")


class Site(BaseRetailCrmScheme):
    catalog_id: Optional[str] = Field(
        None, alias="catalogId", description="ID каталога"
    )
    isCatalogMainSite: Optional[bool] = Field(
        None, description="Основной магазин каталога"
    )
    isDemo: Optional[bool] = Field(None, description="Магазин с демо данными")
    id: Optional[int] = Field(None, description="ID")
    name: Optional[str] = Field(None, description="Название")
    url: Optional[str] = Field(None, description="URL магазина")
    code: Optional[str] = Field(None, description="Символьный код магазина")
    description: Optional[str] = Field(None, description="Комментарий")
    phones: Optional[str] = Field(None, description="Телефоны магазина")
    address: Optional[str] = Field(None, description="Адрес магазина")
    zip: Optional[str] = Field(None, description="Почтовый индекс")
    defaultForCrm: Optional[bool] = Field(
        None,
        description="Устанавливается по умолчанию для заказов, создаваемых в системе",
    )
    ymlUrl: Optional[str] = Field(None, description="Адрес расположения YML")
    loadFromYml: Optional[bool] = Field(
        None, description="Загружать ли каталог данного магазина из YML/ICML или нет"
    )
    catalogUpdatedAt: Optional[datetime] = Field(
        None, description="Дата/время последней успешной загрузки YML/ICML"
    )
    catalogLoadingAt: Optional[datetime] = Field(
        None, description="Дата/время последней загрузки YML/ICML"
    )
    ordering: Optional[int] = Field(None, description="Порядок")
    contragent: Optional[LegalEntity] = Field(None, description="Юридическое лицо")
    countryIso: Optional[str] = Field(None, description="ISO код страны")
    currency: Optional[str] = Field(None, description="Валюта")
    senderEmail: Optional[str] = Field(
        None, description="Адрес отправителя для магазина"
    )
    senderName: Optional[str] = Field(None, description="Имя отправителя")
    usedInSimlaweb: Optional[bool] = Field(
        None, description="Связан ли магазин с Simlaweb"
    )


class SerializedSite(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    url: Optional[str] = Field(None, description="URL магазина")
    code: Optional[str] = Field(None, description="Символьный код магазина")
    description: Optional[str] = Field(None, description="Комментарий")
    phones: Optional[str] = Field(None, description="Телефоны магазина")
    address: Optional[str] = Field(None, description="Адрес магазина")
    zip: Optional[str] = Field(None, description="Почтовый индекс")
    yml_url: Optional[str] = Field(
        None, alias="ymlUrl", description="Адрес расположения YML"
    )
    defaultForCrm: Optional[bool] = Field(
        None,
        description="Устанавливается по умолчанию для заказов, создаваемых в системе",
    )
    loadFromYml: Optional[bool] = Field(
        None, description="Загружать ли каталог данного магазина из YML/ICML или нет"
    )
    countryIso: Optional[str] = Field(None, description="ISO код страны")
    contragentCode: Optional[str] = Field(
        None, description="Символьный код контрагента"
    )
    currency: Optional[str] = Field(None, description="Валюта")


class StatusGroup(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    active: Optional[bool] = Field(None, description="Статус активности")
    ordering: Optional[int] = Field(None, description="Порядок")
    process: Optional[bool] = Field(
        None, description="Является или нет процессным состоянием заказа"
    )
    statuses: list[str] = Field(
        default_factory=list,
        description="Статусы заказов, которые входят в данную группу",
    )


class Status(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    active: Optional[bool] = Field(None, description="Статус активности")
    ordering: Optional[int] = Field(None, description="Порядок")
    group: Optional[str] = Field(
        None, description="Группа статусов, к которой относится статус"
    )


class Point(BaseRetailCrmScheme):
    latitude: Optional[float] = Field(None, description="Широта")
    longitude: Optional[float] = Field(None, description="Долгота")


class StoreAddress(BaseRetailCrmScheme):
    index: Optional[str] = Field(None, description="Индекс")
    country_iso: Optional[str] = Field(
        None, alias="countryIso", description="ISO код страны"
    )
    region: Optional[str] = Field(None, description="Регион")
    region_id: Optional[int] = Field(
        None, alias="regionId", description="Идентификатор региона в Geohelper"
    )
    city: Optional[str] = Field(None, description="Город")
    city_id: Optional[int] = Field(
        None, alias="cityId", description="Идентификатор города в Geohelper"
    )
    city_type: Optional[str] = Field(
        None, alias="cityType", description="Тип населенного пункта"
    )
    street: Optional[str] = Field(None, description="Улица")
    street_id: Optional[int] = Field(
        None, alias="streetId", description="Идентификатор улицы в Geohelper"
    )
    street_type: Optional[str] = Field(
        None, alias="streetType", description="Тип улицы"
    )
    building: Optional[str] = Field(None, description="Дом")
    flat: Optional[str] = Field(None, description="Номер квартиры/офиса")
    floor: Optional[int] = Field(None, description="Этаж")
    block: Optional[int] = Field(None, description="Подъезд")
    house: Optional[str] = Field(None, description="Строение")
    housing: Optional[str] = Field(None, description="Корпус")
    metro: Optional[str] = Field(None, description="Метро")
    notes: Optional[str] = Field(None, description="Примечания к адресу")
    text: Optional[str] = Field(None, description="Адрес в текстовом виде")
    coordinates: Optional[Point] = Field(None, description="Координаты точки")


class StorePhone(BaseRetailCrmScheme):
    number: Optional[str] = Field(None, description="Номер телефона")


class StoreWorkTime(BaseRetailCrmScheme):
    start_time: Optional[str] = Field(
        None,
        alias="startTime",
        description="Время начала работы склада (в формате H:i)",
    )
    end_time: Optional[str] = Field(
        None,
        alias="endTime",
        description="Время окончания работы склада (в формате H:i)",
    )
    lunch_start_time: Optional[str] = Field(
        None,
        alias="lunchStartTime",
        description="Время начала перерыва (в формате H:i)",
    )
    lunch_end_time: Optional[str] = Field(
        None,
        alias="lunchEndTime",
        description="Время окончания перерыва (в формате H:i)",
    )


class SerializedStoreWeekOpeningHours(BaseRetailCrmScheme):
    mo: Optional[list[StoreWorkTime]] = Field(
        None, description="Время работы склада в понедельник"
    )
    tu: Optional[list[StoreWorkTime]] = Field(
        None, description="Время работы склада во вторник"
    )
    we: Optional[list[StoreWorkTime]] = Field(
        None, description="Время работы склада в среду"
    )
    th: Optional[list[StoreWorkTime]] = Field(
        None, description="Время работы склада в четверг"
    )
    fr: Optional[list[StoreWorkTime]] = Field(
        None, description="Время работы склада в пятницу"
    )
    sa: Optional[list[StoreWorkTime]] = Field(
        None, description="Время работы склада в субботу"
    )
    su: Optional[list[StoreWorkTime]] = Field(
        None, description="Время работы склада в воскресенье"
    )


class Store(BaseRetailCrmScheme):
    external_id: Optional[str] = Field(
        None, alias="externalId", description="Внешний ID"
    )
    xml_id: Optional[str] = Field(None, alias="xmlId", description="Идентификатор 1С")
    description: Optional[str] = Field(None, description="Описание склада")
    email: Optional[str] = Field(None, description="Email склада")
    type: Optional[str] = Field(None, description="Тип склада")
    inventory_type: Optional[str] = Field(
        None, alias="inventoryType", description="Вид остатков на складе"
    )
    address: Optional[StoreAddress] = Field(None, description="Адрес склада")
    active: Optional[bool] = Field(None, description="Статус активности")
    ordering: Optional[str] = Field(None, description="Порядок")
    phone: Optional[StorePhone] = Field(None, description="Телефон склада")
    contact: Optional[str] = Field(None, description="Контактное лицо на складе")
    code: Optional[str] = Field(None, description="Символьный код")
    work_time: Optional[SerializedStoreWeekOpeningHours] = Field(
        None, alias="workTime", description="Время работы склада"
    )
    name: Optional[str] = Field(None, description="Название")


class SerializedUnit(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код")
    name: Optional[str] = Field(None, description="Название")
    sym: Optional[str] = Field(None, description="Краткое обозначение")
    default: Optional[bool] = Field(
        None,
        description="Устанавливается по умолчанию для товаров, создаваемых в системе",
    )
    active: Optional[bool] = Field(None, description="Статус активности")
