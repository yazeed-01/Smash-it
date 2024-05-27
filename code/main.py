from initialization import *
from paddle_class import *
from brick_class import *
from ball_class import *
from functions import *
#-------------------------------------------------------------------------------------
pygame.mixer.init()

#-------------------------------------------------------------------------------------
# values for items (potions):
x = randint(0, 500)
y = 100 
speed = 2
radius = 50
random_number = 0

potion_live = pygame.image.load("img/lives.png")
potion_flash = pygame.image.load("img/flash.png")
potion_paddle = pygame.image.load("img/green.png")

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------


#functions for items (potions):

def incLives():# for increase lives
  global lives
  lives += 1


def init(): # for draw items (potions)
    global x, y
    if y > HEIGHT - radius:
        y = 0
        x = randint(0, 800)


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------


clock = pygame.time.Clock()
display_output = [800, 600]
screen = pygame.display.set_mode(display_output)


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

color_ball = (173, 172, 172)

def main():
  global lives

  # GAME SETUP

  clock = pygame.time.Clock()
  play_song("sounds/song.mp3")  # play song
  paddle_x = WIDTH/2 - Paddle.width_paddle/2
  paddle_y = HEIGHT - Paddle.height_paddle - 5
  paddle = Paddle( # make paddle
    paddle_x,
    paddle_y, 
    Paddle.width_paddle, 
    Paddle.height_paddle,
    "green"
  )
  ball = Ball( # make ball
    WIDTH/2, 
    paddle_y - BALL_RADIUS, 
    BALL_RADIUS, 
    "white"
  )
  rows = 2  # number of rows bricks
  columns = 1 # number of columns bricks

  bricks = generate_bricks(rows, columns) # make bricks
  show_start_screen() # show start screen (main menu)
  

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
  def radom_num(): # for create random number for items
        global random_number
        random_number = random.randint(1, 4) # random number for items
        if random_number == 1: # if 1 increse live
          incLives()
        if random_number == 2: # if 2 increase paddle width
          paddle.inc_paddle()
        if random_number == 3: # if 3 increase paddle speed
          paddle.inc_Vel()



  def items(): # for draw items (potions)
        global y
        y+= speed
        if random_number == 1:
          screen.blit(resize_image(potion_live), (x, y)) 
        if random_number == 2:
          screen.blit(resize_image(potion_paddle), (x, y))
        if random_number == 3:
          screen.blit(resize_image(potion_flash), (x, y))

        pygame.display.flip()


#-------------------------------------------------------------------------------------


# GAME LOOP

  run = True
  while run:
    clock.tick(FPS) # FPS (60) lock the frame rate
    if not pygame.mixer.music.get_busy():
        play_song("sounds/song.mp3") # play the song 
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
        break
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.x - paddle.vel >= 0:
      paddle.move(-1) # for move paddle to left
    if keys[pygame.K_RIGHT] and paddle.x + paddle.width + paddle.vel <= WIDTH:
      paddle.move(1) # for move paddle to right
    ball.move()
    ball_collision(ball) 
    ball_paddle_collision(ball, paddle) # type: ignore
    for brick in bricks[:]:
      brick.collide(ball)
      if brick.health <= 0:
        radom_num() # for create random number for items (potions)
        bricks.remove(brick) # remove brick when health is 0
        init() # for draw items (potions)
    if ball.y + ball.radius >= HEIGHT:
      lives -=1
      ball.x = paddle.x + paddle.width/2
      ball.y = paddle_y - BALL_RADIUS
      ball.set_vel(0, ball.VEL * -1)
    items() # for draw items (potions)
    items() # for draw items (potions)
    if lives <= 0:
      lose_screen() # show lose screen when all lives are lost
    if len(bricks) == 0:
      win_screen() # show win screen when all bricks are destroyed
    items()        
    draw(win, paddle, ball, bricks, lives) # draw game elements
    items()
  pygame.quit()
  quit()




if __name__ == "__main__":
    main() #run the game