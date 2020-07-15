from classes import *

symbols = {0: "  ", 1: "██", 2: "🧪", 3: "🍼", 4: "💉", 5: "🕴️", 6: "👻", 7: "🏁", 8: "🏆"}
convertion_csv = {" ": 0, "X": 1, "M": 5, "G": 6, "E": 7}

macgyver = Character("MacGyver", 0)
plastic_tube = Items(2, "Plastic Tube")
ether = Items(3, "Ether")
needle = Items(4, "Needle")
plastic_tube.add_item(), ether.add_item(), needle.add_item()
background_image = "D:/Programmation/Repos_Git/MacGyverOPCR/background.jpg"
MacGyver_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/MacGyver.png"
guardian_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/Gardien.png"
ether_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/ether.png"
needle_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/aiguille.png"
plastic_tube_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/tube_plastique.png"
syringe_image = "D:/Programmation/Repos_Git/MacGyverOPCR/ressource/seringue.png"
