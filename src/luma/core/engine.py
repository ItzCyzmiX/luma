import ctypes
import os
from luma.sdl.event import SDL_Event
from luma.graphics.graphics import Luma_Graphics
import luma.sdl.keys


class Luma:

    SDL_INIT_AUDIO = 0x10
    SDL_INIT_VIDEO = 0x20
    SDL_INIT_JOYSTICK = 0x200
    SDL_INIT_HAPTIC = 0x1000
    SDL_INIT_GAMEPAD = 0x2000
    SDL_INIT_EVENTS = 0x4000
    SDL_INIT_SENSOR = 0x8000
    SDL_INIT_CAMERA = 0x10000
    SDL_EVENT_QUIT = 0x100
    SDL_BLENDMODE_BLEND = 0x00000001

    SDL_EVENT_KEY_DOWN = 0x300
    SDL_EVENT_KEY_UP = 0x301

    KEYS = luma.sdl.keys

    def __init__(self, sdl_path: str | None = None):
        self.window = None
        self.renderer = None
        self.sdl_path = sdl_path or os.path.abspath("./src/luma/lib/SDL3.dll")
        self.sdl = ctypes.CDLL(self.sdl_path)
        self._setup_functions()
        self.graphics = None

        self.running = True
        self._draw_method = None
        self._update_method = None

        self._keys_pressed = set()

        self.sdl.SDL_Init(Luma.SDL_INIT_VIDEO)

    def _setup_functions(self):
        self.sdl.SDL_CreateWindow.argtypes = [
            ctypes.c_char_p,  # title
            ctypes.c_int,  # w
            ctypes.c_int,  # h
            ctypes.c_uint64,  # SDL_WindowFlags
        ]

        self.sdl.SDL_CreateWindow.restype = ctypes.c_void_p

        self.sdl.SDL_CreateRenderer.argtypes = [
            ctypes.c_void_p,  # window
            ctypes.c_char_p,  # renderer name
        ]

        self.sdl.SDL_CreateRenderer.restype = ctypes.c_void_p

        self.sdl.SDL_RenderClear.argtypes = [
            ctypes.c_void_p,  # renderer
        ]

        self.sdl.SDL_RenderClear.restype = ctypes.c_bool

        self.sdl.SDL_RenderPresent.argtypes = [
            ctypes.c_void_p,  # renderer
        ]

        self.sdl.SDL_RenderPresent.restype = ctypes.c_bool

        self.sdl.SDL_DestroyRenderer.argtypes = [
            ctypes.c_void_p,  # renderer
        ]

        self.sdl.SDL_DestroyRenderer.restype = ctypes.c_void_p

        self.sdl.SDL_DestroyWindow.argtypes = [
            ctypes.c_void_p,  # window
        ]

        self.sdl.SDL_DestroyWindow.restype = ctypes.c_void_p

        self.sdl.SDL_PollEvent.argtypes = [ctypes.POINTER(SDL_Event)]

        self.sdl.SDL_PollEvent.restype = ctypes.c_bool

        self.sdl.SDL_GetTicks.restype = ctypes.c_uint64

        self.sdl.SDL_SetRenderDrawBlendMode.argtypes = [
            ctypes.c_void_p,
            ctypes.c_uint64,
        ]

        self.sdl.SDL_SetRenderDrawBlendMode.restype = ctypes.c_bool

    def create_window(self, title: str, width: int, height: int, flags: int = 0):

        self.window = self.sdl.SDL_CreateWindow(title.encode(), width, height, flags)

        if self.window is None:
            self.quit()

        self.renderer = self.sdl.SDL_CreateRenderer(self.window, None)

        if self.renderer is None:
            self.quit()

        self.sdl.SDL_SetRenderDrawBlendMode(self.renderer, Luma.SDL_BLENDMODE_BLEND)

        self.graphics = Luma_Graphics(self)

    def draw(self, fn):
        self._draw_method = fn

    def update(self, func):
        self._update_method = func

    def isKeyPressed(self, key: str):
        return key in self._keys_pressed

    def run(self):
        lastTime = self.sdl.SDL_GetTicks()
        try:
            while self.running:

                now = self.sdl.SDL_GetTicks()

                dt = float(now - lastTime) / 1000.0

                lastTime = now
                event = SDL_Event()

                while self.sdl.SDL_PollEvent(ctypes.byref(event)):
                    if event.type == Luma.SDL_EVENT_QUIT:
                        self.running = False
                        break

                    if event.type == Luma.SDL_EVENT_KEY_DOWN:
                        self._keys_pressed.add(event.key.key)

                    if event.type == Luma.SDL_EVENT_KEY_UP:
                        try:

                            self._keys_pressed.remove(event.key.key)
                        except KeyError:
                            pass

                if callable(self._update_method):
                    self._update_method(dt)

                self.sdl.SDL_RenderClear(self.renderer)

                if callable(self._draw_method):
                    self._draw_method()

                self.sdl.SDL_RenderPresent(self.renderer)

        except Exception as e:
            print(e)

        finally:
            self.quit()

    def quit(self):
        if self.renderer:
            self.sdl.SDL_DestroyRenderer(self.renderer)
        if self.window:
            self.sdl.SDL_DestroyWindow(self.window)

        self.sdl.SDL_Quit()
