import pygame
import pygame.locals

from character import Character

symbols = {0: "  ", 1: "██", 2: "🧪", 3: "🍼", 4: "💉", 5: "🕴️", 6: "👻", 7: "🏁", 8: "🏆"}
convertion_csv = {" ": 0, "X": 1, "M": 5, "G": 6, "E": 7}

# macgyver = Character("MacGyver", 0)
background_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/fond.png"
MacGyver_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/MacGyver.png"
guardian_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/Gardien.png"
ether_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/ether.png"
needle_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/aiguille.png"
plastic_tube_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/tube_plastique.png"
syringe_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/seringue.png"
wall_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/wall.png"
corridor_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/corridor.png"
exit_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/exit.jpg"
raws_maze = 15
columns_maze = 15
taille_sprite = 30

images = {0: corridor_image,
          1: wall_image, 
          2: plastic_tube_image, 
          3: ether_image, 
          4: needle_image, 
          5: MacGyver_image, 
          6: guardian_image,
          7: exit_image}
