  
import pygame
from pygame.locals import *

pygame.init()

ecran = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
fond = pygame.image.load("D:/Programmation/Repos_Git/MacGyverOPCR/background.jpg").convert()
MacGyver = pygame.image.load("D:/Programmation/Repos_Git/MacGyverOPCR/ressource/MacGyver.png").convert()

MacGyver_position = MacGyver.get_rect()

ecran.blit(fond, (0,0))
ecran.blit(MacGyver, MacGyver_position)
pygame.display.flip()

continuer = True

pygame.key.set_repeat(400, 30)

while continuer:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                MacGyver_position = MacGyver_position.move(0, -3)
            elif event.key == K_DOWN:
                MacGyver_position = MacGyver_position.move(0, 3)
            elif event.key == K_LEFT:
                MacGyver_position = MacGyver_position.move(-3, 0)
            elif event.key == K_RIGHT:
                MacGyver_position = MacGyver_position.move(3, 0)
        elif event.type == QUIT:
            continuer = False
    ecran.blit(fond, (0,0))
    ecran.blit(MacGyver, MacGyver_position)
    pygame.display.flip()            


pygame.quit()