import ctypes
from typing import TYPE_CHECKING

from luma.sdl.consts import SDL_EVENT
from luma.sdl.event import SDL_Event

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


def mouse_down_and_up(luma: "Luma", event: SDL_Event):
    from luma.core.event import DEFAULT_EVENTS_ENUM

    button = ""
    try:
        button = ["L", "M", "R"][event.button.button - 1]
    except IndexError:
        pass

    luma.event_manager.dispatch(
        DEFAULT_EVENTS_ENUM.MOUSEPRESS
        if event.type == SDL_EVENT.SDL_EVENT_MOUSE_DOWN
        else DEFAULT_EVENTS_ENUM.MOUSEUP,
        button,
        (event.button.x, event.button.y),
        event.button.clicks,
    )


def mouse_motion(luma: "Luma", event: SDL_Event):
    from luma.core.event import DEFAULT_EVENTS_ENUM

    luma.event_manager.dispatch(
        DEFAULT_EVENTS_ENUM.MOUSEMOTION,
        (event.motion.x, event.motion.y),
        (event.motion.relx, event.motion.rely),
    )
    luma.Mouse._set_pos((event.motion.x, event.motion.y))
