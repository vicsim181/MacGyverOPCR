"""File hosting the classes of the items"""
import pygame
from pygame.locals import *
from constantes import SIZE_SPRITE

class Items():
    def __init__(self):
        pass

    def draw(self, screen):
        screen.blit(pygame.image.load(self.image), (self.position))
    
    def get_position(self):
        """Function determining the pygame position of the object"""
        x_pos, y_pos = 75, 75
        if self.index == 0:
            pass
        elif self.index % 15 == 0 and self.index > 0:
                y_pos += (self.index/15) * SIZE_SPRITE
        elif self.index % 15 < 8 and self.index > 0:
            x_pos += (self.index % 15 * SIZE_SPRITE)
            y_pos += round(self.index/15) * SIZE_SPRITE
        else:
            x_pos += (self.index % 15 * SIZE_SPRITE)
            y_pos += (round(self.index/15) - 1) * SIZE_SPRITE
        self.position = (x_pos, y_pos)

class PlasticTube(Items):
    def __init__(self, name):
        Items.__init__(self)
        self.status = name
        self.image = "./ressource/tube.png"
        self.position = None
        self.index = 0
        

class Ether(Items):
    def __init__(self, name):
        Items.__init__(self)
        self.status = name
        self.image = "./ressource/ether.png"
        self.position = None
        self.index = 0

class Needle(Items):
    def __init__(self, name):
        Items.__init__(self)
        self.status = name
        self.image = "./ressource/needle.png"
        self.position = None
        self.index = 0
