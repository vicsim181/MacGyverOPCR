"""File which contains the various constants variables used by the game"""
import pygame

BACKGROUND_IMAGE = "./ressource/background1.png"
BACKGROUND_IMAGE_2 = "./ressource/background2.jpg"
MACGYVER_IMAGE = "./ressource/macgyver.png"
GUARDIAN_IMAGE = "./ressource/Gardien.png"
ETHER_IMAGE = "./ressource/ether.png"
NEEDLE_IMAGE = "./ressource/needle.png"
PLASTIC_TUBE_IMAGE = "./ressource/tube.png"
SYRINGE_IMAGE = "./ressource/syringe.png"
WALL_IMAGE = "./ressource/wall.png"
EXIT_IMAGE = "./ressource/exit2.png"
REPLAY_IMAGE = "./ressource/replay.png"
DEFEAT_IMAGE = "./ressource/defeat.png"
MESSAGE_IMAGE = "./ressource/message.png"
SIZE_SPRITE = 30

IMAGES = {1: WALL_IMAGE,
          2: PLASTIC_TUBE_IMAGE,
          3: ETHER_IMAGE,
          4: NEEDLE_IMAGE,
          5: MACGYVER_IMAGE,
          6: GUARDIAN_IMAGE,
          7: EXIT_IMAGE}

IMAGES_REVERSE = {"Plastic Tube": PLASTIC_TUBE_IMAGE, "Ether": ETHER_IMAGE, "Needle": NEEDLE_IMAGE}

SCREEN = pygame.display.set_mode((600, 600))
BACKGROUND = pygame.image.load(BACKGROUND_IMAGE).convert()
BACKGROUND2 = pygame.image.load(BACKGROUND_IMAGE_2).convert()

MOVEMENTS = {pygame.K_UP: [(0, -30), "u"],
             pygame.K_DOWN: [(0, 30), "d"],
             pygame.K_LEFT: [(-30, 0), "l"],
             pygame.K_RIGHT: [(30, 0), "r"]}
