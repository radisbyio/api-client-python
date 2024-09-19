from datetime import datetime, time
from typing import Any, Callable, Optional

from pydantic_core.core_schema import ValidationInfo


def errors_dict_validator() -> Callable[[Any, ValidationInfo], Optional[dict]]:
    """
    Вспомогательная функция, которая позволяет преобразовать массив errors в словарь для более общей обработки.
    """

    def validator(v, info: ValidationInfo) -> Optional[dict]:
        if isinstance(v, list) and v:
            return {"default": ". ".join(v)}
        else:
            return v

    return validator


def dict_validator() -> Callable[[Any, ValidationInfo], dict]:
    """
    Вспомогательная функция, которая позволяет преобразовать пустой list в dict.
    Необходим для некоторых полей, например - customFields.
    """

    def validator(v, info: ValidationInfo) -> dict:
        if isinstance(v, dict):
            return v
        if isinstance(v, list) and not v:
            return {}
        else:
            raise ValueError("Not empty list")

    return validator


def datetime_serializer(format_str: str) -> Callable[[Optional[datetime]], str]:
    """
    Вспомогательная функция для форматирования даты при сериализации объекта datetime
    """

    def serializer(value: Optional[datetime]) -> Optional[str]:
        if value:
            return datetime.strftime(value, format_str)
        else:
            return None

    return serializer


def time_serializer(format_str: str) -> Callable[[Optional[time]], str]:
    """
    Вспомогательная функция для форматирования времени при сериализации объекта time
    """

    def serializer(value: Optional[time]) -> Optional[str]:
        if value:
            return value.strftime(format_str)
        else:
            return None

    return serializer


def payments_validator() -> Callable[[Any, ValidationInfo], dict]:
    """
    Вспомогательная функция, которая позволяет преобразовать список оплат в словарь по ключу payment.id
    Пример использования - orders/history
    """

    def validator(v, info: ValidationInfo) -> dict:
        if isinstance(v, dict):
            return v
        if isinstance(v, list):
            return {str(payment_item["id"]): payment_item for payment_item in v}
        else:
            raise ValueError("cannot validate payment")

    return validator


def bool_flag_serializer() -> Callable[[Optional[time]], int]:
    """
    Вспомогательная функция, которая позволяет преобразовать флаги типа bool в int значение
    """

    def serializer(value: Optional[bool]) -> Optional[int]:
        if value is None:
            return None
        else:
            return int(value)

    return serializer
