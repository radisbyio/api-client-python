from pydantic import Field

from retailcrm.v5.schemas import BaseRetailCrmScheme


class HistoryApiKey(BaseRetailCrmScheme):
    current: bool | None = Field(None, description="Изменение было сделано с помощью ключа, используемого в данный момент")
    id: int | None = Field(None, description="ID API-ключа")