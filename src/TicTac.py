import random

from TicTacIA import HumanPlayer, RandomPlayer, NotSoDumbPlayer, LethalPlayer, DarwinPlayer, AIPlayer


def play(player, grid):
    while True:
        try:
            position = player.generate_play(grid.copy())
            if len(grid) > position >= 0 == grid[position]:
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
    # NO MORE SPACE IN GRID, NO WINNER
    if 0 not in grid:
        return 3
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

    return False


if __name__ == '__main__':
    import sys
    random.seed()
    human = 0
    if "-human" in sys.argv:
        human = 1
        players = [AIPlayer("Santiago", 1, sys.argv[2]), HumanPlayer("Human", 2)]
    else:
        players = [AIPlayer("Santiago", 1, sys.argv[2]), AIPlayer("Castaneda", 2, sys.argv[3])]
        #players = [AIPlayer("Santiago", 1, sys.argv[2]), LethalPlayer("Di10", 2)]
        #players = [AIPlayer("Santiago", 1, sys.argv[2]), NotSoDumbPlayer("Di10", 2)]
    wins = [0, 0, 0]
    for i in range(int(sys.argv[1])):
        print("Game number:", i + 1)
        #players = [AIPlayer("Santiago", 1, "learning"), NotSoDumbPlayer("Di10", 2)]
        grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        player = random.randint(0, 1)
        if human:
            print(players[player], " starts !")
        winner = 0
        while not winner:
            play(players[player], grid)
            player = (player + 1) % 2
            if human:
                display(grid)
            winner = end(grid)
        if winner == 3:
            #print("Draw ! ")
            players[0].draw()
            players[1].draw()
        else:
            players[winner - 1].win()
            players[winner % 2].loss()
            if human:
                print(players[winner - 1], "Wins !")
        wins[winner - 1] += 1
    print(wins)
