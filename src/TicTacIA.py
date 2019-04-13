import json
import random

class GenericPlayer:
    def __init__(self, name, position):
        self.name = name.lower()
        self.position = position

    def get_name(self):
        return self.name

    def generate_play(self, grid):
        pass

    def win(self):
        pass

    def loss(self):
        pass

    def draw(self):
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


class DarwinPlayer(GenericPlayer):

    def __init__(self, name, position):
        super().__init__(name, position)
        self.moves, self.stats = self._load_memory()
        # self.tryhard = (self.stats[1] * 100 +
        #                 self.stats[2] * 50 -
        #                 self.stats[0] * 100) / (sum(self.stats)+10)
        self.tryhard = (2 * self.stats[1] - self.stats[0]) / (sum(self.stats) + 1) * 100
        print(self.tryhard)

    def _load_memory(self):
        try:
            with open('ressources/darwin.json', 'r') as file:
                dataset = json.load(file)
                return dataset[self.name]["moves"], dataset[self.name]["stats"]
        except (FileNotFoundError, AttributeError):
            print("No AI with the name")
        return {}, [0, 0, 0]

    def _save(self):
        try:
            with open('ressources/darwin.json', 'r') as file:
                dataset = json.load(file)
                dataset[self.name] = {"moves": self.moves, "stats": self.stats}
        except (FileNotFoundError, AttributeError):
            print("No existing file")
            dataset = {self.name: {"moves": self.moves, "stats": self.stats}}
        try:
            with open('ressources/darwin.json', 'w+') as file:
                json.dump(dataset, file)
        except (FileNotFoundError, AttributeError):
            print("Fails to save")

    def generate_play(self, grid):
        if self.tryhard < random.randint(0, 100):
            if ''.join(str(i) for i in grid) in self.moves:
                play = self.moves[''.join(str(i) for i in grid)]
                return play
        picks = [i for i, x in enumerate(grid) if not x]
        play = random.choice(picks)
        self.moves[''.join(str(i) for i in grid)] = play
        return play

    def win(self):
        self.stats[0] += 1
        self._save()

    def draw(self):
        self.stats[2] += 1
        self._save()

    def loss(self):
        self.stats[1] += 1
        # self._save()


class AIPlayer(GenericPlayer):

    def _saveFile(self):
        # ASSIGNING STATS FOR CURRENT GAME
        for key, value in self._game.items():
            grid = str(key)
            if grid in self.memory:
                # GRID EXIST
                for i in value:
                    if i not in self.memory[grid]:
                    # PLAY DOES NOT EXIST
                        self.memory[grid][i] = [0, 0, 0]
                    if self._state == "win":
                        self.memory[grid][i][0] += 1
                    elif self._state == "draw":
                        self.memory[grid][i][1] += 1
                    elif self._state == "loss":
                        self.memory[grid][i][2] += 1
            else:
                for i in value:
                    value[i] = [0, 0, 0]
                    if self._state == "win":
                        value[i][0] += 1
                    elif self._state == "draw":
                        value[i][1] += 1
                    elif self._state == "loss":
                        value[i][2] += 1
                self.memory[grid] = value
        self._game = {}

    def _load(self):
        import os
        import sys
        if os.path.exists("../memory/" + self.name + ".json") == 0:
            try:
                if os.path.isdir("../memory") == 0:
                        os.mkdir("../memory")
                open("../memory/" + self.name + ".json", 'a').close()
            except OSError:
                sys.exit('Fatal Error: cant create the memory for player' + self.name)
        fd = open("../memory/" + self.name + ".json", "r+")
        try:
            data = json.load(fd)
        except ValueError:
            data = {'': ''}
        fd.close()
        self.memory = data or ""

    def __init__(self, name, position, mode=""):
        super().__init__(name, position)
        self.mode = mode
        self._game = {}
        self._state = ""
        self._load()
        # INVALID MODE MESSAGE
        if self.mode != "learning":
            self.mode = "tryhard"
        self._file = open("../memory/" + self.name + ".json", "w+")

    def win(self):
        self._state = "win"
        self._saveFile()

    def loss(self):
        self._state = "loss"
        self._saveFile()

    def draw(self):
        self._state = "draw"
        self._saveFile()

    def __del__(self):
        json.dump(self.memory, self._file)
        self._file.close()

    def generate_play(self, grid):
        if self.mode == "learning":
            play = random.randint(0, 8)
            while grid[play] != 0:
                play = random.randint(0, 8)
            self._game[str(grid)]= {play: ''}
        elif self.mode == "tryhard":
            #get_best_play(memoire)
            play = random.randint(0, 8)
        return play
