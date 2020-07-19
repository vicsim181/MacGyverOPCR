from character import Character
from maze import Maze

class Game():
    def __init__(self):
        pass    

    def start(self):
        self.number, self.macgyver, self.maze = 0, Character("MacGyver", 0), Maze()
        self.macgyver.position, self.macgyver.inventory = 0, []
        self.maze.get_free_locations(); self.maze.place_items(self.maze.places)

    def loop(self, movement):
        """Function asking what action the player wants to realise.
        It then calls the appropriate function, movement, or exiting.
        """
        if movement == "u":
            mouv = 0 if self.macgyver.position / 15 < 1 else -15
        elif movement == "d":
            mouv = 0 if self.macgyver.position / 15 >= 14 else 15
        elif movement == "l":
            mouv = 0 if self.macgyver.position % 15 == 0 else -1
        elif movement == "r":
            mouv = 0 if self.macgyver.position % 15 == 14 else 1
        elif movement == "q":
            print("MacGyver exits the game."); exit()
        if isinstance(mouv, int):
            self.move(mouv)

    def move(self, mouv):
        """Movement function in case the player asks for it. Depending on the letter entered,
        MacGyver will move to the right, left, up or down.
        """
        if self.maze.liste[self.macgyver.position + mouv] == 1:
            return
        elif self.maze.liste[self.macgyver.position + mouv] == 6:
            if self.number == 3:
                print("Well done! MacGyver fought the guardian and won! He can now exit the maze\n")
                self.maze.liste[self.macgyver.position], self.maze.liste[self.macgyver.position + mouv], self.macgyver.position = 0, 5, self.macgyver.position + mouv
            else:
                print("MacGyver didn't collect all the necessary items! The guardian wins!\n", "😭"), exit()
        elif self.maze.liste[self.macgyver.position + mouv] == 7:
            print("MacGyver wins and exit the maze!")
            self.maze.liste[self.macgyver.position], self.maze.liste[self.macgyver.position + mouv], self.macgyver.position = 0, 8, self.macgyver.position + mouv
            print("🙂"), self.replay()
        else:
            self.collect_item(mouv)
            self.maze.liste[self.macgyver.position], self.maze.liste[self.macgyver.position + mouv], self.macgyver.position = 0, 5, self.macgyver.position + mouv

    def collect_item(self, mouv):
        """Fonction checking if the target tile has an object on it. 
        If it does, the object gets collected inside MacGyver's bag.
        """
        for item in Maze.TOOLS.keys():
            if self.maze.liste[self.macgyver.position + mouv] == item:
                print("MacGyver has collected the object: {}. It has been added to his bag.".format(Maze.TOOLS[item]))
                self.macgyver.inventory.append(Maze.TOOLS[item])
                self.number += 1
                print(self.macgyver.inventory)
                return
    
    def replay(self):
        print("Do you wish to play another game? Y = Yes, N = No.\n")
        action = input("").lower()
        print("\n")
        if action == "y" or action == "n": 
            self.start() if action == "y" else exit()
        else:
            print("Please insert a correct answer\n"); self.replay()