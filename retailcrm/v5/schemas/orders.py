from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


class OrderHistoryFilterV4Type(BaseModel):
    orderId: Optional[int] = Field(None, description="ID заказа")
    sinceId: Optional[int] = Field(None, description="Начиная с ID истории заказов")
    externalId: Optional[str] = Field(None, description="Внешний ID заказа")
    startDate: Optional[datetime] = Field(None, description="Дата/время изменения (от)")
    endDate: Optional[datetime] = Field(None, description="Дата/время изменения (до)")


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
    createdAtFrom: Optional[date] = Field(
        None, description="Дата оформления заказа (от)"
    )
    createdAtTo: Optional[date] = Field(None, description="Дата оформления заказа (до)")
    fullPaidAtFrom: Optional[date] = Field(None, description="Дата полной оплаты (от)")
    fullPaidAtTo: Optional[date] = Field(None, description="Дата полной оплаты (до)")
    deliveryDateFrom: Optional[date] = Field(None, description="Дата доставки (от)")
    deliveryDateTo: Optional[date] = Field(None, description="Дата доставки (до)")
