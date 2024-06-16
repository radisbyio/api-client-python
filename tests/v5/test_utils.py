from retailcrm.v5.schemas.orders import OrderFilterData
from retailcrm.v5.utils import pydantic_to_nested_dict


def test_pydantic_to_nested_dict():
    model_obj = OrderFilterData(ids=[10, 2], customer="John Doe")
    target_dict = {
        "filter[ids][0]": 10,
        "filter[ids][1]": 2,
        "filter[customer]": "John Doe"
    }
    processed_dict = pydantic_to_nested_dict(model_obj, "filter")
    assert target_dict == processed_dict
