from pathlib import Path

from luma import Luma

engine = Luma()
engine.create_window("Luma sprites", 900, 600)
graphics = engine.Graphics
image_path = str(Path(__file__).with_name("Ultron.jpg"))

sprite = engine.Sprite.create(image_path, 330, 210, 240, 180)
sprite.alpha = 220
sprite.color_mod = (255, 220, 220)
sprite.center_point = (0, 0)

flip_modes = [
    engine.Sprite.FLIP.NONE,
    engine.Sprite.FLIP.HORIZONTAL,
    engine.Sprite.FLIP.VERTICAL,
    engine.Sprite.FLIP.HORIZONTAL_AND_VERTICAL,
]
flip_index = 0


graphics.setBackgroundColor(20, 24, 32)


@engine.draw
def draw():
    sprite.draw()


@engine.update
def update(dt):
    sprite.angle += 45 * dt


@engine.on(Luma.EVENTS.KEYPRESS)
def on_key_press(key):
    global flip_index

    if key == engine.Keyboard.F:
        flip_index = (flip_index + 1) % len(flip_modes)
        sprite.flip_mode = flip_modes[flip_index]
    elif key == engine.Keyboard.C:
        sprite.center_point = None
    elif key == engine.Keyboard.A:
        sprite.alpha = 100 if sprite.alpha == 220 else 220
    elif key == engine.Keyboard.R:
        sprite.color_mod = (
            (255, 220, 220) if sprite.color_mod != (255, 220, 220) else (220, 255, 220)
        )
    elif key == engine.Keyboard.K:
        sprite.kill()


engine.run()
