from luma import Luma

engine = Luma()

engine.create_window("aloha", 600, 400)

g = engine.graphics

x, y = 10, 10
speed = 330.0


@engine.draw
def draw():
    g.setDrawColor(105, 0, 0)

    g.drawRect(x, y, 100, 100)

    g.setDrawColor(0, 140, 0)

    g.drawRect(x + 30, y + 20, 100, 100)

    g.resetDrawColor()


@engine.on(Luma.EVENTS.QUIT)
def quit():
    print("bye bye")


@engine.on(Luma.EVENTS.KEYPRESS)
def input(key: Luma.KEYS):
    if key == Luma.KEYS.SPACE:
        print("jump")


@engine.on(Luma.EVENTS.KEYPRESS)
def e(key: Luma.KEYS):
    if key == Luma.KEYS.A:
        print("a")


@engine.update
def update(dt):
    global x, y

    if engine.isKeyHeld(Luma.KEYS.D):
        x += speed * dt
    elif engine.isKeyHeld(Luma.KEYS.Q):
        x -= speed * dt
    elif engine.isKeyHeld(Luma.KEYS.S):
        y += speed * dt
    elif engine.isKeyHeld(Luma.KEYS.Z):
        y -= speed * dt


engine.run()
