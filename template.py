# Dungeon Crawler
# By Luke Heitman & Jckson Enright
# https://github.com/LukeHeitman/Dungeon-Crawler.git

import pygame
import sys
from sprites import *
from pygame.locals import *

FPS = 30 # Maximum frames per second
DISPLAY_WIDTH = 500 # width of display window
DISPLAY_HEIGHT = 500 # height of display window
HALF_DW = DISPLAY_WIDTH/2
HALF_DH = DISPLAY_HEIGHT/2

 #color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DEFAULTFONT = 'Assets/dungeon.ttf'

TILE = 16 # Size of game tile

player = Sprite(DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2, 24, 32)

# code for adding music
# music = pygame.mixer.music.load('music.mp3')
# pygame.mixer.music.play(-1)

def main():
    global FPSCLOCK, DISPLAYSURFACE, BASICFONT, IMAGEDICT

    pygame.init() # Pygame initialization
    FPSCLOCK = pygame.time.Clock()

    # Creation of display surface and font
    DISPLAYSURFACE = pygame.display.set_mode((DISPLAY_HEIGHT, DISPLAY_HEIGHT))
    pygame.display.set_caption('Dungeon Crawler')
    BASICFONT = pygame.font.Font(DEFAULTFONT, 20)

    # Create global dictionary of all loaded images
    IMAGEDICT = {'player' : pygame.image.load('Assets/player.png'), 'bronzekey' : pygame.image.load('Assets/bronzekey.png'), 'silverkey' : pygame.image.load('Assets/silverkey.png'),'goldkey' : pygame.image.load('Assets/goldkey.png'), 'ghost' : pygame.image.load('Assets/ghostdown.png')}

    intro_Screen() # Begin game with intro screen

    # level variable that will be incremented each time the player picks up a key
    score = 0

    #keyone = (10,10)
    #keytwo = (150,150)
    #keythree = (400,400)

    # main game loop
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                game_Quit()

        keys = pygame.key.get_pressed() # handles key pressed events
        if keys[pygame.K_RIGHT] and player.x < DISPLAY_WIDTH - player.vel - player.width:
            player.x += player.vel
        if keys[pygame.K_LEFT] and player.x > player.vel:
            player.x -= player.vel
        if keys[pygame.K_UP] and player.y > player.vel:
            player.y -= player.vel
        if keys[pygame.K_DOWN] and player.y < DISPLAY_HEIGHT - player.vel - player.height:
            player.y += player.vel
        
        window_Draw()
        FPSCLOCK.tick(FPS)

    game_Quit()

def intro_Screen():
    # Set up title
    introFont = pygame.font.Font(DEFAULTFONT, 60)
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

# draw all objects on screen
def window_Draw():
    DISPLAYSURFACE.fill(BLACK)
    player.draw(DISPLAYSURFACE, IMAGEDICT['player'])
    DISPLAYSURFACE.blit(IMAGEDICT['bronzekey'], (10,10))
    DISPLAYSURFACE.blit(IMAGEDICT['silverkey'], (50,50))
    DISPLAYSURFACE.blit(IMAGEDICT['goldkey'], (100,100))
    DISPLAYSURFACE.blit(IMAGEDICT['ghost'], (200,200))
    pygame.display.update()


# game quit function
def game_Quit():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()