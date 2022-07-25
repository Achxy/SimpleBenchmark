from typing import Literal
from .abstract import BaseBenchmark
from collections.abc import Callable
from .typeshack import P, R, MISSING
from time import perf_counter, process_time
from .helpers import get_name


NOT_MEASUREd_EXC_MSG = "{name} has not been called to obtain benchmark time"


class SyncBenchmark(BaseBenchmark[P, R]):
    def __init__(self, func: Callable[P, R]) -> None:
        self._func = func
        self._result: R | Literal[MISSING] = MISSING
        self._process_delta: float | None = None
        self._perf_delta: float | None = None

    def benchmark(self, *args: P.args, **kwargs: P.kwargs) -> R:
        pc, pt = perf_counter(), process_time()
        ret: R = self.function(*args, **kwargs)
        self._perf_delta = perf_counter() - pc
        self._process_delta = process_time() - pt
        self.show_performance()
        return ret

    @property
    def function(self) -> Callable[P, R]:
        return self._func

    @property
    def process_time_delta(self) -> float:
        if self._process_delta is None:
            raise
        return self._process_delta
