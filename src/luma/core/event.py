class DEFAULT_EVENTS_ENUM:
    KEYPRESS = "keypress"
    KEYUP = "keyup"
    QUIT = "quit"


class Luma_Event:
    def __init__(self, name: str, callback_=None):
        self.name = name

        self.callbacks = [callback_]

    def dispatch(self, *args):
        for c in self.callbacks:
            if callable(c):
                c(*args)


class Luma_EventManager:
    def __init__(self):
        self._events = {}

    def new_event_callback(self, name, callback_):
        if self._events.get(name):
            self._events[name].callbacks.append(callback_)
        else:
            self._events[name] = Luma_Event(name, callback_)

    def dispatch(self, name, *args):
        event = self._events.get(name)
        if not event or not hasattr(event, "callbacks"):
            return

        event.dispatch(*args)
