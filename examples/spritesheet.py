from pathlib import Path

from luma import Luma

engine = Luma()
engine.create_window("Luma spritesheet", 800, 500)
graphics = engine.Graphics
image_path = str(Path(__file__).with_name("Ultron.jpg"))

# A regular sprite can display one frame from a larger source image.
sprite = engine.Sprite.create(image_path, 300, 160, 200, 150)
sprite.source_rect = (0, 0, 100, 75)


graphics.setBackgroundColor(24, 28, 38)


@engine.draw
def draw():
    sprite.draw()


@engine.update
def update(dt):
    pass


engine.run()
