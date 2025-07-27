from pydantic import Field

from retailcrm.v5.schemas import BaseRetailCrmScheme


# TODO: Исправить доку
class HistoryUser(BaseRetailCrmScheme):
    id: int | None = Field(None, description="ID")