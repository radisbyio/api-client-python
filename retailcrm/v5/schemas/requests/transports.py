from datetime import datetime

from pydantic import BaseModel, Field, field_serializer

from retailcrm.v5.helpers import datetime_serializer


class MGTransportOnlineRequest(BaseModel):
    externalUserId: str = Field(None, description="GET-параметр с внешним идентификатором клиента чата")

class MGTransportVisitsRequest(BaseModel):
    externalUserId: str = Field(None, description="GET-параметр с внешним идентификатором клиента чата")
