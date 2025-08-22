from typing import Optional

from pydantic import Field, field_serializer, model_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.custom_fields import (
    SerializedCustomDictionary,
    SerializedCustomFieldApiDocModel,
)
from retailcrm.v5.schemas.filters.custom_fields import (
    CustomDictionaryFilter,
    CustomFieldFilter,
)
from retailcrm.v5.utils import pydantic_to_nested_dict


class CustomFieldsFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(None, description="Количество элементов в ответе")
    page: Optional[int] = Field(None, description="Номер страницы с результатами")
    filter_obj: Optional[CustomFieldFilter] = Field(None, description="Объект фильтра")

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter"),
        }


class CustomDictionariesFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(None, description="Количество элементов в ответе")
    page: Optional[int] = Field(None, description="Номер страницы с результатами")
    filter_obj: Optional[CustomDictionaryFilter] = Field(
        None, description="Объект фильтра"
    )

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter"),
        }


class CustomDictionaryCreateRequest(BaseRetailCrmScheme):
    customDictionary: SerializedCustomDictionary

    customDictionary_serializer = field_serializer("customDictionary")(
        to_json_serializer()
    )


class CustomDictionaryEditRequest(BaseRetailCrmScheme):
    customDictionary: SerializedCustomDictionary

    customDictionary_serializer = field_serializer("customDictionary")(
        to_json_serializer()
    )


class CustomFieldCreateRequest(BaseRetailCrmScheme):
    customField: SerializedCustomFieldApiDocModel

    customField_serializer = field_serializer("customField")(to_json_serializer())


class CustomFieldEditRequest(BaseRetailCrmScheme):
    customField: SerializedCustomFieldApiDocModel

    customField_serializer = field_serializer("customField")(to_json_serializer())
