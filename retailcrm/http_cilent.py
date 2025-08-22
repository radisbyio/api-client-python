import logging
from typing import Optional

import httpx

from retailcrm.exceptions import RetailCrmTimeoutException
from retailcrm.heplers.transports import RetryTransport
from retailcrm.response import Response

logger = logging.getLogger("retailcrm.http_client")


class BaseHttpClient:
    async def get(self, endpoint: str, params: Optional[dict] = None, use_version: bool = True) -> Response:
        raise NotImplementedError

    async def post(
        self,
            endpoint: str,
            params: Optional[dict] = None,
            content: Optional[str | bytes] = None,
            headers: Optional[dict] = None,
            use_version: bool = True
    ) -> Response:
        raise NotImplementedError


class HttpClient(BaseHttpClient):
    _client: httpx.AsyncClient

    def __init__(self, crm_url: str, api_key: str, version: str, use_retries=True):
        self._crm_url = crm_url
        self._api_key = api_key
        self._version = version

        headers = {"X-API-KEY": self._api_key}

        transport = httpx.AsyncHTTPTransport()
        if use_retries:
            transport = RetryTransport(transport)

        self._client = httpx.AsyncClient(
            headers=headers, base_url=crm_url + "/api/", transport=transport
        )

    async def get(self, endpoint: str, params: Optional[dict] = None, use_version: bool = True) -> Response:
        if use_version:
            endpoint = self._version + endpoint

        try:
            logger.debug(f"Request to {endpoint} with params: {params}")
            response = await self._client.get(endpoint, params=params, timeout=15.0)
            logger.debug(f"Received {response.status_code} with {response.text}")
        except httpx.TimeoutException:
            raise RetailCrmTimeoutException()
        else:
            return Response(response.status_code, response.content)

    async def post(
        self,
            endpoint: str,
            params: Optional[dict] = None,
            content: Optional[str | bytes] = None,
        headers: Optional[dict] = None,
            use_version: bool = True,
    ) -> Response:
        if headers is None:
            headers = {"Content-Type": "application/json"}

        if use_version:
            endpoint = self._version + endpoint

        try:
            logger.debug(
                f"Request to {endpoint} with params: {params} and body: {content}"
            )
            response = await self._client.post(
                endpoint, params=params, content=content, timeout=15.0, headers=headers
            )
            logger.debug(f"Received {response.status_code} with {response.text}")
        except httpx.TimeoutException:
            raise RetailCrmTimeoutException()
        else:
            return Response(response.status_code, response.content)
