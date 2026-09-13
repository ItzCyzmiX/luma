# Examples

The repository includes examples that show how Luma programs are structured.
Run them from the repository root.

## Starter

```bash
python examples/starter.py
```

`starter.py` demonstrates a window, a loaded sprite, overlapping rectangles,
press callbacks, held-key movement, flipping, rotation, and frame-rate-
independent motion.

## Pong

```bash
python examples/pong.py
```

`pong.py` is a complete procedural game. It demonstrates game state, paddle
movement, a simple AI opponent, rectangle collision checks, scoring, and reset
logic.

## Object-oriented Pong

```bash
python examples/pong_oop.py
```

`pong_oop.py` organizes the same style of game around `Paddle`, `Ball`, and
`Game` classes. Use it as a starting point when a larger game needs clearer
ownership of state.

All gameplay rules in these examples are ordinary Python. Luma supplies the
window, event loop, timing value, and drawing primitives.