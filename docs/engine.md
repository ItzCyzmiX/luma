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

Use the platform-specific library extension on Linux (`.so`) and macOS
(`.dylib`). If SDL initialization fails, Luma raises `Luma_Error`.

## Creating a window

```python
engine.create_window("Title", 800, 600)
```

The method takes `title`, `width`, `height`, and an optional SDL window `flags`
integer. After it succeeds, `engine.graphics` is ready to use.

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