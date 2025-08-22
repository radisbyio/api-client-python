from typing import Optional, Any

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class SerializedAdditionalCodes(BaseRetailCrmScheme):
    userId: Optional[int] = Field(None, description="Id пользователя")
    code: Optional[str] = Field(None, description="Добавочный код в телефонии")

class SerializedExternalPhones(BaseRetailCrmScheme):
    siteCode: Optional[str] = Field(None, description="Код магазина")
    externalPhone: Optional[str] = Field(None, description="Внешний номер")

class TelephonyConfiguration(BaseRetailCrmScheme):
    makeCallUrl: Optional[str] = Field(None, description="Адрес инициации звонка")
    allowEdit: Optional[bool] = Field(None, description="Разрешить редактировать из интерфейса системы")
    inputEventSupported: Optional[bool] = Field(None, description="Поддерживает оповещения о входящем звонке")
    outputEventSupported: Optional[bool] = Field(None, description="Поддерживает оповещения о исходящем звонке")
    hangupEventSupported: Optional[bool] = Field(None, description="Поддерживает оповещения о завершении звонке")
    changeUserStatusUrl: Optional[str] = Field(None, description="Уведомлять по этому адресу при смене сатуса менеджера в системе")
    additionalCodes: Optional[list[SerializedAdditionalCodes]] = Field(None, description="Добавочные коды пользователей")
    externalPhones: Optional[list[SerializedExternalPhones]] = Field(None, description="Внешние номера")


class DeliveryStatus(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код статуса доставки")
    name: Optional[str] = Field(None, description="Наименование статуса")
    isEditable: Optional[bool] = Field(None, description='Статус ("isEditable": true) допускает редактирование данных доставки')
    isError: Optional[bool] = Field(None, description='Статус ("isError": true) сигнализирует о наличии проблем в процессе доставки. При попадании в этот статус менеджеру будет отправлено оповещение')
    isPreprocessing: Optional[bool] = Field(None, description='Статус ("isPreprocessing": true) указывает, что доставка находится в процессе оформления и любые изменения с заказом не желательны. Данный флаг может быть необходим для интеграций, где оформление доставки выполняется в асинхронном режиме')

class Plate(BaseRetailCrmScheme):
    type: Optional[str] = Field(None, description="Тип сущности для печатной формы (order - печатная форма для заказа (по умолчанию), shipment - печатная форма для отгрузки)")
    code: Optional[str] = Field(None, description="Код печатной формы")
    label: Optional[str] = Field(None, description="Наименование печатной формы")

class DeliveryDataFieldChoice(BaseRetailCrmScheme):
    value: Optional[str] = Field(None)
    label: Optional[str] = Field(None)

class DeliveryDataField(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код поля")
    label: Optional[str] = Field(None, description="Имя поля")
    hint: Optional[str] = Field(None, description="Пояснение к полю")
    type: Optional[str] = Field(None, description="Тип поля. Возможны варианты (integer - числовое поле, text - текстовое поле, autocomplete - автокомплит поле, checkbox, choice - выпадающий список, date - поле с датой)")
    multiple: Optional[bool] = Field(None, description="Указывается для типа поля choice. Означает что можно выбирать несколько вариантов")
    choices: Optional[list[DeliveryDataFieldChoice]] = Field(None, description="Указывается для типа поля choice. Список возможных вариантов в выпадающем списке")
    autocompleteUrl: Optional[str] = Field(None, description="Указывается для типа поля autocomplete. Адрес, по окторому можно получить данные для автокомплит поля.")
    visible: Optional[bool] = Field(None, description="Отображать поле в карточке заказа")
    required: Optional[bool] = Field(None, description="Поле обязательно для заполнения")
    affectsCost: Optional[bool] = Field(None, description="Поле влияет на стоимость доставки. Если 'affectsCost': true - значение поля используется в методе calculate")
    editable: Optional[bool] = Field(None, description="Разрешено ли редактировать поле.")


class DeliveryPaymentTypeSettings(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код типа платежа в системе")
    active: Optional[bool] = Field(None, description="Возможность использования типа оплаты")
    cod: Optional[bool] = Field(None, description="Оплата наложенным платежом")

class DeliveryShipmentPointSettings(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код склада в системе")
    shipmentPointId: Optional[str] = Field(None, description="Идентификатор терминала по умолчанию")
    shipmentPointLabel: Optional[str] = Field(None, description="Название терминала по умолчанию")

class DeliveryStatusSettings(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код статуса в системе")
    trackingStatusCode: Optional[str] = Field(None, description="Код статуса в службе доставки")

class DeliverySettings(BaseRetailCrmScheme):
    defaultPayerType: Optional[str] = Field(None, description="Плательщик за доставку по умолчанию")
    costCalculateBy: Optional[str] = Field(None, description="Стоимость доставки по умолчанию (Возможные значения auto|manual)")
    nullDeclaredValue: Optional[bool] = Field(None, description="Нулевая объявленная стоимость по умолчанию")
    lockedByDefault: Optional[bool] = Field(None, description="По умолчанию не синхронизировать со службой доставки")
    paymentTypes: Optional[list[DeliveryPaymentTypeSettings]] = Field(None, description="Способы оплаты (Справочник объектов)")
    shipmentPoints: Optional[list[DeliveryShipmentPointSettings]] = Field(None, description="Склады (Справочник объектов)")
    statuses: Optional[list[DeliveryStatusSettings]] = Field(None, description="Соответствие статусов (Справочник объектов)")
    deliveryExtraData: Optional[dict[str, Any]] = Field(None, description="Дополнительные значения полей доставки по умолчанию (deliveryDataField.code => значение)")
    shipmentExtraData: Optional[dict[str, Any]] = Field(None, description="Дополнительные значения полей отгрузки по умолчанию (shipmentDataField.code => значение)")


class DeliveryConfiguration(BaseRetailCrmScheme):
    description: Optional[str] = Field(None, description="Описание подключения")
    actions: Optional[list[str]] = Field(None, description="Относительные пути от базового URL до конкретных методов")
    payerType: Optional[list[str]] = Field(None, description="Допустимые типы плательщиков за доставку")
    platePrintLimit: Optional[int] = Field(None, description="Максимальное количество заказов при печати документов")
    rateDeliveryCost: Optional[bool] = Field(None, description="Рассчитывает ли интеграция со службой доставки стоимость самой доставки")
    allowPackages: Optional[bool] = Field(None, description="Разрешить использование упаковок")
    codAvailable: Optional[bool] = Field(None, description="Доставка наложенным платежом доступна/не доступна")
    selfShipmentAvailable: Optional[bool] = Field(None, description="Возможен самопривоз на терминал.")
    duplicateOrderProductSupported: Optional[bool] = Field(None, description="Возможность работы с заказом, содержащим несколько позиций с одинаковым торговым предложением")
    allowTrackNumber: Optional[bool] = Field(None, description="Передавать дополнительно трек номер помимо идентификатора доставки")
    availableCountries: Optional[list[str]] = Field(None, description="Список ISO кодов стран (ISO 3166-1 alpha-2) с которыми работает доставка.")
    requiredFields: Optional[list[str]] = Field(None, description="Список обязательных полей заказа")
    statuslist: Optional[list[DeliveryStatus]] = Field(None, description="Статусы службы доставки")
    platelist: Optional[list[Plate]] = Field(None, description="Печатные формы, предоставляемых службой")
    deliveryDataFieldlist: Optional[list[DeliveryDataField]] = Field(None, description="Дополнительные поля, необходимые для оформления доставки")
    shipmentDataFieldlist: Optional[list[DeliveryDataField]] = Field(None, description="Дополнительные поля, необходимые для оформления доставки")
    settings: Optional[DeliverySettings] = Field(None, description="Настройки модуля")


class Action(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код")
    url: Optional[str] = Field(None, description="Url метода")
    callPoints: Optional[list[str]] = Field(None, description="Точки вызова метода")

class StoreConfiguration(BaseRetailCrmScheme):
    actions: Optional[list[Action]] = Field(None, description="Callback методы")


class Mode(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код вкладки")
    names: Optional[list[str]] = Field(None, description="[массив] Код языка => Название вкладки")

class RecommendationConfiguration(BaseRetailCrmScheme):
    actions: Optional[list[str]] = Field(None, description="Относительные пути от базового URL до конкретных методов")
    addDefaultModes: Optional[bool] = Field(None, description="Показывать системные вкладки Также покупают и Аналоги")
    modes: Optional[list[Mode]] = Field(None, description="Массив вкладок, предоставляемых модулем")


class PaymentActions(BaseRetailCrmScheme):
    create: Optional[str] = Field(None, description="Метод создания оплаты")
    approve: Optional[str] = Field(None, description="Метод подтверждения оплаты")
    cancel: Optional[str] = Field(None, description="Метод отмены оплаты")
    refund: Optional[str] = Field(None, description="Метод возврата")

class Shop(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Код магазина")
    name: Optional[str] = Field(None, description="Название магазина")
    active: Optional[bool] = Field(None, description="Статус активности")

class PaymentConfiguration(BaseRetailCrmScheme):
    actions: Optional[PaymentActions] = Field(None, description="Относительные пути от базового URL до конкретных методов")
    currencies: Optional[list[str]] = Field(None, description="Список кодов доступных валют")
    invoiceTypes: Optional[list[str]] = Field(None, description="Массив поддерживаемых типов инвойсов.")
    shops: Optional[list[Shop]] = Field(None, description="Список магазинов на стороне платежной системы")


class NativeConfiguration(BaseRetailCrmScheme): # embedJs
    entrypoint: Optional[str] = Field(None, description="Относительный url к html-странице с js-скриптом")
    stylesheet: Optional[str] = Field(None, description="Относительный url к файлу стилей")
    targets: Optional[list[str]] = Field(None, description="Массив точек встраивания")


class TransportConfiguration(BaseRetailCrmScheme):
    token: Optional[str] = Field(None, description="Ключ безопасности")
    isActive: Optional[bool] = Field(None, description="Признак активности")
    webhookUrl: Optional[str] = Field(None, description="URL на который отправлять события")
    actions: Optional[list[str]] = Field(None, description="Относительные пути от базового URL до конкретных методов")
    refreshToken: Optional[bool] = Field(None, description="Обновить токен")


class BotConfiguration(BaseRetailCrmScheme): # mgBot
    isActive: Optional[bool] = Field(None, description="Признак активности")
    logo: Optional[str] = Field(None, description="Ссылка на логотип")
    token: Optional[str] = Field(None, description="Ключ безопасности")
    name: Optional[str] = Field(None, description="Название бота")
    refreshToken: Optional[bool] = Field(None, description="Обновить токен")


class Integrations(BaseRetailCrmScheme):
    telephony: Optional[TelephonyConfiguration] = Field(None, description="Конфигурация интеграции с телефонией")
    delivery: Optional[DeliveryConfiguration] = Field(None, description="Конфигурация интеграции со службой доставки")
    store: Optional[StoreConfiguration] = Field(None, description="Конфигурация интеграции со складской системой")
    recommendation: Optional[RecommendationConfiguration] = Field(None, description="Конфигурация интеграции с системой рекомендаций")
    payment: Optional[PaymentConfiguration] = Field(None, description="Конфигурация интеграции с платежной системой")
    embedJs: Optional[NativeConfiguration] = Field(None, description="Конфигурация встраиваемого js api")
    mgTransport: Optional[TransportConfiguration] = Field(None, description="Конфигурация интеграции с системой мгновенного обмена сообщениями")
    mgBot: Optional[BotConfiguration] = Field(None, description="Конфигурация интеграции с MessageGateway ботом")

class IntegrationModule(BaseRetailCrmScheme):
    code: Optional[str] = Field(None, description="Символьный код экземпляра модуля")
    integrationCode: Optional[str] = Field(None, description="Символьный код модуля (должен совпадать с кодом модуля, заданным через партнерский кабинет)")
    active: Optional[bool] = Field(None, description="Статус активности")
    freeze: Optional[bool] = Field(None, description="Работа модуля заморожена")
    name: Optional[str] = Field(None, description="Название (требуется, если модуль не опубликован в маркетплейсе)")
    logo: Optional[str] = Field(None, description="Ссылка на svg логотип (требуется, если модуль не опубликован в маркетплейсе)")
    native: Optional[bool] = Field(None, description="Системный модуль")
    baseUrl: Optional[str] = Field(None, description="Базовый URL, на который делает запросы система")
    actions: Optional[list[str]] = Field(None, description="Относительные пути от базового URL до конкретных методов")
    availableCountries: Optional[list[str]] = Field(None, description="Массив ISO кодов стран (ISO 3166-1 alpha-2) для которых доступен модуль")
    accountUrl: Optional[str] = Field(None, description="Адрес личного кабинета (при переходе по этой ссылке отправляется POST запрос с параметром clientId)")
    integrations: Optional[Integrations] = Field(None, description="Массив конфигураций интеграций")
    clientId: Optional[str] = Field(None, description="Уникальный хеш-ключ клиента для авторизации и идентификации во внешней системе")


class Requires(BaseRetailCrmScheme):
    scopes: Optional[list[str]] = Field(None, description="Разрешения, необходимые API ключу для работы модуля")
