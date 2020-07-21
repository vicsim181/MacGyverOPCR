"""File which contains the various constants variables used by the game"""
import pygame
import pygame.locals

symbols = {0: "  ", 1: "██", 2: "🧪", 3: "🍼", 4: "💉", 5: "🕴️", 6: "👻", 7: "🏁", 8: "🏆"}
convertion_csv = {" ": 0, "X": 1, "M": 5, "G": 6, "E": 7}

background_image = "./ressource/background1.png"
background_image_2 = "./ressource/background2.jpg"
MacGyver_image = "./ressource/macgyver.png"
guardian_image = "./ressource/Gardien.png"
ether_image = "./ressource/ether.png"
needle_image = "./ressource/needle.png"
plastic_tube_image = "./ressource/tube.png"
syringe_image = "./ressource/syringe.png"
wall_image = "./ressource/wall.png"
exit_image = "./ressource/exit2.png"
replay_image = "./ressource/replay.png"
defeat_image = "./ressource/defeat.png"
message_image = "./ressource/message.png"
raws_maze = 15
columns_maze = 15
taille_sprite = 30

images = {1: wall_image, 
          2: plastic_tube_image, 
          3: ether_image, 
          4: needle_image, 
          5: MacGyver_image, 
          6: guardian_image,
          7: exit_image}

images_reverse = {"Plastic Tube": plastic_tube_image, "Ether": ether_image, "Needle": needle_image}

ecran = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
fond = pygame.image.load(background_image).convert()
fond2 = pygame.image.load(background_image_2).convert()

movements = { pygame.K_UP: [(0, -30), "u"], 
              pygame.K_DOWN: [(0, 30), "d"],
              pygame.K_LEFT: [(-30, 0), "l"],
              pygame.K_RIGHT: [(30, 0), "r"]}