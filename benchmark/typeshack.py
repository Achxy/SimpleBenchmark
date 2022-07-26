from typing import TypeVar, ParamSpec, Literal, TypeAlias, TYPE_CHECKING
from enum import Enum
from collections.abc import Callable

if TYPE_CHECKING:
    from .impl import SyncBenchmark
    from .abstract import SkeletalBaseBenchmark
    from .containers import TimingReport
else:
    SyncBenchmark = TypeVar("SyncBenchmark")
    SkeletalBaseBenchmark = TypeVar("SkeletalBaseBenchmark")
    TimingReport = TypeVar("TimingReport")

R = TypeVar("R")
P = ParamSpec("P")
Q = TypeVar("Q")

ContraBenchmark = TypeVar("ContraBenchmark", bound=SyncBenchmark, contravariant=True)


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
BenchmarkProgenitor: TypeAlias = SkeletalBaseBenchmark
# NewType is tedious here, simple aliasing aids in legible IDE reccomendations
Name: TypeAlias = str | None
MilliSeconds: type[float] = float
PerfDeltaMSec: TypeAlias = MilliSeconds
ProcessDeltaMsec: TypeAlias = MilliSeconds
FormatHook: TypeAlias = Callable[[TimingReport], str]
PostBenchmarkHook: TypeAlias = Callable[[ContraBenchmark], None]
