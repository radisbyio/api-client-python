from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas import BaseRetailCrmScheme


class MGChannel(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID канала")
    externalId: Optional[int] = Field(None, description="Внешний ID канала")
    allowedSendByPhone: Optional[bool] = Field(None, description="Можно ли писать первыми в этот канал по номеру телефона")
    type: Optional[str] = Field(None, description="Тип канала")
    active: Optional[bool] = Field(False, description="Активность канала")
    name: Optional[str] = Field(None, description="Название канала")