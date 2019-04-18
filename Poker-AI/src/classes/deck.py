import random

from classes.card import Card

class Deck:

    def _createColor(self, color, deck):
        for i in range(1, 13):
            deck.append(Card(color, i))
        return deck

    def __init__(self):
        self._deck = self._createColor("Clubs", [])
        self._deck = self._createColor("Diamond", self._deck)
        self._deck = self._createColor("Hearts", self._deck)
        self._deck = self._createColor("Spades", self._deck)

    def getRemaining(self):
        return [ card.getValues() for card in self._deck ]

    def throw(self):
        choice = random.choice(self._deck)
        self._deck.remove(choice)
        return choice.getValues()