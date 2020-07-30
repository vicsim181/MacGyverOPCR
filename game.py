"""File which contains the Game class, its attributes and functions.These functions are the mechanic of the game."""
import pygame
from pygame.locals import *
from tiles import Tiles
from constantes import REPLAY_IMAGE, DEFEAT_IMAGE, MOVEMENTS, MESSAGE_IMAGE
from character import Character
from maze import Maze

class Game():
    """Class holding the main mechanisms of the game"""
    BACKGROUND_IMAGE, BACKGROUND_IMAGE_2 = "./ressource/background1.png", "./ressource/background2.jpg"

    def __init__(self):
        """Constructor"""
        self.screen = pygame.display.set_mode((600, 600))
        self.background = pygame.image.load(Game.BACKGROUND_IMAGE).convert()
        self.background2 = pygame.image.load(Game.BACKGROUND_IMAGE_2).convert()
        self.custom_font, self.custom_text = None, None
        self.macgyver, self.maze = None, None

    def start(self):
        """Function creating the attributes and starting the loop which allows the game running"""
        pygame.key.set_repeat(400, 30); pygame.font.init()
        self.custom_font = pygame.font.SysFont('Arial', 20)
        self.custom_text = self.custom_font.render("MacGyver's bag:", False, (0, 0, 0))
        self.macgyver, self.maze = Character("MacGyver", 0, "./ressource/macgyver.png"), Maze()
        self.maze.get_free_locations(); self.maze.place_items(self.maze.places)
        self.maze.liste_2[0] = self.macgyver
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.loop(MOVEMENTS[event.key][1]) if event.key in MOVEMENTS else ""
                elif event.type == QUIT:
                    continuer = False
            self.draw()

    def loop(self, movement):
        """Function waiting for the player to choose one direction with the arrays of the keyboard.
        It then executes a movement if this one is valid, it does nothing if not. 
        """
        if movement == "u":
            mouv = 0 if self.macgyver.index / 15 < 1 else -15
        elif movement == "d":
            mouv = 0 if self.macgyver.index / 15 >= 14 else 15
        elif movement == "l":
            mouv = 0 if self.macgyver.index % 15 == 0 else -1
        elif movement == "r":
            mouv = 0 if self.macgyver.index % 15 == 14 else 1
        if self.maze.liste_2[self.macgyver.index + mouv].status == "wall":
            return
        elif self.maze.liste_2[self.macgyver.index + mouv].status == "guardian":
            self.macgyver.winning(self.maze, mouv) if len(self.macgyver.inventory) == 3 else self.replay()
        elif self.maze.liste_2[self.macgyver.index + mouv].status == "exit":
            self.replay()
        else:
            self.macgyver.collect_item(Maze.TOOLS, self.maze, mouv)
            self.maze.liste_2[self.macgyver.index] = Tiles(self.macgyver.index, 0)
            self.maze.liste_2[self.macgyver.index + mouv] = self.macgyver
            self.macgyver.index = self.macgyver.index + mouv

    def replay(self):
        """Function offering the choice to the player to play another game or quitting once he won or lose"""
        if len(self.macgyver.inventory) == 3:
            self.screen.blit(pygame.image.load(REPLAY_IMAGE), (0, 0))
        else:
            self.screen.blit(pygame.image.load(DEFEAT_IMAGE), (0, 0))
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == K_F1:
                    self.start()
                elif event.type == KEYDOWN and event.key == K_F2:
                    exit()
            pygame.display.flip()

    def draw(self):
        "Function drawing the maze, the tiles and MacGyver"
        self.screen.blit(self.background, (0, 0)); self.screen.blit(self.background2, (75, 75))
        self.screen.blit(self.custom_text, (0, 0)); self.maze.draw(self.screen)
        self.macgyver.draw_inventory(self.screen)
