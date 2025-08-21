from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class FileFilter(BaseRetailCrmScheme):
    ids: Optional[list[int]] = Field(None, description="Массив ID файлов")
    orderIds: Optional[list[int]] = Field(None, description="Массив внутренних ID заказов")
    orderExternalIds: Optional[list[str]] = Field(None, description="Массив внешних ID заказов")
    customerIds: Optional[list[int]] = Field(None, description="Массив внутренних ID клиентов")
    customerExternalIds: Optional[list[str]] = Field(None, description="Массив внешних ID клиентов")
    sites: Optional[list[str]] = Field(None, description="Магазины")
    type: Optional[list[str]] = Field(None, description="Массив MIME типов файлов")
    filename: Optional[str] = Field(None, description="Название файла")
    isAttached: Optional[bool] = Field(None, description="Привязан ли файл хотя бы к одному заказу или клиенту")
    createdAtFrom: Optional[datetime] = Field(None, description="Дата загрузки файла (от)")
    createdAtTo: Optional[datetime] = Field(None, description="Дата загрузки файла (до)")
    sizeFrom: Optional[int] = Field(None, description="Размер файла (от)")
    sizeTo: Optional[int] = Field(None, description="Размер файла (до)")

    createdAtFrom_serializer = field_serializer("createdAtFrom")(
        datetime_serializer("%Y-%m-%d")
    )
    createdAtTo_serializer = field_serializer("createdAtTo")(
        datetime_serializer("%Y-%m-%d")
    )
