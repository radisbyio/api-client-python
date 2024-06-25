import logging

import httpx

from retailcrm.exceptions import RetailCrmTimeoutException
from retailcrm.response import Response

logger = logging.getLogger("retailcrm.http_client")


class BaseHttpClient:
    async def get(self, endpoint: str, params: dict = None) -> Response:
        raise NotImplementedError

    async def post(self, endpoint: str, params=None, data: dict = None) -> Response:
        raise NotImplementedError


class HttpClient(BaseHttpClient):
    _client: httpx.AsyncClient

    def __init__(self, crm_url: str, api_key: str, version="v5"):
        self._crm_url = crm_url
        self._api_key = api_key

        headers = {"X-API-KEY": self._api_key}
        self._client = httpx.AsyncClient(
            headers=headers,
            base_url=crm_url + "/api/" + version,
        )

    async def get(self, endpoint: str, params: dict = None) -> Response:
        try:
            logger.debug(f"Request to {endpoint} with params: {params}")
            response = await self._client.get(
                endpoint,
                params=params,
                timeout=15.0,
            )
            logger.debug(f"Received {response.status_code} with {response.text}")
        except httpx.TimeoutException:
            raise RetailCrmTimeoutException
        else:
            return Response(response.status_code, response.text)

    async def post(self, endpoint: str, params=None, data: dict = None) -> Response:
        try:
            logger.debug(
                f"Request to {endpoint} with params: {params} and body: {data}"
            )
            response = await self._client.post(
                endpoint,
                params=params,
                data=data,
                timeout=15.0,
            )
            logger.debug(f"Received {response.status_code} with {response.text}")
        except httpx.TimeoutException:
            raise RetailCrmTimeoutException
        else:
            return Response(response.status_code, response.text)
