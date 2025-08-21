from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import PaginatedResponse, SuccessResponse
from retailcrm.v5.schemas.entities.files import File


class FilesFilterResponse(PaginatedResponse):
    files: list[File] = Field(default_factory=list, description="Список файлов")


class FileUploadResponse(SuccessResponse):
    file: Optional[File] = Field(None, description="Загруженный файл")


class FileGetResponse(SuccessResponse):
    file: Optional[File] = Field(None, description="Информация о файле")


class FileEditResponse(SuccessResponse):
    file: Optional[File] = Field(None, description="Отредактированный файл")
