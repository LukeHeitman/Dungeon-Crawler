import pygame
pygame.init()
class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.vel = 4
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.width , self.height = self.rect.size


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
 