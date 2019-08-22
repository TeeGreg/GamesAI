from classes.card import Card
from classes.informations import Informations

class Player:

    def __init__(self, name, position, chips):
        self.name = name.lower()
        self.position = position
        self._hand = []
        self._brain = Informations()
        self.chips = chips
        # CALL, RAISE, FOLD
        # NUM , NUM  , -1
        self.state = 0

    def getName(self):
        return self.name

    def getState(self):
        return self.state

    def getChips(self):
        return self.chips

    def getPlayer(self):
        return {'name': self.name, 'position': self.position}

    def takeCards(self, cards):
        for card in cards:
            self._hand.append(card)

    def showCards(self, mode="console"):
        if mode == "console":
            return [ card.getValues() for card in self._hand ]
        return [ card.display() for card in self._hand ]

    def giveCards(self):
        ret = [ card for card in self._hand ]
        self._hand = []
        return ret

    def play(self, play):
        if play >= 0 and play <= self.chips:
            self.state += play
            self.chips -= play
            return play
        return -1


class HumanPlayer(Player):

    def action(self, phase, highest):
        while True:
            print("=", self.getName(), phase, "=")
            self._brain.availableActions()
            self._brain.displayCurrentChips(self.chips)
            call = highest - self.state
            self._brain.displayCurrentBet(call)
            action = self._brain.thinking()
            if "bet" in action.lower():
                try:
                    amount = int(action.split(' ')[1])
                    if amount >= call:
                        if self.play(amount) != -1:
                            return amount
                        self._brain.chipsMissing()
                    else:
                        self._brain.moreChips(call)
                except IndexError:
                    self._brain.betAmount()
                    pass
            elif "follow" in action.lower():
                if self.play(call) != -1:
                    return call
                self._brain.moreChips(call)
            elif "check" in action.lower():
                if call == 0:
                    return call
                self._brain.invalidCheck()
            elif "fold" in action.lower():
                self.state = -1
                return -1
            elif "all-in" in action.lower():
                maxChips = self.chips
                if self.play(maxChips) != -1:
                    return maxChips
                self._brain.actionError()
            else:
                self._brain.invalidAction()
