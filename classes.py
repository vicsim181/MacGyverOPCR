import random

class Maze():
    """Class which holds and initiates the maze we will use in the game."""
    def __init__(self):
        pass


class Character():
    """Class allowing to create characters in the game"""
    def __init__(self, name, position):
        self.name = name
        self.inventory = []
        self.position = position
    

class Items():
    """Class initiating the 3 items MacGyver needs to collect in order to escape the maze."""
    LIST=[]

    def __init__(self, num, name):
        self.num = num
        self.name = name

    def place_items(self, maze, places):
        """Function allowing random places from the free spots to the items"""
        item_pos = random.choice(places)
        places.remove(item_pos)
        maze[item_pos] = self.num

    def add_item(self):
        Items.LIST.append(self)
        return Items.LIST


class Tiles():
    """Class where the tiles are created"""
    def __init__(self, index, value):
        self.value = value
        self.type = ""
        self.index = index         
    
    def __repr__(self):
        return ("index: {}, type: {}".format(self.index, self.type))
    
    def set_attributes(self, liste):
        if self.value == 0:
            self.type = "corridor"
        elif self.value == 1:
            self.type = "wall"
        elif self.value == 5:
            self.type = "MacGyver"
        elif self.value == 6:
            self.type = "guardian"
        elif self.value == 7:
            self.type = "exit"
        else: 
            for element in liste:
                if self.value == element.num:
                    self.type = element.name   