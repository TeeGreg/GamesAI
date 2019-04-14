# MAIN GAME PROCESS
from TicTac import game
# CLASSES
from TicTacIA import AIPlayer, HumanPlayer

# IMPORTS
import sys
import random
import time
import json

def print_values(players, count, wins):
    if "-s" not in sys.argv:
        print("Played:", count, "games")
        print(players[0].name + ":", players[0].degree)
        print(players[1].name + ":", players[1].degree)
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
    cases = [0, 25, 50, 75, 100]
    if "-v" in sys.argv:
        # CHANGE TRYHARD AMOUNT
        cases = json.loads(sys.argv[sys.argv.index("-v") + 1])
    if "-human" in sys.argv:
        sys.argv.append("-d")
        cases = [100]
        end = "Limit"
        limit = int(sys.argv[sys.argv.index("-l") + 1])
        players = [HumanPlayer("Ezen", 1), AIPlayer("Santiago", 2)]
    else:
        players = [AIPlayer("Santiago", 1), AIPlayer("Dummy", 2)]
    count = 1
    players[0].degree = random.choice(cases)
    players[1].degree = random.choice(cases)
    while True:
        try:
            winner = game(players)
            wins[winner - 1] += 1
            if count % 1000 == 0:
                print_values(players, count, wins)
                players[0].degree = random.choice(cases)
                players[1].degree = random.choice(cases)
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