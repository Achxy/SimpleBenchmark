"""
SimpleBenchmark is a tool for benchmarking callable objects in Python.
Copyright (C) 2022-present  Achxy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from collections.abc import Callable
from enum import Enum
from typing import (
    TYPE_CHECKING,
    Final,
    Literal,
    ParamSpec,
    TypeAlias,
    TypeVar,
    ClassVar,
)

if TYPE_CHECKING:
    from .abstract import SkeletalBaseBenchmark
    from .containers import TimingReport
    from .impl import SyncBenchmark
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


Slots = ClassVar[tuple[str, ...]]
All: TypeAlias = Final[tuple[str, ...]]
MISSING: Literal[_Sentinel.MISSING] = _Sentinel.MISSING
BenchmarkProgenitor: TypeAlias = SkeletalBaseBenchmark
# NewType is tedious here, simple aliasing aids in legible IDE reccomendations
Name: TypeAlias = str | None
MilliSeconds: type[float] = float
PerfDeltaMSec: TypeAlias = MilliSeconds
ProcessDeltaMsec: TypeAlias = MilliSeconds
FormatHook: TypeAlias = Callable[[TimingReport], str]
PostBenchmarkHook: TypeAlias = Callable[[ContraBenchmark], None]
