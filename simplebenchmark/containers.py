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
from __future__ import annotations

from typing import TYPE_CHECKING, NamedTuple

from .typeshack import PerfDeltaMSec, ProcessDeltaMsec

if TYPE_CHECKING:
    from .abstract import SkeletalBaseBenchmark


class TimingReport(NamedTuple):
    instance: SkeletalBaseBenchmark
    perf_delta: PerfDeltaMSec
    process_delta: ProcessDeltaMsec

    @classmethod
    def from_benchmark(cls, instance) -> TimingReport:
        pf = instance.perf_counter_delta
        pt = instance.process_time_delta
        return cls(instance=instance, perf_delta=pf, process_delta=pt)
