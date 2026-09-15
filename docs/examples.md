# Examples

The repository includes examples that show how Luma programs are structured.
Run them from the repository root.

## Starter boilerplate

```bash
python examples/boilerplate.py
```

`boilerplate.py` is the smallest complete window, draw callback, update
callback, and shutdown example.

## Input

```bash
python examples/input.py
```

`input.py` demonstrates key press and release callbacks, held-key movement,
mouse button callbacks, mouse motion, and the tracked mouse position.

## Shapes

```bash
python examples/shapes.py
```

`shapes.py` demonstrates filled and outlined rectangles and circles, points,
lines, draw colors, and a background color.

## Sprites

```bash
python examples/sprites.py
```

`sprites.py` demonstrates sprite size and position, rotation, custom rotation
centers, all flip modes, alpha, color modulation, and `kill()`.

## Spritesheet

```bash
python examples/spritesheet.py
```

`spritesheet.py` demonstrates selecting a source-image frame with
`source_rect`. Luma uses a regular sprite for spritesheet frames; it does not
require a separate spritesheet class.

## Fonts

```bash
python examples/font.py
```

`font.py` demonstrates loading a TTF font, creating text objects with
`engine.Font.open(...)` and `font.write(...)`, and updating drawable text each
frame. It also shows changing text content and position at runtime.

## Starter

```bash
python examples/starter.py
```

`starter.py` demonstrates a window, a loaded sprite, primitive shapes,
overlapping rectangles, press callbacks, held-key movement, flipping, rotation,
and frame-rate-independent motion.

## Pong

```bash
python examples/pong.py
```

`pong.py` is a complete procedural game. It demonstrates game state, paddle
movement, a simple AI opponent, rectangle collision checks, scoring, and reset
logic.

All gameplay rules in these examples are ordinary Python. Luma supplies the
window, event loop, timing value, and drawing primitives.
