NOT_MEASUREd_EXC_MSG = "{name} has not been called to obtain benchmark time"


class TimeNotMeasuredError(RuntimeError):
    def __init__(self, name) -> None:
        msg = NOT_MEASUREd_EXC_MSG.format(name=name)
        super().__init__(msg)
