# Dungeon Crawler
# By Luke Heitman & Jckson Enright
# https://github.com/LukeHeitman/Dungeon-Crawler.git

import pygame, sys
from pygame.locals import *

FPS = 30 # Maximum frames per second
DISPLAY_WIDTH = 500 # width of display window
DISPLAY_HEIGHT = 500 # height of display window
HALF_DW = DISPLAY_WIDTH/2
HALF_DH = DISPLAY_HEIGHT/2

 #color constants
BLACK = (0,0,0)
WHITE = (255,255,255)
defaultFont = 'Assets/dungeon.ttf'

TILE = 16 # Size of game tile

def main():
    global FPSCLOCK, DISPLAYSURFACE, BASICFONT, IMAGEDICT

    pygame.init() # Pygame initialization
    FPSCLOCK = pygame.time.Clock()

    # Creation of display surface and font
    DISPLAYSURFACE = pygame.display.set_mode((DISPLAY_HEIGHT,DISPLAY_HEIGHT))
    pygame.display.set_caption('Dungeon Crawler')
    BASICFONT = pygame.font.Font(defaultFont, 20)

    # Create global dictionary of all loaded images
    IMAGEDICT = {'player' : pygame.image.load('Assets/player.png'), 'bronzekey' : pygame.image.load('Assets/bronzekey.png'),
    'silverkey' : pygame.image.load('Assets/silverkey.png'),'goldkey' : pygame.image.load('Assets/goldkey.png')}

    intro_Screen() # Begin game with intro screen

    # Define player position
    playerX = DISPLAY_WIDTH/2
    playerY = DISPLAY_HEIGHT/2

    VELOCITY = 5 # set movement of player

    # main game loop
    while True:

        DISPLAYSURFACE.fill(BLACK)
        DISPLAYSURFACE.blit(IMAGEDICT['player'], (playerX,playerY))
        DISPLAYSURFACE.blit(IMAGEDICT['bronzekey'], (10,10)
        DISPLAYSURFACE.blit(IMAGEDICT['silverkey'], (50,50))
        DISPLAYSURFACE.blit(IMAGEDICT['goldkey'], (100,100))

        for event in pygame.event.get():
            if event.type == QUIT:
                game_Quit()

        keys = pygame.key.get_pressed() # handles key pressed events
        if keys[pygame.K_RIGHT]:
            playerX += VELOCITY
        if keys[pygame.K_LEFT]:
            playerX -= VELOCITY
        if keys[pygame.K_UP]:
            playerY -= VELOCITY
        if keys[pygame.K_DOWN]:
            playerY += VELOCITY

        pygame.display.update()
        FPSCLOCK.tick(FPS)

    game_Quit()



#def read_template():
    #mapTemplate =   [WWWW,
                    # WFFW,
    #                 WWWW]
   # for line in mapTemplate:


#def make_board():
    #TODO

def intro_Screen():
    # Set up title
    introFont = pygame.font.Font(defaultFont, 60)
    introText = introFont.render('Dungeon Crawler', True, WHITE)
    introRect = introText.get_rect()
    introRect.center = (HALF_DW,HALF_DH/4)

    DISPLAYSURFACE.fill(BLACK) # Display background image TODO

    DISPLAYSURFACE.blit(introText,introRect) # Display title text
    
    # Full list of all instructions, line by line
    instructions = ['Press Spacebar to Play', 'Use arrow keys to move']
    instructHeight = HALF_DH * 7/8
    for i in range(len(instructions)):
        instructText = BASICFONT.render(instructions[i], True, WHITE)
        instructRect = instructText.get_rect()
        
        instructRect.centerx = HALF_DW
        instructRect.top = instructHeight
        instructHeight += instructHeight + 10
        DISPLAYSURFACE.blit(instructText, instructRect)
    
    while True: # break out of intro screen with the space button
        for event in pygame.event.get():
            if event.type == QUIT:
                game_Quit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return

        pygame.display.update()
        FPSCLOCK.tick(FPS)

#game quit function
def game_Quit():
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
