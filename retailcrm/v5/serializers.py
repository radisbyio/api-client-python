from datetime import datetime
from typing import Callable


def datetime_serializer(format_str: str) -> Callable[[datetime], str]:
    def serializer(value: datetime) -> str:
        return datetime.strftime(value, format_str)

    return serializer
