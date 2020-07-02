import random

tools={"plastic tube":"1", "ether":"2", "needle":"3"}
global last_pos
last_pos = 0  

class Character():
    def __init__(self, pos, inventory):
        self.pos = pos 
        self.inventory = inventory

macgyver = Character(0,[])

class Error_Mouvement():
    def __init__(self):


#Fonction qui génère et modifie le labyrinthe à partir du fichier CSV
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

# Function finding the free spots in the maze, to later place the items
def get_free_locations(maze):    
    return [i for i in range(0,len(maze)) if maze[i] == 0]

# Function allowing random places from the free spots to the items    
def place_items(maze, places):
    for index, item in enumerate(tools):
        item_pos=random.choice(places)
        places.remove(item_pos)
        maze[item_pos]= index + 2

symbols={0: "  ", 1: "██", 2: "Ꝣ ", 3: "ꞵ ", 4: "ꜫ ", 5: "M ", 6: "G "}

# Function that draws the maze on the terminal for the player 
def draw_maze(maze, symbols):
    for index, tile in enumerate(maze):
        print(symbols[tile], end="\n" if index % 15 == 14 else "")

# Function asking what action the player wants to realise. It then call the appropriate function, movement, or exiting.
def action(last_pos):
    action = input(print("What action do you want to make?\n", "To quit the game, press Q.\n", "To move MacGyver, press 'R' to move right, 'L' to move left, 'U' to move upward, 'D' to move downward."))
    print(action)
    if action == "U" or action == "u":
        movement(maze1, "U", last_pos)
        draw_maze(maze1, symbols)
    elif action == "D" or action == "d":
        movement(maze1, "D", last_pos)
        draw_maze(maze1, symbols)
    elif action == "L" or action == "l":
        movement(maze1, "L", last_pos)
        draw_maze(maze1, symbols)
    elif action == "R" or action == "r":
        movement(maze1, "R", last_pos)
        draw_maze(maze1, symbols)
    elif action == "Q" or action == "q":
        exiting()
    # if winning(tools) == True:
    #     print("Well done! MacGyver fough the guardian and won! Exiting the game")
    #     exit()
    
# Movement function in case the player asks for it. Depending on the letter entered, MacGyver will move to the right, left, up or down. 
def movement(maze, direction, last_pos):
    if direction == "R":
        mouv = 1
    elif direction == "L":
        mouv = -1
    elif direction == "U":
        mouv = -15
    elif direction == "D":
        mouv = 15
    ###################################################################################################################################
    ######################## Voir comment intégrer des erreurs au lieu de plusieurs If 
    if maze[macgyver.pos + mouv] == 1:
        return WallError
    elif maze[macgyver.pos + mouv] == 2:
        return Item2
    elif maze[macgyver.pos + mouv] == 3:
        return Item3
    elif maze[macgyver.pos + mouv] == 4:
        return Item4 
    try:    
        maze[macgyver.pos] = 0
        maze[macgyver.pos + mouv] = 5
        macgyver.pos = macgyver.pos + mouv
    except WallError:   
        print("MacGyver can't move ") 
    except Item2:   
        print("MacGyver collected the Ꝣ object!")
        macgyver.inventory.append(tools(2))
        print(macgyver.inventory)
        maze[macgyver.pos] = 0
        maze[macgyver.pos + mouv] = 5
        macgyver.pos = macgyver.pos + mouv
    except Item3:   
        print("MacGyver collected the ꞵ object!")
        macgyver.inventory.append(tools(3))
        print(macgyver.inventory)
        maze[macgyver.pos] = 0
        maze[macgyver.pos + mouv] = 5
        macgyver.pos = macgyver.pos + mouv
    except Item4:   
        print("MacGyver collected the ꜫ object!")
        macgyver.inventory.append(tools(4))
        print(macgyver.inventory)
        maze[macgyver.pos] = 0
        maze[macgyver.pos + mouv] = 5
        macgyver.pos = macgyver.pos + mouv

# Exiting function when the player wants to quit
def exiting():
    print("MacGyver gives up and quit the game!")
    exit()

# Function which determines if we won the game
def winning():
    verification = 0
    for element in tools.keys():
    # if all (keys for keys in tools in macgyver.inventory and macgyver.pos == 239):
        if element in macgyver.inventory:
            verification += 1
    if verification == 3:
        return True
    else:
        return False

  
maze1 = maze_creation()
available = get_free_locations(maze1)
place_items(maze1, available)
draw_maze(maze1, symbols)  
while winning() == False:
    action(macgyver.pos)     

