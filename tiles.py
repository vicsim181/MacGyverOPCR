"""File containing the different child classes of the Tile class."""
from tile import Tile 
from constants import WALL_IMAGE, EXIT_IMAGE, GUARDIAN_IMAGE, MACGYVER_IMAGE, PLASTICTUBE_IMAGE, ETHER_IMAGE, NEEDLE_IMAGE


class Corridor(Tile):
    def __init__(self):
        super().__init__()

class Wall(Tile):
    def __init__(self):
        super().__init__(WALL_IMAGE)

class Exit(Tile):
    def __init__(self):
        super().__init__(EXIT_IMAGE)

class Guardian(Tile):
    def __init__(self):
        super().__init__(GUARDIAN_IMAGE)

class Macgyver(Tile):
    def __init__(self):
        super().__init__(MACGYVER_IMAGE)

class PlasticTube(Tile):
    def __init__(self):
        super().__init__(PLASTICTUBE_IMAGE)

class Ether(Tile):
    def __init__(self):
        super().__init__(ETHER_IMAGE)

class Needle(Tile):
    def __init__(self):
        super().__init__(NEEDLE_IMAGE)
