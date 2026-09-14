# API Reference

The public entry point is:

```python
from luma import Luma
```

## `Luma`

### `Luma(sdl_path: str | None = None, sdl_image_path: str | None = None)`

Loads SDL3 and SDL3_image and initializes video. The optional paths override
the default bundled library locations.

### `create_window(title: str, width: int, height: int, flags: int = 0)`

Creates the SDL window and renderer. On success, `engine.Graphics` is a
`Luma_Graphics` instance and `engine.Mouse` is available.

### `draw(function)`

Registers the function called after the renderer is cleared. The function
should take no arguments.

### `start(function)`

Registers a function called once after window creation and before the main
loop starts.

### `Sprite`

`engine.Sprite` is a sprite creator tied to the engine's renderer.

#### `Sprite.create(path, x, y, w=None, h=None)`

Loads an image and returns a sprite. `path` is the image path, `x` and `y` are
the destination coordinates, and omitted `w` or `h` use the image dimensions.
See [Sprites](sprites.md) for transformations and sprite-sheet cropping.

### `update(function)`

Registers the function called once per frame before drawing. The function
receives `dt`, elapsed seconds since the previous frame.

### `on(event_name)`

Returns a decorator for registering an event callback. See [Input](input.md).

### `isKeyHeld(key: Luma.KEYS) -> bool`

Returns whether a key is currently pressed.

### `run()`

Starts the main loop and returns after shutdown.

### `quit()`

Destroys SDL resources, quits SDL, and dispatches `Luma.EVENTS.QUIT`.

## `Luma.EVENTS`

| Member | Callback arguments |
| --- | --- |
| `KEYPRESS` | `key: Luma.KEYS` |
| `KEYUP` | `key: Luma.KEYS` |
| `QUIT` | none |
| `MOUSEPRESS` | `button, position, clicks` |
| `MOUSEUP` | `button, position, clicks` |
| `MOUSEMOTION` | `position, relative` |

## `Luma.KEYS`

An enum containing the supported keyboard values. It includes alphabetic keys
`A` through `Z`, `NUM_0` through `NUM_9`, punctuation, `SPACE`, `RETURN`,
`ESCAPE`, `BACKSPACE`, `TAB`, `DELETE`, `CAPSLOCK`, and `F1` through `F12`.

## `Luma_Graphics`

### `setDrawColor(*args)`

Accepts `r, g, b`, `r, g, b, a`, or one tuple/list containing those values.

### `resetDrawColor()`

Sets the draw color to opaque black.

### `drawRect(x, y, w, h, fill: bool = True)`

Draws a filled rectangle by default. Pass `fill=False` to draw only its
outline.

### `setBackgroundColor(*args)`

Sets the RGBA color used to clear the renderer before each draw callback.

## `Luma.Mouse`

`engine.Mouse.x` and `engine.Mouse.y` expose the latest mouse position from a
motion event. `engine.Mouse.get_pos()` queries SDL and returns `(x, y)`.

## Sprite properties

Sprites support `angle`, `flip_mode`, `source_rect`, and `center_point` for
transforms and sprite-sheet cropping. `alpha` and `color_mod` apply texture
modulation during `draw()`. Call `kill()` when a sprite is no longer needed.

## Errors

SDL initialization, window creation, renderer creation, and rendering failures
raise `Luma_Error` with SDL's error message.