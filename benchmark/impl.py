from benchmark.containers import TimingReport
from .mixin import PartialBenchmarkMixin
from .helpers import get_name
from ._internals import default_format_hook, default_post_benchmark_hook
from .typeshack import (
    P,
    R,
    FormatHook,
    PerfDeltaMSec,
    Name,
    ProcessDeltaMsec,
    PostBenchmarkHook,
)
from collections.abc import Callable


class SyncBenchmark(PartialBenchmarkMixin[P, R]):
    def __init__(
        self,
        callable: Callable[P, R],
        *,
        name: Name,
        external_format_hook: FormatHook,
        external_post_benchmark_hook: PostBenchmarkHook,
    ) -> None:
        self._name = name
        self._fmt_hook = external_format_hook
        self._post_bench_hook = external_post_benchmark_hook
        super().__init__(callable)

    def format_hook(self, report: TimingReport) -> str:
        return self._fmt_hook(report)

    def post_benchmark_hook(self):
        self._post_bench_hook(self)

    @property
    def name(self):
        if self._name is None:
            return get_name(self.function, "<anonymous>")
        return self._name

    @name.setter
    def name_setter(self, name: str):
        if not isinstance(name, str):
            raise TypeError(f"New name should be a str instance, got {name!r}")
        self._name = name
