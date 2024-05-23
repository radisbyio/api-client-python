from pydantic import BaseModel


class RetailCrmResponse(BaseModel):
    success: bool = False
    errorMsg: str = ""
