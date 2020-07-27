"""File in which is located the Maze class"""
import pygame
from pygame.locals import *
from character import Character
from tiles import Tiles
from items import Items, PlasticTube, Ether, Needle
from constantes import SIZE_SPRITE, REPLAY_IMAGE, DEFEAT_IMAGE, MESSAGE_IMAGE, IMAGES_REVERSE, MOVEMENTS
import random

class Maze():
    """Class which holds and initiates the maze we will use in the game."""
    CONVERTION_CSV = {" ": 0, "X": 1, "M": 5, "G": 6, "E": 7}
    TOOLS = {2: None, 3: None, 4: None}

    def __init__(self):
        """Fonction qui génère et modifie le labyrinthe à partir du fichier CSV"""
        self.plastic_tube, self.ether, self.needle = PlasticTube("plastic tube"), Ether("ether"), Needle("needle")
        self.liste = []
        self.liste_2 = []
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
            for index, value in enumerate(self.liste):
                self.liste_2[index] = Tiles(index, value)

    def get_free_locations(self):
        """Function finding the free spots in the maze, to later place the items"""
        self.places = [i for i in range(0, len(self.liste)) if self.liste[i] == 0]

    def place_items(self, places):
        """Function allowing random places from the free spots to the items"""
        Maze.TOOLS[2], Maze.TOOLS[3], Maze.TOOLS[4] = self.plastic_tube, self.ether, self.needle
        for tool in Maze.TOOLS:
            item_pos = random.choice(places)
            self.places.remove(item_pos)
            self.liste_2[item_pos] = Maze.TOOLS[tool]

    def draw(self, screen):
        """Function displaying the maze through the pygame interface"""
        for tiles in self.liste_2:
            screen.blit(pygame.image.load(tiles.image).convert_alpha(), (tiles.position))
        
# Mettre à jour les imports depuis constantes
# vérifier le concept d'avoir deux listes, si nécessaire ou non vu que l'index est sauvegardé dans chaque tuile
# Vérifier processus de construction du labyrinthe et dessin