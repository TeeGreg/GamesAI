import random

from TicTacIA import HumanPlayer, RandomPlayer, NotSoDumbPlayer, LethalPlayer, DarwinPlayer, \
    SemiLethalPlayer, DefensivePlayer


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

def game(players):
        import sys
        grid = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        player = random.randint(0, 1)
        winner = 0
        if "-d" in sys.argv:
            display(grid)
        while not winner:
            if "-d" in sys.argv:
                print(players[player].name + "'s turn:")
            play(players[player], grid)
            player = (player + 1) % 2
            winner = end(grid)
            if "-d" in sys.argv:
                display(grid)
        if winner == 3:
            if "-d" in sys.argv:
                print("Draw ! ")
            players[0].draw()
            players[1].draw()
        else:
            players[winner - 1].win()
            players[winner % 2].loss()
            if "-d" in sys.argv:
                print(players[winner - 1], "Wins !")
        return winner

if __name__ == '__main__':
    import sys
    random.seed()
    if "-lethal" in sys.argv:
        players = [AIPlayer("Santiago", 1, sys.argv[2]), LethalPlayer("Lethal", 2)]
    if "-random" in sys.argv:
        players = [AIPlayer("Santiago", 1, sys.argv[2]), NotSoDumbPlayer("Random", 2)]
    if "-human" in sys.argv:
        # ADD HUMAN PLAYER
        players = [AIPlayer("Santiago", 1), HumanPlayer("Human", 2)]
    else:
        players = [AIPlayer("Santiago", 1, sys.argv[2]), AIPlayer("Dummy", 2, sys.argv[3])]
    wins = [0, 0, 0]
    for i in range(int(sys.argv[1])):
        winner = game(players)
        wins[winner - 1] += 1
    print(wins)
