import random
from classes.player import AIPlayer

class RandomPlayer(AIPlayer):
    def select_cards(self):
        choices = []
        for i in range(1, 6):
            if bool(random.getrandbits(1)):
                choices.append(int(i))
        print("CHOICES:", choices)
        return choices