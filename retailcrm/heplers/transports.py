import asyncio
import logging
from typing import Iterable, Union

import httpx

logger = logging.getLogger("retailcrm.http_client")


class RetryTransport(httpx.AsyncBaseTransport, httpx.BaseTransport):
    RETRYABLE_STATUS_CODES = frozenset([413, 429, 500])

    def __init__(
        self,
        wrapped_transport: Union[httpx.BaseTransport, httpx.AsyncBaseTransport],
        max_attempts: int = 5,
        backoff_factor: float = 0.1,
        jitter_ratio: float = 0.2,
        retry_status_codes: Iterable[int] = None,
    ) -> None:
        self.wrapped_transport = wrapped_transport
        if jitter_ratio < 0 or jitter_ratio > 0.5:
            msg = f"jitter ratio should be between 0 and 0.5, actual {jitter_ratio}"
            raise ValueError(msg)

        self.max_attempts = max_attempts
        self.backoff_factor = backoff_factor
        self.jitter_ratio = jitter_ratio
        self.retry_status_codes = (
            frozenset(retry_status_codes)
            if retry_status_codes
            else self.RETRYABLE_STATUS_CODES
        )

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        for attempt in range(self.max_attempts + 1):
            try:
                response = await self.wrapped_transport.handle_async_request(request)
            except httpx.TimeoutException as exc:
                logger.debug(f"Request timeout (attempt {attempt}/{self.max_attempts})")
                if attempt == self.max_attempts:
                    raise exc

                delay = self.backoff_factor * self.jitter_ratio * attempt
                await asyncio.sleep(delay)
            else:
                if (
                    attempt == self.max_attempts
                    and response.status_code in self.retry_status_codes
                ):
                    return response
