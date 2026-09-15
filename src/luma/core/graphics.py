from typing import TYPE_CHECKING
import ctypes
from luma.core.error import Luma_Error
from luma.sdl.shapes import SDL_Rect

if TYPE_CHECKING:
    from luma.core.engine import Luma

import math


class Colors:
    RED = (255, 0, 0, 255)
    GREEN = (0, 255, 0, 255)
    BLUE = (0, 0, 255, 255)
    BLACK = (0, 0, 0, 255)
    WHITE = (255, 255, 255, 255)


class Alpha:
    OPAQUE = 255
    TRANSPARENT = 0


def get_rgba(*args) -> tuple[int, int, int, int]:
    if len(args) == 1 and isinstance(args[0], (tuple, list)):
        args = args[0]

    r, g, b, *alpha = args
    a = alpha[0] if alpha else 255

    return (r, g, b, a)


class Luma_Graphics:
    ALPHA = Alpha
    COLORS = Colors

    def __init__(self, sdl: "Luma"):
        self.engine = sdl
        self._background_color: tuple[int, int, int, int] = Colors.BLACK
        self._current_draw_color: tuple[int, int, int, int] = Colors.WHITE

    @property
    def renderer(self):
        return self.engine.renderer

    @property
    def sdl(self):
        return self.engine.sdl

    @property
    def backgroundColor(self):
        return self._background_color

    @backgroundColor.setter
    def backgroudColor(self, *args):
        self._background_color = get_rgba(*args)

    def setBackgroundColor(self, *args):
        self._background_color = get_rgba(*args)

    def setDrawColor(self, *args):
        r, g, b, a = get_rgba(*args)

        if not self.sdl.set_render_draw_color(self.renderer, r, g, b, a):
            error_msg = self.sdl.get_error()
            raise Luma_Error(error_msg)

        self._current_draw_color = (r, g, b, a)

    def getDrawColor(self):
        # r, g, b, a = (
        #     ctypes.c_uint8(),
        #     ctypes.c_uint8(),
        #     ctypes.c_uint8(),
        #     ctypes.c_uint8(),
        # )

        # self.sdl.get_render_draw_color(self.renderer, r, g, b, a)

        # return (r.value, g.value, b.value, a.value)
        return self._current_draw_color

    def resetDrawColor(self):
        self.setDrawColor(self.COLORS.WHITE)

    def drawRect(self, x: float, y: float, w: float, h: float, fill: bool = True):
        if fill:
            if not self.sdl.render_fill_rect(self.renderer, SDL_Rect(x, y, w, h)):
                error_msg = self.sdl.get_error()
                raise Luma_Error(error_msg)
        else:
            if not self.sdl.render_rect(self.renderer, SDL_Rect(x, y, w, h)):
                error_msg = self.sdl.get_error()
                raise Luma_Error(error_msg)

    def drawPoint(self, x: float, y: float):
        if not self.sdl.render_point(self.renderer, x, y):
            error_msg = self.sdl.get_error()
            raise Luma_Error(error_msg)

    def drawLine(self, x1: float, y1: float, x2: float, y2: float):
        if not self.sdl.render_line(self.renderer, x1, y1, x2, y2):
            error_msg = self.sdl.get_error()
            raise Luma_Error(error_msg)

    def drawCircle(
        self, center_x: float, center_y: float, radius: float, filled: bool = True
    ):
        if filled:
            self._drawFilledCircle(center_x, center_y, radius)
        else:
            self._drawLineCircle(center_x, center_y, radius)

    def _drawFilledCircle(self, center_x: float, center_y: float, radius: float):
        for y in range(int(-radius), int(radius)):
            dx = math.sqrt(radius * radius - y * y)
            if not self.sdl.render_line(
                self.renderer, center_x - dx, center_y + y, center_x + dx, center_y + y
            ):
                error_msg = self.sdl.get_error()
                raise Luma_Error(error_msg)

    def _drawLineCircle(self, center_x: float, center_y: float, radius: float):
        x = radius
        y = 0
        err = 0

        while x >= y:
            if not any(
                [
                    self.sdl.render_point(self.renderer, center_x + x, center_y + y),
                    self.sdl.render_point(self.renderer, center_x + y, center_y + x),
                    self.sdl.render_point(self.renderer, center_x - y, center_y + x),
                    self.sdl.render_point(self.renderer, center_x - x, center_y + y),
                    self.sdl.render_point(self.renderer, center_x - x, center_y - y),
                    self.sdl.render_point(self.renderer, center_x - y, center_y - x),
                    self.sdl.render_point(self.renderer, center_x + y, center_y - x),
                    self.sdl.render_point(self.renderer, center_x + x, center_y - y),
                ]
            ):
                error_msg = self.sdl.get_error()
                raise Luma_Error(error_msg)

            if err <= 0:
                y += 1
                err += 2 * y + 1

            if err > 0:
                x -= 1
                err -= 2 * x + 1
