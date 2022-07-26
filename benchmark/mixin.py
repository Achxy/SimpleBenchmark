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
from time import perf_counter, process_time
from typing import Literal

from ._internals import get_name
from .abstract import SkeletalBaseBenchmark
from .containers import TimingReport
from .errors import FragmentaryBenchmarkError
from .typeshack import MISSING, P, PerfDeltaMSec, ProcessDeltaMsec, Q, R


class PartialBenchmarkMixin(SkeletalBaseBenchmark[P, R]):
    def __init__(self, func: Callable[P, R]) -> None:
        self._func: Callable[P, R] = func
        self._result: R | Literal[MISSING] = MISSING
        self._process_delta: float | None = None
        self._perf_delta: float | None = None

    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        return self.benchmark(*args, **kwargs)

    def __str__(self) -> str:
        report = self.time_report
        return self.format_hook(report)

    def benchmark(self, *args: P.args, **kwargs: P.kwargs) -> R:
        pc, pt = perf_counter(), process_time()
        result: R = self.function(*args, **kwargs)
        self._perf_delta = perf_counter() - pc
        self._process_delta = process_time() - pt
        self._result = result
        self.post_benchmark_hook()
        return result

    @property
    def function(self) -> Callable[P, R]:
        return self._func

    @property
    def result(self) -> R:
        if self._result is MISSING:
            raise FragmentaryBenchmarkError()
        return self._result

    @property
    def process_time_delta(self) -> ProcessDeltaMsec:
        if self._process_delta is None:
            raise FragmentaryBenchmarkError()
        return self._process_delta

    @property
    def perf_counter_delta(self) -> PerfDeltaMSec:
        if self._perf_delta is None:
            raise FragmentaryBenchmarkError()
        return self._perf_delta

    @property
    def time_report(self) -> TimingReport:
        return TimingReport.from_benchmark(self)
