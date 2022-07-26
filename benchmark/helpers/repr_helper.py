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
from typing import final

from .helper import repr_fmt


class AutoRepr:
    __slots__ = ("__repr_data__",)

    def __new__(cls: type, *args, **kwargs):
        self = super().__new__(cls)
        self.__repr_data__ = args, kwargs
        return self

    @final
    def __repr__(self) -> str:
        cls = type(self)
        args, kwargs = self.__repr_data__
        return repr_fmt(cls, *args, **kwargs)
