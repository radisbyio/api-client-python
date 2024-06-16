from typing import Any, Callable, Optional
from datetime import datetime

from pydantic_core.core_schema import ValidationInfo


def errors_dict_validator() -> Callable[[Any, ValidationInfo], Optional[dict]]:
    def validator(v, info: ValidationInfo) -> Optional[dict]:
        if isinstance(v, list) and not v:
            return {"default": [" ".join(v)]}
        else:
            return v

    return validator


def dict_validator() -> Callable[[Any, ValidationInfo], dict]:
    def validator(v, info: ValidationInfo) -> dict:
        if isinstance(v, dict):
            return v
        if isinstance(v, list) and not v:
            return {}
        else:
            raise ValueError("Not empty list")

    return validator


def datetime_serializer(format_str: str) -> Callable[[datetime], str]:
    def serializer(value: Optional[datetime]) -> Optional[str]:
        if value:
            return datetime.strftime(value, format_str)
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
        if isinstance(v, list) and not v:
            return {payment_item["id"]: payment_item for payment_item in v}
        else:
            raise ValueError("cannot validate payment")

    return validator
