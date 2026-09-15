from luma import Luma

engine = Luma()
engine.create_window("Luma input", 800, 600)
graphics = engine.Graphics

player_x, player_y = 380.0, 280.0
player_speed = 260.0
last_key = "None"
last_mouse_event = "Move the mouse or click a button"


graphics.setBackgroundColor(18, 24, 30)


@engine.start
def init():
    print(engine.Keyboard.keyToKeyCode("a"))


@engine.draw
def draw():
    graphics.setDrawColor(graphics.COLORS.GREEN)
    graphics.drawRect(player_x, player_y, 40, 40)

    graphics.setDrawColor(graphics.COLORS.WHITE)
    graphics.drawPoint(engine.Mouse.x, engine.Mouse.y)


@engine.update
def update(dt):
    global player_x, player_y

    if engine.Keyboard.isKeyHeld(engine.Keyboard.A):
        player_x -= player_speed * dt
    if engine.Keyboard.isKeyHeld(engine.Keyboard.D):
        player_x += player_speed * dt
    if engine.Keyboard.isKeyHeld(engine.Keyboard.W):
        player_y -= player_speed * dt
    if engine.Keyboard.isKeyHeld(engine.Keyboard.S):
        player_y += player_speed * dt


@engine.on(Luma.EVENTS.KEYPRESS)
def on_key_press(key):
    global last_key
    last_key = f"Pressed: {key.name}"
    if key == engine.Keyboard.ESCAPE:
        engine.quit()


@engine.on(Luma.EVENTS.KEYUP)
def on_key_up(key):
    global last_key
    last_key = f"Released: {key.name}"


@engine.on(Luma.EVENTS.MOUSEPRESS)
def on_mouse_press(button, position, clicks):
    global last_mouse_event
    last_mouse_event = f"Pressed {button or 'other'} at {position}, clicks={clicks}"


@engine.on(Luma.EVENTS.MOUSEUP)
def on_mouse_up(button, position, clicks):
    global last_mouse_event
    last_mouse_event = f"Released {button or 'other'} at {position}, clicks={clicks}"


@engine.on(Luma.EVENTS.MOUSEMOTION)
def on_mouse_motion(position, relative):
    global last_mouse_event
    last_mouse_event = f"Mouse {position}, moved {relative}"


@engine.on(Luma.EVENTS.QUIT)
def on_quit():
    print(last_key)
    print(last_mouse_event)


engine.run()
