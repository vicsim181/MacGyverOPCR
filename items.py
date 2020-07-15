import random

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
