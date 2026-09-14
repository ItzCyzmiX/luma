import ctypes
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from luma.core.engine import Luma


class Luma_Mouse:
    def __init__(self, sdl: "Luma"):
        self.engine = sdl
        self._x = ctypes.c_float()
        self._y = ctypes.c_float()
        self.get_pos()

    @property
    def sdl(self):
        return self.engine.sdl

    @property
    def x(self) -> float:
        return self._x.value

    @property
    def y(self) -> float:
        return self._y.value

    def get_pos(self) -> tuple[float, float]:
        return (self._x.value, self._y.value)

    def _set_pos(self, pos):
        self._x, self._y = ctypes.c_float(pos[0]), ctypes.c_float(pos[1])
