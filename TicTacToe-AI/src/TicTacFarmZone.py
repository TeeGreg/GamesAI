# MAIN GAME PROCESS
from TicTac import game
# CLASSES
from TicTacIA import HumanPlayer, RandomPlayer, NotSoDumbPlayer, LethalPlayer, DarwinPlayer, \
    SemiLethalPlayer, DefensivePlayer, AIPlayer

# IMPORTS
import sys
import random
import time
import json

def print_values(players, count, wins):
    if "-s" not in sys.argv:
        print("Played:", count, "games")
        print(wins)


if __name__ == '__main__':
    end = "Ctrl"
    if "-l" in sys.argv:
        # SET A LIMIT
        end = "Limit"
        limit = int(sys.argv[sys.argv.index("-l") + 1])
    elif "-t" in sys.argv:
        # SET A TIME LIMIT
        end = "Time"
        final_date = time.time() + int(sys.argv[sys.argv.index("-t") + 1])
    wins = [0, 0, 0]
    if "-human" in sys.argv:
        sys.argv.append("-d")
        end = "Limit"
        limit = 1
        players = [HumanPlayer("Ezen", 1), AIPlayer("Santiago", 2)]
    elif "-random" in sys.argv:
        players = [AIPlayer("Santiago", 1), NotSoDumbPlayer("NotSoDumb", 2)]
    elif "-defensive" in sys.argv:
        players = [AIPlayer("Santiago", 1), DefensivePlayer("Defensive", 2)]
    elif "-lethal" in sys.argv:
        players = [AIPlayer("Santiago", 1), LethalPlayer("Lethal", 2)]
    else:
        players = [AIPlayer("Santiago", 1), DarwinPlayer("Darwin", 2)]
    count = 1
    print("Player 1:", players[0].get_name())
    print("Player 2:", players[1].get_name())
    while True:
        try:
            winner = game(players, "-d" in sys.argv)
            wins[winner - 1] += 1
            if count % 10000 == 0:
                print_values(players, count, wins)
            if end == "Time" and time.time() >= final_date:
                print_values(players, count, wins)
                exit()
            if end == "Limit" and count >= limit:
                print_values(players, count, wins)
                exit()
            count += 1
        except KeyboardInterrupt:
            print_values(players, count, wins)
            exit()