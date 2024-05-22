from pydantic import BaseModel


class BaseRetailCrmResponse(BaseModel):
    success: bool = False
    errorMsg: str = ""
