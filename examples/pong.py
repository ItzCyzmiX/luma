from luma import Luma

engine = Luma()

WIDTH = 600
HEIGHT = 400

engine.create_window("Luma Pong", WIDTH, HEIGHT)

g = engine.graphics


# -------------------------
# Game state
# -------------------------

paddle_width = 15
paddle_height = 80

left_x = 20
left_y = HEIGHT / 2 - paddle_height / 2

right_x = WIDTH - 20 - paddle_width
right_y = HEIGHT / 2 - paddle_height / 2

ball_size = 15
ball_x = WIDTH / 2 - ball_size / 2
ball_y = HEIGHT / 2 - ball_size / 2

ball_speed_x = 300.0
ball_speed_y = 180.0

paddle_speed = 400.0

left_score = 0
right_score = 0


def reset_ball(direction):
    global ball_x, ball_y
    global ball_speed_x, ball_speed_y

    ball_x = WIDTH / 2 - ball_size / 2
    ball_y = HEIGHT / 2 - ball_size / 2

    ball_speed_x = 300.0 * direction
    ball_speed_y = 180.0


# -------------------------
# Drawing
# -------------------------


@engine.draw
def draw():
    g.setDrawColor(255, 255, 255)

    # Left paddle
    g.drawRect(left_x, left_y, paddle_width, paddle_height)

    # Right paddle
    g.drawRect(right_x, right_y, paddle_width, paddle_height)

    # Ball
    g.drawRect(ball_x, ball_y, ball_size, ball_size)

    g.resetDrawColor()


# -------------------------
# Update
# -------------------------


@engine.update
def update(dt):
    global left_y
    global right_y
    global ball_x
    global ball_y
    global ball_speed_x
    global ball_speed_y
    global left_score
    global right_score

    # ---------------------
    # Player movement
    # ---------------------

    if engine.isKeyHeld(Luma.KEYS.Z):
        left_y -= paddle_speed * dt

    if engine.isKeyHeld(Luma.KEYS.S):
        left_y += paddle_speed * dt

    # Keep player paddle inside screen
    if left_y < 0:
        left_y = 0

    if left_y + paddle_height > HEIGHT:
        left_y = HEIGHT - paddle_height

    # ---------------------
    # Simple AI
    # ---------------------

    paddle_center = right_y + paddle_height / 2
    ball_center = ball_y + ball_size / 2

    if ball_center < paddle_center:
        right_y -= paddle_speed * dt

    if ball_center > paddle_center:
        right_y += paddle_speed * dt

    if right_y < 0:
        right_y = 0

    if right_y + paddle_height > HEIGHT:
        right_y = HEIGHT - paddle_height

    # ---------------------
    # Ball movement
    # ---------------------

    ball_x += ball_speed_x * dt
    ball_y += ball_speed_y * dt

    # ---------------------
    # Top / bottom collision
    # ---------------------

    if ball_y <= 0:
        ball_y = 0
        ball_speed_y *= -1

    if ball_y + ball_size >= HEIGHT:
        ball_y = HEIGHT - ball_size
        ball_speed_y *= -1

    # ---------------------
    # Paddle collision
    # ---------------------

    # Left paddle
    if (
        ball_x <= left_x + paddle_width
        and ball_x + ball_size >= left_x
        and ball_y + ball_size >= left_y
        and ball_y <= left_y + paddle_height
        and ball_speed_x < 0
    ):
        ball_x = left_x + paddle_width
        ball_speed_x *= -1

    # Right paddle
    if (
        ball_x + ball_size >= right_x
        and ball_x <= right_x + paddle_width
        and ball_y + ball_size >= right_y
        and ball_y <= right_y + paddle_height
        and ball_speed_x > 0
    ):
        ball_x = right_x - ball_size
        ball_speed_x *= -1

    # ---------------------
    # Scoring
    # ---------------------

    if ball_x + ball_size < 0:
        right_score += 1
        reset_ball(1)

    if ball_x > WIDTH:
        left_score += 1
        reset_ball(-1)


# -------------------------
# Quit
# -------------------------


@engine.on(Luma.EVENTS.QUIT)
def quit():
    print("Game over!")
    print(f"Final score: {left_score} - {right_score}")


engine.run()
