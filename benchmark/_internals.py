from .typeshack import AnyBenchmark, PerfDeltaMSec, ProcessDeltaMsec
from .containers import TimingReport


def default_format_hook(report: TimingReport) -> str:
    name = report.instance.name
    result = report.instance.result
    pf, pt = report.perf_delta, report.process_delta
    return f"{name} took {pf:.2f} Δperf msec and {pt:.2f} Δprocess msec and returned <{result!r}>"


def default_post_benchmark_hook(instance) -> None:
    print(instance)
