from pydantic import Field

from retailcrm.v5.schemas import BaseRetailCrmScheme


class Pagination(BaseRetailCrmScheme):
    limit: int | None = Field(None, description="Количество элементов в ответе")
    totalCount: int | None = Field(None, description="Общее количество найденных элементов")
    currentPage: int | None = Field(None, description="Текущая страница выдачи")
    totalPageCount: int | None = Field(None, description="Общее количество страниц выдачи")
