import pygame
from pygame.locals import *
from character import Character
from game import Game
from constantes import *

pygame.init()

game = Game()
ecran = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
fond = pygame.image.load(background_image).convert()
pygame.key.set_repeat(400, 30)
movements = { K_UP: [(0, -30), "u"], 
              K_DOWN: [(0, 30), "d"],
              K_LEFT: [(-30, 0), "l"],
              K_RIGHT: [(30, 0), "r"]}

def show_maze(maze):
    x_pos = 0
    y_pos = 0
    for index, tile in enumerate(game.maze.liste):
        if game.maze.liste[index] in images:
            if index % 15 == 0 and index > 0:
                x_pos = 0
                y_pos += taille_sprite
                ecran.blit(pygame.image.load(images[tile]).convert(), (x_pos, y_pos))
                x_pos += taille_sprite
            else:
                ecran.blit(pygame.image.load(images[tile]).convert(), (x_pos, y_pos))
                x_pos += taille_sprite
    pygame.display.flip()

def main():
    game.start()
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in movements:
                    game.loop(movements[event.key][1])
            elif event.type == QUIT:
                continuer = False
        ecran.blit(fond, (0,0))
        show_maze(game.maze)
        pygame.display.flip()            
    pygame.quit()

main()