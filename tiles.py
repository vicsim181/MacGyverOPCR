"""File containing the different child classes of the Tile class."""
from tile import Tile
from constants import WALL_IMAGE, EXIT_IMAGE, GUARDIAN_IMAGE, MACGYVER_IMAGE, PLASTICTUBE_IMAGE, ETHER_IMAGE, NEEDLE_IMAGE


class Corridor(Tile):
    """Child class for the corridor elements"""
    def __init__(self):
        super().__init__()

class Wall(Tile):
    """Child class for the wall elements"""
    def __init__(self):
        super().__init__(WALL_IMAGE)

class Exit(Tile):
    """Child class for the exit"""
    def __init__(self):
        super().__init__(EXIT_IMAGE)

class Guardian(Tile):
    """Child class for the guardian"""
    def __init__(self):
        super().__init__(GUARDIAN_IMAGE)

class Macgyver(Tile):
    """Child class for MacGyver"""
    def __init__(self):
        super().__init__(MACGYVER_IMAGE)

class PlasticTube(Tile):
    """Child class for the plastic tube"""
    def __init__(self):
        super().__init__(PLASTICTUBE_IMAGE)

class Ether(Tile):
    """Child class for the ether"""
    def __init__(self):
        super().__init__(ETHER_IMAGE)

class Needle(Tile):
    """Child class for the needle"""
    def __init__(self):
        super().__init__(NEEDLE_IMAGE)
