# Engine

## Creating an engine

```python
engine = Luma()
```

`Luma()` loads SDL3 and initializes video. To load SDL3 from a custom path,
pass it explicitly:

```python
engine = Luma(sdl_path="path/to/SDL3.dll")
```

Pass `sdl_image_path` as well when SDL3_image is installed in a custom
location. Both paths default to bundled libraries.

Use the platform-specific library extension on Linux (`.so`) and macOS
(`.dylib`). If SDL initialization fails, Luma raises `Luma_Error`.

## Creating a window

```python
engine.create_window("Title", 800, 600)
```

The method takes `title`, `width`, `height`, and an optional SDL window `flags`
value. Use `Luma.WINDOW_FLAGS` for a readable, flag-combinable API:

```python
flags = (
    Luma.WINDOW_FLAGS.RESIZABLE
    | Luma.WINDOW_FLAGS.BORDERLESS
    | Luma.WINDOW_FLAGS.ALWAYS_ON_TOP
)
engine.create_window("Title", 800, 600, flags=flags)
```

`Luma.WINDOW_FLAGS` is an `IntFlag`, so each option is a named bitmask and can
be combined with `|`. After it succeeds, `engine.Graphics` and `engine.Mouse`
are ready to use.

## Callbacks

Register one update callback and one draw callback:

```python
@engine.update
def update(dt):
    ...


@engine.draw
def draw():
    ...
```

`update(dt)` is for changing game state. `draw()` is for rendering the current
state. The callbacks are called once per frame when registered.

Use `@engine.start` for one-time setup that should run after the window is
created and immediately before the loop begins.

## Frame order

Each iteration of `engine.run()`:

1. Calculates `dt` in seconds.
2. Polls SDL events and dispatches input callbacks.
3. Calls `update(dt)`.
4. Clears the renderer.
5. Calls `draw()`.
6. Presents the rendered frame.

Call `engine.run()` after registering callbacks. It runs until the window is
closed or `engine.running` becomes false.

## Shutdown

Luma destroys the renderer and window, calls `SDL_Quit`, and dispatches the
`QUIT` event when the loop exits. Register cleanup or final-score behavior with
`Luma.EVENTS.QUIT`.

```python
@engine.on(Luma.EVENTS.QUIT)
def on_quit():
    print("Game over")
```
