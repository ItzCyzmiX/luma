# Input

Luma exposes keyboard input through `Luma.EVENTS` and `Luma.Keyboard`.

## Key press and release

`KEYPRESS` receives a `Luma.Keyboard` value when a key is initially pressed.
Holding the key does not repeatedly dispatch `KEYPRESS`.

```python
@engine.on(Luma.EVENTS.KEYPRESS)
def on_key_press(key):
    if key == Luma.Keyboard.SPACE:
        print("jump")


@engine.on(Luma.EVENTS.KEYUP)
def on_key_up(key):
    if key == Luma.Keyboard.SPACE:
        print("space released")
```

Multiple callbacks can be registered for the same event.

## Held keys

Use `engine.isKeyHeld(key)` inside `update` for continuous movement:

```python
speed = 300.0
x = 100.0


@engine.update
def update(dt):
    global x

    if engine.Keyboard.isKeyHeld(Luma.Keyboard.D):
        x += speed * dt
    if engine.Keyboard.isKeyHeld(Luma.Keyboard.A):
        x -= speed * dt
```

This tracks the current pressed state separately from press and release
callbacks. The key is a member of `Luma.Keyboard`, not a string.

Available event names are `KEYPRESS`, `KEYUP`. The key enum
contains letters, number keys, punctuation, `SPACE`, `RETURN`, `ESCAPE`,
`DELETE`, `CAPSLOCK`, and `F1` through `F12`.

## Mouse input

Mouse callbacks receive button and motion data:

```python
@engine.on(Luma.EVENTS.MOUSEPRESS)
def on_mouse_press(button, position, clicks):
    print(button, position, clicks)


@engine.on(Luma.EVENTS.MOUSEMOTION)
def on_mouse_motion(position, relative):
    print(position, relative)
```

`button` is `"L"`, `"M"`, or `"R"` for the primary three buttons, or an
empty string for another button. `engine.Mouse.x` and `engine.Mouse.y` track
the latest motion position; `engine.Mouse.get_pos()` queries SDL.
