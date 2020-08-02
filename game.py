"""File which contains the Game class, its attributes and functions.These functions are the mechanic of the game."""
import pygame
from pygame.locals import *
from tile import Tile
from tiles import Wall, Corridor, Exit, Guardian, Macgyver, PlasticTube, Ether, Needle
from constantes import REPLAY_IMAGE, DEFEAT_IMAGE, MOVEMENTS, MESSAGE_IMAGE, BACKGROUND_IMAGE_2, BACKGROUND_IMAGE, PLASTICTUBE_IMAGE, ETHER_IMAGE, NEEDLE_IMAGE
from maze import Maze

class Game():
    """Class holding the main mechanisms of the game"""
    DECISION = {pygame.K_F1: 1,
                pygame.K_F2: 2}

    def __init__(self):
        """Constructor"""
        self.binary = 1
        self.screen = pygame.display.set_mode((600, 600))
        self.background = pygame.image.load(BACKGROUND_IMAGE).convert()
        self.background2 = pygame.image.load(BACKGROUND_IMAGE_2).convert()
        self.plastic_tube_img = pygame.image.load(PLASTICTUBE_IMAGE).convert_alpha()
        self.ether_img = pygame.image.load(ETHER_IMAGE).convert_alpha()
        self.needle_img = pygame.image.load(NEEDLE_IMAGE).convert_alpha()
        self.victory_img = pygame.image.load(REPLAY_IMAGE).convert_alpha()
        self.defeat_img = pygame.image.load(DEFEAT_IMAGE).convert_alpha()
        self.custom_font, self.custom_text = None, None
        self.message_img = pygame.image.load(MESSAGE_IMAGE).convert_alpha()
        self.maze, self.state, self.decision = None, "running", 0

    def start(self):
        """Function creating the attributes and starting the loop which allows the game running"""
        pygame.key.set_repeat(400, 30) 
        pygame.font.init()
        self.custom_font = pygame.font.SysFont('Arial', 20)
        self.custom_text = self.custom_font.render("MacGyver's bag:", False, (0, 0, 0))
        self.maze, self.maze.liste[0] = Maze(), Macgyver()
        self.maze.get_free_locations() 
        self.maze.place_items(self.maze.places)
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.move(MOVEMENTS[event.key][1]) if event.key in MOVEMENTS else ""
                    if self.state == "win" or self.state == "defeat":
                        self.binary = Game.DECISION[event.key] if event.key in Game.DECISION else 0
                        self.end()
                elif event.type == QUIT:
                    continuer = False
            self.draw()

    def move(self, movement):
        """Function waiting for the player to choose one direction with the arrays of the keyboard.
        It then executes a movement if this one is valid, it does nothing if not.
        """
        macgyver_pos = self.maze.find_macgyver()
        if movement == "u":
            mouv = 0 if macgyver_pos / 15 < 1 else -15
        elif movement == "d":
            mouv = 0 if macgyver_pos / 15 >= 14 else 15
        elif movement == "l":
            mouv = 0 if macgyver_pos % 15 == 0 else -1
        elif movement == "r":
            mouv = 0 if macgyver_pos % 15 == 14 else 1
        if isinstance(self.maze.liste[macgyver_pos + mouv], Wall):
            return
        elif isinstance(self.maze.liste[macgyver_pos + mouv], Guardian):
            if self.state == "beat":
                self.maze.liste[macgyver_pos] = Corridor()
                self.maze.liste[macgyver_pos + mouv] = Macgyver()
            else:
                self.state = "defeat"
        elif isinstance(self.maze.liste[macgyver_pos + mouv], Exit):
            self.state = "win"
        else:
            self.maze.liste[macgyver_pos] = Corridor()
            self.maze.liste[macgyver_pos + mouv] = Macgyver()
        self.check_ready()

    def draw_inventory(self):
        if not self.maze.find_plastic_tube():
            self.screen.blit(self.plastic_tube_img, (0, 30))
        if not self.maze.find_ether():
            self.screen.blit(self.ether_img, (35, 30))
        if not self.maze.find_needle():
            self.screen.blit(self.needle_img, (70, 30))

    def draw_message(self):
        if self.state == "beat":
            self.screen.blit(self.message_img, (170, 7))
        if self.state == "win":
            self.screen.blit(self.victory_img, (0, 0))
        if self.state == "defeat":
            self.screen.blit(self.defeat_img, (0, 0))

    def check_ready(self):
        if not self.maze.find_plastic_tube() and not self.maze.find_ether() and not self.maze.find_needle() and self.maze.find_guardian():
            self.state = "beat"

    def end(self):
        if self.binary == 1:
            self.__init__()
            self.start()
        elif self.binary == 2:
            exit()

    def draw(self):
        "Function drawing the maze, the tiles and MacGyver"
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.background2, (75, 75))
        self.screen.blit(self.custom_text, (0, 0))
        self.maze.draw(self.screen)
        self.draw_inventory()
        self.draw_message()
        pygame.display.flip()
