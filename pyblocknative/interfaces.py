import typing

class NotificationObject:
    type: typing.Literal['pending', 'success', 'error', 'hint']
    message: typing.AnyStr
    auto_dismiss: typing.Any
    on_click: typing.Callable
    event_cold: typing.AnyStr


class ContractCall:
    method_name: typing.AnyStr
    params: typing.Dict
