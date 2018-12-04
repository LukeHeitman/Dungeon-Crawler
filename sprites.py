class Sprite(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5

    def draw(self, window, image):
        window.blit(image, (self.x, self.y))        


class Key(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visible = False
    def draw(self, window, image):
        window.blit(image, (self.x, self.y))
