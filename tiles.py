import items

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
#  modif 
