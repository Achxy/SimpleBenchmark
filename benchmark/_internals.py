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
from typing import Any

from .containers import TimingReport
from .typeshack import BenchmarkProgenitor, PerfDeltaMSec, ProcessDeltaMsec


def get_name(obj: Any, default: str | None = None) -> str:
    ret: Any = getattr(obj, "__name__", default)
    if not isinstance(default, str) and default is not None:
        msg = "Expected default value to be 'str' instance or None"
        raise ValueError(msg)
    if ret is None:
        msg = f"{obj!r} has no '__name__' attribute and a default has not been provided"
        raise TypeError(msg)
    if not isinstance(ret, str):
        msg = f"Expected return value of __name__ descriptor to be 'str' instance, got {ret!r} instead"
        raise ValueError(msg)
    return ret


def default_format_hook(report: TimingReport) -> str:
    name = report.instance.name
    result = report.instance.result
    pf, pt = report.perf_delta, report.process_delta
    return f"{name} took {pf:.2f} Δperf msec and {pt:.2f} Δprocess msec and returned <{result!r}>"


def default_post_benchmark_hook(instance: BenchmarkProgenitor) -> None:
    print(instance)
