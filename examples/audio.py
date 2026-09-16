from luma import Luma

engine = Luma()
engine.create_window("Luma boilerplate", 800, 600)
graphics = engine.Graphics


graphics.setBackgroundColor(24, 28, 38)
sound = None


@engine.start
def init():
    global sound

    sound = engine.Audio.loadSound("examples/fx.mp3")


@engine.on(engine.EVENTS.KEYPRESS)
def input(key):
    if key == engine.Keyboard.R:
        sound.rewind()

    if key == engine.Keyboard.SPACE:
        if sound.paused:
            sound.resume()
        else:
            sound.pause()

    if key == engine.Keyboard.P:
        sound.play()

    if key == engine.Keyboard.RIGHT:
        sound.position += 1000
    elif key == engine.Keyboard.LEFT:
        sound.position -= 1000


@engine.draw
def draw():
    pass


@engine.update
def update(dt):
    pass


@engine.on(Luma.EVENTS.QUIT)
def on_quit():
    print("Window closed")


engine.run()
