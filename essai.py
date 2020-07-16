import random
import pygame
import pygame.locals

from classes import *
from constantes import *
from functions import *

pygame.init()
ecran = pygame.display.set_mode((450, 450), pygame.RESIZABLE)
fond = pygame.image.load(background_image).convert()
ecran.blit(fond, (0,0))
exemple = pygame.image.load(wall_image).convert()



def essai_maze(maze):
    x_pos = 0
    y_pos = 0
    for index, tile in enumerate(maze):
            if maze[index] in images:
                if index % 15 == 0 and index > 0:
                    x_pos = 0
                    y_pos += taille_sprite
                    ecran.blit(pygame.image.load(images[tile]).convert(), (x_pos, y_pos))
                    x_pos += taille_sprite
                else:
                    ecran.blit(pygame.image.load(images[tile]).convert(), (x_pos, y_pos))
                    x_pos += taille_sprite
    # pygame.display.flip()

pygame.key.set_repeat(400, 30)

macgyver.position = 0
macgyver.inventory = []
maze = Maze()
maze = maze_creation()
available = get_free_locations(maze)
for tool in Items.LIST:  
    tool.place_items(maze, available)
continuer = 1
while continuer:
    # ecran.blit(exemple, (420, 420)
    essai_maze(maze)
    pygame.display.flip()

