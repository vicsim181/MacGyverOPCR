"""File hosting the classe of the tiles"""
import pygame
from pygame.locals import *
from constantes import SIZE_SPRITE
class Tiles():
    """Class holding the tiles, their attributes and a function determining the pygame position"""
    STATUS = {0: "corridor",
              1: "wall",
              5: "macgyver",
              6: "guardian",
              7: "exit"}
    
    IMAGES = {"wall": "./ressource/wall.png",
              "corridor": "",
              "macgyver": "",
              "exit": "./ressource/exit2.png",
              "guardian": "./ressource/Gardien.png"}

    def __init__(self, index, value):
        """Initialization of the tile object"""
        self.position = None
        self.index, self.value = index, value
        self.status = Tiles.STATUS[self.value]
        self.image = Tiles.IMAGES[self.status]
    
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
        screen.blit(pygame.image.load(self.image), (self.position))

class Guardian(Tiles):
    def __init__(self):
        super.__init__()
    

