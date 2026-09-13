# Input

Luma exposes keyboard input through `Luma.EVENTS` and `Luma.KEYS`.

## Key press and release

`KEYPRESS` receives a `Luma.KEYS` value when a key is initially pressed.
Holding the key does not repeatedly dispatch `KEYPRESS`.

```python
@engine.on(Luma.EVENTS.KEYPRESS)
def on_key_press(key):
    if key == Luma.KEYS.SPACE:
        print("jump")


@engine.on(Luma.EVENTS.KEYUP)
def on_key_up(key):
    if key == Luma.KEYS.SPACE:
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

    if engine.isKeyHeld(Luma.KEYS.D):
        x += speed * dt
    if engine.isKeyHeld(Luma.KEYS.A):
        x -= speed * dt
```

This tracks the current pressed state separately from press and release
callbacks. The key is a member of `Luma.KEYS`, not a string.

## Quit

The quit event receives no arguments:

```python
@engine.on(Luma.EVENTS.QUIT)
def on_quit():
    print("Window closed")
```

Available event names are `KEYPRESS`, `KEYUP`, and `QUIT`. The key enum
contains letters, number keys, punctuation, `SPACE`, `RETURN`, `ESCAPE`,
`DELETE`, `CAPSLOCK`, and `F1` through `F12`.