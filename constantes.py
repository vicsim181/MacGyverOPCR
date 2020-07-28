"""File which contains the various constants variables used by the game"""
import pygame

SYRINGE_IMAGE = "./ressource/syringe.png"
REPLAY_IMAGE = "./ressource/replay.png"
DEFEAT_IMAGE = "./ressource/defeat.png"
MESSAGE_IMAGE = "./ressource/message.png"
SIZE_SPRITE = 30


MOVEMENTS = {pygame.K_UP: [(0, -30), "u"],
             pygame.K_DOWN: [(0, 30), "d"],
             pygame.K_LEFT: [(-30, 0), "l"],
             pygame.K_RIGHT: [(30, 0), "r"]}
