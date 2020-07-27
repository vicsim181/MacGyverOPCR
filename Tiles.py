"""File hosting the classe of the tiles"""
import pygame
from pygame.locals import *
from constantes import SIZE_SPRITE
class Tiles():
    
    STATUS = {0: "corridor",
              1: "wall",
              5: "macgyver",
              6: "guardian",
              7: "exit"}
    
    IMAGES = {"wall": "./ressource/wall.png",
              "corridor": "",
              "exit": "./ressource/exit2.png",
              "guardian": "./ressource/Gardien.png"}

    def __init__(self, index, value):
        self.position = ""
        self.index, self.value = index, value
        self.status, self.image = Tiles.STATUS[self.value], Tiles.IMAGES[self.status]
    
    def get_position(self):
        x_pos, y_pos = 60, 60
        if self.index == 0:
            self.position = (x_pos, y_pos)
        elif self.index % 15 == 0 and self.index > 0:
                y_pos += (self.index/15) * SIZE_SPRITE
        elif self.index % 15 < 8 and self.index > 0:
            x_pos, y_pos = self.index % 15 * SIZE_SPRITE, round(self.index/15) * SIZE_SPRITE
        else:
            x_pos, y_pos = self.index % 15 * SIZE_SPRITE, round(self.index/15) - 1 * SIZE_SPRITE
        self.position = (x_pos, y_pos)

    # def draw(self):
    #     if self.status in Tiles.IMAGES.keys():
    #             screen.blit(pygame.image.load(Tiles.IMAGES[self.status]).convert_alpha(), self.position)

class Guardian(Tiles):
    def __init__(self):
        super.__init__()
    
    def get_position(self):
        super.get_position()
    

