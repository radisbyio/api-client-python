from datetime import datetime, timedelta

import httpx
import pytest
import respx

from retailcrm import RetailCrmApiClientV5, RetailCrmApiError
from retailcrm.v5.schemas import entities, responses


@pytest.mark.asyncio
async def test_sms_confirm_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    verification_data = entities.verification.SmsVerificationConfirm(code="123456", checkId="sms_check_id_1")
    now = datetime.now()
    mock_response = {
        "success": True,
        "verification": {
            "createdAt": now.strftime("%Y-%m-%d %H:%M:%S"),
            "expiredAt": (now + timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S"),
            "checkId": "sms_check_id_1",
            "actionType": "loyalty_account_confirmation",  # Example action type
        },
    }

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/verification/sms/confirm"
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.verification.sms_confirm(verification_data)

    assert isinstance(response, responses.verification.VerificationConfirmResponse)
    assert response.success is True
    assert isinstance(response.verification, entities.verification.SmsVerification)
    assert response.verification.checkId == "sms_check_id_1"


@pytest.mark.asyncio
async def test_sms_confirm_failure_invalid_code(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    verification_data = entities.verification.SmsVerificationConfirm(code="invalid_code", checkId="sms_check_id_2")
    mock_response = {
        "success": False,
        "errorMsg": "Invalid code.",
        "errors": {"code": "Invalid code format"},  # Example errors
    }

    respx_mock.post(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/verification/sms/confirm"
    ).mock(httpx.Response(json=mock_response, status_code=400))

    with pytest.raises(RetailCrmApiError) as exc_info:
        await mock_retailcrm_client_v5.verification.sms_confirm(verification_data)

    assert exc_info.value.status_code == 400
    assert exc_info.value.error_msg == "Invalid code."
    assert exc_info.value.errors == {"code": "Invalid code format"}


@pytest.mark.asyncio
async def test_sms_status_success(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    check_id = "sms_check_id_3"
    verified_at = (datetime.now() - timedelta(minutes=2)).strftime("%Y-%m-%d %H:%M:%S")
    mock_response = {
        "success": True,
        "verification": {"checkId": check_id, "verifiedAt": verified_at},
    }

    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/verification/sms/{check_id}/status"
    ).mock(httpx.Response(json=mock_response, status_code=200))

    response = await mock_retailcrm_client_v5.verification.sms_status(check_id)

    assert isinstance(response, responses.verification.VerificationConfirmResponse)
    assert response.success is True
    assert isinstance(response.verification, entities.verification.SmsVerification)
    assert response.verification.checkId == check_id
    assert response.verification.verifiedAt is not None


@pytest.mark.asyncio
async def test_sms_status_failure_not_found(
        respx_mock: respx.router.MockRouter,
        mock_retailcrm_client_v5: RetailCrmApiClientV5,
):
    check_id = "non_existing_check_id"
    mock_response = {
        "success": False,
        "errorMsg": "Verification not found."
    }
    respx_mock.get(
        f"{mock_retailcrm_client_v5.crm_url}/api/v5/verification/sms/{check_id}/status"
    ).mock(httpx.Response(json=mock_response, status_code=404))

    with pytest.raises(RetailCrmApiError) as exc:
        await mock_retailcrm_client_v5.verification.sms_status(check_id)

    assert exc.value.status_code == 404
    assert exc.value.error_msg == "Verification not found."
