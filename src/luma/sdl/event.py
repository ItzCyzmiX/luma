import ctypes

from luma.sdl.keys import SDL_KeyboardEvent
from luma.sdl.mouse import SDL_MouseButtonEvent, SDL_MouseMotionEvent


class SDL_Event(ctypes.Union):
    _fields_ = [
        ("type", ctypes.c_uint32),
        ("padding", ctypes.c_uint8 * 128),
        ("key", SDL_KeyboardEvent),
        ("button", SDL_MouseButtonEvent),
        ("motion", SDL_MouseMotionEvent),
    ]
