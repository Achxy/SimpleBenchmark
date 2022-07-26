from collections.abc import Callable

from ._internals import default_format_hook, default_post_benchmark_hook
from .impl import SyncBenchmark
from .typeshack import FormatHook, MilliSeconds, P, PostBenchmarkHook, R


def sync_benchmark(
    name: str | None = None,
    format_hook: FormatHook = default_format_hook,
    post_benchmark_hook: PostBenchmarkHook = default_post_benchmark_hook,
) -> Callable[[Callable[P, R]], SyncBenchmark[P, R]]:
    def wrapper(callable: Callable[P, R]) -> SyncBenchmark[P, R]:
        return SyncBenchmark[P, R](
            callable=callable,
            name=name,
            external_format_hook=format_hook,
            external_post_benchmark_hook=post_benchmark_hook,
        )

    return wrapper
