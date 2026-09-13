from luma import Luma

engine = Luma()

engine.create_window("aloha", 1280, 720)
spr = engine.Sprite.create("examples/Ultron.jpg", 0, 0)
g = engine.graphics

x, y = 10, 10
speed = 330.0


@engine.start
def init_():
    print("initing very important stuff")


@engine.draw
def draw():
    spr.draw()

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
        spr.flip_mode = engine.Sprite.FLIP.VERTICAL
    elif engine.isKeyHeld(Luma.KEYS.Q):
        x -= speed * dt
        spr.flip_mode = engine.Sprite.FLIP.NONE
    elif engine.isKeyHeld(Luma.KEYS.S):
        y += speed * dt
    elif engine.isKeyHeld(Luma.KEYS.Z):
        y -= speed * dt

    if engine.isKeyHeld(Luma.KEYS.R):
        spr.angle += 1


engine.run()
