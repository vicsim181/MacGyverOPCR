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

laby=[]
laby=[1]*225

print(labyrinthe)
print(laby)


