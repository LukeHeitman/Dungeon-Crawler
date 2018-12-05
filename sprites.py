import pygame
pygame.init()
class Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vel = 4

    def draw(self, window):
        window.blit(self.image, (self.x, self.y))

    def collide(self, sprite):
        return self.rect.colliderect(sprite)

class Key(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.visible = False

    def draw(self, window):
        if self.visible == True:
            window.blit(self.image, (self.x, self.y))
 
