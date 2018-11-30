# Dungeon Crawler
import pygame, sys
from pygame.locals import *

pygame.init()

#creating game clock
FPS = 30 
fpsClock = pygame.time.Clock()

#creating game surface
DISPLAY_HEIGHT = 500
DISPLAY_WIDTH = 500

DISPLAYSURF = pygame.display.set_mode((DISPLAY_HEIGHT,DISPLAY_HEIGHT))
pygame.display.set_caption('Dungeon Crawler')

#color constants
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)

# comment

#create player sprite
playerimg = pygame.image.load('Assets/player.png')
playerx = DISPLAY_WIDTH/2
playery = DISPLAY_HEIGHT/2

#create text box
fontObj = pygame.font.Font('Assets/dungeon.ttf', 60)
textSurfaceObj = fontObj.render('~ Dungeon Crawler ~', True, WHITE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/8)

VELOCITY = 5

# main game loop
while True:

    DISPLAYSURF.fill(BLACK)
    DISPLAYSURF.blit(playerimg, (playerx,playery))
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    for event in pygame.event.get():
        if event.type == QUIT:
            game_quit()

    # handles key pressed events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        x+= VELOCITY
    if keys[pygame.K_LEFT]:
        x-= VELOCITY
    if keys[pygame.K_UP]:
        y-= VELOCITY
    if keys[pygame.K_DOWN]:
        y+= VELOCITY
    
    pygame.display.update()
    fpsClock.tick(FPS)
game_quit()

#game quit function
def game_quit():
    pygame.quit()
    sys.exit()

#test