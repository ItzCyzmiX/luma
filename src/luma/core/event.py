from collections.abc import Callable
from enum import Enum

from luma.core.keyboard import key_down, key_up
from luma.core.mouse import mouse_down_and_up, mouse_motion
from luma.sdl.consts import SDL_EVENT


class DEFAULT_EVENTS_ENUM(Enum):
    KEYPRESS = "keypress"
    KEYUP = "keyup"
    QUIT = "quit"
    MOUSEPRESS = "mousepress"
    MOUSEUP = "mouseup"
    MOUSEMOTION = "mousemotion"


class Luma_Event:
    def __init__(self, name: DEFAULT_EVENTS_ENUM, callback_: Callable | None = None):
        self.name = name

        self.callbacks = []

        if callback_ and callable(callback_):
            self.callbacks.append(callback_)

    def dispatch(self, *args):
        for c in self.callbacks:
            if callable(c):
                c(*args)


class Luma_EventManager:
    def __init__(self):
        self._events = {}
        self._events_dispatch_table = {
            SDL_EVENT.SDL_EVENT_KEY_DOWN: key_down,
            SDL_EVENT.SDL_EVENT_KEY_UP: key_up,
            SDL_EVENT.SDL_EVENT_MOUSE_DOWN: mouse_down_and_up,
            SDL_EVENT.SDL_EVENT_MOUSE_UP: mouse_down_and_up,
            SDL_EVENT.SDL_EVENT_MOUSE_MOTION: mouse_motion,
        }

    def new_event_callback(self, name: DEFAULT_EVENTS_ENUM, callback_: Callable):
        if self._events.get(name):
            self._events[name].callbacks.append(callback_)
        else:
            self._events[name] = Luma_Event(name, callback_)

    def dispatch(self, name: DEFAULT_EVENTS_ENUM, *args):
        event = self._events.get(name)
        if not event or not hasattr(event, "callbacks"):
            return

        event.dispatch(*args)
