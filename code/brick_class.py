from initialization import *
class Brick:

    def __init__(self, x, y, width, height, health, colors):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.max_health = health
        self.colors = colors
        self.color = colors[0]

    def draw(self, win):
        pygame.draw.rect(
        win,
        self.color,
        (
            self.x,
            self.y,
            self.width,
            self.height
        )
        )


    def collide(self, ball):
        if not (ball.x <= self.x + self.width and ball.x >= self.x):
            return False
        if not (ball.y - ball.radius <= self.y + self.height):
            return False

        self.hit()
        ball.set_vel(ball.x_vel, ball.y_vel * -1)
        return True

        
    def hit(self):
        self.health -= 1
        self.color = self.interpolate(*self.colors, self.health / self.max_health)

    @staticmethod
    def interpolate(color_a, color_b, t):
        return tuple(int(a + (b - a) * t) for a, b in zip(color_a, color_b))
