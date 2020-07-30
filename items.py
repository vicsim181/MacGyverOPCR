"""File hosting the classes of the items"""
import pygame
from constantes import SIZE_SPRITE

class Items():
    """Parent class of the items, defining their basic attributes and the method to get their pygame position"""
    def __init__(self, name):
        self.position, self.index, self.image = None, 0, ""

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

    def draw(self, screen):
        """function used to draw them on the pygame interface"""
        screen.blit(pygame.image.load(self.image), (self.position))


class PlasticTube(Items):
    """Child class for the plastic tube"""
    def __init__(self, name):
        self.image = "./ressource/tube.png"
        Items.__init__(self, name)


class Ether(Items):
    """Child class for the ether"""
    def __init__(self, name):
        self.image = "./ressource/ether.png"
        Items.__init__(self, name)


class Needle(Items):
    """Child class for the needle"""
    def __init__(self, name):
        self.image = "./ressource/needle.png"
        Items.__init__(self, name)
