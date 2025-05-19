from pydantic import Field

from retailcrm.v5.schemas import BaseRetailCrmScheme


# TODO: Исправить доку
class HistoryUser(BaseRetailCrmScheme):
    current: bool | None = Field(None, description="")