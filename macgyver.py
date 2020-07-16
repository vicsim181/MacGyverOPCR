import pygame
from pygame.locals import *
from classes import *
from functions import *
from constantes import *

pygame.init()

ecran = pygame.display.set_mode((450, 450), pygame.RESIZABLE)
fond = pygame.image.load(background_image).convert()
MacGyver = pygame.image.load(MacGyver_image).convert()
MacGyver_position = MacGyver.get_rect()
pygame.key.set_repeat(400, 30)

movements = { K_UP: [(0, -30), "u"], 
              K_DOWN: [(0, 30), "d"],
              K_LEFT: [(-30, 0), "l"],
              K_RIGHT: [(30, 0), "r"]}

def draw_maze_2(maze):
    x_pos = 0
    y_pos = 0
    for index, tile in enumerate(maze):
        if maze[index] == 5:
            ecran.blit(MacGyver, MacGyver_position)
        elif maze[index] in images:
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
    MacGyver_position = MacGyver.get_rect()
    maze = Maze()
    maze = maze_creation()
    available = get_free_locations(maze)
    for tool in Items.LIST:  
        tool.place_items(maze, available)
    continuer = True
    while continuer:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in movements:
                    loop(maze, movements[event.key][1])
                    MacGyver_position = MacGyver_position.move(macgyver.position % 15, macgyver.position / 15) 
            elif event.type == QUIT:
                continuer = False
        ecran.blit(fond, (0,0))
        draw_maze_2(maze)
        ecran.blit(MacGyver, MacGyver_position)
        pygame.display.flip()            

    pygame.quit()

main()