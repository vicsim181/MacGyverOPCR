"""Module implementing the maze, the items and the characters."""
import random

from character import * 
from maze import *
from items import *
# from tiles import *

symbols = {0: "  ", 1: "██", 2: "🧪", 3: "🍼", 4: "💉", 5: "🕴️", 6: "👻", 7: "🏁", 8: "🏆"}
macgyver = Character("MacGyver", 0)
plastic_tube = Items(2, "Plastic Tube")
ether = Items(3, "Ether")
needle = Items(4, "Needle")
plastic_tube.add_item(), ether.add_item(), needle.add_item()

def get_free_locations(maze):
    """Function finding the free spots in the maze, to later place the items"""
    return [i for i in range(0, len(maze)) if maze[i] == 0]

def draw_maze(maze, symbols):
        """Function that draws the maze on the terminal for the player"""
        for index, tile in enumerate(maze):
            print(symbols[tile], end="\n" if index % 15 == 14 else "")

def loop(maze):
    """Function asking what action the player wants to realise.
    It then calls the appropriate function, movement, or exiting.
    """
    while loop:
        print("What action do you want to make?\n", "To quit the game, press Q.\n",
                         "To move MacGyver, press 'R' to move right, 'L' to move left,",
                         "'U' to move upward, 'D' to move downward.")
        action = input("").lower()
        print("\n")
        mouv = 0
        if action == "u":
            mouv = "Impossible move!\n" if macgyver.position / 15 < 1 else -15
        elif action == "d":
            mouv = "Impossible move!\n" if macgyver.position / 15 >= 14 else 15
        elif action == "l":
            mouv = "Impossible move!\n" if macgyver.position % 15 == 0 else -1
        elif action == "r":
            mouv = "Impossible move!\n" if macgyver.position % 15 == 14 else 1
        elif action == "q":
            print("MacGyver exits the game.")
            exit()
        if isinstance(mouv, int):
            move(maze, mouv)
            draw_maze(maze, symbols)
        else: 
            print(mouv)    

def move(maze, mouv):
    """Movement function in case the player asks for it. Depending on the letter entered,
    MacGyver will move to the right, left, up or down.
    """
    if maze[macgyver.position + mouv] == 1:
        print("MacGyver can't move through a wall!\n")
        return
    elif maze[macgyver.position + mouv] == 6:
        if winning():
            print("Well done! MacGyver fought the guardian and won! He can now exit the maze\n")
            maze[macgyver.position] = 0
            maze[macgyver.position + mouv] = 5
            macgyver.position = macgyver.position + mouv
        else:
            print("MacGyver didn't collect all the necessary items! The guardian wins!\n", "😭")
            exit()
    elif maze[macgyver.position + mouv] == 7:
        print("MacGyver wins and exit the maze!")
        maze[macgyver.position] = 0
        maze[macgyver.position + mouv] = 8
        macgyver.position = macgyver.position + mouv
        draw_maze(maze, symbols)
        print("🙂")
        replay()
    else:
        collect_item(maze, mouv)
        maze[macgyver.position] = 0
        maze[macgyver.position + mouv] = 5
        macgyver.position = macgyver.position + mouv

def collect_item(maze, mouv):
    """Fonction checking if the target tile has an object on it. 
    If it does, the object gets collected inside MacGyver's bag.
    """
    for item in Items.LIST:
        if maze[macgyver.position + mouv] == item.num:
            print("MacGyver has collected the object: {}. It has been added to his bag.".format(item.name))
            macgyver.inventory.append(item.name)
            print(macgyver.inventory)
            return

def replay():
    print("Do you wish to play another game? Y = Yes, N = No.\n")
    action = input("").lower()
    print("\n")
    if action == "y": 
        main()
    elif action == "n":
        exit()
    else:
        print("Please insert a correct answer")
        replay()

def winning():
    """Function which determines if we won the game"""
    verification = 0
    for element in Items.LIST:
        if element.name in macgyver.inventory:
            verification += 1
    return verification == 3
        
def main():
    macgyver.position = 0
    macgyver.inventory = []
    maze = Maze()
    maze = maze.creation()
    available = get_free_locations(maze)
    for tool in Items.LIST:  
        tool.place_items(maze, available)
    draw_maze(maze, symbols)
    # for index, tiles in enumerate(maze):
    #     index = Tiles(index, tiles)
    #     index.set_attributes(Items.LIST)
    continuer = 1
    while continuer:
        loop(maze)

main()
