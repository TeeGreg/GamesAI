import random
import json

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
            locgrid = grid
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

class AIPlayer(GenericPlayer):

    def _saveFile(self):
        json.dump(self.memory, self._file)
        self._file.close()

    def _load(self):
        fd = open("../memory/" + self.name + ".json", "r+")
        data = json.load(fd)
        fd.close()
        self.memory = data or ""

    def __init__(self, name, position, mode=""):
        super().__init__(name, position)
        self.mode = mode
        self._load()
        self._file = open("../memory/" + self.name + ".json", "w+")
        # INVALID MODE MESSAGE
        if self.mode != "learning":
            self.mode = "tryhard"

    def __del__(self):
        self._saveFile()

    def generate_play(self, grid):
        if self.mode == "learning":
            locdic = {}
            play = random.randint(0, 8)
            while grid[play] != 0:
                play = random.randint(0, 8)
            locdic['grid'] = grid
            locdic['play'] = play
            self.memory.append(locdic)
        elif self.mode == "tryhard":
            #get_best_play(memoire)
            play = random.randint(0, 8)
        return play
