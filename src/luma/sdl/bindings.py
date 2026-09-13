import ctypes
from collections.abc import Sequence


class NativeBindings:
    def __init__(self, library: ctypes.CDLL):
        self.library = library

    def bind(
        self,
        name: str,
        argtypes: Sequence[object] | None = None,
        restype: object = None,
    ):
        try:
            function = getattr(self.library, name)
        except AttributeError as error:
            raise RuntimeError(
                f"Missing native function {name!r} in {self.library._name!r}"
            ) from error

        function.argtypes = list(argtypes or [])
        function.restype = restype
        return function
