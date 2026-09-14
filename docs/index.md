# Luma Engine

Luma is a small Python game engine built on SDL3. It gives you a window, a
frame loop, keyboard input, and immediate-mode primitive shape drawing while leaving
game state and game rules in ordinary Python code. Its graphics API includes
immediate-mode primitive shape drawing and image sprites.

## Documentation

- [Getting started](getting-started.md): install Luma and build a first game.
- [Engine](engine.md): understand windows, callbacks, the frame loop, and
  shutdown.
- [Input](input.md): respond to key presses, key releases, and held keys.
- [Graphics](graphics.md): set colors and draw primitive shapes, textures, and sprites.
- [Sprites](sprites.md): load, draw, transform, and crop image textures.
- [Examples](examples.md): run the included starter and Pong programs.
- [API reference](api.md): signatures, constants, and supported behavior.

## Smallest useful program

```python
from luma import Luma


engine = Luma()
engine.create_window("Luma", 640, 480)
graphics = engine.graphics


@engine.draw
def draw():
   graphics.setDrawColor(40, 120, 220)
   graphics.drawRect(220, 160, 200, 120)


@engine.update
def update(dt):
	pass


engine.run()
```

The [Getting started](getting-started.md) guide expands this into a complete
input-driven example.

## Scope

Luma currently provides keyboard and quit events, primitive shape rendering,
and image sprites. It does not yet provide built-in text, audio, collision
detection, scenes, cameras, or asset management. Those systems can be built in
Python on top of the engine, as the Pong example demonstrates.
