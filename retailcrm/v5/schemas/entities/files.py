from datetime import datetime
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class AttachmentCustomer(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID клиента")
    externalId: Optional[str] = Field(None, description="Внешний ID клиента")
    site: Optional[str] = Field(None, description="Магазин")

class AttachmentOrder(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="	ID заказа")
    number: Optional[str] = Field(None, description="	Номер заказа")
    externalId: Optional[str] = Field(None, description="	Внешний ID заказа")
    site: Optional[str] = Field(None, description="	Магазин")


class Attachment(BaseRetailCrmScheme):
    customer: Optional[AttachmentCustomer] = Field(None, description="Клиент")
    order: Optional[AttachmentOrder] = Field(None, description="Заказ")


class File(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID файла")
    filename: Optional[str] = Field(None, description="Имя файла")
    type: Optional[str] = Field(None, description="MIME-тип файла")
    createdAt: Optional[datetime] = Field(None, description="Дата создания")
    size: Optional[int] = Field(None, description="Размер файла в байтах")
    attachment: list[Attachment] = Field(default_factory=list, description="Прикрепленный объект (вложение)")


class SerializedFile(BaseRetailCrmScheme):
    filename: Optional[str] = Field(None, description="Имя файла")
    attachment: Optional[list[Attachment]] = Field(None, description="Прикрепленные объекты")