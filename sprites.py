import pygame
class Sprite(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 4

    def draw(self, window, image):
        window.blit(image, (self.x, self.y))

    def tile(self, tile):
        tilex = int(self.x // tile)
        tiley = int(self.y // tile)
        return(tilex,tiley)  


class Key(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = False

    def draw(self, window, image):
        if self.visible == True:
            window.blit(image, (self.x, self.y))
    
    def tile(self, tile):
        tilex = int(self.x // tile)
        tiley = int(self.y // tile)
        return(tilex,tiley)     
