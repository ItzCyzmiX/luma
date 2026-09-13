from pysdl import PySDL3

engine = PySDL3()

engine.create_window("aloha", 600, 400)

g = engine.graphics

x, y = 10, 10
speed = 330.0


@engine.draw
def draw():
    g.setDrawColor(105, 0, 0)

    g.drawRect(x, y, 100, 100)

    g.resetDrawColor()


@engine.update
def update(dt):
    global x, y

    if engine.isKeyPressed(PySDL3.KEYS.KEY_D):
        x += speed * dt
    elif engine.isKeyPressed(PySDL3.KEYS.KEY_Q):
        x -= speed * dt
    elif engine.isKeyPressed(PySDL3.KEYS.KEY_S):
        y += speed * dt
    elif engine.isKeyPressed(PySDL3.KEYS.KEY_Z):
        y -= speed * dt


engine.run()
