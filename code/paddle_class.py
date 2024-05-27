from initialization import *
class Paddle:
    vel = 4 #speed
    width_paddle = 100
    height_paddle = 10

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = Paddle.width_paddle
        self.height = Paddle.height_paddle
        self.color = color


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
    def inc_Vel(self):
        self.vel +=  4


    def move(self, direction=5):
        self.x = self.x + self.vel * direction
    
    def inc_paddle (self):
       self.width += 50