"""File containing the Character class"""
import pygame
# from pygame.locals import *
from items import PlasticTube, Ether, Needle
from constantes import MESSAGE_IMAGE
class Character():
    """Class allowing to create characters in the game, holding its name, inventory and position"""
    def __init__(self, name, position, image):
        self.name = name
        self.inventory = []
        self.position = position
        self.image = image
    
    def draw_inventory(self, number):
        for index, items in enumerate(self.inventory):
            screen.blit(pygame.image.load(items.image).convert_alpha(), (index*35, 30))
        if number == 3:
            screen.blit(pygame.image.load(MESSAGE_IMAGE).convert_alpha(), (170, 7))
        pygame.display.flip()
