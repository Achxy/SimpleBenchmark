from typing import Literal
from .abstract import SkeletalBaseBenchmark
from collections.abc import Callable
from .typeshack import P, R, MISSING, Q
from time import perf_counter, process_time
from .helpers import get_name
from .errors import FragmentaryBenchmarkError
from .containers import TimingReport


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
    def process_time_delta(self) -> float:
        if self._process_delta is None:
            raise FragmentaryBenchmarkError()
        return self._process_delta

    @property
    def perf_counter_delta(self) -> float:
        if self._perf_delta is None:
            raise FragmentaryBenchmarkError()
        return self._perf_delta

    @property
    def time_report(self) -> TimingReport:
        return TimingReport.from_benchmark(self)
