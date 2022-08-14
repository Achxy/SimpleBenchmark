"""
SimpleBenchmark is a tool for benchmarking callable objects in Python.
Copyright (C) 2022-present  Achxy

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from collections.abc import Callable

from ._internals import default_format_hook, default_post_benchmark_hook
from .impl import SyncBenchmark
from .typeshack import FormatHook, P, PostBenchmarkHook, R


def sync_benchmark(
    format_hook: FormatHook = default_format_hook,
    post_benchmark_hook: PostBenchmarkHook = default_post_benchmark_hook,
) -> Callable[[Callable[P, R]], SyncBenchmark[P, R]]:
    def wrapper(callable: Callable[P, R]) -> SyncBenchmark[P, R]:
        return SyncBenchmark[P, R](
            callable=callable,
            external_format_hook=format_hook,
            external_post_benchmark_hook=post_benchmark_hook,
        )

    return wrapper
