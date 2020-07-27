"""File which contains the various constants variables used by the game"""
import pygame

# MACGYVER_IMAGE = "./ressource/macgyver.png"
GUARDIAN_IMAGE = "./ressource/Gardien.png"
# ETHER_IMAGE = "./ressource/ether.png"
# NEEDLE_IMAGE = "./ressource/needle.png"
# PLASTIC_TUBE_IMAGE = "./ressource/tube.png"
SYRINGE_IMAGE = "./ressource/syringe.png"
# WALL_IMAGE = "./ressource/wall.png"
# EXIT_IMAGE = "./ressource/exit2.png"
REPLAY_IMAGE = "./ressource/replay.png"
DEFEAT_IMAGE = "./ressource/defeat.png"
MESSAGE_IMAGE = "./ressource/message.png"
SIZE_SPRITE = 30


MOVEMENTS = {pygame.K_UP: [(0, -30), "u"],
             pygame.K_DOWN: [(0, 30), "d"],
             pygame.K_LEFT: [(-30, 0), "l"],
             pygame.K_RIGHT: [(30, 0), "r"]}

# Continuer le tri