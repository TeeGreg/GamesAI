import json
import random

from utils import convert_string, perm_x


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
        pass
#       try:
            # print(self.new_moves)
        for move in self.new_moves:
            if move in self.moves and self.moves[move]["play"] == self.new_moves[move]:
                self.moves[move][issue] += 1
            else:
                self.moves[move] = {"play": self.new_moves[move], "win": 0, "loss": 0, "draw": 0}
                self.moves[move][issue] += 1
        self.new_moves = {}
            #with open('ressources/darwin.json', 'r') as file:
                #dataset = json.load(file)
                #dataset[self.name] = {"moves": self.moves, "stats": self.stats}
        #except (FileNotFoundError, AttributeError):
            #print("No existing file")
            #dataset = {self.name: {"moves": self.moves, "stats": self.stats}}
        #try:
            #try:
                #with open('ressources/darwin.json', 'w+') as file:
                    #json.dump(dataset, file)
            #except KeyboardInterrupt:
                #with open('ressources/darwin.json', 'w+') as file:
                    #json.dump(dataset, file)
                #exit(0)
        #except (FileNotFoundError, AttributeError):
            #print("Fails to save")

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
            # print("tryhard --------------------------------------------------")
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

    def _save_data(self):
        # ASSIGNING STATS FOR CURRENT GAME
        for key, value in self._game.items():
            grid = str(key)
            if grid in self._memory:
                # GRID EXIST
                for play in value:
                    i = str(play)
                    if i not in self._memory[grid]:
                        # PLAY DOES NOT EXIST, CREATE IT
                        self._memory[grid][i] = [0, 0, 0]
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
            data = {}
        fd.close()
        self._memory = data

    def __init__(self, name, position, degree='100'):
        super().__init__(name, position)
        self.degree = '100'
        if degree.isdigit() and 100 >= int(degree) >= 0:
            self.degree = degree
        self._game = {}
        self._state = ""
        self._load()
        # INVALID MODE MESSAGE
        self._file = open("../memory/" + self.name + ".json", "w+")

    def win(self):
        self._state = "win"
        self._save_data()

    def loss(self):
        self._state = "loss"
        self._save_data()

    def draw(self):
        self._state = "draw"
        self._save_data()

    def __del__(self):
        # WRITING DATA TO FILE
        json.dump(self._memory, self._file)
        self._file.close()

    def _play_random(self, grid):
        play = random.randint(0, 8)
        while grid[play] != 0:
            play = random.randint(0, 8)
        return play

    def _get_best_play(self, grid):
        # IF NO PLAY, PLAY RANDOM
        try:
            possibilities = self._memory[str(grid)]
        except KeyError:
            return self._play_random(grid)
        wplays = {}
        dplays = {}
        for play, stats in possibilities.items():
            wrate = float(stats[0] / max(stats[0] + stats[1] + stats[2], 1)) * 100
            drate = float(stats[1] / max(stats[0] + stats[1] + stats[2], 1)) * 100
            if wrate >= 30:
                wplays[play] = wrate
            elif drate >= 60:
                dplays[play] = drate
        if wplays:
            best = int(max(wplays, key=wplays.get))
            return best
        elif dplays:
            best = int(max(dplays, key=dplays.get))
            return best
        return self._play_random(grid)

    def _grid_replace(self, grid):
        # REPLACE GRID IN ORDER TO BE ABLE TO PLAY PLAYER 1 OR PLAYER 2
        for i, _ in enumerate(grid):
            if grid[i] == self.position:
                grid[i] = 1
            elif grid[i] != 0:
                grid[i] = 2
        return grid

    def generate_play(self, grid):
        grid = self._grid_replace(grid)
        play = self._get_best_play(grid)
        self._game[str(grid)] = {str(play): ''}
        return play
