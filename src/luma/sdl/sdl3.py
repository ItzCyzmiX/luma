import ctypes

from luma.sdl.bindings import NativeBindings
from luma.sdl.event import SDL_Event
from luma.sdl.shapes import SDL_Point, SDL_Rect
from luma.sdl.surface import SDL_Surface
from luma.sdl.texture import SDL_Texture


class SDL3Bindings(NativeBindings):
    def __init__(self, library: ctypes.CDLL):
        super().__init__(library)

        self.init = self.bind("SDL_Init", [ctypes.c_uint32], ctypes.c_bool)
        self.create_window = self.bind(
            "SDL_CreateWindow",
            [ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_uint64],
            ctypes.c_void_p,
        )
        self.create_renderer = self.bind(
            "SDL_CreateRenderer",
            [ctypes.c_void_p, ctypes.c_char_p],
            ctypes.c_void_p,
        )
        self.destroy_renderer = self.bind(
            "SDL_DestroyRenderer", [ctypes.c_void_p], None
        )
        self.destroy_window = self.bind("SDL_DestroyWindow", [ctypes.c_void_p], None)
        self.render_clear = self.bind(
            "SDL_RenderClear", [ctypes.c_void_p], ctypes.c_bool
        )
        self.render_present = self.bind(
            "SDL_RenderPresent", [ctypes.c_void_p], ctypes.c_bool
        )
        self.poll_event = self.bind(
            "SDL_PollEvent", [ctypes.POINTER(SDL_Event)], ctypes.c_bool
        )
        self.get_ticks = self.bind("SDL_GetTicks", [], ctypes.c_uint64)
        self.get_error = self.bind("SDL_GetError", [], ctypes.c_char_p)
        self.set_render_draw_blend_mode = self.bind(
            "SDL_SetRenderDrawBlendMode",
            [ctypes.c_void_p, ctypes.c_uint64],
            ctypes.c_bool,
        )
        self.set_render_draw_color = self.bind(
            "SDL_SetRenderDrawColor",
            [
                ctypes.c_void_p,
                ctypes.c_uint8,
                ctypes.c_uint8,
                ctypes.c_uint8,
                ctypes.c_uint8,
            ],
            ctypes.c_bool,
        )
        self.render_rect = self.bind(
            "SDL_RenderRect", [ctypes.c_void_p, ctypes.POINTER(SDL_Rect)], ctypes.c_bool
        )
        self.render_fill_rect = self.bind(
            "SDL_RenderFillRect",
            [ctypes.c_void_p, ctypes.POINTER(SDL_Rect)],
            ctypes.c_bool,
        )
        self.create_texture_from_surface = self.bind(
            "SDL_CreateTextureFromSurface",
            [ctypes.c_void_p, ctypes.POINTER(SDL_Surface)],
            ctypes.POINTER(SDL_Texture),
        )
        self.destroy_surface = self.bind(
            "SDL_DestroySurface", [ctypes.POINTER(SDL_Surface)], None
        )
        self.destroy_texture = self.bind(
            "SDL_DestroyTexture", [ctypes.POINTER(SDL_Texture)], None
        )
        self.render_texture = self.bind(
            "SDL_RenderTextureRotated",
            [
                ctypes.c_void_p,
                ctypes.POINTER(SDL_Texture),
                ctypes.POINTER(SDL_Rect),
                ctypes.POINTER(SDL_Rect),
                ctypes.c_double,
                ctypes.POINTER(SDL_Point),
                ctypes.c_uint32,
            ],
            ctypes.c_bool,
        )

        self.get_mouse_position = self.bind(
            "SDL_GetMouseState",
            [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)],
            ctypes.c_uint32,
        )
        self.set_texture_alpha = self.bind(
            "SDL_SetTextureAlphaMod",
            [ctypes.POINTER(SDL_Texture), ctypes.c_uint8],
            ctypes.c_bool,
        )
        self.set_texture_color_mod = self.bind(
            "SDL_SetTextureColorMod",
            [
                ctypes.POINTER(SDL_Texture),
                ctypes.c_uint8,
                ctypes.c_uint8,
                ctypes.c_uint8,
            ],
            ctypes.c_bool,
        )

        self.set_texture_blendmode = self.bind(
            "SDL_SetTextureBlendMode",
            [ctypes.POINTER(SDL_Texture), ctypes.c_uint32],
            ctypes.c_bool,
        )

        self.quit = self.bind("SDL_Quit", [], None)
