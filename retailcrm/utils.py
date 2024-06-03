from typing import Dict, Any

from pydantic import BaseModel


def pydantic_to_nested_dict(model: BaseModel, prefix: str = "") -> dict[str, str]:
    """
    Преобразует поля модели Pydantic в словарь с вложенными ключами вида "fieldA[fieldB]=valueB".
    """

    def _pydantic_to_nested_dict(model_dict: dict, prefix: str = "") -> Dict[str, Any]:
        """
        Вспомогательная функция для рекурсивного преобразования данных.
        """
        data = {}
        for key, value in model_dict.items():
            data[f"{prefix}[{key}]"] = value
        return data

    return _pydantic_to_nested_dict(model.model_dump(exclude_none=True, by_alias=True), prefix)
