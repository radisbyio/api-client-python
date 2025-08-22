from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.base import SuccessResponse, IdTypesLiteral
from retailcrm.v5.schemas.entities.corporate_customers import SerializedCustomerCorporate, SerializedCustomerAddress, \
    SerializedCompany, SerializedCustomerContact
from retailcrm.v5.schemas.entities.customers import SerializedCustomerReference, SerializedCustomerNote
from retailcrm.v5.schemas.filters.customers_corporate import CustomerCorporateApiFilterData, \
    CustomerHistoryFilterV4Type, CustomerNoteFilter, CustomerAddressFilter, CompanyFilter, CustomerContactFilter
from retailcrm.v5.schemas.requests.customers_corporate import CustomerCorporateFilterRequest, \
    CustomerCorporateFixExternalIdsRequest, CustomerCorporateCreateRequest, CustomerCorporateCombineRequest, \
    CustomerCorporateHistoryRequest, CustomerCorporateNotesFilterRequest, CustomerCorporateNoteCreateRequest, \
    CustomerCorporateUploadRequest, CustomerCorporateGetRequest, CustomerCorporateAddressesRequest, \
    CustomerCorporateAddressCreateRequest, CustomerCorporateAddressEditRequest, CustomerCorporateCompaniesRequest, \
    CustomerCorporateCompanyCreateRequest, CustomerCorporateCompanyEditRequest, CustomerCorporateContactsRequest, \
    CustomerCorporateContactEditRequest, CustomerCorporateEditRequest, CustomerCorporateContactCreateRequest
from retailcrm.v5.schemas.responses.customers_corporate import CustomerCorporateResponse, \
    CustomerCorporateCombineResponse, CustomerCorporateCreateResponse, CustomerCorporateFixExternalIdsResponse, \
    CustomerCorporateHistoryResponse, CustomerCorporateNotesResponse, CustomerCorporateNoteCreateResponse, \
    CustomerCorporateUploadResponse, CustomerCorporateGetResponse, CustomerCorporateAddressesResponse, \
    CustomerCorporateAddressCreateResponse, CustomerCorporateAddressEditResponse, CustomerCorporateCompaniesResponse, \
    CustomerCorporateCompanyCreateResponse, CustomerCorporateCompanyEditResponse, CustomerCorporateContactsResponse, \
    CustomerCorporateContactCreateResponse, CustomerCorporateContactEditResponse, CustomerCorporateEditResponse
from retailcrm.v5.schemas.shared.fix_external_row import FixExternalRow


class CustomersCorporateApiResource(ApiResource):
    async def filter_obj(
        self, filter_obj: CustomerCorporateApiFilterData | None = None, limit: int = 20, page: int = 1
    ) -> CustomerCorporateResponse:
        """
        **Получение списка корпоративных клиентов, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate
        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: CustomerCorporateResponse
        """
        request = CustomerCorporateFilterRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint="/customers-corporate",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateResponse)

    async def combine(
        self, result_customer: SerializedCustomerReference, customers: list[SerializedCustomerReference]
    ) -> CustomerCorporateCombineResponse:
        """
        **Объединение корпоративных клиентов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-combine
        :param result_customer: Клиент, в которого произойдет объединение.
        :param customers: Список клиентов, которые будут объединены.
        :return: CustomerCorporateCombineResponse
        """
        request = CustomerCorporateCombineRequest(resultCustomer=result_customer, customers=customers)
        response = await self._client.post(
            endpoint="/customers-corporate/combine",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateCombineResponse)

    async def create(self, customer_corporate: SerializedCustomerCorporate) -> CustomerCorporateCreateResponse:
        """
        **Создание корпоративного клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-create
        :param customer_corporate: Объект корпоративного клиента.
        :return: CustomerCorporateCreateResponse
        """
        request = CustomerCorporateCreateRequest(customerCorporate=customer_corporate)
        response = await self._client.post(
            endpoint="/customers-corporate/create",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateCreateResponse)

    async def fix_external_ids(self, customers_corporate: list[FixExternalRow]) -> CustomerCorporateFixExternalIdsResponse:
        """
        **Массовая запись внешних ID корпоративных клиентов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-fix-external-ids
        :param customers_corporate: Идентификаторы загруженных объектов.
        :return: CustomerCorporateFixExternalIdsResponse
        """
        request = CustomerCorporateFixExternalIdsRequest(customersCorporate=customers_corporate)
        response = await self._client.post(
            endpoint="/customers-corporate/fix-external-ids",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateFixExternalIdsResponse)

    async def history(
        self, filter_obj: CustomerHistoryFilterV4Type | None = None, limit: int = 20, page: int = 1
    ) -> CustomerCorporateHistoryResponse:
        """
        **Получение истории изменения корпоративных клиентов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate-history
        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: CustomerCorporateHistoryResponse
        """
        request = CustomerCorporateHistoryRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint="/customers-corporate/history",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateHistoryResponse)

    async def notes(
        self, filter_obj: CustomerNoteFilter | None = None, limit: int = 20, page: int = 1
    ) -> CustomerCorporateNotesResponse:
        """
        **Получение заметок**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate-notes
        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: CustomerCorporateNotesResponse
        """
        request = CustomerCorporateNotesFilterRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint="/customers-corporate/notes",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateNotesResponse)

    async def notes_create(self, note: SerializedCustomerNote, site: str | None = None) -> CustomerCorporateNoteCreateResponse:
        """
        **Создание заметки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-notes-create
        :param note: Объект заметки.
        :param site: Символьный код магазина.
        :return: CustomerCorporateNoteCreateResponse
        """
        request = CustomerCorporateNoteCreateRequest(note=note, site=site)
        response = await self._client.post(
            endpoint="/customers-corporate/notes/create",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateNoteCreateResponse)

    async def notes_delete(self, note_id: int) -> SuccessResponse:
        """
        **Удаление заметки**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-notes-id-delete
        :param note_id: ID заметки.
        :return: SuccessResponse
        """
        response = await self._client.post(
            endpoint=f"/customers-corporate/notes/{note_id}/delete",
        )
        return self._process_response(response, SuccessResponse)

    async def upload(self, customers_corporate: list[SerializedCustomerCorporate], site: str) -> CustomerCorporateUploadResponse:
        """
        **Пакетная загрузка корпоративных клиентов**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-upload
        :param customers_corporate: Список корпоративных клиентов.
        :param site: Символьный код магазина.
        :return: CustomerCorporateUploadResponse
        """
        if len(customers_corporate) > 50:
            raise ValueError("Too many customers, only 50 are allowed")
        request = CustomerCorporateUploadRequest(customersCorporate=customers_corporate, site=site)
        response = await self._client.post(
            endpoint="/customers-corporate/upload",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateUploadResponse)

    async def get(
        self, customer_corporate_id: str, by: IdTypesLiteral = "externalId", site: str | None = None
    ) -> CustomerCorporateGetResponse:
        """
        **Получение информации о корпоративном клиенте**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate-externalId
        :param customer_corporate_id: ID корпоративного клиента (внутренний или внешний).
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :return: CustomerCorporateGetResponse
        """
        request = CustomerCorporateGetRequest(by=by, site=site)
        response = await self._client.get(
            endpoint=f"/customers-corporate/{customer_corporate_id}",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateGetResponse)

    async def addresses(
        self, customer_corporate_id: str, by: IdTypesLiteral = "externalId", site: str | None = None,
        filter_obj: CustomerAddressFilter | None = None, limit: int = 20, page: int = 1
    ) -> CustomerCorporateAddressesResponse:
        """
        **Список адресов корпоративного клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate-externalId-addresses
        :param customer_corporate_id: ID корпоративного клиента.
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: CustomerCorporateAddressesResponse
        """
        request = CustomerCorporateAddressesRequest(by=by, site=site, filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint=f"/customers-corporate/{customer_corporate_id}/addresses",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateAddressesResponse)

    async def addresses_create(
        self, customer_corporate_id: str, address: SerializedCustomerAddress, by: IdTypesLiteral = "externalId", site: str | None = None
    ) -> CustomerCorporateAddressCreateResponse:
        """
        **Создание адреса для корпоративного клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-externalId-addresses-create
        :param customer_corporate_id: ID корпоративного клиента.
        :param address: Объект адреса.
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :return: CustomerCorporateAddressCreateResponse
        """
        request = CustomerCorporateAddressCreateRequest(by=by, site=site, address=address)
        response = await self._client.post(
            endpoint=f"/customers-corporate/{customer_corporate_id}/addresses/create",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateAddressCreateResponse)

    async def addresses_edit(
        self, customer_corporate_id: str, entity_external_id: str, address: SerializedCustomerAddress,
        by: IdTypesLiteral = "externalId", site: str | None = None, entity_by: IdTypesLiteral = "externalId"
    ) -> CustomerCorporateAddressEditResponse:
        """
        **Редактирование адреса корпоративного клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-externalId-addresses-entityExternalId-edit
        :param customer_corporate_id: ID корпоративного клиента.
        :param entity_external_id: ID адреса (внутренний или внешний).
        :param address: Объект адреса.
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :param entity_by: Тип ID адреса (id или externalId).
        :return: CustomerCorporateAddressEditResponse
        """
        request = CustomerCorporateAddressEditRequest(by=by, site=site, entityBy=entity_by, address=address)
        response = await self._client.post(
            endpoint=f"/customers-corporate/{customer_corporate_id}/addresses/{entity_external_id}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateAddressEditResponse)

    async def companies(
        self, customer_corporate_id: str, by: IdTypesLiteral = "externalId", site: str | None = None,
        filter_obj: CompanyFilter | None = None, limit: int = 20, page: int = 1
    ) -> CustomerCorporateCompaniesResponse:
        """
        **Список компаний корпоративного клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate-externalId-companies
        :param customer_corporate_id: ID корпоративного клиента.
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: CustomerCorporateCompaniesResponse
        """
        request = CustomerCorporateCompaniesRequest(by=by, site=site, filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint=f"/customers-corporate/{customer_corporate_id}/companies",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateCompaniesResponse)

    async def companies_create(
        self, customer_corporate_id: str, company: SerializedCompany, by: IdTypesLiteral = "externalId", site: str | None = None
    ) -> CustomerCorporateCompanyCreateResponse:
        """
        **Создание компании для корпоративного клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-externalId-companies-create
        :param customer_corporate_id: ID корпоративного клиента.
        :param company: Объект компании.
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :return: CustomerCorporateCompanyCreateResponse
        """
        request = CustomerCorporateCompanyCreateRequest(by=by, site=site, company=company)
        response = await self._client.post(
            endpoint=f"/customers-corporate/{customer_corporate_id}/companies/create",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateCompanyCreateResponse)

    async def companies_edit(
        self, customer_corporate_id: str, entity_external_id: str, company: SerializedCompany,
        by: IdTypesLiteral = "externalId", site: str | None = None, entity_by: IdTypesLiteral = "externalId"
    ) -> CustomerCorporateCompanyEditResponse:
        """
        **Редактирование компании корпоративного клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-externalId-companies-entityExternalId-edit
        :param customer_corporate_id: ID корпоративного клиента.
        :param entity_external_id: ID компании (внутренний или внешний).
        :param company: Объект компании.
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :param entity_by: Тип ID компании (id или externalId).
        :return: CustomerCorporateCompanyEditResponse
        """
        request = CustomerCorporateCompanyEditRequest(by=by, site=site, entityBy=entity_by, company=company)
        response = await self._client.post(
            endpoint=f"/customers-corporate/{customer_corporate_id}/companies/{entity_external_id}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateCompanyEditResponse)

    async def contacts(
        self, customer_corporate_id: str, by: IdTypesLiteral = "externalId", site: str | None = None,
        filter_obj: CustomerContactFilter | None = None, limit: int = 20, page: int = 1
    ) -> CustomerCorporateContactsResponse:
        """
        **Список контактных лиц корпоративного клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate-externalId-contacts
        :param customer_corporate_id: ID корпоративного клиента.
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: CustomerCorporateContactsResponse
        """
        request = CustomerCorporateContactsRequest(by=by, site=site, filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint=f"/customers-corporate/{customer_corporate_id}/contacts",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateContactsResponse)

    async def contacts_create(
        self, customer_corporate_id: str, contact: SerializedCustomerContact, by: IdTypesLiteral = "externalId", site: str | None = None
    ) -> CustomerCorporateContactCreateResponse:
        """
        **Создание связи корпоративного клиента с контактным лицом**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-externalId-contacts-create
        :param customer_corporate_id: ID корпоративного клиента.
        :param contact: Объект контактного лица.
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :return: CustomerCorporateContactCreateResponse
        """
        request = CustomerCorporateContactCreateRequest(by=by, site=site, contact=contact)
        response = await self._client.post(
            endpoint=f"/customers-corporate/{customer_corporate_id}/contacts/create",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateContactCreateResponse)

    async def contacts_edit(
        self, customer_corporate_id: str, entity_external_id: str, contact: SerializedCustomerContact,
        by: IdTypesLiteral = "externalId", site: str | None = None, entity_by: IdTypesLiteral = "externalId"
    ) -> CustomerCorporateContactEditResponse:
        """
        **Редактирование связи корпоративного клиента с контактным лицом**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-externalId-contacts-entityExternalId-edit
        :param customer_corporate_id: ID корпоративного клиента.
        :param entity_external_id: ID контактного лица (внутренний или внешний).
        :param contact: Объект контактного лица.
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :param entity_by: Тип ID контактного лица (id или externalId).
        :return: CustomerCorporateContactEditResponse
        """
        request = CustomerCorporateContactEditRequest(by=by, site=site, entityBy=entity_by, contact=contact)
        response = await self._client.post(
            endpoint=f"/customers-corporate/{customer_corporate_id}/contacts/{entity_external_id}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateContactEditResponse)

    async def edit(
        self, customer_corporate_id: str, customer_corporate: SerializedCustomerCorporate,
        by: IdTypesLiteral = "externalId", site: str | None = None
    ) -> CustomerCorporateEditResponse:
        """
        **Редактирование корпоративного клиента**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-externalId-edit
        :param customer_corporate_id: ID корпоративного клиента (внутренний или внешний).
        :param customer_corporate: Объект корпоративного клиента с изменениями.
        :param by: Тип ID клиента (id или externalId).
        :param site: Символьный код магазина.
        :return: CustomerCorporateEditResponse
        """
        request = CustomerCorporateEditRequest(by=by, site=site, customerCorporate=customer_corporate)
        response = await self._client.post(
            endpoint=f"/customers-corporate/{customer_corporate_id}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, CustomerCorporateEditResponse)