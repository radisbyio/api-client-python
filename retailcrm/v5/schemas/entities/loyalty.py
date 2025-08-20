import decimal
from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas import BaseRetailCrmScheme


class LoyaltyLevel(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID уровня")
    name: str | None = Field(None, description="Название уровня")
    sum: decimal.Decimal | None = Field(None, description="Сумма, необходимая для перехода на данный уровень (в валюте объекта)")
    privilegeSize: int | None = Field(None, description="Размер скидки, процент или курс начисления бонусов для товаров по обычной цене (в валюте объекта)")
    privilegeSizePromo: int | None = Field(None, description="Размер скидки, процент или курс начисления бонусов для акционных товаров (в валюте объекта)")


# todo: заполнить
class LoyaltyEventDiscount(BaseRetailCrmScheme):
    id: Optional[int] = Field(None, description="ID")