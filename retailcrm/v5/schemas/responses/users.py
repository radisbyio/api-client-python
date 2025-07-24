from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse, SuccessPaginatedResponse
from retailcrm.v5.schemas.entities.users import Group, SerializedUser

__all__ = ["UserGroupsResponse", "UserListResponse", "UserResponse"]


class UserGroupsResponse(SuccessPaginatedResponse):
    groups: list[Group] = Field(
        default_factory=list, description="Группа пользователей"
    )


class UserListResponse(SuccessPaginatedResponse):
    users: Optional[list[SerializedUser]] = Field(
        None, description="Информация о пользователях"
    )


class UserResponse(SuccessResponse):
    user: Optional[SerializedUser] = Field(
        None, description="Информация о пользователе"
    )
