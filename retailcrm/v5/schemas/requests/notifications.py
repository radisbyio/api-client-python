from pydantic import field_serializer

from retailcrm.v5.helpers import to_json_serializer
from retailcrm.v5.schemas.base import BaseRetailCrmScheme
from retailcrm.v5.schemas.entities.notifications import SerializedApiNotification


class SendNotificationRequest(BaseRetailCrmScheme):
    notification: SerializedApiNotification

    notification_serializer = field_serializer("notification")(to_json_serializer())
