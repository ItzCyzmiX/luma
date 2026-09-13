# API Reference

The public entry point is:

```python
from luma import Luma
```

## `Luma`

### `Luma(sdl_path: str | None = None)`

Loads SDL3 and initializes video. `sdl_path` overrides the default bundled
library location.

### `create_window(title: str, width: int, height: int, flags: int = 0)`

Creates the SDL window and renderer. On success, `engine.graphics` is a
`Luma_Graphics` instance.

### `draw(function)`

Registers the function called after the renderer is cleared. The function
should take no arguments.

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

## Errors

SDL initialization, window creation, renderer creation, and rendering failures
raise `Luma_Error` with SDL's error message.