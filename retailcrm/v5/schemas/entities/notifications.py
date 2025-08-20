from typing import Optional

from pydantic import Field

from retailcrm.v5.enums.notifications import NotificationTypes
from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class SerializedApiNotification(BaseRetailCrmScheme):
    type: Optional[NotificationTypes] = Field(None, description="Тип")
    message: Optional[str] = Field(
        None, description="Сообщение (допускается использование html тегов)."
    )
    userIds: Optional[list[int]] = Field(
        None, description="Массив идентификаторов получателей"
    )
    userGroups: Optional[list[int]] = Field(
        description="Массив кодов групп получателей"
    )
