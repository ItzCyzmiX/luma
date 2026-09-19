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
    graphics.drawRect(100, 110, 180, 100, filled=False, thickness=5)

    graphics.setDrawColor(90, 210, 140)
    graphics.drawPoint(350, 140)
    graphics.drawLine(350, 140, 540, 220, thickness=3)

    graphics.setDrawColor(90, 160, 240)
    graphics.drawCircle(620, 160, 70)

    graphics.setDrawColor(190, 110, 230)
    graphics.drawCircle(620, 360, 70, filled=False, thickness=4)

    graphics.setDrawColor(graphics.COLORS.WHITE)
    graphics.drawLine(80, 360, 280, 480, thickness=2)
    graphics.drawPoint(280, 480)

    graphics.setDrawColor(graphics.COLORS.RED)
    graphics.drawPolygon(
        [
            (400, 360),
            (500, 300),
            (620, 380),
            (520, 500),
        ],
        thickness=4,
    )


@engine.update
def update(dt):
    pass


engine.run()
