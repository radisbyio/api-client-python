from typing import Literal, Optional

from pydantic import Field

from retailcrm.v5.enums.recommendation import Mode
from retailcrm.v5.schemas import BaseRetailCrmScheme


class RecommendationResponse(BaseRetailCrmScheme):
    by: Optional[str] = Field(
        None,
        description="Название поля для идентификации товаров. Возможные значения id, externalId",
    )
    ids: Optional[list[int | str]] = Field(
        None, description="Массив с идентификаторами товаров"
    )
