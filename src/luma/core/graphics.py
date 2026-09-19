from typing import TYPE_CHECKING

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

    r, g, b, *alpha = args  # type: ignore
    a = alpha[0] if alpha else 255

    return (r, g, b, a)


class Luma_Graphics:
    ALPHA = Alpha
    COLORS = Colors

    def __init__(self, sdl: "Luma"):
        self.engine = sdl
        self._background_color: tuple[int, int, int, int] = Colors.BLACK
        self._current_draw_color: tuple[int, int, int, int] = Colors.WHITE
        self._thickness_offest: float = 0.3

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

    def drawRect(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        filled: bool = True,
        thickness: int = 1,
    ):
        if filled:
            if not self.sdl.render_fill_rect(self.renderer, SDL_Rect(x, y, w, h)):
                error_msg = self.sdl.get_error()
                raise Luma_Error(error_msg)
        else:
            for i in range(thickness):
                if not self.sdl.render_rect(
                    self.renderer, SDL_Rect(x + i / 2, y + i / 2, w - i, h - i)
                ):
                    error_msg = self.sdl.get_error()
                    raise Luma_Error(error_msg)

    def drawPoint(self, x: float, y: float):
        if not self.sdl.render_point(self.renderer, x, y):
            error_msg = self.sdl.get_error()
            raise Luma_Error(error_msg)

    def drawLine(self, x1: float, y1: float, x2: float, y2: float, thickness: int = 1):
        dx = x2 - x1
        dy = y2 - y1

        length = (dx * dx + dy * dy) ** 0.5

        if length == 0:
            return

        nx = -dy / length
        ny = dx / length

        for i in range(thickness):
            offset = i - (thickness - 1) / 2

            self.sdl.render_line(
                self.renderer,
                x1 + nx * offset,
                y1 + ny * offset,
                x2 + nx * offset,
                y2 + ny * offset,
            )

    def drawPolygon(
        self,
        points: list[tuple[float, float]],
        filled: bool = False,
        thickness: int = 1,
    ):
        if filled:
            raise NotImplementedError("Filled polygons arent available yet")
        else:
            self._drawLinePolygon(points, thickness)

    def _drawLinePolygon(self, points: list[tuple[float, float]], thickness: int = 1):
        if len(points) < 2:
            return

        for i in range(len(points) - 1):
            point1 = points[i]
            point2 = points[i + 1]
            self.drawLine(*point1, *point2, thickness=thickness)

        self.drawLine(*points[-1], *points[0], thickness=thickness)

    def drawCircle(
        self,
        center_x: float,
        center_y: float,
        radius: float,
        filled: bool = True,
        thickness: int = 1,
    ):
        if filled:
            self._drawFilledCircle(center_x, center_y, radius)
        else:
            for i in range(thickness):
                if radius - i < 0:
                    break
                self._drawLineCircle(center_x, center_y, radius - i)

    def _drawFilledCircle(self, center_x: float, center_y: float, radius: float):
        for y in range(int(-radius), int(radius)):
            dx = math.sqrt(radius * radius - y * y)
            if not self.sdl.render_line(
                self.renderer,
                center_x - dx,
                center_y + y,
                center_x + dx,
                center_y + y,
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
