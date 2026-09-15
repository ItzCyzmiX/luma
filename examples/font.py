from luma import Luma

engine = Luma()
engine.create_window("Luma Fonts", 800, 600)
graphics = engine.Graphics


font = None
text = None
text2 = None


@engine.start
def init():
    global font, text, text2
    graphics.setBackgroundColor(24, 28, 38)

    font = engine.Font.open("examples/font.TTF", 16)

    text = font.write("hello world")
    text2 = font.write("PRESS SPACE!", 0, 100)


@engine.draw
def draw():
    graphics.setDrawColor(255, 0, 0)
    text.draw()
    graphics.resetDrawColor()

    text2.draw()


@engine.on(engine.EVENTS.KEYPRESS)
def input(key):
    if key == engine.Keyboard.SPACE:
        text2.text = "U SPACED"


@engine.update
def update(dt):
    text.x += 10 * dt


@engine.on(Luma.EVENTS.QUIT)
def on_quit():
    print("Window closed")


engine.run()
