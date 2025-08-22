from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.files import SerializedFile
from retailcrm.v5.schemas.filters.files import FileFilter


class FilesFilterRequest(BaseRetailCrmScheme):
    limit: Optional[int] = Field(20, description="Количество элементов в ответе")
    page: Optional[int] = Field(1, description="Номер страницы с результатами")
    filter_obj: Optional[FileFilter] = Field(None)


class FileEditRequest(BaseRetailCrmScheme):
    file: SerializedFile