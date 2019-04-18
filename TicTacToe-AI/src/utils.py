

PERMUTATIONS = {
    "0": 6,
    "1": 3,
    "2": 0,
    "3": 7,
    "4": 4,
    "5": 1,
    "6": 8,
    "7": 5,
    "8": 2
}


def rotate(grid):
    return [grid[PERMUTATIONS[str(i)]] for i in range(len(grid))]


def get_max_rotation(grid):
    grids = [convert_string(grid)]
    grids.append(convert_string(rotate(grids[0])))
    grids.append(convert_string(rotate(grids[1])))
    grids.append(convert_string(rotate(grids[2])))
    return max(grids), grids.index(max(grids))


def convert_string(grid):
    return "".join(map(lambda i : str(i), grid))


def perm_x(play, count):
    for _ in range(count):
        play = str(PERMUTATIONS[str(play)])
    return play


# if __name__ == '__main__':
#     grid = 0, 1, 2, 0, 1, 2, 0, 1, 0
#     print(grid)
#     print(rotate(grid))
#     print(rotate(rotate(grid)))
#     print(rotate(rotate(rotate(grid))))
#     print(get_max_rotation("012012000"))
#     for i in range(9):
#         print(perm_x(i, 5))