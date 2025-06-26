from enum import Enum
from typing import Optional

from pydantic import Field

from retailcrm.v5.enums import (
    CustomFieldEntityTypes,
    CustomFieldTypes,
    DisplayAreaTypes,
)
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


class CustomFieldFilter(BaseRetailCrmScheme):
    name: Optional[str] = None
    code: Optional[str] = None
    type: Optional[CustomFieldsTypes] = None
    viewMode: Optional[ViewModeTypes] = None
    viewModeMobile: Optional[ViewModeMobileTypes] = None
    entity: Optional[CustomFieldEntityTypes] = None
    inFilter: Optional[int] = None


class CustomFieldApiDocModel(BaseRetailCrmScheme):
    name: str = Field(description="Название")
    code: str = Field(description="Символьный код")
    required: bool = Field(False, description="Обязательное")
    inFilter: bool = Field(False, description="Доступно в фильтре")
    inList: bool = Field(False, description="Доступно в списке")
    inGroupActions: bool = Field(description="Доступно в групповых операциях")
    type: CustomFieldsTypes = Field(description="Тип поля")
    entityType: Optional[CustomFieldEntityTypes] = Field(
        None, description="Поля для таблицы"
    )
    ordering: int = Field(description="Сортировка")
    displayArea: Optional[DisplayAreaTypes] = Field(
        None, description="Область отображения"
    )
    viewMode: Optional[ViewModeTypes] = Field(None, description="Вид поля в форме")
    viewModeMobile: Optional[ViewModeMobileTypes] = Field(
        None, description="Вид поля в мобильном приложении"
    )
    dictionary: Optional[str] = Field(None, description="Связанный словарь")


class CustomFieldsRetrieveResponse(RetailCrmResponse):
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


class CustomDictionariesRetrieveResponse(RetailCrmResponse):
    customDictionaries: list[CustomDictionary] = Field(
        default_factory=list, description="Справочник"
    )


class SerializedCustomFieldApiDocModel(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    type: Optional[CustomFieldTypes] = Field(None, description="Тип поля")
    entity: Optional[CustomFieldEntityTypes] = Field(
        None, description="Поля для таблицы"
    )
    code: Optional[str] = Field(None, description="Символьный код")
    ordering: Optional[int] = Field(None, description="Сортировка")
    displayArea: Optional[DisplayAreaTypes] = Field(
        None, description="Область отображения"
    )
    viewMode: Optional[ViewModeTypes] = Field(None, description="Вид поля в форме")
    viewModeMobile: Optional[ViewModeMobileTypes] = Field(
        None, description="Вид поля в мобильном приложении"
    )
    required: Optional[bool] = Field(None, description="Обязательное")
    inFilter: Optional[bool] = Field(None, description="Доступно в фильтре")
    inList: Optional[bool] = Field(None, description="Доступно в списке")
    inGroupActions: Optional[bool] = Field(
        None, description="Доступно в групповых операциях"
    )
    default: Optional[str] = Field(None, description="[deprecated] Связанный словарь")
    dictionary: Optional[str] = Field(
        None, description="Типизированное значение по умолчанию"
    )
    defaultTyped: Optional[bool] = Field(
        None, description="Типизированное значение по умолчанию"
    )


class CustomFieldCreateResponse(RetailCrmResponse):
    code: str | None = Field(None, description="Символьный код")


class CustomFieldRetrieveResponse(RetailCrmResponse):
    customField: Optional[CustomFieldApiDocModel] = Field(None, description="Символьный код")


class SerializedCustomDictionary(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    elements: Optional[list[SerializedCustomDictionaryElement]] = Field(
        None, description="Элемент справочника"
    )


class CustomFieldDictionaryCreateResponse(RetailCrmResponse):
    code: str | None = Field(None, description="Символьный код")


class CustomFieldDictionaryRetrieveResponse(RetailCrmResponse):
    customDictionary: Optional[CustomDictionary] = Field(None, description="Справочник")


class CustomFieldDictionaryEditResponse(RetailCrmResponse):
    code: str = Field(description="Символьный код")
