from typing import Any, Type, TypeVar

from pydantic import BaseModel, RootModel

from retailcrm.v5.schemas import BaseRetailCrmScheme


def pydantic_to_nested_dict(model: BaseModel | None, prefix: str = "") -> dict[str, str]:
    """
    Преобразует поля модели Pydantic в словарь с вложенными ключами вида "fieldA[fieldB]=valueB".
    Если на входе объект model имеет значение None, будет возвращён пустой словарь

    :param model: pydantic модель
    :param prefix: строка префикса для fieldA
    :return: dict[str, str]
    """

    result = {}
    if not model:
        return result

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


T = TypeVar("T", bound=BaseRetailCrmScheme)

def pydantic_list_dumps_to_json(obj_list: list[T], obj_type: Type | None = None) -> str:
    """
    Преобразует массив объектов Pydantic в JSON строку

    :param obj_list: список объектов Pydantic
    :param obj_type: базовый тип списка (DEPRECATED)
    :return: str

    TODO: Вырезать использование obj_type
    """
    if not obj_list:
        return "[]"

    obj_root_model = RootModel[list[T]]
    return obj_root_model(obj_list).model_dump_json(exclude_unset=True, by_alias=True)


def validate_crm_url(crm_url: str) -> None:
    """
    Проверяет адрес RetailCRM на валидность
    """
    if not crm_url.startswith("http") or not crm_url.startswith("https"):
        raise ValueError("crm_url must start with http or https")

    if crm_url.endswith("/"):
        raise ValueError("crm_url must not end with /")