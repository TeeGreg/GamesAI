import json
import random
import json

from utils import convert_string, get_max_rotation, perm_x


class GenericPlayer:
    def __init__(self, name, position):
        self.name = name
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


class DefensivePlayer(GenericPlayer):

    def generate_play(self, grid):
        picks = [i for i, x in enumerate(grid) if not x]
        from TicTac import end
        for play in picks:
            locgrid = grid.copy()
            locgrid[play] = self.position % 2 + 1
            if end(locgrid) == self.position % 2 + 1:
                return play
        play = random.choice(picks)
        return play


class SemiLethalPlayer(GenericPlayer):

    def generate_play(self, grid):
        picks = [i for i, x in enumerate(grid) if not x]
        from TicTac import end
        for play in picks:
            locgrid = grid.copy()
            locgrid[play] = self.position
            if end(locgrid) == self.position:
                return play
        play = random.choice(picks)
        return play


class DarwinPlayer(GenericPlayer):
    
    def __init__(self, name, position):
        super().__init__(name, position)
        self.new_moves = {}
        self.moves, self.stats = self._load_memory()
        # self.tryhard = (self.stats[1] * 100 +
        #                 self.stats[2] * 50 -
        #                 self.stats[0] * 100) / (sum(self.stats)+10)
        # self.tryhard = (2 * self.stats[1] - self.stats[0]) / (sum(self.stats) + 1) * 100
        # print(self.tryhard)

    def _load_memory(self):
        try:
            with open('ressources/darwin.json', 'r') as file:
                dataset = json.load(file)
                return dataset[self.name]["moves"], dataset[self.name]["stats"]
        except (FileNotFoundError, KeyError):
            print("No AI with the name")
        return {}, [0, 0, 0]

    def _save(self, issue):
        try:
            # print(self.new_moves)
            for move in self.new_moves:
                if move in self.moves and self.moves[move]["play"] == self.new_moves[move]:
                    self.moves[move][issue] += 1
                else:
                    self.moves[move] = {"play": self.new_moves[move], "win": 0, "loss": 0, "draw": 0}
                    self.moves[move][issue] += 1
            self.new_moves = {}
            with open('ressources/darwin.json', 'r') as file:
                dataset = json.load(file)
                dataset[self.name] = {"moves": self.moves, "stats": self.stats}
        except (FileNotFoundError, AttributeError):
            print("No existing file")
            dataset = {self.name: {"moves": self.moves, "stats": self.stats}}
        try:
            try:
                with open('ressources/darwin.json', 'w+') as file:
                    json.dump(dataset, file)
            except KeyboardInterrupt:
                with open('ressources/darwin.json', 'w+') as file:
                    json.dump(dataset, file)
                exit(0)
        except (FileNotFoundError, AttributeError):
            print("Fails to save")

    def generate_play(self, grid):
        # print("received grid : ", grid)
        # maxgrid, index = get_max_rotation(grid)
        maxgrid, index = grid.copy(), 0
        # print("maxgrid", maxgrid, "index", index)
        strigrid = convert_string(maxgrid)
        if strigrid in self.moves:
            move = self.moves[strigrid]
            tryhard = (move["loss"] - move["win"]) * 100
            if tryhard < random.randint(0, 100):
                # print("found move on maxgrid", move["play"])
                play = perm_x(move["play"], 4 - index)
                self.new_moves[strigrid] = perm_x(play, index)

                # print("returned move", play)
                return int(play)
            print("tryhard --------------------------------------------------")
        picks = [i for i, x in enumerate(grid) if not x]
        play = random.choice(picks)
        self.new_moves[strigrid] = perm_x(play, index)
        if not strigrid[int(play)]:
            print("picked move :")
            from TicTac import display
            display(grid)
            print("play :", play)
            print("saved move :")
            display(strigrid)
            print("play :", perm_x(play, index))

        return play

    def win(self):
        self.stats[0] += 1
        self._save("win")

    def draw(self):
        self.stats[2] += 1
        self._save("draw")

    def loss(self):
        self.stats[1] += 1
        self._save("loss")


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
