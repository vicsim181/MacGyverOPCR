import pygame
from pygame.locals import *

pygame.init()

ecran = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
fond = pygame.image.load("D:/Programmation/Repos_Git/MacGyverOPCR/background.jpg").convert()
MacGyver = pygame.image.load("D:/Programmation/Repos_Git/MacGyverOPCR/ressource/MacGyver.png").convert()

ecran.blit(fond, (0,0))
ecran.blit(MacGyver, (300, 220))
pygame.display.flip()

continuer = True

while continuer:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            continuer = False

pygame.quit()

