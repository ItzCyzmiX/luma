from luma import Luma

engine = Luma()
engine.create_window("Luma shapes", 800, 600)
graphics = engine.Graphics

graphics.setBackgroundColor(22, 26, 34)


@engine.draw
def draw():
    graphics.setDrawColor(230, 80, 80)
    graphics.drawRect(80, 90, 180, 100)

    graphics.setDrawColor(240, 190, 70)
    graphics.drawRect(100, 110, 180, 100, fill=False)

    graphics.setDrawColor(90, 210, 140)
    graphics.drawPoint(350, 140)
    graphics.drawLine(350, 140, 540, 220)

    graphics.setDrawColor(90, 160, 240)
    graphics.drawCircle(620, 160, 70)

    graphics.setDrawColor(190, 110, 230)
    graphics.drawCircle(620, 360, 70, filled=False)

    graphics.setDrawColor(graphics.COLORS.WHITE)
    graphics.drawLine(80, 360, 280, 480)
    graphics.drawPoint(280, 480)


@engine.update
def update(dt):
    pass


engine.run()
