from typing import Callable, Any

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
