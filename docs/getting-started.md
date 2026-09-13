# Getting Started

## Requirements

- Python 3.10 or newer.

Install the package from PyPI:

```bash
python -m pip install luma-engine
```

## First window

Create `main.py`:

```python
from luma import Luma


engine = Luma()
engine.create_window("My Luma Game", 640, 480)
graphics = engine.graphics


@engine.draw
def draw():
    graphics.setDrawColor(40, 120, 220)
    graphics.drawRect(220, 160, 200, 120)
    graphics.resetDrawColor()


@engine.update
def update(dt):
    # Put movement and other game-state changes here.
    pass


engine.run()
```

Run it with:

```bash
python main.py
```

The window is cleared before every call to `draw`, so redraw the complete
visible scene each frame. `dt` is the elapsed time since the previous frame in
seconds; multiply speeds by it to make movement independent of frame rate.

## Adding input

Register an event callback with `engine.on`:

```python
@engine.on(Luma.EVENTS.KEYPRESS)
def on_key_press(key):
    if key == Luma.KEYS.SPACE:
        print("Space pressed")
```

See [Input](input.md) for key-held movement and the full event behavior.