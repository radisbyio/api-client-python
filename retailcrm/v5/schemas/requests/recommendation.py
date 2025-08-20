from typing import Optional

from pydantic import Field

from retailcrm.v5.enums.recommendation import Mode
from retailcrm.v5.schemas import BaseRetailCrmScheme


class RecommendationRequest(BaseRetailCrmScheme):
    clientId: Optional[str] = Field(None, description="Идентификатор клиента во внешнем сервисе")
    ids: Optional[list[int]] = Field(None, description="ID товаров")
    externalIds: Optional[list[str]] = Field(None, description="externalId товаров")
    mode: Optional[Mode] = Field(None, description="Тип рекомендаций: товары из серии «Покупают с» или товары из серии «Аналоги». Возможные значения buying_with, analogs")