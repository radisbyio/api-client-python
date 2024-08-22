from enum import Enum
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme, RetailCrmResponse


class CustomFieldsTypes(str, Enum):
    BOOLEAN = "boolean"
    DATE = "date"
    DATETIME = "datetime"
    DICTIONARY = "dictionary"
    EMAIL = "email"
    INTEGER = "integer"
    MULTISELECT_DICTIONARY = "multiselect_dictionary"
    NUMERIC = "numeric"
    STRING = "string"
    TEXT = "text"


class ViewModeTypes(str, Enum):
    EDITABLE = "editable"
    MISS = "miss"
    NOT_EDITABLE = "not_editable"


class ViewModeMobileTypes(str, Enum):
    EDITABLE = "editable"
    MISS = "miss"
    NOT_EDITABLE = "not_editable"


class DisplayAreaTypes(str, Enum):
    ADDRESS = "address"
    CUSTOMER = "customer"
    DELIVERY = "delivery"
    DIMENSIONS = "dimensions"
    LEGAL_DETAILS = "legal_details"
    MAIN_DATA = "main_data"
    PAYMENT = "payment"
    SHIPMENT = "shipment"


class EntityTypes(str, Enum):
    CUSTOMER = "customer"
    LOYALTY_ACCOUNT = "loyalty_account"
    ORDER = "order"


class CustomFieldFilter(BaseRetailCrmScheme):
    name: Optional[str] = None
    code: Optional[str] = None
    type: Optional[CustomFieldsTypes] = None
    viewMode: Optional[ViewModeTypes] = None
    viewModeMobile: Optional[ViewModeMobileTypes] = None
    entity: Optional[EntityTypes] = None
    inFilter: Optional[int] = None


class CustomFieldApiDocModel(BaseRetailCrmScheme):
    name: str = Field(description="Название")
    code: str = Field(description="Символьный код")
    required: bool = Field(False, description="Обязательное")
    inFilter: bool = Field(False, description="Доступно в фильтре")
    inList: bool = Field(False, description="Доступно в списке")
    inGroupActions: bool = Field(description="Доступно в групповых операциях")
    type: CustomFieldsTypes = Field(description="Тип поля")
    entityType: Optional[EntityTypes] = Field(None, description="Поля для таблицы")
    ordering: int = Field(description="Сортировка")
    displayArea: Optional[DisplayAreaTypes] = Field(
        None, description="Область отображения"
    )
    viewMode: Optional[ViewModeTypes] = Field(None, description="Вид поля в форме")
    viewModeMobile: Optional[ViewModeMobileTypes] = Field(
        None, description="Вид поля в мобильном приложении"
    )
    dictionary: Optional[str] = Field(None, description="Связанный словарь")


class CustomFieldsResponse(RetailCrmResponse):
    customFields: list[CustomFieldApiDocModel] = Field(default_factory=list)


class CustomDictionaryFilter(BaseRetailCrmScheme):
    name: Optional[str] = None
    code: Optional[str] = None


class SerializedCustomDictionaryElement(BaseRetailCrmScheme):
    name: str = Field(description="Название")
    code: str = Field(description="Символьный код")
    ordering: int = Field(description="Сортировка")


class CustomDictionary(BaseRetailCrmScheme):
    name: str = Field(description="Название")
    code: str = Field(description="Символьный код")
    elements: list[SerializedCustomDictionaryElement] = Field(
        description="Элемент справочника"
    )


class CustomDictionariesResponse(RetailCrmResponse):
    customDictionaries: list[CustomDictionary] = Field(
        default_factory=list, description="Справочник"
    )
