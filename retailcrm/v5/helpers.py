from typing import Any, Callable, Optional
from datetime import datetime

from pydantic_core.core_schema import ValidationInfo


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
    def serializer(value: Optional[datetime]) -> str:
        if value:
            return datetime.strftime(value, format_str)
        else:
            return value

    return serializer
