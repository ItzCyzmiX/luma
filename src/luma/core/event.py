from enum import Enum
from typing import Callable


class DEFAULT_EVENTS_ENUM(Enum):
    KEYPRESS = "keypress"
    KEYUP = "keyup"
    QUIT = "quit"


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
