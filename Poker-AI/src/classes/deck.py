import random

from classes.card import Card

# COLORS:
#   CLUBS, DIAMONDS, HEARTS, SPADES
# VALUES:
#   ACE: 1, NORMAL: 2-10, JACK: 11, QUEEN: 12, KING: 13

class Deck:

    def _createColor(self, color, deck):
        for i in range(1, 14):
            deck.append(Card(color, i))
        return deck

    def __init__(self):
        self._deck = self._createColor("Clubs", [])
        self._deck = self._createColor("Diamonds", self._deck)
        self._deck = self._createColor("Hearts", self._deck)
        self._deck = self._createColor("Spades", self._deck)

    def shuffleCards(self):
        random.shuffle(self._deck)
        return self._deck

    def displayCards(self):
        return [ card.getValues() for card in self._deck ]

    def cardCount(self):
        return len(self._deck)

    def throwCard(self):
        choice = random.choice(self._deck)
        self._deck.remove(choice)
        return choice

    def getCard(self, card):
        self._deck.append(card)
        return card
