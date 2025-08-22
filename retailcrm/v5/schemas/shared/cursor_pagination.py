from pydantic import Field

from retailcrm.v5.schemas import BaseRetailCrmScheme


class CursorPagination(BaseRetailCrmScheme):
    nextCursor: str | None = Field(None, description="")  # TODO: Заполнить
