from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class HistoryUser(BaseRetailCrmScheme):
    id: int | None = Field(None, description="ID пользователя")