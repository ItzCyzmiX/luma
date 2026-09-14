from luma import Luma

engine = Luma()
engine.create_window("Luma boilerplate", 800, 600)
graphics = engine.Graphics


graphics.setBackgroundColor(24, 28, 38)


@engine.draw
def draw():
    graphics.setDrawColor(80, 160, 240)
    graphics.drawRect(300, 220, 200, 120)


@engine.update
def update(dt):
    pass


@engine.on(Luma.EVENTS.QUIT)
def on_quit():
    print("Window closed")


engine.run()
