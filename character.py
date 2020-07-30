"""File containing the Character class"""
import pygame
from items import PlasticTube, Ether, Needle
from constantes import MESSAGE_IMAGE, SIZE_SPRITE
from tiles import Tiles
class Character():
    """Class allowing to create characters in the game, holding its name, inventory and position"""
    def __init__(self, name, position, image):
        self.status, self.inventory, self.position = name, [], position
        self.image, self.index = image, 0
    
    def draw_inventory(self, screen):
        for index, items in enumerate(self.inventory):
            screen.blit(pygame.image.load(items.image).convert_alpha(), (index*35, 30))
        screen.blit(pygame.image.load(MESSAGE_IMAGE).convert_alpha(), (170, 7)) if len(self.inventory) == 3 else ""
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

    def winning(self, maze, mouv):
        maze.liste_2[self.index] = Tiles(self.index, 0)
        maze.liste_2[self.index + mouv], self.index = self, self.index + mouv
 
    def collect_item(self, tools, maze, mouv):
        """Fonction checking if the target tile has an object on it.
        If it does, the object gets collected inside MacGyver's bag.
        """
        for item in tools.keys():
            if maze.liste_2[self.index + mouv] == tools[item]:
                self.inventory.append(tools[item])
