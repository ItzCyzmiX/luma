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

## `Luma.Audio`

The audio manager is initialized by `Luma()` and uses the default playback
device.

### `loadSound(path: str) -> Luma_Sound`

Loads an audio file immediately and returns a sound object. See [Audio](audio.md)
for the playback and lifecycle guide.

## `Luma_Sound`

### `play()`

Starts playback, or resumes the sound when it is paused.

### `pause()`

Pauses a currently playing sound.

### `stop()`

Stops playback and resets `position` to zero.

### Properties

| Property    | Description                                                                      |
| ----------- | -------------------------------------------------------------------------------- |
| `path`      | Audio file path. Assigning a new path reloads the sound.                         |
| `playing`   | `True` while the sound is actively playing.                                      |
| `paused`    | `True` while playback is paused.                                                 |
| `loop`      | Restart the sound automatically when it finishes.                                |
| `volume`    | Floating-point gain, defaulting to `1.0`. Values below zero are clamped to zero. |
| `position`  | Current or requested playback position in milliseconds.                          |
| `duration`  | Sound length in milliseconds.                                                    |
| `on_finish` | No-argument callback invoked when non-looping playback finishes.                 |

### `kill()`

Releases the native audio and track resources. The audio manager releases all
remaining sounds during engine shutdown.

## `engine.Keyboard`

### `isKeyHeld(key) -> bool`

Returns whether a key is currently pressed.

### `isAnyPressed() -> bool`

Returns whether at least one key is currently pressed.

### `currentPressed() -> set`

Returns the set of currently pressed keys.

### `keyToKeyCode(name: str)`

Converts a key name, such as `"a"`, to its corresponding keyboard value.

### `run()`

Starts the main loop and returns after shutdown.

### `quit()`

Destroys SDL resources, quits SDL, and dispatches `Luma.EVENTS.QUIT`.

## `Luma.EVENTS`

| Member        | Callback arguments          |
| ------------- | --------------------------- |
| `KEYPRESS`    | `key: engine.Keyboard.KEYS` |
| `KEYUP`       | `key: engine.Keyboard.KEYS` |
| `QUIT`        | none                        |
| `MOUSEPRESS`  | `button, position, clicks`  |
| `MOUSEUP`     | `button, position, clicks`  |
| `MOUSEMOTION` | `position, relative`        |

## `engine.Keyboard.KEYS`

An enum containing the supported keyboard values. It includes alphabetic keys
`A` through `Z`, `NUM_0` through `NUM_9`, punctuation, `SPACE`, `RETURN`,
`ESCAPE`, `BACKSPACE`, `TAB`, `DELETE`, `CAPSLOCK`, and `F1` through `F12`.

Use it as `engine.Keyboard.KEYS.SPACE`, `engine.Keyboard.KEYS.A`, and similar.

## `Luma_Graphics`

### `setDrawColor(*args)`

Accepts `r, g, b`, `r, g, b, a`, or one tuple/list containing those values.

### `resetDrawColor()`

Sets the draw color to opaque black.

### `drawRect(x, y, w, h, fill: bool = True)`

Draws a filled rectangle by default. Pass `fill=False` to draw only its
outline.

### `drawPoint(x, y)`

Draws a single point using the current draw color.

### `drawLine(x1, y1, x2, y2)`

Draws a line between the two supplied points using the current draw color.

### `drawCircle(center_x, center_y, radius, filled: bool = True)`

Draws a filled circle by default. Pass `filled=False` to draw only its
circumference.

### `setBackgroundColor(*args)`

Sets the RGBA color used to clear the renderer before each draw callback.

## `Luma.Mouse`

`engine.Mouse.x` and `engine.Mouse.y` expose the latest mouse position from a
motion event. `engine.Mouse.get_pos()` returns `(x, y)`.

`LEFT_BUTTON`, `MIDDLE_BUTTON`, and `RIGHT_BUTTON` are the button constants
`"L"`, `"M"`, and `"R"`.

### `isButtonHeld(button: Literal["L", "M", "R"]) -> bool`

Returns whether a primary mouse button is currently held.

### `currentPressed() -> set[str]`

Returns the set of currently held primary mouse buttons.

## Sprite properties

Sprites support `angle`, `flip_mode`, `source_rect`, and `center_point` for
transforms and sprite-sheet cropping. `alpha` and `color_mod` apply texture
modulation during `draw()`. Call `kill()` when a sprite is no longer needed.

## Errors

SDL initialization, window creation, renderer creation, and rendering failures
raise `Luma_Error` with SDL's error message.
