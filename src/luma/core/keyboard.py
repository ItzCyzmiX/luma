from typing import TYPE_CHECKING

from luma.sdl.event import SDL_Event
from luma.sdl.keys import KEYS as KEYS_

if TYPE_CHECKING:
    from luma.core.engine import Luma


class Luma_Keyboard:
    KEYS = KEYS_

    def __init__(self, engine: "Luma"):
        self.engine = engine
        self._keys_pressed: set[KEYS] = set() 

    @property
    def sdl(self):
        return self.engine.sdl

    def isKeyHeld(self, key):
        return key in self._keys_pressed

    def isAnyPressed(self):
        return len(self._keys_pressed) > 0

    def currentPressed(self):
        return self._keys_pressed

    def keyToKeyCode(self, key: str):
        return KEYS(self.sdl.get_keycode_from_name(key.encode()))


def key_down(luma: "Luma", event: SDL_Event):
    from luma.core.event import DEFAULT_EVENTS_ENUM

    if KEYS(event.key.key) not in luma.Keyboard.currentPressed():
        luma.event_manager.dispatch(DEFAULT_EVENTS_ENUM.KEYPRESS, KEYS(event.key.key))

    luma.Keyboard._keys_pressed.add(KEYS(event.key.key))


def key_up(luma: "Luma", event: SDL_Event):
    from luma.core.event import DEFAULT_EVENTS_ENUM

    luma.Keyboard._keys_pressed.discard(KEYS(event.key.key))

    luma.event_manager.dispatch(DEFAULT_EVENTS_ENUM.KEYUP, KEYS(event.key.key))
