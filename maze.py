"""File in which is located the Maze class"""
import random
from tiles import Wall, Corridor, Guardian, Exit, Macgyver, PlasticTube, Ether, Needle
from constants import LEVEL

class Maze():
    """Class which holds and initiates the maze we will use in the game."""
    CONVERSION_CSV = {" ": Corridor, "X": Wall, "G": Guardian, "E": Exit}

    def __init__(self):
        """Fonction qui génère et modifie le labyrinthe à partir du fichier CSV"""
        self.liste = []
        self.places = []
        self.lvl = 1
        with open(LEVEL[self.lvl], encoding="utf8") as fichier:
            data = fichier.read()
            data = data[1:]
            data = data.split("\n")
            data = data[:-1]
            for k in range(len(data)):
                data[k] = data[k].split(";")
            for line in data:
                for element in line:
                    self.liste.append(self.tile_factory(element))
    
    def get_free_locations(self):
        """Function finding the free spots in the maze, to later place the items"""
        self.places = [i for i in range(0, len(self.liste)) if isinstance(self.liste[i], Corridor)]

    def place_items(self, places):
        """Function allowing random places from the free spots to the items"""
        for tool in PlasticTube, Ether, Needle:
            item_pos = random.choice(places)
            self.places.remove(item_pos)
            self.liste[item_pos] = tool()

    def draw(self, screen):
        """Function displaying the maze through the pygame interface"""
        for index, tile in enumerate(self.liste):
            tile.draw(screen, index)

    def tile_factory(self, character):
        """Function creating the tile object depending on the character found in the csv file"""
        try:
            cls = Maze.CONVERSION_CSV[character]
            return cls()
        except KeyError as err:
            print("The CSV file contains a {}, it is not a valid character,\
therefore the maze cannot be converted into a visible element. Please fix it.".format(err))
            exit()

    def find_first_tile(self, cls):
        """Base function used to find an element in the list"""
        for index, tile in enumerate(self.liste):
            if isinstance(tile, cls):
                return index

    def find_macgyver(self):
        """Adapted to find MacGyver"""
        return self.find_first_tile(Macgyver)

    def find_guardian(self):
        """Adapted to find the guardian"""
        return self.find_first_tile(Guardian)

    def find_plastic_tube(self):
        """Adapted to find the plastic tube"""
        return self.find_first_tile(PlasticTube)

    def find_ether(self):
        """Adapted to find the ether"""
        return self.find_first_tile(Ether)

    def find_needle(self):
        """Adapted to find the needle"""
        return self.find_first_tile(Needle)
