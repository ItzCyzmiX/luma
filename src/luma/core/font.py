import ctypes
from typing import TYPE_CHECKING

from luma.core.error import Luma_Error

if TYPE_CHECKING:
    from luma.core.engine import Luma


class Luma_Font:
    def __init__(self, engine: "Luma") -> None:
        self.engine = engine

        if not self.sdl_ttf.init():
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        self._text_renderer = self.sdl_ttf.create_text_engine(self.engine.renderer)

    @property
    def sdl_ttf(self):
        return self.engine.sdl_ttf

    @property
    def sdl(self):
        return self.engine.sdl

    def open(self, font_path: str, size: float):
        self.font_path = font_path
        self.size = size

        self._font = self.sdl_ttf.open_font(self.font_path.encode(), self.size)

        if self._font is None:
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        self.engine._created_fonts.append(self._font)

        return self

    def write(self, text: str, x: float = 0.0, y: float = 0.0):
        return Luma_Text(self.engine, self, text, x, y)

    def _cleanup(self):
        self.sdl_ttf.destroy_text_renderer(self._text_renderer)
        self.sdl_ttf.quit()

    def kill(self):
        if not self.sdl_ttf.close_font(self._font):
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        try:
            self.sdl_ttf.close_font(self._font)
        except ValueError:
            pass

        self._font = None


class Luma_Text:
    def __init__(
        self, engine: "Luma", font: Luma_Font, text: str, x: float, y: float
    ) -> None:
        self.engine = engine

        if self.engine.Font is None:
            return
        self._text_str = text
        self._font = font

        payload = text.encode("utf-8")
        self._text = self.sdl_ttf.create_text(
            self.engine.Font._text_renderer,
            self._font._font,
            payload,
            0,
        )

        if self._text is None:
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

        self.x = x
        self.y = y

        self._width = ctypes.c_int()
        self._height = ctypes.c_int()

        self.sdl_ttf.get_text_size(self._text, self._width, self._height)

        self.is_alive = True
        self._color: tuple[int, int, int, int] = (255, 255, 255, 255)

    @property
    def sdl_ttf(self):
        return self.engine.sdl_ttf

    @property
    def sdl(self):
        return self.engine.sdl

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, new_font: Luma_Font):
        self._font = new_font
        self._rebuild_text(self._text_str)

    @property
    def text(self):
        return self._text_str

    @text.setter
    def text(self, new_text: str):
        if not self.is_alive:
            return

        if new_text != self._text_str:
            self._rebuild_text(new_text)

    @property
    def width(self):
        return self._width.value

    @property
    def height(self):
        return self._height.value

    @height.setter
    def height(self, value):
        self._height = value

    def _rebuild_text(self, text: str):
        self._text_str = text

        payload = text.encode("utf-8")

        self._text = self.sdl_ttf.create_text(
            self.engine.Font._text_renderer,
            self._font._font,
            payload,
            0,
        )

        self.sdl_ttf.get_text_size(self._text, self._width, self._height)

    def draw(self):
        if not self._text or not self.engine.Graphics:
            return

        draw_color = self.engine.Graphics.getDrawColor()

        if self._color != draw_color:
            self._color = draw_color
            if not self.sdl_ttf.set_text_color(self._text, *self._color):
                msg = self.sdl.get_error()
                raise Luma_Error(msg)

        if not self.sdl_ttf.render_text(self._text, self.x, self.y):
            msg = self.sdl.get_error()
            raise Luma_Error(msg)

    def isAlive(self):
        return self.is_alive

    def kill(self):
        if self._text:
            self.sdl_ttf.destroy_text(self._text)
            self._text = None

        self.is_alive = False
