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

from .typeshack import Slots

_FRAGMENTARY_CAUSE_MSG = "Benchmarking object has not been invoked to obtain values such as result, \
time delta and other runtime obtainable assesssments"


class BenchmarkingError(Exception):
    __slots__: Slots = ()


class FragmentaryBenchmarkError(BenchmarkingError):
    __slots__: Slots = ()

    def __init__(self, msg: str = _FRAGMENTARY_CAUSE_MSG, *args) -> None:
        super().__init__(msg, *args)
