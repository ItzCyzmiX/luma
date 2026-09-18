# Input

Luma exposes keyboard input through `Luma.EVENTS` and `engine.Keyboard`.

## Key press and release

`KEYPRESS` receives a `Luma.Keyboard.KEYS` value when a key is initially pressed.
Holding the key does not repeatedly dispatch `KEYPRESS`.

```python
@engine.on(Luma.EVENTS.KEYPRESS)
def on_key_press(key):
    if key == engine.Keyboard.KEYS.SPACE:
        print("jump")


@engine.on(Luma.EVENTS.KEYUP)
def on_key_up(key):
    if key == engine.Keyboard.KEYS.SPACE:
        print("space released")
```

Multiple callbacks can be registered for the same event.

## Held keys

Use `engine.Keyboard.isKeyHeld(key)` inside `update` for continuous movement:

```python
speed = 300.0
x = 100.0


@engine.update
def update(dt):
    global x

    if engine.Keyboard.isKeyHeld(engine.Keyboard.KEYS.D):
        x += speed * dt
    if engine.Keyboard.isKeyHeld(engine.Keyboard.KEYS.A):
        x -= speed * dt
```

This tracks the current pressed state separately from press and release
callbacks. The key is a member of `engine.Keyboard.KEYS`, not a string.

`engine.Keyboard.isAnyPressed()` reports whether at least one key is held.
`engine.Keyboard.currentPressed()` returns the set of currently held
keyboard values. `engine.Keyboard.keyToKeyCode(name)` converts a key name such
as `"a"` to its corresponding keyboard value.

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
empty string for another button. The same arguments are sent for `MOUSEUP`.
Use `engine.Mouse.LEFT_BUTTON`, `engine.Mouse.MIDDLE_BUTTON`, and
`engine.Mouse.RIGHT_BUTTON` for the named button values.

`engine.Mouse.isButtonHeld(button)` reports whether a primary button is held,
and `engine.Mouse.currentPressed()` returns the set of held button values.
`engine.Mouse.x` and `engine.Mouse.y` track the latest motion position;
`engine.Mouse.get_pos()` returns the same position as `(x, y)`.
