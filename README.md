# Luma

Luma Engine is a lightweight Python game engine powered by SDL3

## Installation

```bash
python -m pip install luma-engine
```

## Quick Start

Create a file named `main.py`:

```python
from luma import Luma


engine = Luma()
engine.create_window("Luma", 640, 480)
graphics = engine.Graphics


@engine.draw
def draw():
	graphics.setDrawColor(40, 120, 220)
	graphics.drawRect(220, 160, 200, 120)
	graphics.resetDrawColor()


@engine.update
def update(dt):
	# Update game state here. dt is elapsed time in seconds.
	pass


@engine.on(Luma.EVENTS.KEYPRESS)
def on_key_press(key):
	if key == engine.Keyboard.KEYS.SPACE:
		print("Space pressed")


engine.run()
```

Run it with:

```bash
python main.py
```

## Examples

The repository includes complete examples in the [`examples`](examples) directory, including a Pong game:

```bash
python examples/pong.py
```

## Docs

Documentation is available [here](https://itzcyzmix.github.io/luma/)

## Requirements

- Python 3.10 or newer
- An SDL3-compatible system

## License

Luma Engine is released under the MIT License.
