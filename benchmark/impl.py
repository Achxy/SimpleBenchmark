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

from benchmark.containers import TimingReport

from ._internals import default_format_hook, default_post_benchmark_hook, get_name
from .mixin import PartialBenchmarkMixin
from .typeshack import (
    FormatHook,
    Name,
    P,
    PerfDeltaMSec,
    PostBenchmarkHook,
    ProcessDeltaMsec,
    R,
    Slots,
)


class SyncBenchmark(PartialBenchmarkMixin[P, R]):
    __slots__: Slots = ()

    def __init__(
        self,
        callable: Callable[P, R],
        *,
        name: Name,
        external_format_hook: FormatHook,
        external_post_benchmark_hook: PostBenchmarkHook,
    ) -> None:
        self._name: Name = name
        self._fmt_hook: FormatHook = external_format_hook
        self._post_bench_hook: PostBenchmarkHook = external_post_benchmark_hook
        super().__init__(callable)

    def format_hook(self, report: TimingReport) -> str:
        return self._fmt_hook(report)

    def post_benchmark_hook(self):
        self._post_bench_hook(self)

    @property
    def name(self):
        if self._name is None:
            return get_name(self.function, "<anonymous>")
        return self._name

    @name.setter
    def name_setter(self, name: str):
        if not isinstance(name, str):
            raise TypeError(f"New name should be a str instance, got {name!r}")
        self._name = name
