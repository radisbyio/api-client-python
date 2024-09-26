from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.enums import IdTypes
from retailcrm.v5.schemas.base import RetailCrmResponse
from retailcrm.v5.schemas.customers import (
    CustomerFilterData,
    CustomerHistoryFilterV4Type,
    CustomerNoteFilter,
    ResponseCustomerCreate,
    ResponseCustomerEdit,
    ResponseCustomerNotesCreate,
    ResponseCustomerNotesDelete,
    ResponseCustomerNotesFilter,
    ResponseCustomerRetrieve,
    ResponseCustomersCombine,
    ResponseCustomersFilter,
    ResponseCustomersFixExternalIds,
    SerializedCustomer,
    SerializedCustomerNote,
    SerializedCustomerReference,
    SerializedSubscription,
)
from retailcrm.v5.utils import pydantic_to_nested_dict


class CustomersController:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def filter(
        self, filter_data: CustomerFilterData, limit: int = 20, page: int = 1
    ) -> ResponseCustomersFilter:
        """
        Получение списка клиентов, удовлетворяющих заданному фильтру

        Результат возвращается постранично. В поле pagination содержится информация о постраничной разбивке.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers
        :param filter_data: Фильтр
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :return: Response
        """
        response = await self._client.get(
            endpoint="/customers",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = ResponseCustomersFilter.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def get(
        self,
        customer_id: str | int,
        site: str = None,
        by: IdTypes = IdTypes.EXTERNAL_ID,
    ) -> ResponseCustomerRetrieve:
        """
        Получение информации о клиенте

        Метод возвращает полную информацию по клиенту.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers
        :param customer_id: Идентификатор клиента
        :param site: Код магазина
        :param by: Тип идентификатора (id или externalId)
        :return: Response
        """
        params = {}
        if site is not None:
            params["site"] = site
        if by is not None:
            params["by"] = by.value

        response = await self._client.get(
            endpoint=f"/customers/{customer_id}", params=params
        )

        response_obj = ResponseCustomerRetrieve.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def create(
        self, customer: SerializedCustomer, site: str
    ) -> ResponseCustomerCreate:
        """
        Создание клиента

        Метод создает клиента и возвращает внутренний ID созданного клиента.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-create
        :param customer: Данные клиента для создания
        :param site: Символьный код магазина
        :return: Response
        """
        response = await self._client.post(
            endpoint="/customers/create",
            params={"site": site},
            data={
                "customer": customer.model_dump_json(exclude_unset=True, by_alias=True)
            },
        )

        response_obj = ResponseCustomerCreate.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(
                response.status_code, response_obj.errorMsg, response_obj.errors
            )
        return response_obj

    async def edit(
        self,
        customer_id: str | int,
        customer: SerializedCustomer,
        site: str = None,
        by: IdTypes = IdTypes.EXTERNAL_ID,
    ) -> ResponseCustomerEdit:
        """
        Редактирование клиента

        Метод редактирует клиента и возвращает внутренний ID измененного клиента.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-externalId-edit
        :param customer_id: Идентификатор клиента
        :param customer: Данные клиента для редактирования
        :param site: Символьный код магазина
        :param by: Тип идентификатора (id или externalId)
        :return: ResponseCustomerEdit
        """
        params = {}
        if site is not None:
            params["site"] = site
        if by is not None:
            params["by"] = by.value

        response = await self._client.post(
            endpoint=f"/customers/{customer_id}/edit",
            params=params,
            data={
                "customer": customer.model_dump_json(exclude_none=True, by_alias=True)
            },
        )

        response_obj = ResponseCustomerEdit.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def combine(
        self,
        result_customer: SerializedCustomerReference,
        customers: list[SerializedCustomerReference],
    ) -> ResponseCustomersCombine:
        """
        Объединение клиентов

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-combine
        :param result_customer: Клиент, в которого произойдет объединение
        :param customers: Массив клиентов для объединения
        :return: ResponseCustomersCombine
        """
        response = await self._client.post(
            "/customers/combine",
            data={
                "customers": [
                    customer.model_dump(exclude_unset=True, by_alias=True)
                    for customer in customers
                ],
                "resultCustomer": result_customer.model_dump(
                    exclude_unset=True, by_alias=True
                ),
            },
        )

        response_obj = ResponseCustomersCombine.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def fix_external_ids(
        self, customers: list[SerializedCustomerReference]
    ) -> ResponseCustomersFixExternalIds:
        """
        Массовая запись внешних ID клиентов

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-fix-external-ids
        :param customers: Массив клиентов с внешними ID
        :return: ResponseCustomersFixExternalIds
        """
        response = await self._client.post(
            "/customers/fix-external-ids",
            data={
                "customers": [
                    customer.model_dump(exclude_unset=True, by_alias=True)
                    for customer in customers
                ]
            },
        )

        response_obj = ResponseCustomersFixExternalIds.model_validate_json(
            response.body
        )

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def history(
        self, filter_obj: CustomerHistoryFilterV4Type, limit: int = 20, page: int = 1
    ) -> RetailCrmResponse:
        """
        Получение истории изменения клиентов

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-history
        :param filter_obj: Фильтр для истории
        :param limit: Количество элементов на странице
        :param page: Номер страницы
        :return: RetailCrmResponse
        """
        response = await self._client.get(
            "/customers/history",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_obj, "filter"),
            },
        )

        response_obj = RetailCrmResponse.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def subscriptions(
        self,
        customer_id: str | int,
        subscriptions: list[SerializedSubscription],
        site: str = None,
        by: IdTypes = IdTypes.EXTERNAL_ID,
    ) -> RetailCrmResponse:
        """
        Подписка/отписка клиента на рассылки

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-externalId-subscriptions
        :param customer_id: ID клиента
        :param subscriptions: Массив подписок
        :param site: Символьный код магазина
        :param by: Тип идентификатора
        :return: RetailCrmResponse
        """
        params = {}
        if site is not None:
            params["site"] = site
        if by is not None:
            params["by"] = by.value

        response = await self._client.post(
            f"/customers/{customer_id}/subscriptions",
            params=params,
            data={
                "subscriptions": [
                    subscription.model_dump(exclude_unset=True, by_alias=True)
                    for subscription in subscriptions
                ]
            },
        )

        response_obj = RetailCrmResponse.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def notes_filter(
        self, filter_data: CustomerNoteFilter, limit: int = 20, page: int = 1
    ) -> ResponseCustomerNotesFilter:
        """
        Получение заметок

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-notes
        :param filter_data: Фильтр
        :param limit: Количество элементов на странице
        :param page: Номер страницы
        :return: CustomerNotesResponse
        """
        response = await self._client.get(
            "/customers/notes",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_data, "filter"),
            },
        )

        response_obj = ResponseCustomerNotesFilter.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def note_create(
        self, note: SerializedCustomerNote, site: str
    ) -> ResponseCustomerNotesCreate:
        """
        Создание заметки

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-notes-create
        :param note: Данные заметки
        :param site: Символьный код магазина
        :return: ResponseCustomerNotesCreate
        """
        response = await self._client.post(
            "/customers/notes/create",
            params={"site": site},
            data={"note": note.model_dump_json(exclude_none=True, by_alias=True)},
        )

        response_obj = ResponseCustomerNotesCreate.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj

    async def note_delete(self, note_id: int) -> ResponseCustomerNotesDelete:
        """
        Удаление заметки

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-notes-id-delete
        :param note_id: ID заметки
        :return: CustomerNotesDeleteResponse
        """
        response = await self._client.post(f"/customers/notes/{note_id}/delete")

        response_obj = ResponseCustomerNotesDelete.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)

        return response_obj
