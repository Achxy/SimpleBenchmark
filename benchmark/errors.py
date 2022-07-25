_FRAGMENTARY_CAUSE_MSG = "Benchmarking object has not been invoked to obtain values such as result, \
time delta and other runtime obtainable assesssments"


class BenchmarkingError(Exception):
    pass


class FragmentaryBenchmarkError(BenchmarkingError):
    def __init__(self, msg: str = _FRAGMENTARY_CAUSE_MSG, *args) -> None:
        super().__init__(msg, *args)
