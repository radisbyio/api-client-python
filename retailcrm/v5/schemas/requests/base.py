from pydantic import BaseModel, ConfigDict


JsonString: str

class BaseRetailCrmRequest(BaseModel):
    model_config = ConfigDict(use_enum_values=True)