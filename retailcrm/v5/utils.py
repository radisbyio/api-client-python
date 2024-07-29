from typing import Any

from pydantic import BaseModel


def pydantic_to_nested_dict(model: BaseModel, prefix: str = "") -> dict[str, str]:
    """
    Преобразует поля модели Pydantic в словарь с вложенными ключами вида "fieldA[fieldB]=valueB".
    """

    result = {}

    def _pydantic_to_nested_dict(data: Any, prefix: str = ""):
        """
        Вспомогательная функция для рекурсивного преобразования данных.
        """

        if isinstance(data, dict):
            for field_name, field_value in data.items():
                _pydantic_to_nested_dict(field_value, f"{prefix}[{field_name}]")
        elif isinstance(data, list):
            for index, item in enumerate(data):
                _pydantic_to_nested_dict(item, f"{prefix}[{index}]")
        else:
            result[prefix] = data

    _pydantic_to_nested_dict(
        model.model_dump(exclude_unset=True, by_alias=True), prefix
    )
    return result
