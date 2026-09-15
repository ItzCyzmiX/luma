# Fonts and text

Luma supports TrueType font rendering through the engine's font system.

## Loading a font

Open a font with `engine.Font.open(path, size)`:

```python
font = engine.Font.open("examples/font.TTF", 16)
```

The returned font object is used to create drawable text surfaces.

## Creating text

Create a text object with `font.write(text, x=0, y=0)`:

```python
text = font.write("hello world", 20, 40)
```

The text object exposes `x`, `y`, `text`, and `font` properties and can be
redrawn every frame with `text.draw()`:

```python
@engine.draw
def draw():
    graphics.setDrawColor(255, 255, 255)
    text.draw()
```

## Updating text at runtime

The current draw color is applied when text is rendered, and the text object
can be updated by changing `text.text`, `text.x`, `text.y`, or `text.font`.
For example:

```python
text.text = "PRESS SPACE!"
text.x += 10
text.y = 100
```

## Example

A full working example is available in `examples/font.py`.

```bash
python examples/font.py
```

That script demonstrates loading a font, creating text objects, drawing them,
and updating their content and position at runtime.
