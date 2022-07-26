from .implementation import SyncBenchmark
from collections.abc import Callable
from .typeshack import P, R, MilliSeconds, FormatHook
from .helpers import same_return


def sync_benchmark(
    name: str | None = None,
    format_hook: FormatHook | None = None,
) -> Callable[[Callable[P, R]], SyncBenchmark[P, R]]:
    def wrapper(func: Callable[P, R]) -> SyncBenchmark[P, R]:
        return SyncBenchmark[P, R](func, name=name)

    return wrapper
