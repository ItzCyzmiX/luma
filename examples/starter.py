from luma import Luma

engine = Luma()

engine.create_window("aloha", 1280, 720)
sprite = engine.Sprite.create(
    "examples/Ultron.jpg",
    0,
    0,
)
sprite_2 = engine.Sprite.create(path="examples/Ultron.jpg", x=0, y=0)

graphics = engine.Graphics


SPRITE_SPEED = 330.0
RECT_X, RECT_Y = 10, 10


@engine.start
def init_():
    print("initing very important stuff")
    graphics.setBackgroundColor(graphics.COLORS.GREEN)


@engine.draw
def draw():

    graphics.setDrawColor(graphics.COLORS.RED)

    graphics.drawRect(RECT_X, RECT_Y, 100, 100)

    graphics.setDrawColor(0, 140, 0)

    graphics.drawRect(RECT_X + 30, RECT_Y + 20, 100, 100)

    graphics.resetDrawColor()

    sprite_2.draw()

    sprite.draw()


@engine.on(Luma.EVENTS.QUIT)
def quit():
    print("bye bye")


@engine.on(Luma.EVENTS.KEYPRESS)
def input(key: Luma.KEYS):
    if key == Luma.KEYS.SPACE:
        print("jump")


@engine.on(Luma.EVENTS.MOUSEPRESS)
def mouse(button: str, pos: tuple[float, float], clicks: int):
    print(button, pos, clicks)


@engine.on(Luma.EVENTS.MOUSEUP)
def mouse2(button: str, pos: tuple[float, float], clicks: int):
    print(button, pos, clicks)


print(engine.Mouse.get_pos())

print(engine.Mouse.x, engine.Mouse.y)


@engine.on(Luma.EVENTS.MOUSEMOTION)
def mouse3(position, relative_motion):
    print(position, relative_motion)


@engine.update
def update(dt):
    if engine.isKeyHeld(Luma.KEYS.D):
        sprite.x += SPRITE_SPEED * dt
        sprite.flip_mode = engine.Sprite.FLIP.VERTICAL
    elif engine.isKeyHeld(Luma.KEYS.Q):
        sprite.x -= SPRITE_SPEED * dt
        sprite.flip_mode = engine.Sprite.FLIP.NONE
    elif engine.isKeyHeld(Luma.KEYS.S):
        sprite.y += SPRITE_SPEED * dt
    elif engine.isKeyHeld(Luma.KEYS.Z):
        sprite.y -= SPRITE_SPEED * dt

    if engine.isKeyHeld(Luma.KEYS.R):
        sprite.angle += 1


engine.run()
