from enum import Enum
from typing import TYPE_CHECKING

from luma.core.error import Luma_Error
from luma.sdl.shapes import SDL_Point, SDL_Rect
from luma.sdl.texture import SDL_Texture

if TYPE_CHECKING:
    from luma.core.engine import Luma


class FLIP_MODE(Enum):
    NONE = 0
    VERTICAL = 1
    HORIZONTAL = 2
    HORIZONTAL_AND_VERTICAL = 1 | 2


class Luma_Sprite:
    def __init__(self, engine: "Luma"):
        self.engine = engine
        self.img_path: str | None = None
        self.texture: SDL_Texture | None = None

        (
            self.x,
            self.y,
            self.w,
            self.h,
            self.angle,
            self.center_point,
            self.flip_mode,
        ) = (
            0.0,
            0.0,
            0.0,
            0.0,
            0.0,
            None,
            FLIP_MODE.NONE,
        )

        self.dest_rect = SDL_Rect(self.x, self.y, self.w, self.h)
        self.source_rect = SDL_Rect(0, 0, self.w, self.h)

    def create(
        self,
        path: str,
        x: float,
        y: float,
        w: float | None = None,
        h: float | None = None,
    ):
        self.img_path = path
        self._load_texture()

        self.x, self.y = x, y
        if w is not None:
            self.w = w
        if h is not None:
            self.h = h

        self.dest_rect = SDL_Rect(self.x, self.y, self.w, self.h)
        self.source_rect: SDL_Rect = SDL_Rect(0, 0, self.w, self.h)
        return self

    def draw(self):
        self.dest_rect = SDL_Rect(self.x, self.y, self.w, self.h)
        point = (
            SDL_Point(self.center_point[0], self.center_point[1])
            if self.center_point is not None
            else None
        )
        self.sdl.render_texture(
            self.renderer,
            self.texture,
            self.source_rect,
            self.dest_rect,
            self.angle,
            point,
            self.flip_mode.value,
        )

    def set_source_rect(self, x: float, y: float, w: float, h: float):
        self.source_rect = SDL_Rect(x, y, w, h)

    @property
    def sdl(self):
        return self.engine.sdl

    @property
    def sdl_image(self):
        return self.engine.sdl_image

    @property
    def renderer(self):
        return self.engine.renderer

    def set_center_point(self, point: tuple[float, float] | None):

        self.center_point = (point[0], point[1]) if point is not None else None

    def _load_texture(self):
        if self.img_path is None or not self.renderer:
            return

        surf = self.sdl_image.load(self.img_path.encode())

        self.w = surf.contents.w
        self.h = surf.contents.h
        if not surf:
            error_msg = self.engine.sdl.get_error()
            raise Luma_Error(error_msg)

        self.texture = self.sdl.create_texture_from_surface(self.renderer, surf)

        if not self.texture:
            error_msg = self.engine.sdl.get_error()
            raise Luma_Error(error_msg)

        self.sdl.destroy_surface(surf)


class Luma_SpriteCreator:
    CENTER_POINT_CENTER = None
    FLIP = FLIP_MODE

    def __init__(self, engine: "Luma"):
        self.engine = engine

    def create(
        self,
        path: str,
        x: float,
        y: float,
        w: float | None = None,
        h: float | None = None,
    ):
        return Luma_Sprite(self.engine).create(path, x, y, w, h)
