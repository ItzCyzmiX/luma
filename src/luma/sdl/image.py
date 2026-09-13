import ctypes

from luma.sdl.bindings import NativeBindings
from luma.sdl.surface import SDL_Surface


class SDLImageBindings(NativeBindings):
    def __init__(self, library: ctypes.CDLL):
        super().__init__(library)
        self.load = self.bind(
            "IMG_Load", [ctypes.c_char_p], ctypes.POINTER(SDL_Surface)
        )
