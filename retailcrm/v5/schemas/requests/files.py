from typing import Optional

from pydantic import Field, model_serializer

from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.files import SerializedFile
from retailcrm.v5.schemas.filters.files import FileFilter
from retailcrm.v5.utils import pydantic_to_nested_dict


class FilesFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(20, description="Количество элементов в ответе")
    page: Optional[int] = Field(1, description="Номер страницы с результатами")
    filter_obj: Optional[FileFilter] = Field(None)

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter"),
        }


class FileEditRequest(BaseRetailCrmScheme):
    file: SerializedFile
