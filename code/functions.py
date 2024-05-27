from initialization import *
from paddle_class import *
from brick_class import *
from ball_class import *
from main import *

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------



def resize_image(image):
    return pygame.transform.scale(image, (30, 30))

#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------


# song


def play_song(filepath):
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play(-1)








#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------


# start screen

def show_start_screen():
    background_img = pygame.image.load("./img/start_screen.jpg")
    win.blit(background_img, (0, 0))

    pygame.display.flip()

    is_muted = False
    # main menu clicks
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()  # Exit the game loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:  # Mute music on 'M' press
                    is_muted = True
                    pygame.mixer.music.set_volume(0)  # Mute music
                elif event.key == pygame.K_n:  # Unmute music on 'N' press
                    is_muted = False
                    pygame.mixer.music.set_volume(1.0) # Unmute music
                elif event.key == pygame.K_q:  # Quit game on 'Q' press
                    waiting = False
                    pygame.quit()
                    quit()  # Exit the game loop
                else:
                    waiting = False  # Start the game on any other key press





#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

#  create bricks


def generate_bricks(rows, cols):
    gap = 2 
    brick_width = WIDTH // cols - gap
    brick_height = 30  # Adjust brick height as needed
    padding_top = 370  # Adjust padding at the bottom
    l = 1 # Start with level 1 (take 1 shot) for the first row 
    bricks = []
    for row in range(rows):
        for col in range(cols):
            brick_y = HEIGHT - padding_top - brick_height - (row * (brick_height + gap)) # Calculate brick Y position considering padding
            brick = Brick(
                col * brick_width + gap * col,
                brick_y,
                brick_width,
                brick_height,
                l,
                [(209, 240, 10), (255, 0, 0)] # Adjust colors as needed
            )
            bricks.append(brick)
        l += 1 # Increment level (take more shots)

    return bricks


#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------

# draw

def draw(win, paddle, ball, bricks, lives):
    background_img = pygame.image.load("./img/galaxy.jpg")
    win.blit(background_img, (0, 0))

    paddle.draw(win)
    ball.draw(win)

    for brick in bricks:
        brick.draw(win)

    # Draw hearts/lives images in a row
    heart_width, heart_height = 25, 25  # Original size
    new_width, new_height = 15, 15  # Desired size after resize
    heart_spacing = 5
    start_x = 10  # Adjust horizontal starting position

    for i in range(lives):
        heart_center_x = start_x + i * (new_width + heart_spacing)

        # Load appropriate image based on remaining lives
        if i < lives:
            heart_img = pygame.image.load("./img/lives.png")
        else:
            heart_img = pygame.image.load("./img/lives.png")

        # Resize the image
        heart_img = pygame.transform.scale(heart_img, (new_width, new_height))

        # Adjust Y position as needed
        win.blit(heart_img, (heart_center_x - new_width // 2, 0))

    pygame.display.update()



#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------


def draw_heart(win, center_x, center_y, width, height, color):
    # Define points for a heart shape (adjust as needed)
    points = [
        (center_x, center_y + height // 3),
        (center_x - width // 2, center_y),
        (center_x, center_y - height // 3),
        (center_x + width // 2, center_y),
        (center_x, center_y + height // 3),
        (center_x - width // 4, center_y + height * 2 // 3),
        (center_x + width // 4, center_y + height * 2 // 3)
    ]
    pygame.draw.polygon(win, color, points)


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

# ball collision

def ball_collision(ball):
  if ball.x - BALL_RADIUS <= 0 or ball.x + BALL_RADIUS >= WIDTH:
    ball.set_vel(ball.x_vel * -1, ball.y_vel)
  if ball.y + BALL_RADIUS >= HEIGHT or ball.y - BALL_RADIUS <= 0:
    ball.set_vel(ball.x_vel, ball.y_vel * -1)




#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

# ball paddle collision


def ball_paddle_collision(ball, paddle):
  if not (ball.x <= paddle.x + paddle.width and ball.x >= paddle.x):
    return
  if not (ball.y + ball.radius >= paddle.y):
    return

  paddle_center = paddle.x + paddle.width/2
  distance_to_center = ball.x - paddle_center

  percent_width = distance_to_center / paddle.width
  angle = percent_width * 90
  angle_radians = math.radians(angle)

  x_vel = math.sin(angle_radians) * ball.VEL
  y_vel = math.cos(angle_radians) * ball.VEL * -1

  ball.set_vel(x_vel, y_vel)


#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------

# win lose screens

def win_screen():
    background_img = pygame.image.load("img/win.png")
    win.blit(background_img, (0, 0))

    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # Check if a key is pressed
                if event.key == pygame.K_q:  # Check if the key is 'Q'
                    waiting = False
                    pygame.quit()
                    quit()





def lose_screen():
    background_img = pygame.image.load("./img/you_lost.jpg")
    win.blit(background_img, (0, 0))

    font = pygame.font.SysFont(None, 58)

    #text = font.render(' YOU LOST!', True, "red")
    text2 = font.render(' Press Q to quit', True, "white")
    #win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 + -200))
    win.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2 - text2.get_height() // 2 + 250))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:  # Check if a key is pressed
                if event.key == pygame.K_q:  # Check if the key is 'Q'
                    waiting = False
                    pygame.quit()
                    quit()
