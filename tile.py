"""File hosting the classe of the tiles"""
import pygame
from constants import SIZE_SPRITE
class Tile():
    """Class holding the tiles, their attributes and a function determining the pygame position"""

    def __init__(self, url=None):
        """Initialization of the tile object"""
        self.image = None
        if url:
            self.image = pygame.image.load(url)


    @classmethod
    def get_position(cls, index, size_screen):
        """Function determining the pygame position of the object"""
        return index % size_screen, index // size_screen

    def draw(self, screen, index, size_screen):
        """Function allowing the tile to draw itself"""
        if self.image:
            line, column = Tile.get_position(index, size_screen)
            screen.blit(self.image, ((line * SIZE_SPRITE) + 75, (column * SIZE_SPRITE) + 75))
