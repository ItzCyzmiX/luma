import os
import sys
from platform import system


def get_lib_path(name: str) -> str:
    if getattr(sys, "frozen", False):
        base = os.path.join(sys._MEIPASS, "luma")
    else:
        base = os.path.join(os.path.dirname(__file__), "luma")

    ext = "dll"

    if system() == "Windows":
        ext = "dll"
    elif system() == "Linux":
        ext = "so"
    elif system() == "Darwin":
        ext = "dylib"

    return os.path.join(base, "lib", f"{name}.{ext}")


def get_sdl_path() -> str:
    return get_lib_path("SDL3")


def get_sdl_image_path() -> str:
    return get_lib_path("SDL3_image")
