from typing import TypeVar, ParamSpec, Literal, TypeAlias, TYPE_CHECKING
from enum import Enum
from collections.abc import Callable

if TYPE_CHECKING:
    from .impl import SyncBenchmark
    from .containers import TimingReport
else:
    SyncBenchmark = TypeVar("SyncBenchmark")
    TimingReport = TypeVar("TimingReport")

R = TypeVar("R")
P = ParamSpec("P")
Q = TypeVar("Q")

AnyBenchmark: TypeAlias = SyncBenchmark
_TDerived_contra = TypeVar("_TDerived_contra", bound=AnyBenchmark, contravariant=True)
AllBenchmark = _TDerived_contra | AnyBenchmark


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
# NewType is tedious here, simple aliasing aids in legible IDE reccomendations
Name: TypeAlias = str | None
MilliSeconds: type[float] = float
PerfDeltaMSec: TypeAlias = MilliSeconds
ProcessDeltaMsec: TypeAlias = MilliSeconds
FormatHook: TypeAlias = Callable[[TimingReport], str]
PostBenchmarkHook: TypeAlias = Callable[[AnyBenchmark], None]
