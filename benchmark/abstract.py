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
from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Awaitable, Callable
from typing import Generic

from ._repr_helper import AutoRepr
from .containers import TimingReport
from .typeshack import MISSING, P, Q, R


class SkeletalBaseBenchmark(AutoRepr, ABC, Generic[P, R]):
    @abstractmethod
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...

    @abstractmethod
    def benchmark(self, *args: P.args, **kwargs: P.kwargs) -> R:
        ...

    @abstractmethod
    def format_hook(self, report: TimingReport) -> str:
        pass

    @abstractmethod
    def post_benchmark_hook(self) -> None:
        ...

    @property
    @abstractmethod
    def function(self) -> Callable[P, R]:
        ...

    @property
    @abstractmethod
    def result(self) -> R:
        ...

    @property
    @abstractmethod
    def perf_counter_delta(self) -> float:
        ...

    @property
    @abstractmethod
    def process_time_delta(self) -> float:
        ...


class AsyncSkeletalBaseBenchmark(Awaitable[R], SkeletalBaseBenchmark[P, R]):
    @property
    @abstractmethod
    def function(self) -> Callable[P, Awaitable[R]]:
        ...

    @property
    @abstractmethod
    def coroutine(self) -> Awaitable[R]:
        ...
