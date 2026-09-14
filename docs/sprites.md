# Sprites

Sprites load an image into an SDL texture and draw it at a position in the
window. Create them through the engine after creating a window:

```python
from luma import Luma


engine = Luma()
engine.create_window("Sprite demo", 800, 600)
sprite = engine.Sprite.create("assets/player.png", 100, 120)


@engine.draw
def draw():
    sprite.draw()


engine.run()
```

`Sprite.create(path, x, y, w=None, h=None)` uses the image dimensions when
`w` or `h` is omitted. The returned sprite can be updated in the normal
`engine.update` callback and drawn in `engine.draw`.

## Position, size, and rotation

The sprite exposes these mutable properties:

| Property       | Meaning                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------- |
| `x`, `y`       | Destination position in pixels.                                                                            |
| `w`, `h`       | Destination size in pixels.                                                                                |
| `angle`        | Rotation angle passed to SDL.                                                                              |
| `flip_mode`    | A value from `engine.Sprite.FLIP`.                                                                         |
| `source_rect`  | a 4 floats tuple representing the drawn source rectangle (x, y, width, height)                             |
| `center_point` | Optional rotation center as a `tuple[float, float]`, or `None` for the center of the sprite (dest_rect/2). |

For example, frame-rate-independent movement and rotation look like this:

```python
@engine.update
def update(dt):
    sprite.x += 180 * dt
    sprite.angle += 90 * dt
```

## Flipping

Use the flip values exposed by `engine.Sprite.FLIP`:

```python
sprite.flip_mode = engine.Sprite.FLIP.HORIZONTAL
sprite.flip_mode = engine.Sprite.FLIP.VERTICAL
sprite.flip_mode = engine.Sprite.FLIP.HORIZONTAL_AND_VERTICAL
sprite.flip_mode = engine.Sprite.FLIP.NONE
```

## Sprite sheets

`source_rect` selects the part of the texture copied to the destination
rectangle. Its a tuple with 4 float the represent the source image's `x`, `y`, `w`, and `h`:

```python
sprite.source_rect = (32, 0, 32, 32)
sprite.w = 96
sprite.h = 96
```

`center_point` is stored as a Python `(x, y)` tuple. It is converted to an
SDL point only when the sprite is drawn, so direct assignment is supported:

```python
sprite.center_point = (16, 16)
```

You can also call `set_center_point((x, y))` to rotate around a custom point.
Pass `None` to use SDL's default center behavior:

```python
sprite.set_center_point((16, 16))
sprite.set_center_point(None)
```

The image path is loaded when the sprite is created. A missing or unreadable
image raises `Luma_Error` with SDL's error message.
