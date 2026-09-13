import ctypes


class SDL_Texture(ctypes.Structure):
    _fields_ = [
        ("format", ctypes.c_uint32),
        ("w", ctypes.c_int),
        ("h", ctypes.c_int),
        ("refcount", ctypes.c_int),
    ]
