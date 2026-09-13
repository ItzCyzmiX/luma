import ctypes

from typing import TYPE_CHECKING
from luma.sdl.shapes import SDL_Rect

if TYPE_CHECKING:
    from luma.core.engine import Luma


class Luma_Graphics:
    OPAQUE = 255
    TRANSPARENT = 0
    RED = (255, 0, 0, 255)
    GREEN = (0, 255, 0, 255)
    BLUE = (0, 0, 255, 255)
    BLACK = (0, 0, 0, 255)
    WHITE = (255, 255, 255, 255)

    def __init__(self, sdl: "Luma"):
        self.engine = sdl
        self._setup_functions()

    def _setup_functions(self):
        self.sdl.SDL_SetRenderDrawColor.argtypes = [
            ctypes.c_void_p,
            ctypes.c_uint8,
            ctypes.c_uint8,
            ctypes.c_uint8,
            ctypes.c_uint8,
        ]

        self.sdl.SDL_SetRenderDrawColor.restype = ctypes.c_bool

        self.sdl.SDL_RenderRect.argtypes = [ctypes.c_void_p, ctypes.POINTER(SDL_Rect)]

        self.sdl.SDL_RenderRect.restype = ctypes.c_bool

        self.sdl.SDL_RenderFillRect.argtypes = [
            ctypes.c_void_p,
            ctypes.POINTER(SDL_Rect),
        ]

        self.sdl.SDL_RenderFillRect.restype = ctypes.c_bool

    @property
    def renderer(self):
        return self.engine.renderer

    @property
    def sdl(self):
        return self.engine.sdl

    def setDrawColor(self, *args):
        if len(args) == 1 and isinstance(args[0], (tuple, list)):
            args = args[0]

        r, g, b, *alpha = args
        a = alpha[0] if alpha else 255

        self.sdl.SDL_SetRenderDrawColor(self.renderer, r, g, b, a)

    def resetDrawColor(self):
        self.sdl.SDL_SetRenderDrawColor(self.renderer, 0, 0, 0, 255)

    def drawRect(self, x, y, w, h, fill: bool = True):
        if fill:
            self.sdl.SDL_RenderFillRect(self.renderer, SDL_Rect(x, y, w, h))
        else:
            self.sdl.SDL_RenderRect(self.renderer, SDL_Rect(x, y, w, h))
