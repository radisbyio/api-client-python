from enum import StrEnum


class CallEventType(StrEnum):
    IN = "in"
    OUT = "out"
    HANGUP = "hangup"


class HangupStatus(StrEnum):
    ANSWERED = "answered"
    NO_ANSWERED = "no answered"
    BUSY = "busy"
    CANCEL = "cancel"
    FAILED = "failed"

class CallUploadType(StrEnum):
    IN = "in"
    OUT = "out"


class CallResult(StrEnum):
    FAILED = "failed"
    ANSWERED = "answered"
    BUSY = "busy"
    NO_ANSWER = "no answer"
    NOT_ALLOWED = "not allowed"
    UNKNOWN = "unknown"
