from __future__ import annotations
from typing import NamedTuple, TYPE_CHECKING
from .typeshack import PerfDeltaMSec, ProcessDeltaMsec

if TYPE_CHECKING:
    from .impl import SyncBenchmark


class TimingReport(NamedTuple):
    instance: SyncBenchmark
    perf_delta: PerfDeltaMSec
    process_delta: ProcessDeltaMsec

    @classmethod
    def from_benchmark(cls, instance) -> TimingReport:
        pf = instance.perf_counter_delta
        pt = instance.process_time_delta
        return cls(instance=instance, perf_delta=pf, process_delta=pt)
