import random

tools={"plastic tube":"", "ether":"", "needle":""}
#Fonction qui génère et modifie le labyrinthe à partir du fichier CSV
def maze_creation():
    with open("Maze.csv", encoding="utf8") as fichier:
        data= fichier.read()
        print(data,"\n")
        data=data[1:]
        print(data,"\n")
        data=data.split("\n")
        print(data,"\n")
        data=data[:-1]
        print(data,"\n")
        for k in range(len(data)):
            data[k]=data[k].split(";")
        print(data,"\n")    
        liste=[[ord(item) for item in line] for line in data]
        print(liste,"\n")
        liste2=[]
        for item in liste:
            for num in item:
                liste2.append(num)
        print(liste2,"\n")        
        liste3=[str(number) for number in liste2]
        print(liste3,"\n")
        for i in range(0,len(liste3)):
            liste3[i]=liste3[i].replace("32","0")
            liste3[i]=liste3[i].replace("88","1")
            liste3[i]=liste3[i].replace("65","8")
            liste3[i]=liste3[i].replace("66","8")
        print(liste3,"\n")    
        liste4=[int(number) for number in liste3]
        print(liste4,"\n")
        for i in range(15,len(liste4),16):
            liste4.insert(i,"\n")  
        print(liste4,"\n")

    # Faire en sorte que l'emplacement généré soit libre, donc un 0 sans objet dessus, et hors entrée et sortie du labyrinthe
    available2=[i for i in range(0,len(liste4)) if liste4[i]==0]
    print(available2,"\n")
    for item in tools:
        tools[item]=random.choice(available2)
        available2.remove(tools[item])
    print(tools,"\n")
    print(available2,"\n")

    



maze_creation()

