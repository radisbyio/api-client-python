from typing import Any, Literal, Optional

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class CustomFieldApiDocModel(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    required: Optional[bool] = Field(None, description="Обязательное")
    inFilter: Optional[bool] = Field(None, description="Доступно в фильтре")
    inList: Optional[bool] = Field(None, description="Доступно в списке")
    inGroupActions: Optional[bool] = Field(
        None, description="Доступно в групповых операциях"
    )
    type: Optional[str] = Field(None, description="Тип поля")
    entity: Optional[str] = Field(None, description="Поля для таблицы")
    default: Optional[str] = Field(None, description="deprecated Значение по умолчанию")
    ordering: Optional[int] = Field(None, description="Сортировка")
    displayArea: Optional[str] = Field(None, description="Область отображения")
    viewMode: Optional[str] = Field(None, description="Вид поля в форме")
    viewModeMobile: Optional[str] = Field(
        None, description="Вид поля в мобильном приложении"
    )
    dictionary: Optional[str] = Field(None, description="Связанный словарь")
    defaultTyped: Optional[Any] = Field(
        None, description="Типизированное значение по умолчанию"
    )


class SerializedCustomDictionaryElement(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    ordering: Optional[int] = Field(None, description="Сортировка")


class CustomDictionary(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    elements: list[SerializedCustomDictionaryElement] = Field(
        default_factory=list, description="Элемент справочника"
    )


class SerializedCustomDictionary(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    elements: Optional[list[SerializedCustomDictionaryElement]] = Field(
        None, description="Элемент справочника"
    )


class SerializedCustomFieldApiDocModel(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    type: Optional[
        Literal[
            "boolean",
            "date",
            "datetime",
            "dictionary",
            "email",
            "integer",
            "multiselect_dictionary",
            "numeric",
            "string",
            "text",
        ]
    ] = Field(None, description="Тип поля")
    entity: Optional[Literal["customer", "loyalty_account", "order"]] = Field(
        None, description="Поля для таблицы"
    )
    code: Optional[str] = Field(None, description="Символьный код")
    ordering: Optional[int] = Field(None, ge=0, description="Сортировка")
    displayArea: Optional[
        Literal[
            "address",
            "customer",
            "delivery",
            "dimensions",
            "legal_details",
            "main_data",
            "payment",
            "shipment",
        ]
    ] = Field(None, description="Область отображения")
    viewMode: Optional[Literal["editable", "miss", "not_editable"]] = Field(
        None, description="Вид поля в форме"
    )
    viewModeMobile: Optional[Literal["editable", "miss", "not_editable"]] = Field(
        None, description="Вид поля в мобильном приложении"
    )
    required: Optional[bool] = Field(None, description="Обязательное")
    inFilter: Optional[bool] = Field(None, description="Доступно в фильтре")
    inList: Optional[bool] = Field(None, description="Доступно в списке")
    inGroupActions: Optional[bool] = Field(
        None, description="Доступно в групповых операциях"
    )
    default: Optional[str] = Field(None, description="deprecated Значение по умолчанию")
    dictionary: Optional[str] = Field(None, description="Связанный словарь")
    defaultTyped: Optional[Any] = Field(
        None, description="Типизированное значение по умолчанию"
    )
