import pygame
from pygame.locals import *
from main import *

pygame.init()

ecran = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
fond = pygame.image.load("D:/Programmation/Repos_Git/MacGyverOPCR/background.jpg").convert()
MacGyver = pygame.image.load("D:/Programmation/Repos_Git/MacGyverOPCR/ressource/MacGyver.png").convert()
MacGyver_position = MacGyver.get_rect()
movements = { K_UP: [(0, -3), action("u")], 
              K_DOWN: [(0, 3), action("d")],
              K_LEFT: [(-3, 0), action("l")],
              K_RIGHT: [(3, 0), action("r")]}

ecran.blit(fond, (0,0))
ecran.blit(MacGyver, MacGyver_position)
pygame.display.flip()

continuer = True

pygame.key.set_repeat(400, 30)

while continuer:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key in movements:
                MacGyver_position = MacGyver_position.move(movements[event.key][0]) # A tester
        elif event.type == QUIT:
            continuer = False
    ecran.blit(fond, (0,0))
    ecran.blit(MacGyver, MacGyver_position)
    pygame.display.flip()            

pygame.quit()
