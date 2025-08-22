from pydantic import Field
from typing import Optional, Literal

from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class CustomFieldFilter(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")
    type: Optional[Literal["boolean", "date", "datetime", "dictionary", "email", "integer", "multiselect_dictionary", "numeric", "string", "text"]] = Field(None, description="Тип поля")
    viewMode: Optional[Literal["editable", "miss", "not_editable"]] = Field(None, description="Вид поля в форме")
    viewModeMobile: Optional[Literal["editable", "miss", "not_editable"]] = Field(None, description="Вид поля в мобильном приложении")
    displayArea: Optional[Literal["address", "customer", "delivery", "dimensions", "empty", "legal_details", "main_data", "payment", "shipment"]] = Field(None, description="Область отображения")
    entity: Optional[Literal["customer", "loyalty_account", "order"]] = Field(None, description="Поля для таблицы")
    inFilter: Optional[Literal[0, 1]] = Field(None, description="Доступно в фильтре")


class CustomDictionaryFilter(BaseRetailCrmScheme):
    name: Optional[str] = Field(None, description="Название")
    code: Optional[str] = Field(None, description="Символьный код")