class Maze():
    """Class which holds and initiates the maze we will use in the game."""
    CONVERTION_CSV = {" ": 0, "X": 1, "M": 5, "G": 6, "E": 7}

    def __init__(self):
        pass

    def creation(self):
        """Fonction qui génère et modifie le labyrinthe à partir du fichier CSV"""
        with open("Maze.csv", encoding="utf8") as fichier:
            data = fichier.read()
            data = data[1:]
            data = data.split("\n")
            data = data[:-1]
            for k in range(len(data)):
                data[k] = data[k].split(";")
            liste = []
            for line in data:
                for element in line:
                    liste.append(Maze.CONVERTION_CSV[element])
        return liste
