"""File containing the Character class"""
import pygame
# from pygame.locals import *
from items import PlasticTube, Ether, Needle
from constantes import MESSAGE_IMAGE, SIZE_SPRITE
class Character():
    """Class allowing to create characters in the game, holding its name, inventory and position"""
    def __init__(self, name, position, image):
        self.status = name
        self.inventory = []
        self.position = position
        self.image = image
        self.index = 0
    
    def draw_inventory(self, number, screen):
        for index, items in enumerate(self.inventory):
            screen.blit(pygame.image.load(items.image).convert_alpha(), (index*35, 30))
        if number == 3:
            screen.blit(pygame.image.load(MESSAGE_IMAGE).convert_alpha(), (170, 7))
        pygame.display.flip()

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
