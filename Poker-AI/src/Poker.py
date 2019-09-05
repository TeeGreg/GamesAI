import sys

from classes.table import Table
from classes.player import HumanPlayer
from AI.ai_player import RandomPlayer

def main():
    if "-bet" in sys.argv:
        players = [RandomPlayer("Bot1", 1, 1000), RandomPlayer("Bot2", 2, 1000)]
        table = Table(players, 50, "bet")
    else:
        players = [HumanPlayer("Player1", 1, 1000), HumanPlayer("Player2", 2, 1000)]
        table = Table(players)
    table.play_one_hand()


if __name__ == '__main__':
    main()