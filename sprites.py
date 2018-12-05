import pygame
import math
pygame.init()
class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.vel = 5
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.width , self.height = self.rect.size


    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

class Enemy(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.vel = 1
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.width , self.height = self.rect.size
    
    def move_towards_player(self, player):
        # find normalized direction vector (dx, dy) between enemy and player
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        dx, dy = dx / dist, dy / dist
        # move along this normalized vector towards the player at current speed
        self.x += dx * self.vel
        self.y += dy * self.vel
        self.rect.center = (self.x, self.y)


    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

class Key(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.visible = False
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        

    def draw(self, window):
        if self.visible == True:
            window.blit(self.image, (self.x, self.y))
 