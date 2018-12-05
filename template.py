# Dungeon Crawler
# By Luke Heitman & Jckson Enright
# https://github.com/LukeHeitman/Dungeon-Crawler.git

import pygame
import sys
import random
from sprites import *
from pygame.locals import *

FPS = 30 # Maximum frames per second
DISPLAY_WIDTH = 512 # width of display window
DISPLAY_HEIGHT = 512 # height of display window
HALF_DW = DISPLAY_WIDTH/2
HALF_DH = DISPLAY_HEIGHT/2

TILE = 32 # Size of game tile
assert DISPLAY_HEIGHT % TILE == 0 # ensures the height is a tile size multiple
assert DISPLAY_WIDTH % TILE == 0 # ensures the width is a tile size multiple

TILE_WIDTH = int(DISPLAY_WIDTH//TILE) # splits map into tiles of 32
TILE_HEIGHT = int(DISPLAY_HEIGHT//TILE)

 #color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DEFAULTFONT = 'Assets/dungeon.ttf'


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
    IMAGEDICT = {'player' : pygame.image.load('Assets/player.png'), 'bronzekey' : pygame.image.load('Assets/bronzekey.png'), 'silverkey' : pygame.image.load('Assets/silverkey.png'),'goldkey' : pygame.image.load('Assets/goldkey.png'), 'ghost' : pygame.image.load('Assets/ghostdown.png'), 'bg' : pygame.image.load('Assets/background.png')}

    intro_screen() # Begin game with intro screen

    score = 0 # score variable that will be incremented each time the player picks up a key

    # initialize all movable sprites into the map
    player = Sprite(IMAGEDICT['player'], DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2)
    ghost = Sprite(IMAGEDICT['ghost'], DISPLAY_WIDTH/4, DISPLAY_HEIGHT/4)

    # initialize keys randomly around the map
    bkey = Key(IMAGEDICT['bronzekey'], rand_tile(TILE_WIDTH) * TILE, rand_tile(TILE_HEIGHT) * TILE)
    bkey.visible = True
    skey = Key(IMAGEDICT['bronzekey'],rand_tile(TILE_WIDTH) * TILE, rand_tile(TILE_HEIGHT) * TILE)
    gkey = Key(IMAGEDICT['bronzekey'],rand_tile(TILE_WIDTH) * TILE, rand_tile(TILE_HEIGHT) * TILE)

    # main game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_quit()
                

        keys = pygame.key.get_pressed() # handles key pressed events
        if keys[pygame.K_RIGHT] and player.x < DISPLAY_WIDTH - player.vel - player.width:
            player.x += player.vel
        if keys[pygame.K_LEFT] and player.x > player.vel:
            player.x -= player.vel
        if keys[pygame.K_UP] and player.y > player.vel:
            player.y -= player.vel
        if keys[pygame.K_DOWN] and player.y < DISPLAY_HEIGHT - player.vel - player.height:
            player.y += player.vel
        
        if player.collide(bkey.rect) and bkey.visible == True: # basic test function for changing key visibility
            bkey.visible = False
            bkey.x = rand_tile(TILE_WIDTH) * TILE
            bkey.y = rand_tile(TILE_HEIGHT) * TILE
            skey.visible = True
            score += 1
        if player.collide(skey.rect) and skey.visible == True: # basic test function for changing key visibility
            skey.visible = False
            skey.x = rand_tile(TILE_WIDTH) * TILE
            skey.y = rand_tile(TILE_HEIGHT) * TILE
            gkey.visible = True
            score += 1
        if player.collide(gkey.rect) and gkey.visible == True: # basic test function for changing key visibility
            gkey.visible = False
            gkey.x = rand_tile(TILE_WIDTH) * TILE
            gkey.y = rand_tile(TILE_HEIGHT) * TILE
            bkey.visible = True
            score += 1

        # dispaly all sprites on screen
        DISPLAYSURFACE.blit(IMAGEDICT['bg'], (0, 0))
        player.draw(DISPLAYSURFACE)
        bkey.draw(DISPLAYSURFACE)
        skey.draw(DISPLAYSURFACE)
        gkey.draw(DISPLAYSURFACE)
        ghost.draw(DISPLAYSURFACE)

        # test code for displaying score
        title_text = BASICFONT.render(str(score), True, WHITE)
        title_rect = title_text.get_rect()
        title_rect.center = (32, 32)
        DISPLAYSURFACE.blit(title_text, title_rect) # Display title text

        pygame.display.update()
        FPSCLOCK.tick(FPS)

    game_quit()

def intro_screen():
    DISPLAYSURFACE.fill(BLACK) # Display background image TODO

    # Set up title
    title_font = pygame.font.Font(DEFAULTFONT, 60)
    title_text = title_font.render('Dungeon Crawler', True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (HALF_DW, HALF_DH/4)
    DISPLAYSURFACE.blit(title_text, title_rect) # Display title text

    # Full list of all instructions, line by line
    instructions = ['Press Spacebar to Play', 'Use arrow keys to move']
    top_margin = HALF_DH * 7/8
    for line in instructions:
        instruct_text = BASICFONT.render(line, True, WHITE)
        instruct_rect = instruct_text.get_rect()
        instruct_rect.centerx = HALF_DW
        instruct_rect.top = top_margin
        top_margin += 20 + 10
        DISPLAYSURFACE.blit(instruct_text, instruct_rect)

    while True: # break out of intro screen with the space button
        for event in pygame.event.get():
            if event.type == QUIT:
                game_quit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    return

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def rand_tile(max):
    rtile = random.randint(0, max -1)
    return rtile


def end_screen():
    DISPLAYSURFACE.fill(BLACK) # Display background image TODO

    # Set up game over
    title_font = pygame.font.Font(DEFAULTFONT, 60)
    title_text = title_font.render('GAME OVER', True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (HALF_DW, HALF_DH/4)
    DISPLAYSURFACE.blit(title_text, title_rect) # Display title text

    # Full list of information
    instructions = ['The ghost caught you before you could escape!', 'Press R to restart']
    top_margin = HALF_DH * 7/8
    for line in instructions:
        instruct_text = BASICFONT.render(line, True, WHITE)
        instruct_rect = instruct_text.get_rect()
        instruct_rect.centerx = HALF_DW
        instruct_rect.top = top_margin
        top_margin += 20 + 10
        DISPLAYSURFACE.blit(instruct_text, instruct_rect)

    while True: # break out of intro screen with the space button
        for event in pygame.event.get():
            if event.type == QUIT:
                game_quit()
            elif event.type == KEYDOWN:
                if event.key == K_r:
                    main()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# game quit function
def game_quit():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
