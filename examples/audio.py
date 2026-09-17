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

    print(sound.duration)

    sound.loop = True

    print(sound.loop)

    sound.on_finish = lambda: print("hi")


@engine.on(engine.EVENTS.KEYPRESS)
def input(key):
    if key == engine.Keyboard.R:
        sound.position = 0

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

    if key == engine.Keyboard.UP:
        sound.volume += 0.5
    elif key == engine.Keyboard.DOWN:
        sound.volume -= 0.5


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
