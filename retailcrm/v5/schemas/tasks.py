from datetime import date, datetime
from typing import Optional, Union

from pydantic import Field, field_serializer

from retailcrm.v5.enums import TasksStatuses
from retailcrm.v5.helpers import datetime_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme, RetailCrmResponse
from retailcrm.v5.schemas.shared import ApiKey, SerializedEntityCustomer, Task, User, SerializedEntityOrder









