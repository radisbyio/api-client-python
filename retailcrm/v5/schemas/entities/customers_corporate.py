import decimal
from datetime import datetime
from typing import Any, Optional

from pydantic import Field, field_serializer, field_validator

from retailcrm.v5.helpers import datetime_serializer, dict_validator
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.customers import CustomerAddress
from retailcrm.v5.schemas.shared.customer import SerializedEntityCustomer
from retailcrm.v5.schemas.shared.customer_phone import CustomerPhone
from retailcrm.v5.schemas.shared.source import SerializedSource
