from datetime import datetime
from typing import Optional

from pydantic import Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas import BaseRetailCrmScheme


class Value(BaseRetailCrmScheme):
    value: Optional[str] = Field(None, description="Значение настройки")
    updated_at: Optional[datetime] = Field(None, description="Время последнего изменения настройки")

    updated_at_serializer = field_serializer("updated_at")(datetime_serializer("%Y-%m-%d %H:%M:%S"))


class WorkTime(BaseRetailCrmScheme):
    day_type: Optional[str] = Field(None, description="День недели")
    start_time: Optional[str] = Field(None, description="Начало рабочего времени")
    end_time: Optional[str] = Field(None, description="Конец рабочего времени")
    lunch_start_time: Optional[str] = Field(None, description="Время начала перерыва")
    lunch_end_time: Optional[str] = Field(None, description="Время конца перерыва")


class NonWorkingDay(BaseRetailCrmScheme):
    start_date: Optional[datetime] = Field(None, description="Начало нерабочих дней")
    end_date: Optional[datetime] = Field(None, description="Конец нерабочих дней")

    start_date_serializer = field_serializer("start_date")(datetime_serializer("%Y-%m-%d %H:%M:%S"))
    end_date_serializer = field_serializer("end_date")(datetime_serializer("%Y-%m-%d %H:%M:%S"))


class ChannelSetting(BaseRetailCrmScheme):
    site: Optional[str] = Field(None, description="Магазин")
    order_type: Optional[str] = Field(None, description="Тип заказа")
    order_method: Optional[str] = Field(None, description="Метод оформления заказа")


class OrderCreationSettings(BaseRetailCrmScheme):
    default: Optional[ChannelSetting] = Field(None, description="Параметры по-умолчанию")
    channels: Optional[list[ChannelSetting]] = Field(
        None, description="Параметры для отдельных каналов (ключ - externalId канала)"
    )


class IntegrationData(BaseRetailCrmScheme):
    mg: Optional[OrderCreationSettings] = Field(None, description="Настройки чатов")


class Settings(BaseRetailCrmScheme):
    default_currency: Optional[Value] = Field(None, description="deprecated Валюта по умолчанию")
    system_language: Optional[Value] = Field(None, description="Язык системы")
    timezone: Optional[Value] = Field(None, description="Временная зона")
    work_times: Optional[list[WorkTime]] = Field(None, description="Рабочее время")
    non_working_days: Optional[list[NonWorkingDay]] = Field(None, description="Нерабочие дни")
    mg: Optional[IntegrationData] = Field(None, description="Настройки чатов")
