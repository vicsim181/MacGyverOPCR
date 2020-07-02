import random


def essai_manuel_1():  
    labyrinthe=[]
    lignes=15
    while lignes>0:
        ligne=[]
        colonnes=15
        while colonnes>0:
            ligne.append(1)
            colonnes-=1    
        lignes-=1
        labyrinthe.append(ligne)
        labyrinthe.append("\n")
    return labyrinthe

def essai_manuel_2():
    laby=[]
    laby=[1]*15
    laby.append("\n")
    total = 210
    while total > 0: 
        if len(laby) % 16 == 0 and len(laby) >16: 
            laby.append("\n")
        else:
            laby.append(1)
            total-=1
    return laby

def manuels():
    print(essai_manuel_1())
    print("\n")
    print(essai_manuel_2())
# manuels()
###########################################################################################################
###########################################################################################################
tools={"plastic tube":"", "ether":"", "needle":""}
#Fonction qui génère et modifie le labyrinthe à partir du fichier CSV
def maze_creation():
    with open("Maze.csv", encoding="utf8") as fichier:
        data= fichier.read()
        data=data[1:]
        data=data.split("\n")
        data=data[:-1]
        for k in range(len(data)):
            data[k]=data[k].split(";")
        liste=[[ord(item) for item in line] for line in data]
        liste2=[]
        for item in liste:
            for num in item:
                liste2.append(num)
        liste3=[str(number) for number in liste2]
        for i in range(0,len(liste3)):
            liste3[i]=liste3[i].replace("32","0")
            liste3[i]=liste3[i].replace("88","1")
            liste3[i]=liste3[i].replace("65","8")
            liste3[i]=liste3[i].replace("66","8")
        liste4=[int(number) for number in liste3]
        for i in range(15,len(liste4),16):
            liste4.insert(i,"\n")  
        print(liste4)
    # Faire en sorte que l'emplacement généré soit libre, donc un 0 sans objet dessus, et hors entrée et sortie du labyrinthe
    for keys in tools:
        try:
            tools[keys]=random.randint(0,225)
        except:
            liste4[tools[keys]]=1
        print(liste4[tools[keys]])      
    print(tools)



maze_creation()

