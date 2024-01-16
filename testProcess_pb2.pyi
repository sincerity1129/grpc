from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TESTRequest(_message.Message):
    __slots__ = ("feature",)
    FEATURE_FIELD_NUMBER: _ClassVar[int]
    feature: str
    def __init__(self, feature: _Optional[str] = ...) -> None: ...

class TESTReply(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
