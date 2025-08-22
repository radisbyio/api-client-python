from retailcrm.v5.resources.base import ApiResource
from retailcrm.v5.schemas.base import SuccessResponse
from retailcrm.v5.schemas.entities.files import SerializedFile
from retailcrm.v5.schemas.filters.files import FileFilter
from retailcrm.v5.schemas.requests.files import FilesFilterRequest, FileEditRequest
from retailcrm.v5.schemas.responses.files import FilesFilterResponse, FileUploadResponse, FileGetResponse, \
    FileEditResponse


__all__ = ["FilesApiResource"]


class FilesApiResource(ApiResource):
    async def filter(
        self, filter_obj: FileFilter | None = None, limit: int = 20, page: int = 1
    ) -> FilesFilterResponse:
        """
        **Получение списка файлов, удовлетворяющих заданному фильтру**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-files

        :param filter_obj: Объект фильтра.
        :param limit: Количество элементов в ответе (по умолчанию равно 20).
        :param page: Номер страницы с результатами (по умолчанию равно 1).
        :return: FilesFilterResponse
        """
        request = FilesFilterRequest(filter_obj=filter_obj, limit=limit, page=page)
        response = await self._client.get(
            endpoint="/files",
            params=request.model_dump(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, FilesFilterResponse)

    async def upload(self, file_content: bytes) -> FileUploadResponse:
        """
        **Загрузка файла на сервер**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-files-upload
        :param file_content: Содержимое файла.
        :return: FileUploadResponse
        """
        response = await self._client.post(
            endpoint="/files/upload",
            content=file_content,
            headers={"Content-Type": "application/octet-stream"}
        )
        return self._process_response(response, FileUploadResponse)

    async def get(self, file_id: int) -> FileGetResponse:
        """
        **Получение информации о файле**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-files-id
        :param file_id: ID файла.
        :return: FileGetResponse
        """
        response = await self._client.get(
            endpoint=f"/files/{file_id}",
        )
        return self._process_response(response, FileGetResponse)

    async def delete(self, file_id: int) -> SuccessResponse:
        """
        **Удаление файла**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-files-id-delete
        :param file_id: ID файла.
        :return: SuccessResponse
        """
        response = await self._client.post(
            endpoint=f"/files/{file_id}/delete",
        )
        return self._process_response(response, SuccessResponse)

    async def download(self, file_id: int) -> bytes:
        """
        **Скачивание файла**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#get--api-v5-files-id-download
        :param file_id: ID файла.
        :return: bytes (содержимое файла)
        """

        response = await self._client.get(
            endpoint=f"/files/{file_id}/download",
        )
        return response.content

    async def edit(self, file_id: int, file: SerializedFile) -> FileEditResponse:
        """
        **Редактирование файла**

        https://docs.retailcrm.ru/Developers/API/APIVersions/APIv5#post--api-v5-files-id-edit
        :param file_id: ID файла.
        :param file: Объект файла с изменениями.
        :return: FileEditResponse
        """
        request = FileEditRequest(file=file)
        response = await self._client.post(
            endpoint=f"/files/{file_id}/edit",
            content=request.model_dump_json(exclude_none=True, by_alias=True),
        )
        return self._process_response(response, FileEditResponse)