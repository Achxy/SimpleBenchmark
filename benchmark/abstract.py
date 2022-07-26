from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Awaitable, Callable
from typing import Generic

from .containers import TimingReport
from .helpers import AutoRepr
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
