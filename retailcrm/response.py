from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Response:
    status_code: int
    content: bytes
