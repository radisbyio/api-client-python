from retailcrm.v5.schemas.base import RetailCrmResponse

from retailcrm.exceptions import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.schemas.corporate_customers import (
    CustomerCorporateApiFilterData,
    ResponseCustomersCorporateGetAll,
    SerializedCustomerCorporate,
    ResponseCustomerCorporateCreate,
    GetByIdCustomerCorporateResponse,
    ResponseCustomerCorporateEdit,
    SerializedCompany,
    SerializedCustomerContact, CustomerHistoryFilterV4Type,
)
from retailcrm.v5.schemas.customers import (
ResponseCustomersHistory, ResponseCustomerNotesCreate, ResponseCustomerNotesFilter, ResponseCustomerNotesDelete, SerializedCustomerNote, CustomerNoteFilter,SerializedCustomerReference,
)
from retailcrm.v5.schemas.shared import SerializedCustomerAddress, FixExternalRow

from retailcrm.v5.utils import pydantic_to_nested_dict, pydantic_list_dumps_to_json
from retailcrm.v5.enums import IdTypes


class CorporateCustomersController:
    def __init__(self, client: BaseHttpClient):
        self._client = client

    async def filter(
        self,
        filter_data: CustomerCorporateApiFilterData | None = None,
        limit: int = 20,
        page: int = 1,
    ) -> ResponseCustomersCorporateGetAll:
        """
        Получение списка корпоративных клиентов, удовлетворяющих заданному фильтру.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate
        """
        params = {
            "limit": limit,
            "page": page,
            **pydantic_to_nested_dict(filter_data, "filter"),
        }

        response = await self._client.get("/customers-corporate", params=params)
        response_obj = ResponseCustomersCorporateGetAll.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

        return response_obj


    async def get(self, customer_id: int| str, site: str = None, by: IdTypes | str = IdTypes.EXTERNAL_ID) -> GetByIdCustomerCorporateResponse:
        """
        Получение информации о корпоративном клиенте.
        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate-externalId
        """
        params = {}
        if site is not None:
            params["site"] = site
        if by is not None:
            params["by"] = by

        response = await self._client.get(f"/customers-corporate/{customer_id}", params=params)
        response_obj = GetByIdCustomerCorporateResponse.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

        return response_obj

    async def create(self, customer: SerializedCustomerCorporate, site: str) -> ResponseCustomerCorporateCreate:
        """
        Создание корпоративного клиента.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-create
        """

        response = await self._client.post(
            "/customers-corporate/create",
            params={"site": site},
            data={"customerCorporate": customer.model_dump_json(exclude_unset=True, by_alias=True)},
        )
        response_obj = ResponseCustomerCorporateCreate.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

        return response_obj

    async def edit(
        self, customer_id: str, customer: SerializedCustomerCorporate, site: str = None, by: IdTypes | str = IdTypes.EXTERNAL_ID
    ) -> ResponseCustomerCorporateEdit:
        """
        Редактирование корпоративного клиента.
        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-externalId-edit
        """
        params = {}
        if site is not None:
            params["site"] = site
        if by is not None:
            params["by"] = by

        response = await self._client.post(
            f"/customers-corporate/{customer_id}/edit",
            params=params,
            data={"customerCorporate": customer.model_dump_json(exclude_none=True, by_alias=True)},
        )
        response_obj = ResponseCustomerCorporateEdit.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

        return response_obj

    async def fix_external_ids(self, customers: list[FixExternalRow]) -> RetailCrmResponse:
        """
        Массовая запись внешних ID клиентов.
        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-fix-external-ids
        """
        response = await self._client.post(
            "/customers-corporate/fix-external-ids",
            data={"customersCorporate": pydantic_list_dumps_to_json(customers, FixExternalRow)},
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

        return response_obj


    async def combine(
        self, customers: list[SerializedCustomerReference], result_customer: SerializedCustomerReference
    ) -> RetailCrmResponse:
        """
        Объединение клиентов.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-combine
        """
        response = await self._client.post(
            "/customers-corporate/combine",
            data={
                "customers": pydantic_list_dumps_to_json(customers, SerializedCustomerReference),
                "resultCustomer": result_customer.model_dump(exclude_unset=True),
            },
        )

        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)
        return response_obj


    async def addresses_get(
        self, customer_id: int | str, site: str = None, by: IdTypes | str = IdTypes.EXTERNAL_ID, limit: int = 20, page: int = 1
    ) -> RetailCrmResponse:
       """
       Список адресов корпоративного клиента.
       https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate-id-addresses
       """

       params = {
           "limit": limit,
           "page": page,
           "by": by
       }
       if site is not None:
           params["site"] = site

       response = await self._client.get(
           f"/customers-corporate/{customer_id}/addresses", params=params
       )
       response_obj = RetailCrmResponse.model_validate_json(response.body)

       if response.status_code >= 400:
           raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

       return response_obj


    async def address_create(self, customer_id: int | str, address: SerializedCustomerAddress, site: str = None, by: IdTypes = IdTypes.EXTERNAL_ID) -> RetailCrmResponse:
       """
       Создание адреса.
       https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-id-addresses-create
       """
       params = {
               "by": by.value

           }
       if site is not None:
           params["site"] = site

       response = await self._client.post(
           f"/customers-corporate/{customer_id}/addresses/create", params=params, data={"address": address.model_dump_json(exclude_unset=True, by_alias=True)}
       )
       response_obj = RetailCrmResponse.model_validate_json(response.body)


       if response.status_code >= 400:
           raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

       return response_obj

    async def address_edit(self, customer_id: int | str, address_id: int | str, address: SerializedCustomerAddress, site: str = None, by: IdTypes | str = IdTypes.EXTERNAL_ID, entity_by: IdTypes | str = IdTypes.EXTERNAL_ID) -> RetailCrmResponse:
       """
       Редактирование адреса.
       https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-id-addresses-entityExternalId-edit
       """

       params = {
               "by": by,
               "entityBy": entity_by
           }
       if site is not None:
           params["site"] = site
       response = await self._client.post(
           f"/customers-corporate/{customer_id}/addresses/{address_id}/edit", params=params, data={"address": address.model_dump_json(exclude_unset=True, by_alias=True)}
       )
       response_obj = RetailCrmResponse.model_validate_json(response.body)

       if response.status_code >= 400:
           raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

       return response_obj


    async def companies_get(self, customer_id: int | str, site: str = None, by: IdTypes | str = IdTypes.EXTERNAL_ID, limit: int = 20, page: int = 1) -> RetailCrmResponse:
       """
       Список компаний корпоративного клиента.
       https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate-id-companies
       """

       params = {
           "limit": limit,
           "page": page,
           "by": by
       }
       if site is not None:
           params["site"] = site

       response = await self._client.get(
           f"/customers-corporate/{customer_id}/companies", params=params
       )
       response_obj = RetailCrmResponse.model_validate_json(response.body)

       if response.status_code >= 400:
           raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

       return response_obj

    async def company_create(self, customer_id: int | str, company: SerializedCompany, site: str = None, by: IdTypes | str = IdTypes.EXTERNAL_ID) -> RetailCrmResponse:
       """
       Создание компании.
       https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-id-companies-create
       """
       params = {
               "by": by
           }
       if site is not None:
           params["site"] = site

       response = await self._client.post(
           f"/customers-corporate/{customer_id}/companies/create", params=params, data={"company": company.model_dump_json(exclude_unset=True, by_alias=True)}
       )
       response_obj = RetailCrmResponse.model_validate_json(response.body)


       if response.status_code >= 400:
           raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

       return response_obj


    async def company_edit(self, customer_id: int | str, company_id: int | str, company: SerializedCompany, site: str = None, by: IdTypes | str = IdTypes.EXTERNAL_ID, entity_by: IdTypes | str = IdTypes.EXTERNAL_ID) -> RetailCrmResponse:
       """
       Редактирование компании.
       https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-id-companies-entityExternalId-edit
       """

       params = {
               "by": by,
               "entityBy": entity_by
           }
       if site is not None:
           params["site"] = site
       response = await self._client.post(
           f"/customers-corporate/{customer_id}/companies/{company_id}/edit", params=params, data={"company": company.model_dump_json(exclude_unset=True, by_alias=True)}
       )
       response_obj = RetailCrmResponse.model_validate_json(response.body)

       if response.status_code >= 400:
           raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

       return response_obj


    async def contacts_get(self, customer_id: int | str, site: str = None, by: IdTypes | str = IdTypes.EXTERNAL_ID, limit: int = 20, page: int = 1) -> RetailCrmResponse:
       """
       Список контактных лиц корпоративного клиента.
       https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate-id-contacts
       """

       params = {
           "limit": limit,
           "page": page,
           "by": by

       }
       if site is not None:
           params["site"] = site

       response = await self._client.get(
           f"/customers-corporate/{customer_id}/contacts", params=params
       )
       response_obj = RetailCrmResponse.model_validate_json(response.body)

       if response.status_code >= 400:
           raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

       return response_obj


    async def contact_create(
        self, customer_id: int | str, contact: SerializedCustomerContact, site: str = None, by: IdTypes | str = IdTypes.EXTERNAL_ID
    ) -> RetailCrmResponse:
        """
        Создать контактное лицо.
        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-id-contacts-create
        """
        params = {"by": by}

        if site is not None:
            params["site"] = site
        response = await self._client.post(
            f"/customers-corporate/{customer_id}/contacts/create",
            params=params,
            data={"contact": contact.model_dump_json(exclude_unset=True, by_alias=True)},
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)  # Placeholder response model

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

        return response_obj


    async def contact_edit(
        self,
        customer_id: int | str,
        contact_id: int | str,
        contact: SerializedCustomerContact,
        site: str = None,
        by: IdTypes | str = IdTypes.EXTERNAL_ID,
        entity_by: IdTypes | str = IdTypes.EXTERNAL_ID
    ) -> RetailCrmResponse:

       """
       Редактирование контактного лица.
       https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-id-contacts-entityExternalId-edit
       """

       params = {
               "by": by,
               "entityBy": entity_by
           }
       if site is not None:
           params["site"] = site

       response = await self._client.post(
           f"/customers-corporate/{customer_id}/contacts/{contact_id}/edit", params=params, data={"contact": contact.model_dump_json(exclude_unset=True, by_alias=True)}
       )
       response_obj = RetailCrmResponse.model_validate_json(response.body)  # Placeholder response model

       if response.status_code >= 400:
           raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

       return response_obj

    # ... other methods for notes, upload, history, etc.  (Follow the pattern from other resources)

    async def upload(self, customers: list[SerializedCustomerCorporate], site: str) -> RetailCrmResponse:
        """
        Пакетная загрузка корпоративных клиентов.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-upload
        """
        if len(customers) > 50:
            raise ValueError("Too many customers, only 50 are allowed")

        response = await self._client.post(
            "/customers-corporate/upload",
            data={
                "site": site,
                "customersCorporate": pydantic_list_dumps_to_json(customers, SerializedCustomerCorporate),
            },
        )
        response_obj = RetailCrmResponse.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

        return response_obj

    async def history(
            self, filter_obj: CustomerHistoryFilterV4Type | None = None, limit: int = 20, page: int = 1
    ) -> ResponseCustomersHistory:
        """
        Получение истории изменения корпоративных клиентов.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate-history
        """
        response = await self._client.get(
            "/customers-corporate/history",
            params={
                "limit": limit,
                "page": page,
                **pydantic_to_nested_dict(filter_obj, "filter"),
            },
        )
        response_obj = ResponseCustomersHistory.model_validate_json(response.body)  # Use a more specific model if defined

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

        return response_obj

    async def get_notes(
            self, filter_data: CustomerNoteFilter | None = None, limit: int = 20, page: int = 1
    ) -> ResponseCustomerNotesFilter:
        """
        Получение заметок корпоративного клиента.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-customers-corporate-notes
        """

        response = await self._client.get("/customers-corporate/notes", params={
            "limit": limit,
            "page": page,
            **pydantic_to_nested_dict(filter_data, "filter"),
        })

        response_obj = ResponseCustomerNotesFilter.model_validate_json(response.body)  # Placeholder
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def note_create(
            self, note: SerializedCustomerNote, site: str
    ) -> ResponseCustomerNotesCreate:
        """
        Создание заметки для корпоративного клиента.
        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-notes-create

        """
        response = await self._client.post(
            "/customers-corporate/notes/create",
            params={"site": site},
            data={"note": note.model_dump_json(exclude_unset=True, by_alias=True)},
        )
        response_obj = ResponseCustomerNotesCreate.model_validate_json(response.body)  # Define the response model

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)
        return response_obj

    async def note_delete(self, note_id: int) -> ResponseCustomerNotesDelete:
        """
        Удаление заметки.

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-customers-corporate-notes-id-delete
        """
        response = await self._client.post(f"/customers-corporate/notes/{note_id}/delete")
        response_obj = ResponseCustomerNotesDelete.model_validate_json(response.body)

        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg, response_obj.errors)

        return response_obj