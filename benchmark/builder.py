from typing import Literal
from .abstract import BaseBenchmark
from collections.abc import Callable
from .typeshack import P, R, MISSING, Q
from time import perf_counter, process_time
from .helpers import get_name
from .errors import FragmentaryBenchmarkError


class PartialBenchmark(BaseBenchmark[P, R]):
    def __init__(self, func: Callable[P, R]) -> None:
        self._func: Callable[P, R] = func
        self._result: R | Literal[MISSING] = MISSING
        self._process_delta: float | None = None
        self._perf_delta: float | None = None

    def post_benchmark_hook(self) -> None:
        self.show_performance()

    def get_result(self, sentinel: Q = MISSING) -> R | Q:
        if self._result is MISSING:
            if sentinel is MISSING:
                msg = "Benchmark objects have not been invoked and a sentinel argument has not been provided"
                raise RuntimeError(msg) from FragmentaryBenchmarkError()
            return sentinel
        return self._result

    @property
    def function(self) -> Callable[P, R]:
        return self._func

    @property
    def result(self) -> R:
        if self._result is MISSING:
            raise FragmentaryBenchmarkError()
        return self._result

    @property
    def process_time_delta(self) -> float:
        if self._process_delta is None:
            raise FragmentaryBenchmarkError()
        return self._process_delta

    @property
    def perf_counter_delta(self) -> float:
        if self._perf_delta is None:
            raise FragmentaryBenchmarkError()
        return self._perf_delta


class SyncBenchmarkBuilder(PartialBenchmark[P, R]):
    def benchmark(self, *args: P.args, **kwargs: P.kwargs) -> R:
        pc, pt = perf_counter(), process_time()
        result: R = self.function(*args, **kwargs)
        self._perf_delta = perf_counter() - pc
        self._process_delta = process_time() - pt
        self._result = result
        self.post_benchmark_hook()
        return result
