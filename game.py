import pygame
# Initialize game engine
pygame.init()

# sets a variable called background to the background image you want to include (we should use this for screen 1)
# background = pygame.image.load("images/background.png")
# adds a picture at the specific coords where you want it to appear
# screen.blit(background, (0, 0))

#TEST

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
# creates the window/display that the game will be played on
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
# displays a caption at the top of the window
pygame.display.set_caption('Dungeon Crawler.')


# add a clock object to put pauses on each iteration of game loop
# fps = frames per second
# setting fps to a lower value will make it run slower..
fps = 30
clock = pygame.time.Clock()

# makes constant color values
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)

# sets x and y vals for where character will start out
# top left corner is 0,0
# bottom right corner is 500,500
x = 50
y = 50
# sets size of character
width = 50
height = 50
# sets speed for how fast character is able to move
velocity = 5

run = True
#  this is the main loop that you will be able to check for everything in
while run:
    # do this in order to have some kind of running clock so everything does not happen at once
    # pygame.time.delay(100)

    # need to use a for loop in order to check for events
    for event in pygame.event.get():
        # handles quit if user quits out of the game window
        if event.type == pygame.QUIT:
            run = False

    # handles key pressed events
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        x+= velocity
    if keys[pygame.K_LEFT]:
        x-= velocity
    if keys[pygame.K_UP]:
        y-= velocity
    if keys[pygame.K_DOWN]:
        y+= velocity

    # if user presses space, check if they are over and object and if they are pick it up and add to some type of inventory
   # if event.key == pygame.K_SPACE:
        # check if they are touching a key object
        # add a sound here for when the character picks up a key


    # fills display before the new rectangle is drawn
    display.fill(BLACK)
    pygame.draw.rect(display, RED, (x, y, width, height))
    # updates the display once the rectangle is added
    pygame.display.update()

    clock.tick(fps)

pygame.quit()
