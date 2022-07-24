from __future__ import annotations
from collections.abc import Callable, Awaitable
from typing import Generic, ParamSpec, TypeVar
from abc import ABC, abstractmethod
from .helpers import AutoRepr

R = TypeVar("R")
P = ParamSpec("P")


class BaseBenchmark(AutoRepr, ABC, Generic[P, R]):
    @abstractmethod
    def __call__(self, *args: P.args, **kwds: P.kwargs) -> R:
        ...

    def time_format_hook(self):
        pass

    def show_performance(self) -> None:
        print(self)

    @property
    @abstractmethod
    def function(self) -> Callable[P, R]:
        ...


class AsyncBaseBenchmark(Awaitable[R], BaseBenchmark[P, R]):
    @property
    @abstractmethod
    def function(self) -> Callable[P, Awaitable[R]]:
        ...
