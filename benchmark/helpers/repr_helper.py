from .helper import repr_fmt


class AutoRepr:
    __slots__ = ("__repr_data__",)

    def __new__(cls: type, *args, **kwargs):
        self = super().__new__(cls)
        self.__repr_data__ = args, kwargs
        return self

    def __repr__(self) -> str:
        cls = type(self)
        args, kwargs = self.__repr_data__
        return repr_fmt(cls, *args, **kwargs)
