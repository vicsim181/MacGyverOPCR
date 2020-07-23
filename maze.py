"""File in which is located the Maze class"""
import pygame
from pygame.locals import *
import random

from constantes import SIZE_SPRITE, REPLAY_IMAGE, DEFEAT_IMAGE, MESSAGE_IMAGE, IMAGES_REVERSE, MOVEMENTS

class Maze():
    """Class which holds and initiates the maze we will use in the game."""
    CONVERTION_CSV = {" ": 0, "X": 1, "M": 5, "G": 6, "E": 7}
    TOOLS = {2: "Plastic Tube", 3: "Ether", 4: "Needle"}

    def __init__(self):
        """Fonction qui génère et modifie le labyrinthe à partir du fichier CSV"""
        self.liste = []
        self.places = []
        with open("Maze.csv", encoding="utf8") as fichier:
            data = fichier.read()
            data = data[1:]
            data = data.split("\n")
            data = data[:-1]
            for k in range(len(data)):
                data[k] = data[k].split(";")
            for line in data:
                for element in line:
                    self.liste.append(Maze.CONVERTION_CSV[element])

    def get_free_locations(self):
        """Function finding the free spots in the maze, to later place the items"""
        self.places = [i for i in range(0, len(self.liste)) if self.liste[i] == 0]

    def place_items(self, places):
        """Function allowing random places from the free spots to the items"""
        for tool in Maze.TOOLS.keys():
            item_pos = random.choice(places)
            self.places.remove(item_pos)
            self.liste[item_pos] = tool

    def draw(self, screen):
        """Function displaying the maze through the pygame interface"""
        x_pos, y_pos = 60, 60
        for index, tile in enumerate(self.liste):
            if index % 15 == 0 and index > 0:
                x_pos = 60
                y_pos += SIZE_SPRITE
            if self.liste[index] in IMAGES:
                screen.blit(pygame.image.load(IMAGES[tile]).convert_alpha(), (x_pos, y_pos))
            x_pos += SIZE_SPRITE
        
