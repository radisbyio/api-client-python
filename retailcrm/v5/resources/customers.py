from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.base import SuccessResponse, IdTypesLiteral
from retailcrm.v5.schemas.entities.customers import SerializedCustomerReference, SerializedCustomer, \
    SerializedCustomerNote, SerializedSubscription
from retailcrm.v5.schemas.filters.customers import CustomerFilter, CustomerHistoryFilterV4Type, CustomerNoteFilter
from retailcrm.v5.schemas.requests.customers import CustomersFilterRequest, CustomersCombineRequest, \
    CustomersCreateRequest, CustomersFixExternalIdsRequest, CustomersHistoryRequest, CustomersNotesFilterRequest, \
    CustomerNoteCreateRequest, CustomersUploadRequest, CustomerGetRequest, CustomerEditRequest, \
    CustomerSubscriptionsRequest
from retailcrm.v5.schemas.responses.customers import CustomersResponse, CustomersCombineResponse, \
    CustomerCreateResponse, CustomersFixExternalIdsResponse, CustomersHistoryResponse, CustomersNotesResponse, \
    CustomerNoteCreateResponse, CustomersUploadResponse, CustomerGetResponse, CustomerEditResponse, \
    CustomerSubscriptionsResponse
from retailcrm.v5.schemas.shared.fix_external_row import FixExternalRow


class CustomersApiResource(ApiResource):
    async def filter(
        self, filter_obj: CustomerFilter | None = None, limit: int = 20, page: int = 1
    ) -> CustomersResponse:
        """
        **Получение списка клиентов, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers

        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: CustomersResponse
        """
        request = CustomersFilterRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint="/customers",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomersResponse)

    async def combine(
        self, result_customer: SerializedCustomerReference, customers: list[SerializedCustomerReference]
    ) -> CustomersCombineResponse:
        """
        **Объединение клиентов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-combine
        :param result_customer: Клиент, в которого произойдет объединение.
        :param customers: Список клиентов, которые будут объединены.
        :return: CustomersCombineResponse
        """
        request = CustomersCombineRequest(resultCustomer=result_customer, customers=customers)
        response = await self._client.post(
            endpoint="/customers/combine",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomersCombineResponse)

    async def create(self, customer: SerializedCustomer, site: str | None = None) -> CustomerCreateResponse:
        """
        **Создание клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-create
        :param customer: Объект клиента.
        :param site: Символьный код магазина.
        :return: CustomerCreateResponse
        """
        request = CustomersCreateRequest(customer=customer, site=site)
        response = await self._client.post(
            endpoint="/customers/create",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCreateResponse)

    async def fix_external_ids(self, customers: list[FixExternalRow]) -> CustomersFixExternalIdsResponse:
        """
        **Массовая запись внешних ID клиентов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-fix-external-ids
        :param customers: Идентификаторы загруженных объектов.
        :return: CustomersFixExternalIdsResponse
        """
        request = CustomersFixExternalIdsRequest(customers=customers)
        response = await self._client.post(
            endpoint="/customers/fix-external-ids",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomersFixExternalIdsResponse)

    async def history(
        self, filter_obj: CustomerHistoryFilterV4Type | None = None, limit: int = 20, page: int = 1
    ) -> CustomersHistoryResponse:
        """
        **Получение истории изменения клиентов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-history
        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: CustomersHistoryResponse
        """
        request = CustomersHistoryRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint="/customers/history",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomersHistoryResponse)

    async def notes(
        self, filter_obj: CustomerNoteFilter | None = None, limit: int = 20, page: int = 1
    ) -> CustomersNotesResponse:
        """
        **Получение заметок**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-notes
        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: CustomersNotesResponse
        """
        request = CustomersNotesFilterRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint="/customers/notes",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomersNotesResponse)

    async def notes_create(self, note: SerializedCustomerNote, site: str | None = None) -> CustomerNoteCreateResponse:
        """
        **Создание заметки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-notes-create
        :param note: Объект заметки.
        :param site: Символьный код магазина.
        :return: CustomerNoteCreateResponse
        """
        request = CustomerNoteCreateRequest(note=note, site=site)
        response = await self._client.post(
            endpoint="/customers/notes/create",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerNoteCreateResponse)

    async def notes_delete(self, note_id: int) -> SuccessResponse:
        """
        **Удаление заметки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-notes-id-delete
        :param note_id: ID заметки.
        :return: SuccessResponse
        """
        response = await self._client.post(
            endpoint=f"/customers/notes/{note_id}/delete",
        )
        return self._process_response(response, SuccessResponse)

    async def upload(self, customers: list[SerializedCustomer], site: str) -> CustomersUploadResponse:
        """
        **Пакетная загрузка клиентов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-upload
        :param customers: Список клиентов.
        :param site: Символьный код магазина.
        :return: CustomersUploadResponse
        """
        if len(customers) > 50:
            raise ValueError("Too many customers, only 50 are allowed")
        request = CustomersUploadRequest(customers=customers, site=site)
        response = await self._client.post(
            endpoint="/customers/upload",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomersUploadResponse)

    async def get(
        self, customer_id: str, by: IdTypesLiteral = "externalId", site: str | None = None
    ) -> CustomerGetResponse:
        """
        **Получение информации о клиенте**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-externalId
        :param customer_id: ID клиента (внутренний или внешний).
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :return: CustomerGetResponse
        """
        request = CustomerGetRequest(by=by, site=site)
        response = await self._client.get(
            endpoint=f"/customers/{customer_id}",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerGetResponse)

    async def edit(
        self, customer_id: str, customer: SerializedCustomer, by: IdTypesLiteral = "externalId", site: str | None = None
    ) -> CustomerEditResponse:
        """
        **Редактирование клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-externalId-edit
        :param customer_id: ID клиента (внутренний или внешний).
        :param customer: Объект клиента с изменениями.
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :return: CustomerEditResponse
        """
        request = CustomerEditRequest(customer=customer, by=by, site=site)
        response = await self._client.post(
            endpoint=f"/customers/{customer_id}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerEditResponse)

    async def subscriptions(
        self, customer_id: str, subscriptions: list[SerializedSubscription], by: IdTypesLiteral = "externalId", site: str | None = None
    ) -> CustomerSubscriptionsResponse:
        """
        **Подписка/отписка клиента на рассылки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-externalId-subscriptions
        :param customer_id: ID клиента (внутренний или внешний).
        :param subscriptions: Список подписок клиента.
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :return: CustomerSubscriptionsResponse
        """
        request = CustomerSubscriptionsRequest(subscriptions=subscriptions, by=by, site=site)
        response = await self._client.post(
            endpoint=f"/customers/{customer_id}/subscriptions",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerSubscriptionsResponse)