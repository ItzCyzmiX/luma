import ctypes
from typing import TYPE_CHECKING, Literal

from luma.sdl.consts import SDL_EVENT
from luma.sdl.event import SDL_Event
from luma.sdl.sdl3 import SDL3Bindings

if TYPE_CHECKING:
    from luma.core.engine import Luma


class Luma_Mouse:
    LEFT_BUTTON = "L"
    RIGHT_BUTTON = "R"
    MIDDLE_BUTTON = "M"

    def __init__(self, sdl: "Luma"):
        self.engine = sdl
        self._x = ctypes.c_float()
        self._y = ctypes.c_float()
        self._buttons_held: set[Literal["L", "M", "R"]] = set()

    @property
    def sdl(self) -> SDL3Bindings:
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

    def isButtonHeld(self, button: Literal["L", "M", "R"]):
        return button in self._buttons_held

    def currentPressed(self):
        return self._buttons_held


def mouse_down_and_up(luma: "Luma", event: SDL_Event):
    from luma.core.event import DEFAULT_EVENTS_ENUM

    button = ""
    try:
        button = ["L", "M", "R"][event.button.button - 1]
        if event.type == SDL_EVENT.SDL_EVENT_MOUSE_DOWN:
            luma.Mouse._buttons_held.add(button)
        else:
            luma.Mouse._buttons_held.discard(button)
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
