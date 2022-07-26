from __future__ import annotations
from collections.abc import Callable, Awaitable
from typing import Generic
from abc import ABC, abstractmethod
from .helpers import AutoRepr
from .typeshack import MISSING, P, R, Q
from .containers import TimingReport


class BaseBenchmark(AutoRepr, ABC, Generic[P, R]):
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        return self.benchmark(*args, **kwargs)

    def __str__(self) -> str:
        report = TimingReport.from_benchmark(self)
        return self.format_hook(report)

    @abstractmethod
    def benchmark(self, *args: P.args, **kwargs: P.kwargs) -> R:
        ...

    @abstractmethod
    def format_hook(self, report: TimingReport) -> str:
        pass

    @abstractmethod
    def post_benchmark_hook(self) -> None:
        ...

    @abstractmethod
    def get_result(self, sentinel: Q = MISSING) -> R | Q:
        ...

    def show_performance(self) -> None:
        print(self)

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


class AsyncBaseBenchmark(Awaitable[R], BaseBenchmark[P, R]):
    @property
    @abstractmethod
    def function(self) -> Callable[P, Awaitable[R]]:
        ...

    @property
    @abstractmethod
    def coroutine(self) -> Awaitable[R]:
        ...
