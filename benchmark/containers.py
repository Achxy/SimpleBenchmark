from typing import NamedTuple
from .typeshack import AnyBenchmark, PerfDeltaMSec, ProcessDeltaMsec, AllBenchmark


class TimingReport(NamedTuple):
    instance: AllBenchmark
    perf_delta: PerfDeltaMSec
    process_delta: ProcessDeltaMsec

    @classmethod
    def from_benchmark(cls, instance):
        pf = instance.perf_counter_delta
        pt = instance.process_time_delta
        return cls(instance=instance, perf_delta=pf, process_delta=pt)
