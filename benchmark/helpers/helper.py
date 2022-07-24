from inspect import isclass
from typing import Any

_SEP = ", "
_KWARG_JOIN = "="


def get_name(obj: Any, default: str | None = None) -> str:
    ret: Any = getattr(obj, "__name__", default)
    if not isinstance(default, str) and default is not None:
        msg = "Expected default value to be 'str' instance or None"
        raise ValueError(msg)
    if ret is None:
        msg = f"{obj!r} has no '__name__' attribute and a default has not been provided"
        raise TypeError(msg)
    if not isinstance(ret, str):
        msg = f"Expected return value of __name__ descriptor to be 'str' instance, got {ret!r} instead"
        raise ValueError(msg)
    return ret


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
