from classes.card import Card

class Player:

    def __init__(self, name, position):
        self.name = name.lower()
        self.position = position
        self._hand = []

    def getName(self):
        return self.name

    def getPlayer(self):
        return {'name': self.name, 'position': self.position}

    def takeCards(self, cards):
        for card in cards:
            self._hand.append(card)

    def showCards(self):
        return [ card.getValues() for card in self._hand ]

    def giveCards(self):
        ret = [ card for card in self._hand ]
        self._hand = []
        return ret