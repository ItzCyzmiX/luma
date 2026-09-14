from typing import TYPE_CHECKING

from luma.core.error import Luma_Error
from luma.sdl.shapes import SDL_Rect

if TYPE_CHECKING:
    from luma.core.engine import Luma


class Colors:
    RED = (255, 0, 0, 255)
    GREEN = (0, 255, 0, 255)
    BLUE = (0, 0, 255, 255)
    BLACK = (0, 0, 0, 255)
    WHITE = (255, 255, 255, 255)


class Alpha:
    OPAQUE = 255
    TRANSPARENT = 0


class Luma_Graphics:
    ALPHA = Alpha
    COLORS = Colors

    def __init__(self, sdl: "Luma"):
        self.engine = sdl

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

        if not self.sdl.set_render_draw_color(self.renderer, r, g, b, a):
            error_msg = self.sdl.get_error()
            raise Luma_Error(error_msg)

    def resetDrawColor(self):
        if not self.sdl.set_render_draw_color(self.renderer, 0, 0, 0, 255):
            error_msg = self.sdl.get_error()
            raise Luma_Error(error_msg)

    def drawRect(self, x: float, y: float, w: float, h: float, fill: bool = True):
        if fill:
            if not self.sdl.render_fill_rect(self.renderer, SDL_Rect(x, y, w, h)):
                error_msg = self.sdl.get_error()
                raise Luma_Error(error_msg)
        else:
            if not self.sdl.render_rect(self.renderer, SDL_Rect(x, y, w, h)):
                error_msg = self.sdl.get_error()
                raise Luma_Error(error_msg)
