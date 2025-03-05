import httpx
import pytest
import respx
from retailcrm.v5.enums import IdTypes
from retailcrm import RetailCrmApiClientV5, RetailCrmApiError
from retailcrm.v5.schemas import (
    CustomerCorporateApiFilterData,
    ResponseCustomersCorporateGetAll,
    SerializedCustomerCorporate,
    FixExternalRow,
    CustomerHistoryFilterV4Type,
    SerializedCustomerReference,
    SerializedCustomerAddress,
    SerializedCompany,
    SerializedCustomerContact,
    CustomerNoteFilter,
    SerializedCustomerNote
)
from datetime import datetime, date



@pytest.mark.asyncio
async def test_corporate_customers_filter_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_corporate_customer: dict,
):
    mock_response = {
        "success": True,
        "pagination": {
            "limit": 20,
            "totalCount": 1,
            "currentPage": 1,
            "totalPageCount": 1
        },
        "customersCorporate": [mock_corporate_customer]
    }
    filter_data = CustomerCorporateApiFilterData()

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate",
        params={"limit": 20, "page": 1},
    ).mock(
        httpx.Response(
            json=mock_response,
            status_code=200,
        )
    )

    get_all_response = await mock_retailcrm_client_v5.corporate_customers.filter(filter_data)

    assert get_all_response.success is True



@pytest.mark.asyncio
async def test_corporate_customers_filter_error(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    filter_data = CustomerCorporateApiFilterData()
    mock_error_response = {
        "success": False,
        "errorMsg": "Incorrect filter param",
        "errors": {"filter[incorrectFilter]": "Should be string"}
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate"
    ).mock(httpx.Response(json=mock_error_response, status_code=400))


    with pytest.raises(RetailCrmApiError) as exc_info:
        await mock_retailcrm_client_v5.corporate_customers.filter(filter_data=filter_data)

    assert exc_info.value.status_code == 400
    assert exc_info.value.error_msg == "Incorrect filter param"
    assert exc_info.value.errors == {"filter[incorrectFilter]": "Should be string"}




@pytest.mark.asyncio
async def test_corporate_customers_create_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_corporate_customer: dict,
):
    customer_corporate_request = SerializedCustomerCorporate(**mock_corporate_customer)
    mock_response = {"success": True, "id": 12345}

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/create"
    ).mock(httpx.Response(json=mock_response, status_code=201))

    response = await mock_retailcrm_client_v5.corporate_customers.create(customer_corporate_request)

    assert response.success is True
    assert response.id == 12345


@pytest.mark.asyncio
async def test_corporate_customers_create_error(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    customer = {"externalId": "test_ext_id", "nickName": "Test"}

    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/create").mock(
        httpx.Response(
            json={
                "success": False,
                "errorMsg": "Customer creation failed",
                "errors": {"nickName": ["This value should not be blank."]},
            },
            status_code=400,
        )
    )

    with pytest.raises(RetailCrmApiError) as exc:
        _ = await mock_retailcrm_client_v5.corporate_customers.create(
            customer=SerializedCustomerCorporate.model_validate(customer)
        )

    assert exc.value.status_code == 400
    assert exc.value.error_msg == "Customer creation failed"


@pytest.mark.asyncio
async def test_corporate_customers_fix_external_ids_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):

    mock_response = {"success": True}
    customers = [
        FixExternalRow(id=1, externalId="externalId1"),
        FixExternalRow(id=2, externalId="externalId2"),
    ]

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/fix-external-ids"
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.corporate_customers.fix_external_ids(customers)

    assert response.success is True


@pytest.mark.asyncio
async def test_corporate_customers_fix_external_ids_error(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):

    mock_response = {
        "success": False,
        "errorMsg": "External IDs fixing failed",
        "errors": {"id": "This value should not be blank."},
    }
    customers = [
        {"id": 1, "externalId": "externalId1"},
        {"id": 2, "externalId": "externalId2"},
    ]

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/fix-external-ids"
    ).mock(httpx.Response(json=mock_response, status_code=400))

    with pytest.raises(RetailCrmApiError) as exc:
        _ = await mock_retailcrm_client_v5.corporate_customers.fix_external_ids(
            [FixExternalRow.model_validate(customer) for customer in customers]
        )

    assert exc.value.status_code == 400
    assert exc.value.error_msg == "External IDs fixing failed"


@pytest.mark.asyncio
async def test_corporate_customers_history_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_corporate_customer_history: dict,
):
    mock_response = {
        "success": True,
        "generatedAt": "2024-07-24 14:37:07",
        "history": [mock_corporate_customer_history],
        "pagination": {
            "limit": 20,
            "totalCount": 1,
            "currentPage": 1,
            "totalPageCount": 1
        }
    }
    filter = CustomerHistoryFilterV4Type()


    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/history",
    ).mock(httpx.Response(json=mock_response, status_code=200))

    history_response = await mock_retailcrm_client_v5.corporate_customers.history(filter_obj=filter)

    assert history_response.success is True



@pytest.mark.asyncio
async def test_corporate_customers_combine_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    customer1 = SerializedCustomerReference(id=1)
    customer2 = SerializedCustomerReference(id=2)
    result_customer = SerializedCustomerReference(id=3)
    mock_response = {"success": True}


    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/combine"
    ).mock(httpx.Response(json=mock_response, status_code=200))

    combine_response = await mock_retailcrm_client_v5.corporate_customers.combine([customer1, customer2], result_customer)

    assert combine_response.success is True


@pytest.mark.asyncio
async def test_corporate_customers_combine_error(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    customers_to_combine = [
        {"id": 123},
        {"id": 456},
    ]
    target_customer = {"id": 789}

    mock_error_response = {
        "success": False,
        "errorMsg": "At least one corporate customer is required for combine operation",
    }
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/combine").mock(
        httpx.Response(
            json=mock_error_response,
            status_code=400,
        )
    )
    with pytest.raises(RetailCrmApiError) as exc:
        _ = await mock_retailcrm_client_v5.corporate_customers.combine(
            customers=[SerializedCustomerReference.model_validate(cust) for cust in customers_to_combine],
            result_customer=SerializedCustomerReference.model_validate(target_customer),
        )

    assert exc.value.status_code == 400
    assert exc.value.error_msg == "At least one corporate customer is required for combine operation"


@pytest.mark.asyncio
async def test_corporate_customers_get_companies_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_company: dict
):

    mock_response = {
        "success": True,
        "companies": [mock_company]
    }
    customer_id = 10
    respx_mock.get(f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/{customer_id}/companies").mock(
        httpx.Response(json=mock_response, status_code=200)
    )
    addresses = await mock_retailcrm_client_v5.corporate_customers.companies_get(customer_id=customer_id)
    assert addresses.success is True


@pytest.mark.asyncio
async def test_corporate_customers_get_contacts_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_customer_contact: dict
):

    mock_response = {
        "success": True,
        "contacts": [mock_customer_contact]
    }
    customer_id = 10
    respx_mock.get(f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/{customer_id}/contacts").mock(
        httpx.Response(json=mock_response, status_code=200)
    )
    addresses = await mock_retailcrm_client_v5.corporate_customers.contacts_get(customer_id=customer_id)
    assert addresses.success is True


@pytest.mark.asyncio
async def test_corporate_customers_create_address_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_customer_address: dict
):

    mock_response = {
        "success": True,
        "id": 123
    }
    customer_id = 10
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/{customer_id}/addresses/create").mock(
        httpx.Response(json=mock_response, status_code=200)
    )
    create_result = await mock_retailcrm_client_v5.corporate_customers.address_create(customer_id=customer_id, address=SerializedCustomerAddress(**mock_customer_address))
    assert create_result.success is True



@pytest.mark.asyncio
async def test_corporate_customers_create_address_error(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    address = {"text": "", "index": "123456"}

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/10/addresses/create"
    ).mock(
        httpx.Response(
            json={
                "success": False,
                "errorMsg": "Address creation failed",
                "errors": {"text": ["This value should not be blank."]},
            },
            status_code=400,
        )
    )

    with pytest.raises(RetailCrmApiError) as exc:
        _ = await mock_retailcrm_client_v5.corporate_customers.address_create(
            customer_id="10", address=SerializedCustomerAddress.model_validate(address)
        )

    assert exc.value.status_code == 400
    assert exc.value.error_msg == "Address creation failed"



@pytest.mark.asyncio
async def test_corporate_customers_edit_address_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_customer_address: dict
):

    mock_response = {
        "success": True,
        "id": 123
    }
    customer_id = 10
    address_id = 20

    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/{customer_id}/addresses/{address_id}/edit").mock(
        httpx.Response(json=mock_response, status_code=200)
    )
    addresses = await mock_retailcrm_client_v5.corporate_customers.address_edit(customer_id=customer_id, address_id=address_id, address=SerializedCustomerAddress(**mock_customer_address))
    assert addresses.success is True


@pytest.mark.asyncio
async def test_corporate_customers_create_company_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_company: dict
):

    mock_response = {
        "success": True,
        "id": 123
    }
    customer_id = 10
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/{customer_id}/companies/create").mock(
        httpx.Response(json=mock_response, status_code=200)
    )
    create_result = await mock_retailcrm_client_v5.corporate_customers.company_create(customer_id=customer_id, company=SerializedCompany(**mock_company))
    assert create_result.success is True


@pytest.mark.asyncio
async def test_corporate_customers_create_company_error(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    company = {"name": "", "externalId": "company-external-id-1"}
    customer_id = 10

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/{customer_id}/companies/create"
    ).mock(
        httpx.Response(
            json={
                "success": False,
                "errorMsg": "Company creation failed",
                "errors": {"name": ["This value should not be blank."]},
            },
            status_code=400,
        )
    )

    with pytest.raises(RetailCrmApiError) as exc:
        _ = await mock_retailcrm_client_v5.corporate_customers.company_create(
            customer_id=customer_id, company=SerializedCompany.model_validate(company)
        )

    assert exc.value.status_code == 400
    assert exc.value.error_msg == "Company creation failed"



@pytest.mark.asyncio
async def test_corporate_customers_edit_company_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_company: dict
):

    mock_response = {
        "success": True,
        "id": 123
    }
    customer_id = 10
    company_id = 20
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/{customer_id}/companies/{company_id}/edit").mock(
        httpx.Response(json=mock_response, status_code=200)
    )
    addresses = await mock_retailcrm_client_v5.corporate_customers.company_edit(customer_id=customer_id, company_id=company_id, company=SerializedCompany(**mock_company))
    assert addresses.success is True


@pytest.mark.asyncio
async def test_corporate_customers_create_contact_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_customer_contact: dict
):

    mock_response = {
        "success": True,
        "id": 123
    }
    customer_id = 10
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/{customer_id}/contacts/create").mock(
        httpx.Response(json=mock_response, status_code=200)
    )

    contact = await mock_retailcrm_client_v5.corporate_customers.contact_create(customer_id=customer_id, contact=SerializedCustomerContact(**mock_customer_contact))
    assert contact.success is True


@pytest.mark.asyncio
async def test_corporate_customers_create_contact_error(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    contact = {"customer": {"id": ""}, "companies": []}
    customer_id = 10

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/{customer_id}/contacts/create"
    ).mock(
        httpx.Response(
            json={
                "success": False,
                "errorMsg": "Contact creation failed",
                "errors": {"customer.id": ["This value should not be blank."]},
            },
            status_code=400,
        )
    )

    with pytest.raises(RetailCrmApiError) as exc:
        _ = await mock_retailcrm_client_v5.corporate_customers.contact_create(
            customer_id=customer_id, contact=SerializedCustomerContact.model_validate(contact)
        )

    assert exc.value.status_code == 400
    assert exc.value.error_msg == "Contact creation failed"




@pytest.mark.asyncio
async def test_corporate_customers_edit_contact_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
        mock_customer_contact: dict
):

    mock_response = {
        "success": True,
        "id": 123
    }
    customer_id = 10
    contact_id = 20
    respx_mock.post(f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/{customer_id}/contacts/{contact_id}/edit").mock(
        httpx.Response(json=mock_response, status_code=200)
    )
    addresses = await mock_retailcrm_client_v5.corporate_customers.contact_edit(customer_id=customer_id, contact_id=contact_id, contact=SerializedCustomerContact(**mock_customer_contact))
    assert addresses.success is True



@pytest.mark.asyncio
async def test_corporate_customers_get_notes_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_customer_note: dict,
):

    mock_response = {
        "success": True,
        "pagination": {
            "limit": 20,
            "totalCount": 1,
            "currentPage": 1,
            "totalPageCount": 1,
        },
        "notes": [mock_customer_note]
    }

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/notes",
        params={"limit": 20, "page": 1},
    ).mock(httpx.Response(json=mock_response, status_code=200))

    notes_response = await mock_retailcrm_client_v5.corporate_customers.get_notes(CustomerNoteFilter())
    assert notes_response.success is True


@pytest.mark.asyncio
async def test_corporate_customers_get_notes_error(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    filter_data = CustomerNoteFilter(ids=[1, 2])

    mock_error_response = {
        "success": False,
        "errorMsg": "Invalid IDs",
        "errors": {"filter[ids][1]": "This value should be of type integer."},
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/notes"
    ).mock(httpx.Response(json=mock_error_response, status_code=400))

    with pytest.raises(RetailCrmApiError) as exc:
        _ = await mock_retailcrm_client_v5.corporate_customers.get_notes(filter_data=filter_data)


    assert exc.value.status_code == 400
    assert exc.value.error_msg == "Invalid IDs"




@pytest.mark.asyncio
async def test_corporate_customers_create_note_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_customer_note: dict,
):
    note_request = SerializedCustomerNote(**mock_customer_note)
    mock_response = {"success": True, "id": 12345}

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/notes/create",
        params={"site": "test_site"},
    ).mock(httpx.Response(json=mock_response, status_code=201))


    response = await mock_retailcrm_client_v5.corporate_customers.note_create(note_request, "test_site")

    assert response.success is True
    assert response.id == 12345




@pytest.mark.asyncio
async def test_corporate_customers_delete_note_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,

):
    note_id = 123
    mock_response = {"success": True}


    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/notes/{note_id}/delete"
    ).mock(httpx.Response(json=mock_response, status_code=200))


    response = await mock_retailcrm_client_v5.corporate_customers.note_delete(note_id)

    assert response.success is True



@pytest.mark.asyncio
async def test_corporate_customers_delete_note_error(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": False,
        "errorMsg": "Note not found"
    }
    note_id = 123

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/notes/{note_id}/delete"
    ).mock(httpx.Response(json=mock_response, status_code=404))


    with pytest.raises(RetailCrmApiError) as exc:
        _ = await mock_retailcrm_client_v5.corporate_customers.note_delete(note_id=note_id)


    assert exc.value.status_code == 404
    assert exc.value.error_msg == "Note not found"


@pytest.mark.asyncio
async def test_corporate_customers_upload_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_corporate_customer: dict
):
    mock_response = {"success": True, "uploadedCustomers": [], "failedCustomers": []}
    customer = SerializedCustomerCorporate(**mock_corporate_customer)


    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/upload"
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.corporate_customers.upload([customer], "test_site")
    assert response.success is True


@pytest.mark.asyncio
async def test_corporate_customers_get_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_corporate_customer: dict,
):
    mock_response = {"success": True, "customerCorporate": mock_corporate_customer}

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/1",
        params={"by": "id"},
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.corporate_customers.get(1, by=IdTypes.ID)
    assert response.success is True



@pytest.mark.asyncio
async def test_corporate_customers_get_error(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    mock_response = {
        "success": False,
        "errorMsg": "Not found"
    }
    customer_id = 1

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/{customer_id}", params={"by": "id"}
    ).mock(httpx.Response(json=mock_response, status_code=404))


    with pytest.raises(RetailCrmApiError) as exc:
        _ = await mock_retailcrm_client_v5.corporate_customers.get(customer_id=customer_id, by=IdTypes.ID)


    assert exc.value.status_code == 404
    assert exc.value.error_msg == "Not found"



@pytest.mark.asyncio
async def test_corporate_customers_edit_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_corporate_customer: dict,
):
    customer_corporate_request = SerializedCustomerCorporate(**mock_corporate_customer)

    mock_response = {"success": True, "id": 12345}
    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/test_ext_id/edit",
        params={"by": "externalId"},
    ).mock(httpx.Response(json=mock_response, status_code=200))


    response = await mock_retailcrm_client_v5.corporate_customers.edit("test_ext_id", customer_corporate_request)


    assert response.success is True
    assert response.id == 12345



@pytest.mark.asyncio
async def test_corporate_customers_edit_error(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    customer = {
        "externalId": "ext_customer_123",
        "createdAt": datetime(2023, 11, 9, 10, 00, 00),
        "firstName": "John",
        "lastName": "Doe",
        "email": "john.doe@example.com",
        "phones": [{"number": "+15551234567"}],
        "birthday": date(1980, 1, 1),
        "address": {"city": "New York"},
    }
    mock_error_response = {
        "success": False,
        "errorMsg": "Customer not found",
    }

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/10/edit",
    ).mock(httpx.Response(json=mock_error_response, status_code=404))

    with pytest.raises(RetailCrmApiError) as exc:
        _ = await mock_retailcrm_client_v5.corporate_customers.edit(
            customer_id="10",
            customer=SerializedCustomerCorporate.model_validate(customer),
        )

    assert exc.value.status_code == 404
    assert exc.value.error_msg == "Customer not found"


@pytest.mark.asyncio
async def test_corporate_customers_get_addresses_success(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
    mock_customer_address: dict,  # Fixture for address data
):
    customer_id = 10
    mock_response = {"success": True, "addresses": [mock_customer_address]}

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/{customer_id}/addresses",
        params={"by": "externalId", "limit": 20, "page": 1}, # Add any default parameters
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.corporate_customers.addresses_get(customer_id)
    assert response.success is True
    assert response.addresses == [mock_customer_address]  # Check the response data


@pytest.mark.asyncio
async def test_corporate_customers_get_addresses_error(
    respx_mock: respx.router.MockRouter,
    mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    customer_id = 10
    mock_response = {"success": False, "errorMsg": "Customer not found"}

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/customers-corporate/{customer_id}/addresses",
        params={"by": "externalId", "limit": 20, "page": 1},

    ).mock(httpx.Response(json=mock_response, status_code=404))

    with pytest.raises(RetailCrmApiError) as exc_info:
        await mock_retailcrm_client_v5.corporate_customers.addresses_get(customer_id)

    assert exc_info.value.status_code == 404
    assert exc_info.value.error_msg == "Customer not found"
