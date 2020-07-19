class Character():
    """Class allowing to create characters in the game"""
    def __init__(self, name, position):
        self.name = name
        self.inventory = []
        self.position = position