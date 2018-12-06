# Dungeon Crawler
# By Luke Heitman & Jackson Enright
# https://github.com/LukeHeitman/Dungeon-Crawler.git

import pygame
import sys
import random
from imagedicts import *
from sprites import *
from pygame.locals import *

FPS = 30 # Maximum frames per second
DISPLAY_WIDTH = 512 # width of display window
DISPLAY_HEIGHT = 512 # height of display window
HALF_DW = DISPLAY_WIDTH/2
HALF_DH = DISPLAY_HEIGHT/2

BLOCK = 16 # Size of background level tiles (walls, floors, etc...)
TILE = 32 # Size of game tile for keys and enemies
assert DISPLAY_HEIGHT % TILE == 0 # ensures the height is a tile size multiple
assert DISPLAY_WIDTH % TILE == 0 # ensures the width is a tile size multiple

# splits map into tiles of 32
TILE_WIDTH = int(DISPLAY_WIDTH//TILE) 
TILE_HEIGHT = int(DISPLAY_HEIGHT//TILE)
BLOCK_WIDTH = int(DISPLAY_WIDTH//BLOCK) 
BLOCK_HEIGHT = int(DISPLAY_HEIGHT//BLOCK)
TOP_MARGIN = 2

 #color constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DEFAULTFONT = 'Assets/dungeon.ttf' # default font directory

def main():
    global FPSCLOCK, DISPLAYSURFACE, FONTSIZE, BASICFONT, IMAGEDICT

    pygame.init() # Pygame initialization
    FPSCLOCK = pygame.time.Clock()
   
    # load music and set it to play forever
    pygame.mixer.music.load('Assets/mariomusic.mp3')
    pygame.mixer.music.play(-1)
    # initialization of display surface and font
    DISPLAYSURFACE = pygame.display.set_mode((DISPLAY_HEIGHT, DISPLAY_HEIGHT))
    pygame.display.set_caption('Dungeon Crawler')
    FONTSIZE = 35
    BASICFONT = pygame.font.Font(DEFAULTFONT, FONTSIZE)

    keys_left = 3

    intro_screen() # Begin game with intro screen

    # initialize all movable sprites into the map
    player = Sprite(PLAYERDICT, DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2)
    monster = Monster(MONSTERDICT, DISPLAY_WIDTH/4, DISPLAY_HEIGHT/4)

    # initialize keys randomly around the map
    bkey = Key(KEYDICT['bronzekey'], rand_xtile(), rand_ytile())
    bkey.visible = True # make first key visible
    skey = Key(KEYDICT['silverkey'], rand_xtile(), rand_ytile())
    gkey = Key(KEYDICT['goldkey'], rand_xtile(), rand_ytile())
    game_keys = [bkey,skey,gkey]
    
    score = 0
    # variable to keep track of number of lives
    lives = 3

    while True: # main game loop
        for event in pygame.event.get(): # exits game if user clicks X
            if event.type == QUIT:
                game_quit()

        player.right = False
        player.left = False
        
        keys = pygame.key.get_pressed() # handles key pressed events and moves player
        if keys[pygame.K_RIGHT] and player.x < DISPLAY_WIDTH - player.width:
            player.x += player.vel
            player.right = True
            player.left = False
            player.direc = 'Right'
        if keys[pygame.K_LEFT] and player.x > player.vel:
            player.x -= player.vel
            player.right = False
            player.left = True
            player.direc = 'Left'
        if keys[pygame.K_UP] and player.y > player.vel + BLOCK * 2:
            player.y -= player.vel
        if keys[pygame.K_DOWN] and player.y < DISPLAY_HEIGHT - BLOCK * 1.5 - player.height:
            player.y += player.vel
        player.rect.topleft = (player.x, player.y)
        player.hitbox = player.rect.inflate(-15, -15) #recenters player rect after movement

        monster.move_towards_player(player) # move ghost sprite towards player

        DISPLAYSURFACE.fill(BLACK)
        
        for y in range(BLOCK_HEIGHT): # create level environment
            for x in range(BLOCK_WIDTH):
                block_rect = pygame.Rect((x * BLOCK, y * BLOCK, BLOCK, BLOCK))
                if y == 2 and not (BLOCK_WIDTH/2 - 2) < x < (BLOCK_WIDTH/2 + 1):
                    DISPLAYSURFACE.blit(LEVELDICT['wall_top'], block_rect)
                if y == 3:
                    door_open_rect = pygame.Rect((DISPLAY_WIDTH/2-1 * BLOCK, (y - 1) * BLOCK, TILE, TILE ))        
                    if keys_left == 0:
                        DISPLAYSURFACE.blit(LEVELDICT['door_open'][0], door_open_rect)
                        door_rect = pygame.Rect((DISPLAY_WIDTH/2-2 * BLOCK, (y - 1) * BLOCK, TILE, TILE ))
                        DISPLAYSURFACE.blit(LEVELDICT['door_open'][1], door_rect)
                        door_rect = pygame.Rect((DISPLAY_WIDTH/2+1 * BLOCK, (y - 1) * BLOCK, TILE, TILE ))
                        DISPLAYSURFACE.blit(LEVELDICT['door_open'][2], door_rect)
                        door_rect = pygame.Rect((DISPLAY_WIDTH/2-1 * BLOCK, (y - 1) * BLOCK - 3, TILE, TILE ))
                        DISPLAYSURFACE.blit(LEVELDICT['door_open'][3], door_rect)


                    else:
                        door_rect = pygame.Rect((DISPLAY_WIDTH/2-2 * BLOCK, (y - 1) * BLOCK - 3, TILE, TILE ))
                        DISPLAYSURFACE.blit(LEVELDICT['door'], door_rect)
                    door_open_hitbox = door_open_rect.inflate(-20, -20)    
                    

                    if x < (BLOCK_WIDTH/2 - 1) or x > (BLOCK_WIDTH/2):
                        DISPLAYSURFACE.blit(LEVELDICT['wall'], block_rect)
                if 3 < y < BLOCK_HEIGHT - 1:
                    DISPLAYSURFACE.blit(LEVELDICT['floor'][(x + y) % 3], block_rect)
                    if x == 0:
                        DISPLAYSURFACE.blit(LEVELDICT['side_wall_left'], block_rect)
                    if x == BLOCK_WIDTH - 1:
                        DISPLAYSURFACE.blit(LEVELDICT['side_wall_right'], block_rect)
                if y == BLOCK_HEIGHT - 1:
                     DISPLAYSURFACE.blit(LEVELDICT['wall'], block_rect)
        
        for key in game_keys: # collision testing for keys
            if player.hitbox.colliderect(key.rect) and key.visible == True:
                key.visible = False
                key.x, key.y = rand_xtile(), rand_ytile() 
                key.rect.center = (key.x, key.y)
                score += 1
                if key == bkey:
                    skey.visible = True
                    keys_left -= 1
                    monster.vel += 1
                elif key == skey:
                    gkey.visible = True
                    keys_left -= 1
                    monster.vel += 1
                elif key == gkey:
                    keys_left -= 1                    
                    monster.vel += 1 # ghost speeds up every 3 keys
        
        if player.hitbox.colliderect(monster.hitbox): # collision testing for ghost
            end_screen() # if ghost touches player - game over
            # player loses a life
            lives = lives - 1
        
        if keys_left == 0 and player.hitbox.colliderect(door_open_rect):
            game_win()
            # Stop music if the player exits through the door
            pygame.mixer.music.stop()

        # display all sprites on screen
        #DISPLAYSURFACE.blit(IMAGEDICT['bg'], (0, 0)) # background image
        player.draw(DISPLAYSURFACE)
        bkey.draw(DISPLAYSURFACE)
        skey.draw(DISPLAYSURFACE)
        gkey.draw(DISPLAYSURFACE)
        monster.draw(DISPLAYSURFACE)

        # test code for displaying score
        score_text = BASICFONT.render('Score:  ' + str(score), True, WHITE)
        score_rect = score_text.get_rect()
        score_rect.topleft = (10, 10)
        DISPLAYSURFACE.blit(score_text, score_rect) # Display title text
    
        # code for displaying lives
        life_text = BASICFONT.render('Lives:  ' + str(lives), True, WHITE)
        life_rect = life_text.get_rect()
        life_rect.topright = (DISPLAY_WIDTH-10, 10)
        DISPLAYSURFACE.blit(life_text, life_rect) # Display title text
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
    instructions = ['Collect keys to escape...', 'Stay away from the monsters!', 'PRESS SPACEBAR TO PLAY', 'USE ARROW KEYS TO MOVE']

    instruct_start = HALF_DH * 7/8 
    for line in instructions:
        instruct_text = BASICFONT.render(line, True, WHITE)
        instruct_rect = instruct_text.get_rect()
        instruct_rect.centerx = HALF_DW
        instruct_rect.top = instruct_start
        instruct_start += FONTSIZE + 10
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


def rand_xtile():
    rtile = random.randint(0, TILE_WIDTH -1) * TILE
    return rtile


def rand_ytile():
    rtile = random.randint(2, TILE_HEIGHT -1) * TILE
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
        top_margin += FONTSIZE + 10
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

def game_win():

    DISPLAYSURFACE.fill(BLACK) # Display background image TODO

    # Set up game over
    title_font = pygame.font.Font(DEFAULTFONT, 60)
    title_text = title_font.render('YOU WON', True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (HALF_DW, HALF_DH/4)
    DISPLAYSURFACE.blit(title_text, title_rect) # Display title text

    # Full list of information
    instructions = ['You collected all the keys and managed to escape!', 'Press R to replay']
    top_margin = HALF_DH * 7/8
    for line in instructions:
        instruct_text = BASICFONT.render(line, True, WHITE)
        instruct_rect = instruct_text.get_rect()
        instruct_rect.centerx = HALF_DW
        instruct_rect.top = top_margin
        top_margin += FONTSIZE + 10
        DISPLAYSURFACE.blit(instruct_text, instruct_rect)

    while True: # break out of intro screen with the space button
        for event in pygame.event.get():
            if event.type == QUIT:
                game_quit()
            elif event.type == KEYDOWN:
                if event.key == K_r:
                    main()
                if event.key == K_n:
                    LEVEL += 1
                    main()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

# game quit function
def game_quit():
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
