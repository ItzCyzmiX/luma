from enum import Enum
from typing import TYPE_CHECKING, TypedDict

from luma.core.error import Luma_Error
from luma.sdl.consts import SDL_BLENDMODE
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
    def __init__(
        self,
        engine: "Luma",
        sprite_creator,
        path: str,
        x: float,
        y: float,
        texture: SDL_Texture,
        w: float | None = None,
        h: float | None = None,
    ):
        self.engine = engine
        self.sprite_creator = sprite_creator
        self.img_path = path
        self.texture = texture
        self.is_alive = True
        self.center_point = None
        self._alpha = 255
        self._color_mod = (255, 255, 255)
        self.flip_mode = FLIP_MODE.NONE
        self.angle = 0.0

        self.x, self.y = x, y

        self.w, self.h = w, h

        self.dest_rect = (
            self.x,
            self.y,
            self.w,
            self.h,
        )
        self.source_rect = (0, 0, self.w, self.h)

        self.sdl.set_texture_blendmode(self.texture, SDL_BLENDMODE.SDL_BLENDMODE_BLEND)

    @property
    def alpha(self):
        return self._alpha

    @alpha.setter
    def alpha(self, a: int):
        self._alpha = a
        # self.sdl.set_texture_alpha(self.texture, self._alpha)

    @property
    def color_mod(self):
        return self._color_mod

    @color_mod.setter
    def color_mod(self, c: tuple[int, int, int]):
        self._color_mod = c
        # self.sdl.set_texture_color_mod(self.texture, *self._color_mod)

    def draw(self):
        if not self.texture or not self.is_alive:
            return

        dest_rect = SDL_Rect(self.x, self.y, self.w, self.h)
        source_rect = SDL_Rect(*self.source_rect)

        center_point = (
            SDL_Point(*self.center_point) if self.center_point is not None else None
        )

        self.sdl.set_texture_alpha(self.texture, self._alpha)
        self.sdl.set_texture_color_mod(self.texture, *self._color_mod)

        self.sdl.render_texture(
            self.renderer,
            self.texture,
            source_rect,
            dest_rect,
            self.angle,
            center_point,
            self.flip_mode.value,
        )

        self.sdl.set_texture_alpha(self.texture, 255)
        self.sdl.set_texture_color_mod(self.texture, 255, 255, 255)

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

    def kill(self):
        if self.img_path and self.sprite_creator and self.texture:
            self.sprite_creator.loaded_textures[self.img_path]["ref_count"] -= 1

            if self.sprite_creator.loaded_textures[self.img_path]["ref_count"] <= 0:
                self.sdl.destroy_texture(self.texture)
                del self.sprite_creator.loaded_textures[self.img_path]

        self.texture = None
        self.is_alive = False

    def isKilled(self):
        return not self.is_alive


class CachedTexture(TypedDict):
    texture: SDL_Texture
    dimensions: tuple[float, float]
    ref_count: int


class Luma_SpriteCreator:
    CENTER_POINT_CENTER = None
    FLIP = FLIP_MODE

    def __init__(self, engine: "Luma"):
        self.engine = engine
        self.loaded_textures: dict[str, CachedTexture] = {}

    def create(
        self,
        path: str,
        x: float,
        y: float,
        w: float | None = None,
        h: float | None = None,
    ):
        texture = self._load_texture(path)

        return Luma_Sprite(
            self.engine,
            self,
            path,
            x,
            y,
            texture["texture"],
            w if w is not None else texture["dimensions"][0],
            h if h is not None else texture["dimensions"][1],
        )

    def _load_texture(self, img_path: str) -> CachedTexture:

        if self.loaded_textures.get(img_path, False):
            self.loaded_textures[img_path]["ref_count"] += 1
            return self.loaded_textures[img_path]

        surf = self.engine.sdl_image.load(img_path.encode())

        if not surf:
            error_msg = self.engine.sdl.get_error()
            raise Luma_Error(error_msg)

        w = surf.contents.w
        h = surf.contents.h

        texture = self.engine.sdl.create_texture_from_surface(
            self.engine.renderer, surf
        )

        if not texture:
            error_msg = self.engine.sdl.get_error()
            raise Luma_Error(error_msg)

        self.engine.sdl.destroy_surface(surf)

        self.loaded_textures[img_path] = {
            "texture": texture.contents,
            "dimensions": (w, h),
            "ref_count": 1,
        }

        return self.loaded_textures[img_path]
