from pydantic import BaseModel, Field, model_serializer

from retailcrm.v5.schemas import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.users import ApiUserFilter
from retailcrm.v5.utils import pydantic_to_nested_dict


class FilterUserGroupsRequest(BaseRetailCrmScheme):
    limit: int
    page: int


class FilterUsersRequest(BaseRetailCrmScheme):
    filter_obj: ApiUserFilter = Field(serialization_alias="filter")
    limit: int
    page: int

    @model_serializer()
    def serialize_model(self) -> dict:
        return {
            "limit": self.limit,
            "page": self.page,
            **pydantic_to_nested_dict(self.filter_obj, "filter")
        }


class SetUserStatusRequest(BaseModel):
    status: str