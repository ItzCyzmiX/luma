import ctypes
import os
import sys
from platform import system

from luma.sdl.image import SDLImageBindings
from luma.sdl.surface import SDL_Surface


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


class SDL_Image:
    def __init__(self, sdl_image_path: str | None = None) -> None:
        self.sdl_image = SDLImageBindings(
            ctypes.CDLL(sdl_image_path or get_sdl_image_path())
        )
