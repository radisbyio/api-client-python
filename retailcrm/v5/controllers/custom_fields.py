from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.enums import CustomFieldEntityTypes
from retailcrm.v5.schemas.custom_fields import (
    CustomDictionariesResponse,
    CustomDictionaryFilter,
    CustomFieldCreateResponse,
    CustomFieldDictionaryCreateResponse,
    CustomFieldDictionaryEditResponse,
    CustomFieldDictionaryRetrieveResponse,
    CustomFieldFilter,
    CustomFieldRetrieveResponse,
    CustomFieldsResponse,
    SerializedCustomDictionary,
    SerializedCustomFieldApiDocModel,
)
from retailcrm.v5.utils import pydantic_to_nested_dict


class CustomFieldsController:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def filter(
        self, filter_data: CustomFieldFilter, limit: int = 20, page: int = 1
    ) -> CustomFieldsResponse:
        """
        **Получение списка пользовательских полей, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-custom-fields
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_data: Фильтр
        :return: Response
        """
        response = await self._client.get(
            endpoint="/custom-fields",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = CustomFieldsResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def dictionaries_filter(
        self, filter_data: CustomDictionaryFilter, limit: int = 20, page: int = 1
    ) -> CustomDictionariesResponse:
        """
        **Получение списка справочников, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-custom-fields-dictionaries
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :param filter_data: Фильтр
        :return: Response
        """
        response = await self._client.get(
            endpoint="/custom-fields/dictionaries",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = CustomDictionariesResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def dictionary_create(
        self, custom_dictionary: SerializedCustomDictionary
    ) -> CustomFieldDictionaryCreateResponse:
        """
        Получение списка справочников, удовлетворяющих заданному фильтру

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-custom-fields-dictionaries
        :param custom_dictionary:
        """
        response = await self._client.post(
            f"/custom-fields/dictionaries/create",
            data={
                "customField": custom_dictionary.model_dump_json(
                    exclude_none=True, by_alias=True
                )
            },
        )

        response_obj = CustomFieldDictionaryCreateResponse.model_validate_json(
            response.body
        )
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def dictionary_get(self, code: str) -> CustomFieldDictionaryRetrieveResponse:
        """
        Получение информации о справочнике

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-custom-fields-dictionaries-code
        :param code: Символьный код
        """
        response = await self._client.get(f"/custom-fields/dictionaries/{code}")

        response_obj = CustomFieldDictionaryRetrieveResponse.model_validate_json(
            response.body
        )
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def dictionary_edit(
        self, code: str, custom_dictionary: SerializedCustomDictionary
    ) -> CustomFieldDictionaryEditResponse:
        """
        Редактирование справочика

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-custom-fields-dictionaries-code-edit
        :param code: Символьный код
        :param custom_dictionary:
        """
        response = await self._client.post(
            f"/custom-fields/dictionaries/{code}/edit",
            data={
                "customDictionary": custom_dictionary.model_dump_json(
                    exclude_none=True, by_alias=True
                )
            },
        )

        response_obj = CustomFieldDictionaryEditResponse.model_validate_json(
            response.body
        )
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def create(
        self, entity: CustomFieldEntityTypes | str, custom_field: SerializedCustomFieldApiDocModel
    ) -> CustomFieldCreateResponse:
        """
        Создание пользовательского поля

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-custom-fields-entity-create
        :param entity:
        :param custom_field:
        """
        response = await self._client.post(
            f"/custom-fields/{entity}/create",
            data={
                "customField": custom_field.model_dump_json(
                    exclude_none=True, by_alias=True
                )
            },
        )

        response_obj = CustomFieldCreateResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def get(self, entity: CustomFieldEntityTypes | str, code: str) -> CustomFieldRetrieveResponse:
        """
        Получение информации о пользовательском поле

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-custom-fields-entity-code
        :param entity: Символьный код
        :param code: Поле для таблицы
        """
        response = await self._client.get(f"/custom-fields/{entity}/{code}")

        response_obj = CustomFieldRetrieveResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def edit(
        self,
        entity: CustomFieldEntityTypes | str,
        code: str,
        custom_field: SerializedCustomFieldApiDocModel,
    ) -> CustomFieldRetrieveResponse:
        """
        Редактирование пользовательского поля

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-custom-fields-entity-code-edit
        :param entity: Символьный код
        :param code: Поле для таблицы
        """
        response = await self._client.post(
            f"/custom-fields/{entity}/{code}/edit",
            data={
                "customField": custom_field.model_dump_json(
                    exclude_none=True, by_alias=True
                )
            },
        )

        response_obj = CustomFieldRetrieveResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj
