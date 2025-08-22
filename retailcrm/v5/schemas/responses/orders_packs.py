from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import PaginatedResponse, SuccessResponse
from retailcrm.v5.schemas.entities.orders_packs import (
    OrderProductPack,
    OrderProductPackHistory,
)


class OrderProductPackFilterResponse(PaginatedResponse):
    packs: Optional[list[OrderProductPack]] = Field(
        None,
        description="Пак - упаковка товаров, в рамках одной товарной позиции, с одного склада",
    )


class OrderProductPackResponse(SuccessResponse):
    packs: Optional[OrderProductPack] = Field(
        None,
        description="	Пак - упаковка товаров, в рамках одной товарной позиции, с одного склада",
    )


class OrderProductPackHistoryListResponse(PaginatedResponse):
    generatedAt: Optional[datetime] = Field(
        None, description="Время формирования ответа"
    )
    history: Optional[list[OrderProductPackHistory]] = Field(
        None, description="Набор изменений в истории комплектации"
    )

    generatedAt_serializer = field_serializer("generatedAt")(
        datetime_serializer("%Y-%m-%d %H:%M:%S")
    )
