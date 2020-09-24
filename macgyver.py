"""Main file, from which the game is launched"""
from game import Game

def main():
    """Main function, launching the game, calling the Game class"""
    game = Game(1)
    game.start()

if __name__ == '__main__':
    main()
