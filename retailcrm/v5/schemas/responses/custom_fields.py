from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import PaginatedResponse, SuccessResponse
from retailcrm.v5.schemas.entities.custom_fields import CustomDictionary, CustomFieldApiDocModel


class CustomFieldsFilterResponse(PaginatedResponse):
    customFields: list[CustomFieldApiDocModel] = Field(default_factory=list)


class CustomDictionariesFilterResponse(PaginatedResponse):
    customDictionaries: list[CustomDictionary] = Field(default_factory=list)


class CustomDictionaryCreateResponse(SuccessResponse):
    code: Optional[str] = Field(None)


class CustomDictionaryGetResponse(SuccessResponse):
    customDictionary: Optional[CustomDictionary] = Field(None)


class CustomDictionaryEditResponse(SuccessResponse):
    code: Optional[str] = Field(None)


class CustomFieldCreateResponse(SuccessResponse):
    code: Optional[str] = Field(None)


class CustomFieldGetResponse(SuccessResponse):
    customField: Optional[CustomFieldApiDocModel] = Field(None)


class CustomFieldEditResponse(SuccessResponse):
    code: Optional[str] = Field(None)