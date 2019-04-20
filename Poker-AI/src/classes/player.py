from classes.card import Card

class Player:

    def __init__(self, name, position, chips):
        self.name = name.lower()
        self.position = position
        self._hand = []
        self.chips = 1000
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

    def showCards(self):
        return [ card.getValues() for card in self._hand ]

    def giveCards(self):
        ret = [ card for card in self._hand ]
        self._hand = []
        return ret

    def play(self, play):
        if play >= 0:
            self.state += play
            self.chips -= play
            return play
        return -1


class HumanPlayer(Player):

    def action(self, phase, highest):
        while True:
            print("=", self.getName(), phase, "=")
            print("Chips:", self.chips)
            call = highest - self.state
            print("To play:", call)
            action = input()
            if "bet" in action.lower():
                try:
                    amount = action.split(' ')[1]
                    if amount.isdigit() and int(amount) >= call and int(amount) <= self.chips:
                        return self.play(int(amount))
                    else:
                        print("! Invalid bet amount !")
                except IndexError:
                    pass
            else:
                print("/_\ Invalid action /_\\")