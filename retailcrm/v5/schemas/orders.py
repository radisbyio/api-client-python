from typing import Optional

from pydantic import BaseModel, Field


# todo: заполнить
class OrderFilterData(BaseModel):
    ids: list[int] = Field([], description="Массив ID заказов")
    externalIds: list[str] = Field([], description="Массив externalID заказов")
    numbers: list[str] = Field([], description="Массив номеров заказов")
    customerId: Optional[int] = Field(None, description="Внутренний ID клиента")
    customerExternalId: Optional[str] = Field(None, description="Внешний ID клиента")
    customer: Optional[str] = Field(None, description="Клиент (ФИО или телефон)")
    customerType: Optional[str] = Field(None, description="Тип клиента")
    email: Optional[str] = Field(None, description="E-mail")

