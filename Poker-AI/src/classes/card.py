# COLORS:
#   CLUBS, DIAMONDS, HEARTS, SPADES
# VALUES:
#   ACE: 1, NORMAL: 2-10, JACK: 11, QUEEN: 12, KING: 13

class Card:

    _values = {11: "J", 12: "Q", 13: "K"}
    _symbols = {"Clubs": "♣️", "Diamonds": "♦️", "Hearts": "♥️", "Spades": "♠️"}

    def __init__(self, color, number):
        self.color = color
        self.number = number

    def _print(self, color, number):
        number = self._values[number] if number > 10 else number
        style = " _______\n"
        style += '|' + str(number) + self._symbols[color]
        if isinstance(number, int) and number > 9:
            style += '    |\n'
        else:
            style += '     |\n'
        style += "|_______|"
        print(style)

    def getValues(self):
        return {'color': self.color, 'number': self.number}

    def display(self):
        self._print(self.color, self.number)
        return self.getValues()
