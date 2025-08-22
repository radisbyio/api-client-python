from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.entities.custom_fields import SerializedCustomFieldApiDocModel, SerializedCustomDictionary
from retailcrm.v5.schemas.filters.custom_fields import CustomDictionaryFilter, CustomFieldFilter
from retailcrm.v5.schemas.requests.custom_fields import CustomFieldEditRequest, CustomFieldCreateRequest, \
    CustomDictionaryEditRequest, CustomDictionaryCreateRequest, CustomDictionariesFilterRequest, \
    CustomFieldsFilterRequest
from retailcrm.v5.schemas.responses.custom_fields import CustomFieldEditResponse, CustomFieldGetResponse, \
    CustomFieldCreateResponse, CustomDictionaryEditResponse, CustomDictionaryGetResponse, \
    CustomDictionaryCreateResponse, CustomDictionariesFilterResponse, CustomFieldsFilterResponse


class CustomFieldsApiResource(ApiResource):
    async def filter(
        self, filter_obj: CustomFieldFilter | None = None, limit: int = 20, page: int = 1
    ) -> CustomFieldsFilterResponse:
        """
        **Получение списка пользовательских полей, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-custom-fields

        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: CustomFieldsFilterResponse
        """
        request = CustomFieldsFilterRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint="/custom-fields",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomFieldsFilterResponse)

    async def dictionaries_filter(
        self, filter_obj: CustomDictionaryFilter | None = None, limit: int = 20, page: int = 1
    ) -> CustomDictionariesFilterResponse:
        """
        **Получение списка справочников, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-custom-fields-dictionaries

        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: CustomDictionariesFilterResponse
        """
        request = CustomDictionariesFilterRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint="/custom-fields/dictionaries",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomDictionariesFilterResponse)

    async def dictionaries_create(self, custom_dictionary: SerializedCustomDictionary) -> CustomDictionaryCreateResponse:
        """
        **Создание справочника**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-custom-fields-dictionaries-create
        :param custom_dictionary: Данные справочника.
        :return: CustomDictionaryCreateResponse
        """
        request = CustomDictionaryCreateRequest(customDictionary=custom_dictionary)
        response = await self._client.post(
            endpoint="/custom-fields/dictionaries/create",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomDictionaryCreateResponse)

    async def dictionaries_get(self, code: str) -> CustomDictionaryGetResponse:
        """
        **Получение информации о справочнике**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-custom-fields-dictionaries-code
        :param code: Символьный код справочника.
        :return: CustomDictionaryGetResponse
        """
        response = await self._client.get(
            endpoint=f"/custom-fields/dictionaries/{code}",
        )
        return self._process_response(response, CustomDictionaryGetResponse)

    async def dictionaries_edit(self, code: str, custom_dictionary: SerializedCustomDictionary) -> CustomDictionaryEditResponse:
        """
        **Редактирование справочника**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-custom-fields-dictionaries-code-edit
        :param code: Символьный код справочника.
        :param custom_dictionary: Данные справочника.
        :return: CustomDictionaryEditResponse
        """
        request = CustomDictionaryEditRequest(customDictionary=custom_dictionary)
        response = await self._client.post(
            endpoint=f"/custom-fields/dictionaries/{code}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomDictionaryEditResponse)

    async def create(self, entity: str, custom_field: SerializedCustomFieldApiDocModel) -> CustomFieldCreateResponse:
        """
        **Создание пользовательского поля**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-custom-fields-entity-create
        :param entity: Поле для таблицы (например, 'order', 'customer').
        :param custom_field: Данные пользовательского поля.
        :return: CustomFieldCreateResponse
        """
        request = CustomFieldCreateRequest(customField=custom_field)
        response = await self._client.post(
            endpoint=f"/custom-fields/{entity}/create",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomFieldCreateResponse)

    async def get(self, entity: str, code: str) -> CustomFieldGetResponse:
        """
        **Получение информации о пользовательском поле**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-custom-fields-entity-code
        :param entity: Поле для таблицы.
        :param code: Символьный код пользовательского поля.
        :return: CustomFieldGetResponse
        """
        response = await self._client.get(
            endpoint=f"/custom-fields/{entity}/{code}",
        )
        return self._process_response(response, CustomFieldGetResponse)

    async def edit(self, entity: str, code: str, custom_field: SerializedCustomFieldApiDocModel) -> CustomFieldEditResponse:
        """
        **Редактирование пользовательского поля**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-custom-fields-entity-code-edit
        :param entity: Поле для таблицы.
        :param code: Символьный код пользовательского поля.
        :param custom_field: Данные пользовательского поля.
        :return: CustomFieldEditResponse
        """
        request = CustomFieldEditRequest(customField=custom_field)
        response = await self._client.post(
            endpoint=f"/custom-fields/{entity}/{code}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomFieldEditResponse)