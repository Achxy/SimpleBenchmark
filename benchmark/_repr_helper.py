from inspect import isclass
from typing import Any, final

from ._internals import get_name

_SEP = ", "
_KWARG_JOIN = "="


def _args_fmt(argument: tuple[Any, ...]) -> str:
    return _SEP.join(map(repr, argument))


def _kwargs_fmt(kw_argument: dict[Any, Any]) -> str:
    return _SEP.join(f"{k}{_KWARG_JOIN}{repr(v)}" for k, v in kw_argument.items())


def param_fmt(argument, kw_argument) -> str:
    join_strategy = _SEP if argument and kw_argument else str()
    return _args_fmt(argument) + join_strategy + _kwargs_fmt(kw_argument)


def repr_fmt(cls, *args, **kwargs):
    if not isclass(cls):
        msg = f"Expected cls argument to be instance of 'type', got {cls!r} instead"
        raise TypeError(msg)
    name = get_name(cls)
    parms = param_fmt(args, kwargs)
    return f"{name}({parms})"


class AutoRepr:
    __slots__ = ("__repr_data__",)

    def __new__(cls: type, *args, **kwargs):
        self = super().__new__(cls)
        self.__repr_data__ = args, kwargs
        return self

    @final
    def __repr__(self) -> str:
        cls = type(self)
        args, kwargs = self.__repr_data__
        return repr_fmt(cls, *args, **kwargs)
