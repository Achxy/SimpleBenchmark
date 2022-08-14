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
from ._helpers import get_name
from .abstract import SkeletalBaseBenchmark
from .containers import TimingReport


def default_format_hook(report: TimingReport) -> str:
    name = get_name(report.instance.function, "<anonymous>")
    result = report.instance.result
    pf, pt = report.perf_delta, report.process_delta
    return f"{name} took {pf:.2f} Δperf msec and {pt:.2f} Δprocess msec and returned <{result!r}>"


def default_post_benchmark_hook(instance: SkeletalBaseBenchmark) -> None:
    print(instance)
