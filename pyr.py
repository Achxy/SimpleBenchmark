from typing import ClassVar

Aliased = ClassVar[str]


class Bar:
    var: Aliased = "Some"

    def __init__(self) -> None:
        self.var = "Should fail but doesn't"  # Typechecks fine
