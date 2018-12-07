# Dungeon Crawler
# By Luke Heitman & Jackson Enright
# Github Link: https://github.com/LukeHeitman/Dungeon-Crawler.git

import pygame
import sys
import random
from imagedicts import *
from sprites import *
from pygame.locals import *

FPS = 30 # maximum frames per second
DISPLAY_WIDTH = 512 # width of display window
DISPLAY_HEIGHT = 512 # height of display window
HALF_DW = DISPLAY_WIDTH/2
HALF_DH = DISPLAY_HEIGHT/2

BLOCK = 16 # size of background level tiles (walls, floors, etc...)
TILE = 32 # size of larger game tile for spawning keys and enemies
assert DISPLAY_HEIGHT % TILE == 0 # ensures the height is a tile size multiple
assert DISPLAY_WIDTH % TILE == 0 # ensures the width is a tile size multiple

# splits map into tiles of 32
TILE_WIDTH = int(DISPLAY_WIDTH//TILE) 
TILE_HEIGHT = int(DISPLAY_HEIGHT//TILE)
BLOCK_WIDTH = int(DISPLAY_WIDTH//BLOCK) 
BLOCK_HEIGHT = int(DISPLAY_HEIGHT//BLOCK)
TOP_MARGIN = 2 # number of empty BLOCKS top of screen

BLACK = (0, 0, 0) # color constants
WHITE = (255, 255, 255)
DEFAULTFONT = 'Assets/dungeon.ttf' # default font directory


def main():
    global FPSCLOCK, DISPLAYSURFACE, FONTSIZE, BASICFONT

    pygame.init() # Pygame initialization
    FPSCLOCK = pygame.time.Clock()

    pygame.mixer.music.load('Assets/mariomusic.mp3') # load game music and set it to play forever
    pygame.mixer.music.play(-1)

    # initialization of display surface and font
    DISPLAYSURFACE = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption('Dungeon Crawler') # set caption of window
    FONTSIZE = 35
    BASICFONT = pygame.font.Font(DEFAULTFONT, FONTSIZE)

    intro_screen() # Begin game with intro screen

    level = 1 # set game level to 1
    lives = 3 # set game lives to 3

    game_loop(level, lives)

    game_quit()


def intro_screen():
    DISPLAYSURFACE.fill(BLACK) # set black background for screen
    
    # set up game title
    title_font = pygame.font.Font(DEFAULTFONT, 60) 
    title_text = title_font.render('Dungeon Crawler', True, WHITE) 
    title_rect = title_text.get_rect()
    title_rect.center = (HALF_DW, HALF_DH/4) # place center of text box
    DISPLAYSURFACE.blit(title_text, title_rect) # Display title text

    # Full list of all instructions and game open, line by line
    instructions = ['Collect keys to escape...', 'Stay away from the monsters!', 'PRESS SPACEBAR TO PLAY', 'USE ARROW KEYS TO MOVE']

    instruct_start = HALF_DH * 7/8 # where the first line of instructions begins
    for line in instructions: # iterate through all lines in instructions
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


def game_loop(level, lives): # main game loop with current level and lives
    
    player = Player(PLAYERDICT, HALF_DW, HALF_DH) # initialize player sprite

    # initialize all monster sprites
    demon = Monster(DEMONDICT, rand_xtile(player.x), rand_ytile(player.y), 1)
    demon.visible = True # make demon visible
    ogre1 = Monster(OGREDICT, HALF_DW-1 * BLOCK, 30, 1)
    ogre2 = Monster(OGREDICT, HALF_DW-1 * BLOCK, 30, 1)
    ogre3 = Monster(OGREDICT, HALF_DW-1 * BLOCK, 30, 1)
    skeleton1 = Monster(SKELETONDICT, HALF_DW - 225, HALF_DH, 3)
    skeleton2 = Monster(SKELETONDICT, HALF_DW + 225, HALF_DH, 3)

    # create lists with monsters
    monsters = [demon, ogre1, ogre2, ogre3, skeleton1, skeleton2]
    ogres = [ogre1, ogre2, ogre3]
    skeletons = [skeleton1, skeleton2]
    
   
    if level > 1: # create conditional to spawn skeletons after level 1
        for skeleton in skeletons:
            skeleton.visible = True

    # initialize keys randomly around the map
    bkey = Key(KEYDICT['bronzekey'], rand_xtile(player.x), rand_ytile(player.y))
    bkey.visible = True # make first key visible
    skey = Key(KEYDICT['silverkey'], rand_xtile(player.x), rand_ytile(player.y))
    gkey = Key(KEYDICT['goldkey'], rand_xtile(player.x), rand_ytile(player.y))
    game_keys = [bkey, skey, gkey] # create list of keys
    key_sound = pygame.mixer.Sound('Assets/keypickup.wav') # load game sound for the picking up of keys
    
    keys = 3  # set keys needed to be picked up to 3

    while True: # erpeating game loop after level initialization
        for event in pygame.event.get(): # tracks all game events
            if event.type == QUIT: # exits game if user clicks X
                game_quit()
            elif event.type == KEYDOWN:
                if event.key == K_r: # restarts game if r key pressed
                    main()

        # initialize level environment
        DISPLAYSURFACE.fill(BLACK) # set background color to black
        for y in range(BLOCK_HEIGHT): # for loops to iterate over all map blocks
            for x in range(BLOCK_WIDTH):
                block_rect = pygame.Rect((x * BLOCK, y * BLOCK, BLOCK, BLOCK)) # create rectangle the size of a block for placing
                if y == 2 and not (BLOCK_WIDTH/2 - 2) < x < (BLOCK_WIDTH/2 + 1): # places wall tops on 3rd block but not over door
                    DISPLAYSURFACE.blit(LEVELDICT['wall_top'], block_rect)
                if y == 3:
                    door_open_rect = pygame.Rect((HALF_DW-1 * BLOCK, (y - 1) * BLOCK, TILE, TILE )) # set rect for open door outside conditional       
<<<<<<< HEAD
=======
                    DISPLAYSURFACE.blit(LEVELDICT['door'], door_rect) # shrinks door hitbox size
>>>>>>> 213f4018e0ab002ad501228e8833f82822e649a9
                    if keys == 0: # creates open door if collected all keys
                        DISPLAYSURFACE.blit(LEVELDICT['door_open'][0], door_open_rect) 
                        door_rect = pygame.Rect((HALF_DW-2 * BLOCK, (y - 1) * BLOCK, TILE, TILE ))
                        DISPLAYSURFACE.blit(LEVELDICT['door_open'][1], door_rect)
                        door_rect = pygame.Rect((HALF_DW+1 * BLOCK, (y - 1) * BLOCK, TILE, TILE ))
                        DISPLAYSURFACE.blit(LEVELDICT['door_open'][2], door_rect)
                        door_rect = pygame.Rect((HALF_DW-1 * BLOCK, (y - 1) * BLOCK - 3, TILE, TILE ))
                        DISPLAYSURFACE.blit(LEVELDICT['door_open'][3], door_rect)
                    else: # spawn closed door 
                        door_rect = pygame.Rect((HALF_DW-2 * BLOCK, (y - 1) * BLOCK - 3, TILE, TILE ))
<<<<<<< HEAD
                        DISPLAYSURFACE.blit(LEVELDICT['door'], door_rect) # shrinks door hitbox size
=======
>>>>>>> 213f4018e0ab002ad501228e8833f82822e649a9
                    door_open_hitbox = door_open_rect.inflate(-20, -20) #  
                    if x < (BLOCK_WIDTH/2 - 1) or x > (BLOCK_WIDTH/2):
                        DISPLAYSURFACE.blit(LEVELDICT['wall'], block_rect)
                if 3 < y < BLOCK_HEIGHT - 1: # spawn randomized floor tiles across map
                    DISPLAYSURFACE.blit(LEVELDICT['floor'][(x + y) % 3], block_rect)
                    if x == 0:
                        DISPLAYSURFACE.blit(LEVELDICT['side_wall_left'], block_rect)
                    if x == BLOCK_WIDTH - 1:
                        DISPLAYSURFACE.blit(LEVELDICT['side_wall_right'], block_rect)
                if y == BLOCK_HEIGHT - 1: #spawn bottom wall
                     DISPLAYSURFACE.blit(LEVELDICT['wall'], block_rect)

        player.right = False # reset player movement
        player.left = False        
        
        inputs = pygame.key.get_pressed() # handles key pressed events and moves player
        if inputs[pygame.K_RIGHT] and player.x < DISPLAY_WIDTH - player.width:
            player.x += player.vel
            player.right = True
            player.left = False
            player.direc = 'Right' # variable to handle sprite animzation
        if inputs[pygame.K_LEFT] and player.x > player.vel:
            player.x -= player.vel
            player.right = False
            player.left = True
            player.direc = 'Left'
        if inputs[pygame.K_UP] and player.y > player.vel + BLOCK * 2:
            player.y -= player.vel
        if inputs[pygame.K_DOWN] and player.y < DISPLAY_HEIGHT - BLOCK * 1.5 - player.height:
            player.y += player.vel
        player.rect.topleft = (player.x, player.y) # recenter player rect after movement
        player.hitbox = player.rect.inflate(-15, -15) # recenter player hitbox

<<<<<<< HEAD
        
=======
        for monster in monsters: # move all monsters toward player
            monster.move_towards_player(player)
>>>>>>> 213f4018e0ab002ad501228e8833f82822e649a9

        for key in game_keys: # collision testing for keys
            if player.hitbox.colliderect(key.rect) and key.visible == True: # tests if player collides with key
                if level == 3: # spawns an ogre for every key if level 3
                    ogres[keys - 1].visible = True
                key.visible = False # hide key
                key_sound.play() # play sound
                
                # conditionals to display next key
                if key == bkey:
                    skey.visible = True
                    keys -= 1
                    demon.vel += 1 # demon speeds up every key
                elif key == skey:
                    gkey.visible = True
                    keys -= 1
                    demon.vel += 1
                elif key == gkey:
                    keys -= 1                    
                    demon.vel += 1 
<<<<<<< HEAD

        for monster in monsters: # move all monsters toward player
            monster.move_towards_player(player)
=======
>>>>>>> 213f4018e0ab002ad501228e8833f82822e649a9

        for monster in monsters: # collision test for each monster
            if monster.visible == True and monster.hitbox.colliderect(player.hitbox): # collision testing for ghost
                lives = lives - 1 # player loses a life
                if lives > 0: # remove life            
                    game_loop(level, lives)
                else: # if no remaining lives -> game over
                    end_screen()
        
        # collision testing for door if all keys have been collected
        if keys == 0 and player.hitbox.colliderect(door_open_rect):
            level += 1 # set to next level
            if level > 3: # if player just finished level 3 -> game won
                pygame.mixer.music.stop() # Stop music if the player exits through the door
                seconds = pygame.time.get_ticks() // 1000
                game_win(seconds)
            else: # else move onto next level
                game_loop(level, lives)

        # draw all sprites   
        player.draw(DISPLAYSURFACE)
        for monster in monsters:
            monster.draw(DISPLAYSURFACE)
        for key in game_keys:
            key.draw(DISPLAYSURFACE)

        # Display current player level
        level_text = BASICFONT.render('Level:  ' + str(level), True, WHITE)
        level_rect = level_text.get_rect()
        level_rect.topleft = (10, 10) # place in top left corner
        DISPLAYSURFACE.blit(level_text, level_rect)
    
        # display current player text
        life_text = BASICFONT.render('Lives:  ' + str(lives), True, WHITE)
        life_rect = life_text.get_rect()
        life_rect.topright = (DISPLAY_WIDTH-10, 10) # place in top right corner
        DISPLAYSURFACE.blit(life_text, life_rect)
        
        pygame.display.update() # update screen with all updated images
        FPSCLOCK.tick(FPS) #tick game clock


def rand_xtile(playerx): # chooses random x tile, as long as not near player
    rtile = playerx
    while abs(playerx - rtile) < 75:
        rtile = random.randint(0, TILE_WIDTH -1) * TILE
    return rtile


def rand_ytile(playery): # chooses random y tile, as long as not near player, or in top margins
    rtile = playery
    while abs(playery - rtile) < 75:
        rtile = random.randint(TOP_MARGIN, TILE_HEIGHT -1) * TILE
    return rtile


def end_screen(): # show when player loses all lives
    DISPLAYSURFACE.fill(BLACK) # fill background as black

    # Initialize game over text
    title_font = pygame.font.Font(DEFAULTFONT, 60)
    title_text = title_font.render('GAME OVER', True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (HALF_DW, HALF_DH/4)
    DISPLAYSURFACE.blit(title_text, title_rect) # Display game over text

    # Full list of end game info
    instructions = ['A monster caught you before you could escape!', 'Press R to restart']
    top_margin = HALF_DH * 7/8 # where to start list of end game comments
    for line in instructions: # iterate over each line of list
        instruct_text = BASICFONT.render(line, True, WHITE)
        instruct_rect = instruct_text.get_rect()
        instruct_rect.centerx = HALF_DW
        instruct_rect.top = top_margin
        top_margin += FONTSIZE + 10
        DISPLAYSURFACE.blit(instruct_text, instruct_rect)

    while True: # restart game with r key
        for event in pygame.event.get():
            if event.type == QUIT:
                game_quit()
            elif event.type == KEYDOWN:
                if event.key == K_r:
                    main()

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def game_win(seconds): # show when player wins game
    DISPLAYSURFACE.fill(BLACK) 

    # Set up game won text
    title_font = pygame.font.Font(DEFAULTFONT, 60)
    title_text = title_font.render('YOU WON', True, WHITE)
    title_rect = title_text.get_rect()
    title_rect.center = (HALF_DW, HALF_DH/4)
    DISPLAYSURFACE.blit(title_text, title_rect) # Display game over text

    # Full list of game win info
    instructions = ['You took ' + str(seconds) + ' seconds!', 'You collected all the keys and managed to escape!', 'Press R to replay']
    top_margin = HALF_DH * 7/8
    for line in instructions:
        instruct_text = BASICFONT.render(line, True, WHITE)
        instruct_rect = instruct_text.get_rect()
        instruct_rect.centerx = HALF_DW
        instruct_rect.top = top_margin
        top_margin += FONTSIZE + 10
        DISPLAYSURFACE.blit(instruct_text, instruct_rect)

    while True: # restart game with r key
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


def game_quit(): # game quit function
    pygame.quit()
    sys.exit()


if __name__ == '__main__':
    main()
