"""File which contains the Game class, its attributes and functions. 
These functions are the mechanic of the game.
"""
import pygame
from pygame.locals import *

from constantes import *
from character import Character
from maze import Maze

class Game():
    def __init__(self):
        """Constructor"""
        pass    

    def start(self):
        """Function creating the attributes and starting the loop which allows the game running"""
        pygame.init()
        pygame.key.set_repeat(400, 30)
        pygame.font.init()
        self.custom_font = pygame.font.SysFont('Arial', 20)
        self.custom_text = self.custom_font.render("MacGyver's bag:", False, (0, 0, 0))
        self.number, self.macgyver, self.maze = 0, Character("MacGyver", 0), Maze()
        self.macgyver.position, self.macgyver.inventory = 0, []
        self.maze.get_free_locations(); self.maze.place_items(self.maze.places)
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key in movements:
                        self.loop(movements[event.key][1])
                elif event.type == QUIT:
                    continuer = False
            self.show_maze()
            pygame.display.flip()            
        pygame.quit()

    def loop(self, movement):
        """Function asking what action the player wants to realise.
        It then calls the appropriate function, movement, or exiting.
        """
        if movement == "u":
            mouv = 0 if self.macgyver.position / 15 < 1 else -15
        elif movement == "d":
            mouv = 0 if self.macgyver.position / 15 >= 14 else 15
        elif movement == "l":
            mouv = 0 if self.macgyver.position % 15 == 0 else -1
        elif movement == "r":
            mouv = 0 if self.macgyver.position % 15 == 14 else 1
        if isinstance(mouv, int):
            self.move(mouv)

    def move(self, mouv):
        """Movement function in case the player asks for it. Depending on the letter entered,
        MacGyver will move to the right, left, up or down.
        """
        if self.maze.liste[self.macgyver.position + mouv] == 1:
            return
        elif self.maze.liste[self.macgyver.position + mouv] == 6:
            if self.number == 3:
                self.maze.liste[self.macgyver.position], self.maze.liste[self.macgyver.position + mouv], self.macgyver.position = 0, 5, self.macgyver.position + mouv
            else:
                self.replay()
        elif self.maze.liste[self.macgyver.position + mouv] == 7:
            self.maze.liste[self.macgyver.position], self.maze.liste[self.macgyver.position + mouv], self.macgyver.position = 0, 8, self.macgyver.position + mouv
            self.replay()
        else:
            self.collect_item(mouv)
            self.maze.liste[self.macgyver.position], self.maze.liste[self.macgyver.position + mouv], self.macgyver.position = 0, 5, self.macgyver.position + mouv

    def collect_item(self, mouv):
        """Fonction checking if the target tile has an object on it. 
        If it does, the object gets collected inside MacGyver's bag.
        """
        for item in Maze.TOOLS.keys():
            if self.maze.liste[self.macgyver.position + mouv] == item:
                self.macgyver.inventory.append(Maze.TOOLS[item])
                self.number += 1
                return
    
    def replay(self):
        """Function offering the choice to the player to play another game or quitting once he won or lose"""
        if self.number == 3:
            ecran.blit(pygame.image.load(replay_image), (0, 0))
        else: 
            ecran.blit(pygame.image.load(defeat_image), (0, 0))
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_F1: 
                    self.start()
                elif event.type == KEYDOWN and event.key == K_F2:
                    exit()
                    pygame.quit()
            pygame.display.flip()

    def show_maze(self):
        """Function displaying the maze through the pygame interface"""
        ecran.blit(fond, (0, 0))
        ecran.blit(fond2, (60, 60))
        ecran.blit(self.custom_text, (0, 0))
        x_pos = 60
        y_pos = 60
        for index, tile in enumerate(self.maze.liste):
            if index % 15 == 0 and index > 0:
                x_pos = 60
                y_pos += taille_sprite
            if self.maze.liste[index] in images:
                ecran.blit(pygame.image.load(images[tile]).convert_alpha(), (x_pos, y_pos))
            x_pos += taille_sprite
        self.x_image = 5
        for items in self.macgyver.inventory:
            ecran.blit(pygame.image.load(images_reverse[items]).convert_alpha(), (self.x_image, 30))
            self.x_image += 35
        if self.number == 3:
            ecran.blit(pygame.image.load(message_image).convert_alpha(), (170, 7))
        pygame.display.flip()