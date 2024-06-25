from pydantic import BaseModel, Field

from retailcrm.v5.schemas.base import RetailCrmResponse


class Status(BaseModel):
    name: str = Field(description="Название")
    code: str = Field(description="Символьный код")
    active: bool = Field(False, description="Статус активности")
    ordering: int = Field(description="Порядок")
    group: str = Field(description="Группа статусов, к которой относится статус")


class ResponseStatuses(RetailCrmResponse):
    statuses: dict[str, Status] = Field(default_factory=list, description="Статусы заказа")


class StatusGroup(BaseModel):
    name: str = Field(description="Название")
    code: str = Field(description="Символьный код")
    active: bool = Field(False, description="Статус активности")
    ordering: int = Field(description="Порядок")
    process: bool = Field(False, description="Является или нет процессным состоянием заказа")
    statuses: list[str] = Field(default_factory=list, description="Статусы заказов, которые входят в данную группу")


class ResponseStatusGroups(RetailCrmResponse):
    statusGroups: dict[str, StatusGroup] = Field(default_factory=list, description="Группа статусов")
