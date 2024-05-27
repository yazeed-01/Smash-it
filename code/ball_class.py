from initialization import *
class Ball:
    VEL = 5 #speed

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.x_vel = 0
        self.y_vel = -self.VEL

    
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

    
    def set_vel(self, x_vel, y_vel):
        self.x_vel = x_vel
        self.y_vel = y_vel

        
    def draw(self, win):
        pygame.draw.circle(
        win, 
        self.color, 
        (
            self.x, 
            self.y
        ), 
        self.radius
        )
