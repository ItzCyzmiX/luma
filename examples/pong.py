from luma import Luma


class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def update(self, dt, up, down):
        if engine.Keyboard.isKeyHeld(up):
            self.y -= self.speed * dt

        if engine.Keyboard.isKeyHeld(down):
            self.y += self.speed * dt

        # Keep inside screen
        if self.y < 0:
            self.y = 0

        if self.y + self.height > HEIGHT:
            self.y = HEIGHT - self.height

    def draw(self):
        g.drawRect(self.x, self.y, self.width, self.height)


class Ball:
    def __init__(self, x, y, size, speed_x, speed_y):
        self.x = x
        self.y = y
        self.size = size

        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self, dt):
        self.x += self.speed_x * dt
        self.y += self.speed_y * dt

        # Top / bottom
        if self.y <= 0:
            self.y = 0
            self.speed_y *= -1

        if self.y + self.size >= HEIGHT:
            self.y = HEIGHT - self.size
            self.speed_y *= -1

    def reset(self, direction):
        self.x = WIDTH / 2 - self.size / 2
        self.y = HEIGHT / 2 - self.size / 2

        self.speed_x = 300.0 * direction
        self.speed_y = 180.0

    def draw(self):
        g.drawRect(self.x, self.y, self.size, self.size)


class Game:
    def __init__(self):
        self.player = Paddle(20, HEIGHT / 2 - 40, 15, 80, 400)

        self.enemy = Paddle(WIDTH - 35, HEIGHT / 2 - 40, 15, 80, 400)

        self.ball = Ball(WIDTH / 2 - 7.5, HEIGHT / 2 - 7.5, 15, 300, 180)

        self.player_score = 0
        self.enemy_score = 0

    def update(self, dt):
        # Player
        self.player.update(dt, engine.Keyboard.Z, engine.Keyboard.S)

        # Simple AI
        ball_center = self.ball.y + self.ball.size / 2
        paddle_center = self.enemy.y + self.enemy.height / 2

        if ball_center < paddle_center:
            self.enemy.y -= self.enemy.speed * dt

        if ball_center > paddle_center:
            self.enemy.y += self.enemy.speed * dt

        if self.enemy.y < 0:
            self.enemy.y = 0

        if self.enemy.y + self.enemy.height > HEIGHT:
            self.enemy.y = HEIGHT - self.enemy.height

        # Ball
        self.ball.update(dt)

        # Player collision
        if (
            self.ball.x <= self.player.x + self.player.width
            and self.ball.x + self.ball.size >= self.player.x
            and self.ball.y + self.ball.size >= self.player.y
            and self.ball.y <= self.player.y + self.player.height
            and self.ball.speed_x < 0
        ):
            self.ball.x = self.player.x + self.player.width
            self.ball.speed_x *= -1

        # Enemy collision
        if (
            self.ball.x + self.ball.size >= self.enemy.x
            and self.ball.x <= self.enemy.x + self.enemy.width
            and self.ball.y + self.ball.size >= self.enemy.y
            and self.ball.y <= self.enemy.y + self.enemy.height
            and self.ball.speed_x > 0
        ):
            self.ball.x = self.enemy.x - self.ball.size
            self.ball.speed_x *= -1

        # Score
        if self.ball.x + self.ball.size < 0:
            self.enemy_score += 1
            self.ball.reset(1)

        if self.ball.x > WIDTH:
            self.player_score += 1
            self.ball.reset(-1)

    def draw(self):
        g.setDrawColor(255, 255, 255)

        self.player.draw()
        self.enemy.draw()
        self.ball.draw()

        g.resetDrawColor()


# --------------------------------
# Luma setup
# --------------------------------

engine = Luma()

WIDTH = 600
HEIGHT = 400

engine.create_window("Luma Pong", WIDTH, HEIGHT)

g = engine.Graphics

game = Game()


@engine.update
def update(dt: float):
    game.update(dt)


@engine.draw
def draw():
    game.draw()


@engine.on(Luma.EVENTS.QUIT)
def quit():
    print(f"Game over! {game.player_score} - {game.enemy_score}")


engine.run()
