import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self, dict, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.vel = 5
        self.step = 0
        self.dx = 0
        self.dx = 0
        self.direc = 'Right'
        self.image = dict
        self.rect = self.image['IdleR'][0].get_rect()
        self.rect.topleft = (self.x, self.y)
        self.hitbox = self.rect.inflate(-10, -10)
        self.width , self.height = self.rect.size


    def draw(self, window):
        if self.step > 15:
            self.step = 0
        if self.left == True:
            window.blit(self.image['Left'][self.step // 5], (self.x, self.y))
            self.step += 1
        elif self.right == True:
            window.blit(self.image['Right'][self.step // 5], (self.x, self.y))
            self.step += 1
        elif self.direc == 'Right': 
            window.blit(self.image['IdleR'][self.step // 5], (self.x, self.y))
            self.step += 1
        elif self.direc == 'Left':
            window.blit(self.image['IdleL'][self.step // 5], (self.x, self.y))
            self.step += 1


class Monster(pygame.sprite.Sprite):
    def __init__(self, dict, x, y, vel):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.visible = False
        self.vel = vel
        self.step = 0
        self.image = dict
        self.rect = self.image['IdleR'][0].get_rect()
        self.rect.topleft = (self.x, self.y)
        self.width , self.height = self.rect.size

    def move_towards_player(self, player):
        # find normalized direction vector (dx, dy) between enemy and player
        if self.visible == True:
            self.dx, self.dy = player.rect.centerx - self.rect.centerx, player.rect.centery - self.rect.centery
            dist = math.hypot(self.dx, self.dy)
            self.dx, self.dy = self.dx / dist, self.dy / dist
            # move along this normalized vector towards the player at current speed
            self.x += self.dx * self.vel
            self.y += self.dy * self.vel
            self.rect.topleft = (self.x, self.y)
            self.hitbox = self.rect.inflate(-10, -10)

    def draw(self, window):
        if self.visible == True:
            if self.step > 15:
                self.step = 0
            if self.dx > 0:
                window.blit(self.image['Right'][self.step // 5], (self.x, self.y))
                self.step += 1
            elif self.dx < 0:
                window.blit(self.image['Right'][self.step // 5], (self.x, self.y))
                self.step += 1


class Key(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.visible = False
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        

    def draw(self, window):
        if self.visible == True:
            window.blit(self.image, (self.x, self.y))
