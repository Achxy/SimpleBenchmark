from __future__ import annotations
from collections.abc import Callable, Awaitable
from typing import Generic
from abc import ABC, abstractmethod
from .helpers import AutoRepr
from .typeshack import P, R


class BaseBenchmark(AutoRepr, ABC, Generic[P, R]):
    def __call__(self, *args: P.args, **kwargs: P.kwargs) -> R:
        return self.benchmark(*args, **kwargs)

    def __str__(self) -> str:
        return self.format_hook(self.perf_counter_delta, self.process_time_delta)

    @abstractmethod
    def benchmark(self, *args: P.args, **kwargs: P.kwargs) -> R:
        ...

    @abstractmethod
    def format_hook(self, perf_delta_sec: float, process_time_delta_sec: float) -> str:
        pass

    @abstractmethod
    def post_benchmark_hook(self) -> None:
        ...

    def show_performance(self) -> None:
        print(self)

    @property
    @abstractmethod
    def function(self) -> Callable[P, R]:
        ...

    @property
    @abstractmethod
    def perf_counter_delta(self) -> float:
        ...

    @property
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
