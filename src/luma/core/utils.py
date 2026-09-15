import os
import sys
from platform import system


def get_sdl_path() -> str:
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS  # type: ignore
    else:
        base = os.path.dirname(__file__)

    lib_ext = "dll"

    if system() == "Linux":
        lib_ext = "so"
    elif system() == "Darwin":
        lib_ext = "dylib"

    return os.path.join(base, f"src/luma/lib/SDL3.{lib_ext}")


def get_sdl_image_path() -> str:
    if getattr(sys, "frozen", False):
        base = sys._MEIPASS  # type: ignore
    else:
        base = os.path.dirname(__file__)

    lib_ext = "dll"

    if system() == "Linux":
        lib_ext = "so"
    elif system() == "Darwin":
        lib_ext = "dylib"

    return os.path.join(base, f"src/luma/lib/SDL3_image.{lib_ext}")
