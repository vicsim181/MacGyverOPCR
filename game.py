from character import Character
from maze import Maze

class Game():
    def __init__(self):
        pass    

    def start(self):
        self.number, self.macgyver, self.maze = 0, Character("MacGyver", 0), Maze()
        self.macgyver.position, self.macgyver.inventory = 0, []
        self.maze.get_free_locations(); self.maze.place_items(self.maze.places); self.maze.draw()
        continuer = True
        while continuer:
            self.loop()

    def loop(self):
        """Function asking what action the player wants to realise.
        It then calls the appropriate function, movement, or exiting.
        """
        loop = True
        while loop:
            print("What action do you want to make?\n", "To quit the game, press Q.\n",
                            "To move MacGyver, press 'R' to move right, 'L' to move left,",
                            "'U' to move upward, 'D' to move downward.")
            mouv, action = 0, input("").lower()
            print("\n")
            if action == "u":
                mouv = "Impossible move!\n" if self.macgyver.position / 15 < 1 else -15
            elif action == "d":
                mouv = "Impossible move!\n" if self.macgyver.position / 15 >= 14 else 15
            elif action == "l":
                mouv = "Impossible move!\n" if self.macgyver.position % 15 == 0 else -1
            elif action == "r":
                mouv = "Impossible move!\n" if self.macgyver.position % 15 == 14 else 1
            elif action == "q":
                print("MacGyver exits the game."); exit()
            if isinstance(mouv, int):
                self.move(mouv); self.maze.draw()
            else: 
                print(mouv) 

    def move(self, mouv):
        """Movement function in case the player asks for it. Depending on the letter entered,
        MacGyver will move to the right, left, up or down.
        """
        if self.maze.liste[self.macgyver.position + mouv] == 1:
            print("MacGyver can't move through a wall!\n"); return
        elif self.maze.liste[self.macgyver.position + mouv] == 6:
            if self.number == 3:
                print("Well done! MacGyver fought the guardian and won! He can now exit the maze\n")
                self.maze.liste[self.macgyver.position], self.maze.liste[self.macgyver.position + mouv], self.macgyver.position = 0, 5, self.macgyver.position + mouv
            else:
                print("MacGyver didn't collect all the necessary items! The guardian wins!\n", "😭"), exit()
        elif self.maze.liste[self.macgyver.position + mouv] == 7:
            print("MacGyver wins and exit the maze!")
            self.maze.liste[self.macgyver.position], self.maze.liste[self.macgyver.position + mouv], self.macgyver.position = 0, 8, self.macgyver.position + mouv
            self.maze.draw(), print("🙂"), self.replay()
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