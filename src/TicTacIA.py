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

    def _saveData(self):
        # ASSIGNING STATS FOR CURRENT GAME
        for key, value in self._game.items():
            grid = str(key)
            if grid in self._memory:
                # GRID EXIST
                for play in value:
                    i = str(play)
                    if str(i) not in self._memory[grid]:
                        self._memory[grid][i] = [0, 0, 0]
                    # PLAY DOES NOT EXIST
                    if self._state == "win":
                        self._memory[grid][i][0] += 1
                    elif self._state == "draw":
                        self._memory[grid][i][1] += 1
                    elif self._state == "loss":
                        self._memory[grid][i][2] += 1
            else:
                for i in value:
                    value[i] = [0, 0, 0]
                    if self._state == "win":
                        value[i][0] += 1
                    elif self._state == "draw":
                        value[i][1] += 1
                    elif self._state == "loss":
                        value[i][2] += 1
                self._memory[grid] = value
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
        self._memory = data or ""

    def __init__(self, name, position, degree=70):
        super().__init__(name, position)
        self._degree = 70
        if degree.isdigit() and 100 >= int(degree) >= 0:
            self._degree = degree
        self._game = {}
        self._state = ""
        self._load()
        # INVALID MODE MESSAGE
        self._file = open("../memory/" + self.name + ".json", "w+")

    def win(self):
        self._state = "win"
        self._saveData()

    def loss(self):
        self._state = "loss"
        self._saveData()

    def draw(self):
        self._state = "draw"
        self._saveData()

    def __del__(self):
        # WRITING DATA TO FILE
        json.dump(self._memory, self._file)
        self._file.close()

    def _playRandom(self, grid):
        play = random.randint(0, 8)
        while grid[play] != 0:
            play = random.randint(0, 8)
        return play

    def _getBestPlay(self, grid):
        # IF NO PLAY, PLAY RANDOM
        try:
            possibilities = self._memory[str(grid)]
        except KeyError:
            return self._playRandom(grid)
        lim = 100 - int(self._degree)
        most = [[-1, 0],
                [-1, 0]]
        for play, stats in possibilities.items():
            rate = 100 * float(stats[0] / (stats[0] + stats[1] + stats[2]))
            if rate > most[0][1]:
                most[0][0] = play
                most[0][1] = rate
            draw_rate = 100 * float(stats[1] / (stats[0] + stats[1] + stats[2]))
            if draw_rate > most[1][1]:
                most[1][0] = play
                most[1][1] = draw_rate
        if int(most[0][1]) > lim:
            # print("RETURN WIN PLAY")
            return int(most[0][0])
        elif int(most[1][1]) > 0:
            # print("RETURN DRAW PLAY")
            return self._playRandom(grid)
        # print("RETURN RANDOM PLAY")
        return self._playRandom(grid)

    def _gridReplace(self, grid):
        # REPLACE GRID IN ORDER TO BE ABLE TO PLAY PLAYER 1 OR PLAYER 2
        for i, _ in enumerate(grid):
            if grid[i] == self.position:
                grid[i] = 1
            elif grid[i] != 0:
                grid[i] = 2
        return grid

    def generate_play(self, grid):
        grid = self._gridReplace(grid)
        play = self._getBestPlay(grid)
        self._game[str(grid)] = {play: ''}
        return play
