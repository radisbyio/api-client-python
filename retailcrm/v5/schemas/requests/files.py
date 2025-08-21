from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class FilesFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(20, description="Количество элементов в ответе")
    page: Optional[int] = Field(1, description="Номер страницы с результатами")
    filter: Optional["FileFilterData"] = Field(None, alias="filter")


class FileEditRequest(BaseRetailCrmScheme):
    file: SerializedFile