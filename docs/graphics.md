# Graphics

After creating a window, access the renderer wrapper through
`engine.Graphics`:

```python
graphics = engine.Graphics
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
graphics.setDrawColor(graphics.COLORS.RED)
```

Built-in colors are `RED`, `GREEN`, `BLUE`, `BLACK`, and `WHITE`. The alpha
constants are `OPAQUE` (`255`) and `TRANSPARENT` (`0`). Color channels use the
usual `0` to `255` range.

`resetDrawColor()` restores opaque white:

```python
graphics.resetDrawColor()
```

Set the color used to clear the renderer at the start of each frame with
`setBackgroundColor`:

```python
graphics.setBackgroundColor(graphics.COLORS.GREEN)
```

## Rectangles

Draw a filled rectangle with `drawRect(x, y, width, height)`:

```python
graphics.setDrawColor(graphics.COLORS.WHITE)
graphics.drawRect(20, 30, 100, 60)
```

Set `filled=False` to draw an outline. The `thickness` argument controls the
outline width and defaults to `1`. Odd thickness values generally look best
for rectangle outlines, such as `5`:

```python
graphics.drawRect(20, 30, 100, 60, filled=False, thickness=4)
```

Coordinates and dimensions accept integers or floats. The origin is the
window's top-left corner, with `x` increasing to the right and `y` increasing
downward.

## Points and lines

Draw a single point with `drawPoint(x, y)`:

```python
graphics.drawPoint(80, 100)
```

Draw a line between two points with `drawLine(x1, y1, x2, y2)`:

```python
graphics.drawLine(80, 100, 220, 160, thickness=3)
```

Point and line coordinates accept integers or floats and use the current draw
color. A line's `thickness` defaults to `1`.

## Polygons

Draw an outlined polygon by passing a list of `(x, y)` points. The final point
is automatically connected back to the first point:

```python
graphics.drawPolygon(
	[(400, 120), (520, 80), (600, 180), (480, 240)],
	thickness=3,
)
```

Polygons use the current draw color. The `thickness` argument defaults to `1`.
Filled polygons are not available yet, so `filled` must remain `False`.

## Circles

Draw a filled circle with `drawCircle(center_x, center_y, radius)`:

```python
graphics.drawCircle(320, 240, 40)
```

Set `filled=False` to draw only the circumference:

```python
graphics.drawCircle(320, 240, 40, filled=False, thickness=3)
```

The center coordinates and radius accept integers or floats. The outline's
`thickness` defaults to `1`. Circles use the current draw color, just like the
other primitive shapes.

## Current rendering surface

The public graphics API supports draw colors, primitive shapes, textures,
and sprites. Audio remains outside the core graphics API.
