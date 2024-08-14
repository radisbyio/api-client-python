from dataclasses import dataclass

from retailcrm import RetailCrmApiError
from retailcrm.http_cilent import BaseHttpClient
from retailcrm.v5.api.users import RetailCrmUsersApi
from retailcrm.v5.enums import UserStatuses
from retailcrm.v5.schemas.base import RetailCrmResponse
from retailcrm.v5.schemas.users import (
    UserGroupsResponse, ApiUserFilter, UserResponse, UserlistResponse
)
from retailcrm.v5.utils import pydantic_to_nested_dict


@dataclass(slots=True)
class UsersController:
    _api: RetailCrmUsersApi

    def __init__(self, client: BaseHttpClient):
        self._api = RetailCrmUsersApi(client)

    async def user_groups(self, limit: int = 20, page: int = 1) -> UserGroupsResponse:
        response = await self._api.user_groups(limit, page)
        response_obj = UserGroupsResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def users(self, filter_obj: ApiUserFilter, limit: int = 20, page: int = 1) -> UserlistResponse:
        response = await self._api.users(
            filter_dict=pydantic_to_nested_dict(filter_obj, "filter"),
            limit=limit,
            page=page
        )
        response_obj = UserlistResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def user(self, user_id: int) -> UserResponse:
        response = await self._api.user(user_id)
        response_obj = UserResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj

    async def user_set_status(self, user_id: int, status: UserStatuses) -> RetailCrmResponse:
        response = await self._api.user_set_status(user_id, status.value)
        response_obj = RetailCrmResponse.model_validate_json(response.body)
        if response.status_code >= 400:
            raise RetailCrmApiError(response.status_code, response_obj.errorMsg)
        return response_obj
