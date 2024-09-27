from typing import Any, Type

from pydantic import BaseModel, RootModel


def pydantic_to_nested_dict(model: BaseModel, prefix: str = "") -> dict[str, str]:
    """
    Преобразует поля модели Pydantic в словарь с вложенными ключами вида "fieldA[fieldB]=valueB".

    :param model: pydantic модель
    :param prefix: строка префикса для fieldA
    :return:
    """

    result = {}

    def _pydantic_to_nested_dict(data: Any, prefix_: str = ""):
        """
        Вспомогательная функция для рекурсивного преобразования данных.
        """

        if isinstance(data, dict):
            for field_name, field_value in data.items():
                _pydantic_to_nested_dict(field_value, f"{prefix_}[{field_name}]")
        elif isinstance(data, list):
            for index, item in enumerate(data):
                _pydantic_to_nested_dict(item, f"{prefix_}[{index}]")
        else:
            result[prefix_] = data

    _pydantic_to_nested_dict(
        model.model_dump(exclude_unset=True, by_alias=True), prefix
    )
    return result


def pydantic_list_dumps_to_json(obj_list: list[BaseModel], obj_type: Type) -> str:
    """
    Преобразует массив объектов Pydantic в JSON строку

    :param obj_list: список объектов Pydantic
    :param obj_type: базовый тип списка
    :return:
    """
    obj_root_model = RootModel[list[obj_type]]
    return obj_root_model(obj_list).model_dump_json(exclude_unset=True, by_alias=True)
