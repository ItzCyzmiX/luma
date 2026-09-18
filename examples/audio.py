from luma import Luma

engine = Luma()
engine.create_window("Luma audio example", 800, 600)
graphics = engine.Graphics
graphics.setBackgroundColor(24, 28, 38)
sound = engine.Audio.loadSound("examples/fx.mp3")


def report_finish():
    print("sound finished")


sound.on_finish = report_finish


@engine.on(engine.EVENTS.KEYPRESS)
def input(key):
    if key == engine.Keyboard.KEYS.R:
        sound.position = 0

    if key == engine.Keyboard.KEYS.SPACE:
        if sound.paused:
            sound.play()
        else:
            sound.pause()
        print(f"playing={sound.playing}, paused={sound.paused}")

    if key == engine.Keyboard.KEYS.P:
        sound.play()
        print("playing")

    if key == engine.Keyboard.KEYS.S:
        sound.stop()
        print("stopped")

    if key == engine.Keyboard.KEYS.L:
        sound.loop = not sound.loop
        print(f"loop={sound.loop}")

    if key == engine.Keyboard.KEYS.RIGHT:
        sound.position += 1000
    elif key == engine.Keyboard.KEYS.LEFT:
        sound.position -= 1000

    if key == engine.Keyboard.KEYS.UP:
        sound.volume += 0.5
        print(f"volume={sound.volume}")
    elif key == engine.Keyboard.KEYS.DOWN:
        sound.volume -= 0.5
        print(f"volume={sound.volume}")


@engine.on(Luma.EVENTS.QUIT)
def on_quit():
    print("window closed")


engine.run()
