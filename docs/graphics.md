# Graphics

After creating a window, access the renderer wrapper through
`engine.graphics`:

```python
graphics = engine.graphics
```

Graphics calls affect the current draw color and renderer. Put them in the
`draw` callback so the scene is rebuilt every frame.

## Colors

Set a color with separate red, green, and blue values. Alpha is optional and
defaults to `255`:

```python
graphics.setDrawColor(40, 120, 220)
graphics.setDrawColor(40, 120, 220, 180)
```

You can also pass a tuple or list:

```python
graphics.setDrawColor(graphics.RED)
```

Built-in colors are `RED`, `GREEN`, `BLUE`, `BLACK`, and `WHITE`. The alpha
constants are `OPAQUE` (`255`) and `TRANSPARENT` (`0`). Color channels use the
usual `0` to `255` range.

`resetDrawColor()` restores opaque black:

```python
graphics.resetDrawColor()
```

## Rectangles

Draw a filled rectangle with `drawRect(x, y, width, height)`:

```python
graphics.setDrawColor(graphics.WHITE)
graphics.drawRect(20, 30, 100, 60)
```

Set `fill=False` for an outline:

```python
graphics.drawRect(20, 30, 100, 60, fill=False)
```

Coordinates and dimensions accept integers or floats. The origin is the
window's top-left corner, with `x` increasing to the right and `y` increasing
downward.

## Current rendering surface

The public graphics API currently supports draw colors and rectangles only.
Textures, sprites, text, fonts, and audio are not part of this API yet.