import random

tools={1: "plastic tube",2: "ether",3: "needle"} 

"""Class allowing to create characters in the game"""
class Character():
    def __init__(self, pos, inventory):
        self.pos = pos 
        self.inventory = inventory


"""Class allowing to create different exceptions when moving MacGyver in the maze"""
class Exceptions():
    def __init__(self):
        pass

macgyver = Character(0,[])

"""Fonction qui génère et modifie le labyrinthe à partir du fichier CSV"""
def maze_creation():
    with open("Maze.csv", encoding="utf8") as fichier:
        data= fichier.read()
        # print(data,"\n")
        data=data[1:]
        # print(data,"\n")
        data=data.split("\n")
        # print(data,"\n")
        data=data[:-1]
        # print(data,"\n")
        for k in range(len(data)):
            data[k]=data[k].split(";")
        # print(data,"\n")    
        liste=[[ord(character) for character in line] for line in data]
        # print(liste,"\n")
        liste2=[]
        for item in liste:
            for num in item:
                liste2.append(num)
        # print(liste2,"\n")        
        liste3=[str(number) for number in liste2]
        # print(liste3,"\n")
        for i in range(0,len(liste3)):
            liste3[i]=liste3[i].replace("32","0")
            liste3[i]=liste3[i].replace("88","1")
            liste3[i]=liste3[i].replace("77","5")
            liste3[i]=liste3[i].replace("71","6")
        # print(liste3,"\n")    
        liste4=[int(number) for number in liste3]
    return liste4

"""Function finding the free spots in the maze, to later place the items"""
def get_free_locations(maze):    
    return [i for i in range(0,len(maze)) if maze[i] == 0]

"""Function allowing random places from the free spots to the items""" 
def place_items(maze, places):
    for index, item in enumerate(tools):
        item_pos=random.choice(places)
        places.remove(item_pos)
        maze[item_pos]= index + 2

symbols={0: "  ", 1: "██", 2: "Ꝣ ", 3: "ꞵ ", 4: "ꜫ ", 6: "G ", 42602: "Ꙫ "}

"""Function that draws the maze on the terminal for the player"""
def draw_maze(maze, symbols):
    for index, tile in enumerate(maze):
        print(symbols[tile], end="\n" if index % 15 == 14 else "")

"""Function asking what action the player wants to realise. 
It then call the appropriate function, movement, or exiting.
"""
def action(last_pos):
    action = input(print("What action do you want to make?\n", "To quit the game, press Q.\n",
    "To move MacGyver, press 'R' to move right, 'L' to move left, 'U' to move upward, 'D' to move downward."))
    if action == "U" or action == "u":
        movement(maze1, "U", mouv=-15)
        draw_maze(maze1, symbols)
    elif action == "D" or action == "d":
        movement(maze1, "D", mouv=15)
        draw_maze(maze1, symbols)
    elif action == "L" or action == "l":
        movement(maze1, "L", mouv=-1)
        draw_maze(maze1, symbols)
    elif action == "R" or action == "r":
        movement(maze1, "R", mouv=1)
        draw_maze(maze1, symbols)
    elif action == "Q" or action == "q":
        exiting()
    
"""Movement function in case the player asks for it. Depending on the letter entered, 
MacGyver will move to the right, left, up or down.
""" 
def movement(maze, direction, mouv):
    if maze[macgyver.pos + mouv] == 1:
        print("MacGyver can't move through a wall!\n")
    elif maze[macgyver.pos + mouv] == 2:
        print("MacGyver collected the Ꝣ object!")
        macgyver.inventory.append(tools[1])
        print(macgyver.inventory)
        maze[macgyver.pos] = 0
        maze[macgyver.pos + mouv] = 42602
        macgyver.pos = macgyver.pos + mouv
    elif maze[macgyver.pos + mouv] == 3:
        print("MacGyver collected the ꞵ object!")
        macgyver.inventory.append(tools[2])
        print(macgyver.inventory)
        maze[macgyver.pos] = 0
        maze[macgyver.pos + mouv] = 42602
        macgyver.pos = macgyver.pos + mouv
    elif maze[macgyver.pos + mouv] == 4:
        print("MacGyver collected the ꜫ object!")
        macgyver.inventory.append(tools[3])
        print(macgyver.inventory)
        maze[macgyver.pos] = 0
        maze[macgyver.pos + mouv] = 42602
        macgyver.pos = macgyver.pos + mouv 
    elif maze[macgyver.pos + mouv] == 6:
        if winning() == True:
            print("Well done! MacGyver fought the guardian and won! Exiting the game")
            exit()
        else:
            print("MacGyver didn't collect all the necessary items! The guardian wins!")
            exit()
    else:
        maze[macgyver.pos] = 0
        maze[macgyver.pos + mouv] = 42602
        macgyver.pos = macgyver.pos + mouv   
        
"""Exiting function when the player wants to quit"""
def exiting():
    print("MacGyver gives up and quit the game!")
    exit()

"""Function which determines if we won the game"""
def winning():
    verification = 0
    for element in tools.keys():
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
    action(macgyver.pos)     

