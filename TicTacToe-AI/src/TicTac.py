import random
import sys

from TicTacIA import HumanPlayer, RandomPlayer, NotSoDumbPlayer, LethalPlayer, DarwinPlayer, \
    SemiLethalPlayer, DefensivePlayer, AIPlayer


def play(player, grid):
    while True:
        try:
            position = player.generate_play(grid.copy())
            # print(position)
            # print(grid, position, grid[position])
            if len(grid) > position >= 0 == grid[position]:
                # print("blup")
                grid[position] = player.position
                return
        except ValueError:
            pass
        print('wrong position')


def display(grid):
    """ """
    print(grid[:3])
    print(grid[3:6])
    print(grid[6:9])
    print()


def end(grid):
    # CHECK DIAGONALES
    if grid[0] == 2 and grid[4] == 2 and grid[8] == 2:
        return 2
    if grid[2] == 2 and grid[4] == 2 and grid[6] == 2:
        return 2
    if grid[0] == 1 and grid[4] == 1 and grid[8] == 1:
        return 1
    if grid[2] == 1 and grid[4] == 1 and grid[6] == 1:
        return 1
    # CHECK COLUMNS
    if grid[0] == 2 and grid[3] == 2 and grid[6] == 2:
        return 2
    if grid[1] == 2 and grid[4] == 2 and grid[7] == 2:
        return 2
    if grid[2] == 2 and grid[5] == 2 and grid[8] == 2:
        return 2
    if grid[0] == 1 and grid[3] == 1 and grid[6] == 1:
        return 1
    if grid[1] == 1 and grid[4] == 1 and grid[7] == 1:
        return 1
    if grid[2] == 1 and grid[5] == 1 and grid[8] == 1:
        return 1
    # CHECK LINES
    if 0 not in grid[0:3] and 2 not in grid[0:3]:
        return 1
    if 0 not in grid[3:6] and 2 not in grid[3:6]:
        return 1
    if 0 not in grid[6:9] and 2 not in grid[6:9]:
        return 1

    if 0 not in grid[0:3] and 1 not in grid[0:3]:
        return 2
    if 0 not in grid[3:6] and 1 not in grid[3:6]:
        return 2
    if 0 not in grid[6:9] and 1 not in grid[6:9]:
        return 2
    # NO MORE SPACE IN GRID, NO WINNER
    if 0 not in grid:
        return 3

    return False


def game(players, disp=False):
        grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        player = random.randint(0, 1)
        winner = 0
        if disp:
            display(grid)
        while not winner:
            if disp:
                print(players[player].name + "'s turn:")
            play(players[player], grid)
            player = (player + 1) % 2
            winner = end(grid)
            if disp:
                display(grid)
        if winner == 3:
            if disp:
                print("Draw ! ")
            players[0].draw()
            players[1].draw()
        else:
            players[winner - 1].win()
            players[winner % 2].loss()
            if disp:
                print(players[winner - 1], "Wins !")
        return winner


def init_players():
    if "-try1" in sys.argv:
        tryhard1 = sys.argv[sys.argv.index("-try1") + 1]
    else:
        tryhard1 = '65'
    if "-try2" in sys.argv:
        tryhard2 = sys.argv[sys.argv.index("-try2") + 1]
    else:
        tryhard2 = '65'

    if '-p1' in sys.argv:
        if "lethal" in sys.argv[sys.argv.index("-p1") + 1]:
            player1 = LethalPlayer("Lethal", 1)
        elif "defensive" in sys.argv[sys.argv.index("-p1") + 1]:
            player1 = DefensivePlayer("Offensive", 1)
        elif "offensive" in sys.argv[sys.argv.index("-p1") + 1]:
            player1 = SemiLethalPlayer("Defensive", 1)
        elif "random" in sys.argv[sys.argv.index("-p1") + 1]:
            player1 = NotSoDumbPlayer("Random", 1)
        elif "human" in sys.argv[sys.argv.index("-p1") + 1]:
            player1 = HumanPlayer("Human", 1)
        elif "darwin" in sys.argv[sys.argv.index("-p1") + 1]:
            player1 = DarwinPlayer("Di10", 1)
        elif "aiplayer" in sys.argv[sys.argv.index("-p1") + 1]:
            player1 = AIPlayer("Santiago", 1, tryhard1)
        else:
            player1 = LethalPlayer("Lethal", 1)
    else:
        player1 = LethalPlayer("Lethal", 1)
    if '-p2' in sys.argv:
        if "lethal" in sys.argv[sys.argv.index("-p2") + 1]:
            player2 = LethalPlayer("Lethal", 2)
        elif "defensive" in sys.argv[sys.argv.index("-p2") + 1]:
            player2 = DefensivePlayer("Offensive", 2)
        elif "offensive" in sys.argv[sys.argv.index("-p2") + 1]:
            player2 = SemiLethalPlayer("Defensive", 2)
        elif "random" in sys.argv[sys.argv.index("-p2") + 1]:
            player2 = NotSoDumbPlayer("Random", 2)
        elif "human" in sys.argv[sys.argv.index("-p2") + 1]:
            player2 = HumanPlayer("Human", 2)
        elif "darwin" in sys.argv[sys.argv.index("-p2") + 1]:
            player2 = DarwinPlayer("Ludo", 2)
        elif "aiplayer" in sys.argv[sys.argv.index("-p2") + 1]:
            player2 = AIPlayer("Santiago", 2, tryhard2)
        else:
            player2 = LethalPlayer("Lethal", 2)
    else:
        player2 = LethalPlayer("Lethal", 2)
    players = [player1, player2]
    return players


def play_games(players, game_number):
    wins = [0, 0, 0]
    for i in range(game_number):
        if i % 100 == 0:
            print("Wins:", wins)
        winner = game(players, "-d" in sys.argv)
        wins[winner - 1] += 1
    print(wins)


if __name__ == '__main__':
    random.seed()
    if '-h' in sys.argv or len(sys.argv) == 1:
        print("""
                -h              | Display the help
                -g {}           | Game Amount
                -pX -aiplayer   | PlayerX is a AI player
                -pX -darwin     | PlayerX is a Darwin player
                -pX -human      | PlayerX is a Human player
                -pX -lethal     | PlayerX is a lethal player
                -pX -offensive  | PlayerX is a offensive player
                -pX -defensive  | PlayerX is a defensive player
                -pX -random     | PlayerX is a random player
                -tryX {}        | Fix the tryhard percentage for player X
              """)
        exit(0)
    if "-g" in sys.argv:
        gamenumber = int(sys.argv[sys.argv.index("-g") + 1])
    else:
        gamenumber = 1

    play_games(init_players(), gamenumber)
