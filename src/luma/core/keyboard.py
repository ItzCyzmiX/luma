from typing import TYPE_CHECKING

from luma.sdl.event import SDL_Event
from luma.sdl.keys import KEYS

if TYPE_CHECKING:
    from luma.core.engine import Luma


def key_down(luma: "Luma", event: SDL_Event):
    from luma.core.event import DEFAULT_EVENTS_ENUM

    if KEYS(event.key.key) not in luma._keys_pressed:
        luma.event_manager.dispatch(DEFAULT_EVENTS_ENUM.KEYPRESS, KEYS(event.key.key))

    luma._keys_pressed.add(KEYS(event.key.key))


def key_up(luma: "Luma", event: SDL_Event):
    from luma.core.event import DEFAULT_EVENTS_ENUM

    luma._keys_pressed.discard(KEYS(event.key.key))

    luma.event_manager.dispatch(DEFAULT_EVENTS_ENUM.KEYUP, KEYS(event.key.key))
