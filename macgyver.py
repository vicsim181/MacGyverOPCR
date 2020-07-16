import pygame
from pygame.locals import *
from classes import *
from functions import *
from constantes import *

pygame.init()

ecran = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
fond = pygame.image.load(background_image).convert()
MacGyver = pygame.image.load(MacGyver_image).convert()
MacGyver_position = MacGyver.get_rect()

movements = { K_UP: [(0, -3), "u"], 
              K_DOWN: [(0, 3), "d"],
              K_LEFT: [(-3, 0), "l"],
              K_RIGHT: [(3, 0), "r"]}

ecran.blit(fond, (0,0))
ecran.blit(MacGyver, MacGyver_position)
pygame.display.flip()

pygame.key.set_repeat(400, 30)

continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key in movements:
                MacGyver_position = MacGyver_position.move(movements[event.key][0]) 
        elif event.type == QUIT:
            continuer = False
    ecran.blit(fond, (0,0))
    ecran.blit(MacGyver, MacGyver_position)
    pygame.display.flip()            

pygame.quit()

# movements = { "a": ["1er élément de a", "2ème élément de a"], 
#               "b": ["1er élément de b", "2ème élément de b"],
#               "c": ["1er élément de c", "2ème élément de c"]}

# d = "c"

# if d in movements:
#     print(movements[d][1])
