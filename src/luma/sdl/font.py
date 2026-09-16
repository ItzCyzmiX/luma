import ctypes

from luma.sdl.bindings import NativeBindings


class SDL_TTF_Font(ctypes.Structure):
    pass


class SDL_TTF_TextEngine(ctypes.Structure):
    pass


class SDL_TTF_Text(ctypes.Structure):
    _fields_ = [
        ("char", ctypes.POINTER(ctypes.c_char)),
        ("num_lines", ctypes.c_int),
        ("refcount", ctypes.c_int),
    ]


class SDLTTFBindings(NativeBindings):
    def __init__(self, library: ctypes.CDLL):
        super().__init__(library)

        self.init = self.bind("TTF_Init", [], ctypes.c_bool)
        self.quit = self.bind("TTF_Quit", [], None)
        self.open_font = self.bind(
            "TTF_OpenFont",
            [ctypes.c_char_p, ctypes.c_float],
            ctypes.c_void_p,
        )

        self.close_font = self.bind(
            "TTF_CloseFont",
            [ctypes.c_void_p],
            ctypes.c_bool
        )

        self.create_text_engine = self.bind(
            "TTF_CreateRendererTextEngine",
            [ctypes.c_void_p],
            ctypes.c_void_p,
        )

        self.create_text = self.bind(
            "TTF_CreateText",
            [
                ctypes.c_void_p,
                ctypes.c_void_p,
                ctypes.c_char_p,
                ctypes.c_size_t,
            ],
            ctypes.POINTER(SDL_TTF_Text),
        )

        self.set_text_color = self.bind(
            "TTF_SetTextColor",
            [
                ctypes.POINTER(SDL_TTF_Text),
                ctypes.c_uint8,
                ctypes.c_uint8,
                ctypes.c_uint8,
                ctypes.c_uint8,
            ],
            ctypes.c_bool,
        )

        self.get_text_size = self.bind(
            "TTF_GetTextSize",
            [
                ctypes.POINTER(SDL_TTF_Text),
                ctypes.POINTER(ctypes.c_int),
                ctypes.POINTER(ctypes.c_int),
            ],
            ctypes.c_bool
        )

        self.render_text = self.bind(
            "TTF_DrawRendererText",
            [ctypes.POINTER(SDL_TTF_Text), ctypes.c_float, ctypes.c_float],
            ctypes.c_bool,
        )

        self.destroy_text = self.bind("TTF_DestroyText", [ctypes.POINTER(SDL_TTF_Text)])

        self.destroy_text_renderer = self.bind(
            "TTF_DestroyRendererTextEngine", [ctypes.c_void_p]
        )
