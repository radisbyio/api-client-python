from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse, PaginatedResponse
from retailcrm.v5.schemas.entities.users import Group, SerializedUser

__all__ = ["UserGroupsResponse", "UserListResponse", "UserResponse"]


class UserGroupsResponse(PaginatedResponse):
    groups: list[Group] = Field(
        default_factory=list, description="Группа пользователей"
    )


class UserListResponse(PaginatedResponse):
    users: Optional[list[SerializedUser]] = Field(
        None, description="Информация о пользователях"
    )


class UserResponse(SuccessResponse):
    user: Optional[SerializedUser] = Field(
        None, description="Информация о пользователе"
    )
