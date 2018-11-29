import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAY_HEIGHT = 800
DISPLAY_WIDTH = 600

DISPLAYSURF = pygame.display.set_mode((DISPLAY_HEIGHT,DISPLAY_HEIGHT))
pygame.display.set_caption('Snake')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()


