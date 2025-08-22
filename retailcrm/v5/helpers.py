from datetime import datetime, time, timezone
from typing import Any, Callable, Optional, TypeVar

from pydantic import BaseModel
from pydantic_core.core_schema import SerializationInfo, ValidationInfo

from retailcrm.v5.utils import pydantic_list_dumps_to_json, pydantic_to_nested_dict


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


def list_to_dict_validator() -> Callable[[Any, ValidationInfo], Optional[dict]]:
    """
    Вспомогательная функция, которая позволяет преобразовать массив errors в словарь для более общей обработки.
    """

    def validator(v, info: ValidationInfo) -> Optional[dict]:
        if isinstance(v, list):
            return {}
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


def datetime_serializer(
    format_str: str,
) -> Callable[[Optional[datetime]], Optional[str]]:
    """
    Вспомогательная функция для форматирования даты при сериализации объекта datetime
    """

    def serializer(value: Optional[datetime]) -> Optional[str]:
        if value:
            return datetime.strftime(value, format_str)
        else:
            return None

    return serializer


def datetime_iso_serializer() -> Callable[[Optional[datetime]], Optional[str]]:
    """
    Вспомогательная функция для форматирования даты в формат ISO8601 при сериализации объекта datetime
    """

    def serializer(value: Optional[datetime]) -> Optional[str]:
        if value:
            if value.tzinfo is None:
                value = value.replace(tzinfo=timezone.utc)
            return value.isoformat()
        else:
            return None

    return serializer


def time_serializer(format_str: str) -> Callable[[Optional[time]], Optional[str]]:
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


def bool_flag_serializer() -> Callable[[Optional[bool]], Optional[int]]:
    """
    Вспомогательная функция, которая позволяет преобразовать флаги типа bool в int значение
    """

    def serializer(value: Optional[bool]) -> Optional[int]:
        if value is None:
            return None
        else:
            return int(value)

    return serializer


T = TypeVar("T", bound=BaseModel)


def to_json_serializer() -> Callable[[list[T], SerializationInfo], str]:
    """
    Вспомогательная функция, которая позволяет преобразовать массив объектов в JSON строку
    """

    def serializer(value: T | list[T], info: SerializationInfo) -> str:
        if isinstance(value, list):
            return pydantic_list_dumps_to_json(value)
        else:
            return value.model_dump_json(exclude_none=True, by_alias=True)

    return serializer


def filter_obj_serializer(
    prefix: str = "",
) -> Callable[[T | None, SerializationInfo], dict[str, Any]]:
    def serializer(value: T | None, info: SerializationInfo) -> dict[str, Any]:
        return pydantic_to_nested_dict(value, prefix)

    return serializer
