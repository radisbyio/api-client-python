from pydantic import Field

from retailcrm.v5.schemas.base import BaseRetailCrmScheme


class Source(BaseRetailCrmScheme):
    source: str | None = Field(None, description="Источник")
    medium: str | None = Field(None, description="Канал")
    campaign: str | None = Field(None, description="Кампания")
    keyword: str | None = Field(None, description="Ключевое слово")
    content: str | None = Field(None, description="Содержание кампании")