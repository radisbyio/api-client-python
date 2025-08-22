from typing import Optional

from pydantic import Field

from retailcrm.v5.schemas.base import SuccessResponse


class IntegrationsConfigResponse(SuccessResponse):
    scopes: Optional[list[str]] = Field(None, description="Разрешения, необходимые API ключу для работы модуля")
    registerUrl: Optional[str] = Field(None, description="URL для регистрации модуля")


class IntegrationsRegisterUrlResponse(SuccessResponse):
    accountUrl: Optional[str] = Field(None, description="Адрес личного кабинета (при переходе по этой ссылке отправляется POST запрос с параметром clientId)")
