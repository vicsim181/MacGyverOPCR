"""Module implementing the maze, the items and the characters."""
import random

tools = {1:"plastic tube", 2:"ether", 3:"needle"}
convertion_csv = {" ": 0, "X": 1, "M": 5, "G": 6, "E": 7}

class Character():
    """Class allowing to create characters in the game"""
    def __init__(self, name, pos, inventory):
        self.name = name
        self.pos = pos
        self.inventory = inventory

    def __repr__(self):
        return self.name + "position: " + self.pos


macgyver = Character("MacGyver", 0, [])

def maze_creation():
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
                liste.append(convertion_csv[element])
    return liste

def get_free_locations(maze):
    """Function finding the free spots in the maze, to later place the items"""
    return [i for i in range(0, len(maze)) if maze[i] == 0]

def place_items(maze, places):
    """Function allowing random places from the free spots to the items"""
    for index, item in enumerate(tools):
        item_pos = random.choice(places)
        places.remove(item_pos)
        maze[item_pos] = index + 2

symbols = {0: "  ", 1: "██", 2: "🧪", 3: "🍼", 4: "💉", 5: "🕴️", 6: "👻", 7: "🏁", 8: "🏆"}

def draw_maze(maze, symbols):
    """Function that draws the maze on the terminal for the player"""
    for index, tile in enumerate(maze):
        print(symbols[tile], end="\n" if index % 15 == 14 else "")

def action():
    """Function asking what action the player wants to realise.
It then call the appropriate function, movement, or exiting.
"""
    print("What action do you want to make?\n", "To quit the game, press Q.\n",
                         "To move MacGyver, press 'R' to move right, 'L' to move left,",
                         "'U' to move upward, 'D' to move downward.")
    action = input("")
    print("\n")
    if action == "U" or action == "u":
        if macgyver.pos / 15 < 1:
            print("MacGyver can't escape the maze anywhere else than through the exit!\n")
        else:
            movement(maze1, "U", mouv=-15)
            draw_maze(maze1, symbols)
    elif action == "D" or action == "d":
        if macgyver.pos / 15 >= 14:
            print("MacGyver can't escape the maze anywhere else than through the exit!\n")
        else:
            movement(maze1, "D", mouv=15)
            draw_maze(maze1, symbols)
    elif action == "L" or action == "l":
        if macgyver.pos % 15 == 0:
            print("MacGyver can't escape the maze anywhere else than through the exit!\n")
        else:
            movement(maze1, "L", mouv=-1)
            draw_maze(maze1, symbols)
    elif action == "R" or action == "r":
        if macgyver.pos % 15 == 14:
            print("MacGyver can't escape the maze anywhere else than through the exit!\n")
        else:
            movement(maze1, "R", mouv=1)
            draw_maze(maze1, symbols)
    elif action == "Q" or action == "q":
        exiting()

def movement(maze, direction, mouv):
    """Movement function in case the player asks for it. Depending on the letter entered,
MacGyver will move to the right, left, up or down.
"""
    if maze[macgyver.pos + mouv] == 1:
        print("MacGyver can't move through a wall!\n")
    elif maze[macgyver.pos + mouv] == 2:
        print("MacGyver collected the 🧪 object!")
        macgyver.inventory.append(tools[1])
        print(macgyver.inventory)
        maze[macgyver.pos] = 0
        maze[macgyver.pos + mouv] = 5
        macgyver.pos = macgyver.pos + mouv
    elif maze[macgyver.pos + mouv] == 3:
        print("MacGyver collected the 🍼 object!")
        macgyver.inventory.append(tools[2])
        print(macgyver.inventory)
        maze[macgyver.pos] = 0
        maze[macgyver.pos + mouv] = 5
        macgyver.pos = macgyver.pos + mouv
    elif maze[macgyver.pos + mouv] == 4:
        print("MacGyver collected the 💉 object!")
        macgyver.inventory.append(tools[3])
        print(macgyver.inventory)
        maze[macgyver.pos] = 0
        maze[macgyver.pos + mouv] = 5
        macgyver.pos = macgyver.pos + mouv
    elif maze[macgyver.pos + mouv] == 6:
        if winning():
            print("Well done! MacGyver fought the guardian and won! He can now exit the maze\n")
            maze[macgyver.pos] = 0
            maze[macgyver.pos + mouv] = 5
            macgyver.pos = macgyver.pos + mouv
        else:
            print("MacGyver didn't collect all the necessary items! The guardian wins!\n", "😭")
            exit()
    elif maze[macgyver.pos + mouv] == 7:
        print("MacGyver wins and exit the maze!")
        maze[macgyver.pos] = 0
        maze[macgyver.pos + mouv] = 8
        macgyver.pos = macgyver.pos + mouv
        draw_maze(maze1, symbols)
        print("🙂")
        exit()
    else:
        maze[macgyver.pos] = 0
        maze[macgyver.pos + mouv] = 5
        macgyver.pos = macgyver.pos + mouv

def exiting():
    """Exiting function when the player wants to quit"""
    print("MacGyver gives up and quit the game!")
    exit()

def winning():
    """Function which determines if we won the game"""
    verification = 0
    for element in tools:
        if tools[element] in macgyver.inventory:
            verification += 1
    if verification == 3:
        return True


maze1 = maze_creation()
available = get_free_locations(maze1)
place_items(maze1, available)
draw_maze(maze1, symbols)
loop = 1
while loop == 1:
    action()
