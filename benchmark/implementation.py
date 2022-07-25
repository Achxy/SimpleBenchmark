from .builder import SyncBenchmarkBuilder
from .helpers import get_name
from .typeshack import P, R
from collections.abc import Callable


class SyncBenchmark(SyncBenchmarkBuilder[P, R]):
    def __init__(self, func: Callable[P, R], *, name=None) -> None:
        self.name = name
        super().__init__(func)

    def format_hook(self, perf_delta_sec, process_time_delta_sec):
        name = self.name or get_name(self.function, "<anonymous>")
        ret = self.result
        perf_msec, process_msec = perf_delta_sec * 1000, process_time_delta_sec * 1000
        return f"{name} took {perf_msec:.2f} Δperf msec and {process_msec:.2f} Δprocess msec and returned <{ret!r}>"
