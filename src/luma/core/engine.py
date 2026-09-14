import ctypes
import os
import sys
from collections.abc import Callable
from platform import system

from luma.core.error import Luma_Error
from luma.core.event import DEFAULT_EVENTS_ENUM, Luma_EventManager
from luma.core.graphics import Luma_Graphics
from luma.core.mouse import Luma_Mouse
from luma.core.sprite import Luma_SpriteCreator
from luma.sdl.consts import SDL_BLENDMODE, SDL_EVENT, SDL_INIT
from luma.sdl.event import SDL_Event
from luma.sdl.image import SDLImageBindings
from luma.sdl.keys import KEYS as KEYS_
from luma.sdl.sdl3 import SDL3Bindings


def get_sdl_image_path():
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS  # type: ignore
    else:
        base = os.path.dirname(__file__)

    lib_ext = "dll"

    if system() == "Linux":
        lib_ext = "so"
    elif system() == "Darwin":
        lib_ext = "dylib"

    return os.path.join(base, os.path.abspath(f"./src/luma/lib/SDL3_image.{lib_ext}"))


def get_sdl_path():
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS  # type: ignore
    else:
        base = os.path.dirname(__file__)

    lib_ext = "dll"

    if system() == "Linux":
        lib_ext = "so"
    elif system() == "Darwin":
        lib_ext = "dylib"

    return os.path.join(base, os.path.abspath(f"./src/luma/lib/SDL3.{lib_ext}"))


class Luma:
    KEYS = KEYS_

    EVENTS = DEFAULT_EVENTS_ENUM

    def __init__(self, sdl_path: str | None = None, sdl_image_path: str | None = None):
        self.window = None
        self.renderer = None

        self.sdl_path = sdl_path or get_sdl_path()
        self.sdl_image_path = sdl_image_path or get_sdl_image_path()
        self.sdl = SDL3Bindings(ctypes.CDLL(self.sdl_path))
        self.sdl_image = SDLImageBindings(ctypes.CDLL(self.sdl_image_path))

        self.running = True

        self._draw_method = None
        self._update_method = None
        self._init_method = None
        self._keys_pressed: set[KEYS_] = set()

        self.event_manager = Luma_EventManager()
        self.Sprite = Luma_SpriteCreator(self)
        self.graphics = None
        self.Mouse = Luma_Mouse(self)

        if not self.sdl.init(SDL_INIT.SDL_INIT_VIDEO):
            error_msg = self.sdl.get_error()

            raise Luma_Error(error_msg)

    def create_window(self, title: str, width: int, height: int, flags: int = 0):

        self.window = self.sdl.create_window(title.encode(), width, height, flags)

        if not self.window:
            self.quit()
            error_msg = self.sdl.get_error()
            raise Luma_Error(error_msg)

        self.renderer = self.sdl.create_renderer(self.window, None)

        if not self.renderer:
            self.quit()
            error_msg = self.sdl.get_error()

            raise Luma_Error(error_msg)

        if not self.sdl.set_render_draw_blend_mode(
            self.renderer, SDL_BLENDMODE.SDL_BLENDMODE_BLEND
        ):
            self.quit()
            error_msg = self.sdl.get_error()
            raise Luma_Error(error_msg)

        self.graphics = Luma_Graphics(self)

    def start(self, fn: Callable):
        self._init_method = fn

    def draw(self, fn: Callable):
        self._draw_method = fn

    def update(self, fn: Callable):
        self._update_method = fn

    def on(self, event_name: DEFAULT_EVENTS_ENUM):
        def decorator(func):
            self.event_manager.new_event_callback(event_name, func)
            return func

        return decorator

    def isKeyHeld(self, key: KEYS_):

        return key in self._keys_pressed

    def run(self):
        if callable(self._init_method):
            self._init_method()

        lastTime = self.sdl.get_ticks()
        try:
            while self.running:
                now = self.sdl.get_ticks()

                dt = float(now - lastTime) / 1000.0

                lastTime = now
                event = SDL_Event()

                while self.sdl.poll_event(ctypes.byref(event)):
                    if event.type == SDL_EVENT.SDL_EVENT_QUIT:
                        self.running = False
                        break

                    if event.type == SDL_EVENT.SDL_EVENT_KEY_DOWN:
                        if Luma.KEYS(event.key.key) not in self._keys_pressed:
                            self.event_manager.dispatch(
                                Luma.EVENTS.KEYPRESS, Luma.KEYS(event.key.key)
                            )

                        self._keys_pressed.add(Luma.KEYS(event.key.key))

                    if event.type == SDL_EVENT.SDL_EVENT_KEY_UP:
                        self._keys_pressed.discard(Luma.KEYS(event.key.key))

                        self.event_manager.dispatch(
                            Luma.EVENTS.KEYUP, Luma.KEYS(event.key.key)
                        )

                    if (
                        event.type == SDL_EVENT.SDL_EVENT_MOUSE_DOWN
                        or event.type == SDL_EVENT.SDL_EVENT_MOUSE_UP
                    ):
                        button = ""
                        try:
                            button = ["L", "M", "R"][event.button.button - 1]
                        except IndexError:
                            pass
                        self.event_manager.dispatch(
                            Luma.EVENTS.MOUSEPRESS
                            if event.type == SDL_EVENT.SDL_EVENT_MOUSE_DOWN
                            else Luma.EVENTS.MOUSEUP,
                            button,
                            (event.button.x, event.button.y),
                            event.button.clicks,
                        )

                    if event.type == SDL_EVENT.SDL_EVENT_MOUSE_MOTION:
                        self.event_manager.dispatch(
                            Luma.EVENTS.MOUSEMOTION,
                            (event.motion.x, event.motion.y),
                            (event.motion.relx, event.motion.rely),
                        )
                        self.Mouse._set_pos((event.motion.x, event.motion.y))

                if callable(self._update_method):
                    self._update_method(dt)

                self.sdl.render_clear(self.renderer)

                if callable(self._draw_method):
                    self._draw_method()

                self.sdl.render_present(self.renderer)

        except Exception as e:
            self.quit()

            raise e

        finally:
            self.quit()

    def quit(self):
        if self.renderer:
            self.sdl.destroy_renderer(self.renderer)
        if self.window:
            self.sdl.destroy_window(self.window)

        self.sdl.quit()

        self.event_manager.dispatch(Luma.EVENTS.QUIT)
