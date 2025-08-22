from retailcrm.v5.enums.user_statuses import UserStatuses
from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.users import ApiUserFilter
from retailcrm.v5.schemas.requests.users import (
    FilterUserGroupsRequest,
    FilterUsersRequest,
    SetUserStatusRequest,
)
from retailcrm.v5.schemas.responses.users import (
    UserGroupsResponse,
    UserListResponse,
    UserResponse,
)


class UsersApiResource(ApiResource):
    async def filter_groups(self, limit: int = 20, page: int = 1) -> UserGroupsResponse:
        """
        **Получение списка групп пользователей**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-user-groups
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :return: UserGroupsResponse
        """

        request = FilterUserGroupsRequest(limit=limit, page=page)

        response = await self._client.get(
            endpoint="/user-groups",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, UserGroupsResponse)

    async def filter(
        self, filter_obj: ApiUserFilter, limit: int = 20, page: int = 1
    ) -> UserListResponse:
        """
        **Получение списка пользователей, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-users
        :param filter_obj: Фильтр
        :param limit: Количество элементов в ответе (по умолчанию равно 20)
        :param page: Номер страницы с результатами (по умолчанию равно 1)
        :return: UserListResponse
        """

        request = FilterUsersRequest(
            limit=limit,
            page=page,
            filter_obj=filter_obj,
        )

        response = await self._client.get(
            endpoint="/users",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, UserListResponse)

    async def user(self, user_id: int) -> UserResponse:
        """
        **Получение информации о пользователе**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-users-id
        :param user_id: ID пользователя
        :return: UserResponse
        """

        response = await self._client.get(
            endpoint=f"/users/{user_id}",
        )
        return self._process_response(response, UserResponse)

    async def user_set_status(
        self, user_id: int, status: UserStatuses
    ) -> SuccessResponse:
        """
        **Смена статуса пользователя**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-users-id-status
        :param user_id: ID пользователя
        :param status: Статус пользователя в системе.
        :return: SuccessResponse
        """

        request = SetUserStatusRequest(status=status)
        response = await self._client.post(
            endpoint=f"/users/{user_id}/status",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, SuccessResponse)
