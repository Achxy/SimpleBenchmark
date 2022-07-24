from __future__ import annotations
from collections.abc import Callable, Awaitable
from typing import Generic
from abc import ABC, abstractmethod
from .helpers import AutoRepr
from .typeshack import P, R


class BaseBenchmark(AutoRepr, ABC, Generic[P, R]):
    @abstractmethod
    def __call__(self, *args: P.args, **kwds: P.kwargs) -> R:
        ...

    def __str__(self) -> str:
        return self.format_hook(self.perf_counter_delta, self.process_time_delta)

    @abstractmethod
    def format_hook(self, perf_delta_sec: float, process_time_delta_sec: float) -> str:
        pass

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
