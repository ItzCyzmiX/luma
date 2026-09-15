import ctypes
import os
import sys
from collections.abc import Callable
from platform import system

from luma.core.error import Luma_Error
from luma.core.event import DEFAULT_EVENTS_ENUM, Luma_EventManager
from luma.core.font import Luma_Font, Luma_Text
from luma.core.graphics import Luma_Graphics
from luma.core.keyboard import Luma_Keyboard
from luma.core.mouse import Luma_Mouse
from luma.core.sprite import Luma_SpriteCreator
from luma.core.utils import get_sdl_image_path, get_sdl_path, get_sdl_ttf_path
from luma.sdl.consts import SDL_BLENDMODE, SDL_EVENT, SDL_INIT
from luma.sdl.event import SDL_Event
from luma.sdl.font import SDLTTFBindings
from luma.sdl.image import SDLImageBindings
from luma.sdl.sdl3 import SDL3Bindings


class Luma:
    EVENTS = DEFAULT_EVENTS_ENUM

    def __init__(
        self,
        sdl_path: str | None = None,
        sdl_image_path: str | None = None,
        sdl_ttf_path: str | None = None,
    ):
        self.window = None
        self.renderer = None

        if getattr(sys, "frozen", False) and system() == "Windows":
            os.add_dll_directory(os.path.join(sys._MEIPASS, "luma", "lib"))

        self.sdl_path = sdl_path or get_sdl_path()
        self.sdl_image_path = sdl_image_path or get_sdl_image_path()
        self.sdl_font_path = sdl_ttf_path or get_sdl_ttf_path()
        self.sdl = SDL3Bindings(ctypes.CDLL(self.sdl_path))
        self.sdl_image = SDLImageBindings(ctypes.CDLL(self.sdl_image_path))
        self.sdl_ttf = SDLTTFBindings(ctypes.CDLL(self.sdl_font_path))

        self.running = True

        self._draw_method = None
        self._update_method = None
        self._init_method = None

        self.event_manager = Luma_EventManager()
        self.Mouse = Luma_Mouse(self)
        self.Keyboard = Luma_Keyboard(self)
        self.Sprite = Luma_SpriteCreator(self)

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

        self.Graphics = Luma_Graphics(self)
        self.Font = Luma_Font(self)

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

    def run(self):
        if not self.window or not self.renderer or not self.Graphics:
            return

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

                    event_func = self.event_manager._events_dispatch_table.get(
                        event.type
                    )

                    if callable(event_func):
                        event_func(self, event)

                if callable(self._update_method):
                    self._update_method(dt)

                self.sdl.set_render_draw_color(
                    self.renderer, *self.Graphics.backgroudColor
                )

                self.sdl.render_clear(self.renderer)

                if callable(self._draw_method):
                    self._draw_method()

                self.sdl.render_present(self.renderer)

        except Exception:
            self._cleanup()
            raise

        finally:
            self._cleanup()

    def quit(self):
        self.running = False

    def _cleanup(self):
        self.event_manager.dispatch(Luma.EVENTS.QUIT)

        self.running = False

        if self.Font:
            self.Font._cleanup()

        if self.renderer:
            self.sdl.destroy_renderer(self.renderer)
        if self.window:
            self.sdl.destroy_window(self.window)

        self.sdl.quit()
