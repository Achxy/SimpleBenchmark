from typing import TypeVar, ParamSpec, Literal
from enum import Enum

R = TypeVar("R")
P = ParamSpec("P")


class _Sentinel(Enum):
    """
    Single member enum for static typecheckers to validate
    code, this is necessitated due to the fact that
    assigning sentinels to value returned by object()
    causes incorrect type inference.
    See, https://peps.python.org/pep-0661/
    """

    MISSING = object()


MISSING: Literal[_Sentinel.MISSING] = _Sentinel.MISSING
