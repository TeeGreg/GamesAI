import random


class GenericPlayer:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_name(self):
        return self.name

    def generate_play(self, grid):
        pass

    def __str__(self):
        return self.get_name()


class RandomPlayer(GenericPlayer):

    def generate_play(self, grid):
        play = random.randint(0, 8)
        return play


class HumanPlayer(GenericPlayer):

    def generate_play(self, grid):
        play = int(input())
        return play


class NotSoDumbPlayer(GenericPlayer):

    def generate_play(self, grid):
        picks = [i for i, x in enumerate(grid) if not x]
        play = random.choice(picks)
        return play


class LethalPlayer(GenericPlayer):

    def generate_play(self, grid):
        picks = [i for i, x in enumerate(grid) if not x]
        from TicTac import end
        for play in picks:
            locgrid = grid.copy()
            locgrid[play] = self.position
            if end(locgrid) == self.position:
                return play
        for play in picks:
            locgrid = grid.copy()
            locgrid[play] = self.position % 2 + 1
            if end(locgrid) == self.position % 2 + 1:
                return play
        play = random.choice(picks)
        return play
